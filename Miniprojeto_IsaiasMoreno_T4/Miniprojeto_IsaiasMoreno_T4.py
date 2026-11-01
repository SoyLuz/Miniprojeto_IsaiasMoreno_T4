# -*- coding: utf-8 -*-
"""Mini-projeto de analise exploratoria da base Varejo - Isaias Moreno, T4."""

# Sprint 1 - importando as bibliotecas e carregando a base
import pandas as pd
import csv

df = pd.read_csv("Base Varejo.csv", sep=";")

print("Numero de registros:", df.shape[0])
print("Numero de colunas:", df.shape[1])
print(df.columns.tolist())
print(df.dtypes)
df.head()

# leitura estruturada com csv.DictReader (cada linha vira um dicionario)
with open("Base Varejo.csv", encoding="latin-1") as f:
    leitor = csv.DictReader(f, delimiter=";")
    linhas = list(leitor)

print("Linhas lidas com DictReader:", len(linhas))
print("Primeira linha:", linhas[0])

# verificando problemas na base
print("Nulos por coluna:")
print(df.isnull().sum())

print("Linhas duplicadas:", df.duplicated().sum())

print("Categorias:")
print(df["PR_CAT"].value_counts(dropna=False))

print("Exemplo de datas:", df["DATA"].head().tolist())

# Sprint 2 - limpeza de texto: maiusculas, tira espacios extras com regex
df = df.loc[:, ~df.columns.str.contains("Unnamed")]   # remove colunas vazias

df["PR_NOME"] = df["PR_NOME"].astype(str).str.upper().str.replace(r"\s+", " ", regex=True).str.strip()
df["PR_CAT"] = df["PR_CAT"].astype(str).str.upper().str.strip()

# converte numero de filhos para tipo numerico
df["CL_FHL"] = pd.to_numeric(df["CL_FHL"], errors="coerce")
print(df.dtypes)

# preenchendo categorias vazias com "Sem Categoria" usando if/else
def arrumar_categoria(cat):
    if pd.isna(cat) or cat in ["", "NAN", "#N/D"]:
        return "Sem Categoria"
    else:
        return cat

df["PR_CAT"] = df["PR_CAT"].apply(arrumar_categoria)
print(df["PR_CAT"].value_counts())

# dimensoes fisicas (peso, altura, largura...): procurei e a base NAO tem essas colunas,
# entao nao ha nulos fisicos para tratar. Se tivesse, eu preencheria com a mediana
# da categoria, porque a mediana nao e afetada por valores extremos.
colunas_fisicas = [c for c in df.columns if any(p in c.upper() for p in ["PESO", "ALT", "LARG", "COMP"])]
print("Colunas fisicas encontradas:", colunas_fisicas)

# numero de filhos nulo: preencho com a mediana (se houver)
if df["CL_FHL"].isnull().sum() > 0:
    df["CL_FHL"] = df["CL_FHL"].fillna(df["CL_FHL"].median())
else:
    print("CL_FHL sem nulos")

# removendo duplicatas exatas
# hipotese adotada: linhas identicas representam registros duplicados
# limitacao: sem quantidade ou identificador do item, nao e possivel
# descartar que sejam unidades repetidas do mesmo produto na mesma compra
antes = len(df)
df = df.drop_duplicates()
print("Duplicatas removidas:", antes - len(df))

# converte datas invalidas para NaT, sem interromper o programa
df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")

print("Datas invalidas ou ausentes:", df["DATA"].isna().sum())

# removo registros sem data valida porque nao podem participar das analises por periodo
df = df.dropna(subset=["DATA"]).copy()

# regra adotada: cada compra deve ter identificador,
# exatamente um cliente identificado e exatamente uma data
regra = df.groupby("CO_ID").agg(
    clientes=("CL_ID", "nunique"),
    datas=("DATA", "nunique"),
    cliente_ausente=("CL_ID", lambda coluna: coluna.isna().any())
)
invalidas = regra[
    (regra["clientes"] != 1)
    | (regra["datas"] != 1)
    | regra["cliente_ausente"]
]
mascara_invalidos = (
    df["CO_ID"].isna()
    | df["CO_ID"].isin(invalidas.index)
)
df_invalidos = df.loc[mascara_invalidos].copy()
df = df.loc[~mascara_invalidos].copy()

print("Compras identificadas que quebram a regra:", len(invalidas))
print("Registros separados pela regra do CO_ID:", len(df_invalidos))

# estatisticas do numero de filhos (1 linha por cliente para nao contar repetido)
filhos = df.drop_duplicates("CL_ID")["CL_FHL"]

print("Contagem:", filhos.count())
print("Media:", round(filhos.mean(), 2))
print("Mediana:", filhos.median())
print("Desvio padrao:", round(filhos.std(), 2))
modas = filhos.mode()
print("Moda:", modas.tolist() if not modas.empty else "Sem dados")
print("Minimo:", filhos.min())
print("Maximo:", filhos.max())
print("Clientes sem filhos:", (filhos == 0).sum())

# agrupamento 1: genero x compras e registros de produtos
print(df.groupby("CL_GENERO").agg(compras=("CO_ID", "nunique"), registros_produtos=("PR_ID", "count")))

# agrupamento 2: quantidade de registros por categoria
print(df.groupby("PR_CAT").size().sort_values(ascending=False))

# agrupamento 3: pivot categoria x segmento
print(pd.pivot_table(df, index="PR_CAT", columns="CL_SEG", values="PR_ID", aggfunc="count"))

# agrupamento 4: compras por mes
print(df.groupby(df["DATA"].dt.to_period("M"))["CO_ID"].nunique())

# relatorio final
print("===== RELATORIO FINAL =====")
print("Registros finais:", len(df))
print("Clientes:", df["CL_ID"].nunique())
print("Compras:", df["CO_ID"].nunique())
print("Produtos:", df["PR_ID"].nunique())
print("Categorias:", df["PR_CAT"].nunique())
print("Registros separados pela regra do CO_ID:", len(df_invalidos))

df.to_csv("df_limpo.csv", index=False)
print("df_limpo.csv salvo")

