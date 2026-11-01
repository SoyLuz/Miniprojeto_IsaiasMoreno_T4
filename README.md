# Mini-Projeto - Analise Exploratoria da base Varejo

Visualizacao de Dados e BI [T4] - Mini-Projeto Avaliativo Modulo 1 Semana 07
Aluno: Isaias Moreno

## Sobre o projeto
Nesse projeto eu peguei a base Varejo do Kaggle e fiz uma analise exploratoria com Python e pandas.
Primeiro eu carreguei a base e olhei os problemas. Depois limpei os nulos, as duplicatas, os tipos e as datas.
Tambem calculei as estatisticas do numero de filhos (CL_FHL) e fiz alguns agrupamentos.
No final salvei a base limpa como df_limpo.

Base usada: https://www.kaggle.com/datasets/namespaiva/base-varejo/data

## Arquivos
- `Miniprojeto_IsaiasMoreno_T4/Miniprojeto_IsaiasMoreno_T4.ipynb` - notebook do Colab executado, com as saidas
- `Miniprojeto_IsaiasMoreno_T4/Miniprojeto_IsaiasMoreno_T4.py` - o mesmo codigo em .py
- `Miniprojeto_IsaiasMoreno_T4/df_limpo.zip` - a base limpa (o df_limpo.csv ta dentro do zip, porque o csv passa de 25 MB)
- `Miniprojeto_IsaiasMoreno_T4/README_IsaiasMoreno_T4.md` - como rodar

## Como executar
Eu fiz tudo no Google Colab. E so abrir o notebook, subir o arquivo Base Varejo.csv e rodar todas as celulas.
Se quiser rodar no computador, tem que ter o pandas instalado e deixar o Base Varejo.csv na mesma pasta.
Ai e so rodar `python Miniprojeto_IsaiasMoreno_T4.py`.

## Reflexao: ETL e qualidade de dados
Antes eu nao entendia muito bem o que era ETL, mas fazendo o projeto ficou mais claro.
Extrair foi ler o CSV. Eu li com o pandas e tambem com o csv.DictReader.
Transformar foi a parte que deu mais trabalho. Tive que tirar as colunas vazias, arrumar o texto,
trocar o #N/D por "Sem Categoria", tirar as linhas repetidas, mudar a data de texto para datetime
e conferir a regra do CO_ID.
Carregar foi salvar o df_limpo, que depois da para usar num dashboard.
Percebi que a qualidade dos dados faz muita diferenca. Por exemplo, a base tinha 96.553 linhas iguais em tudo.
Para mim elas pareciam registros repetidos, entao eu decidi tirar, senao as contagens iam ficar maiores.
Mas isso foi uma decisao com base na minha hipotese, nao uma certeza. Por isso eu deixei anotado mais abaixo.

## Problemas encontrados e tratamento
A base original tinha 830.000 linhas e 14 colunas. Os problemas que eu achei foram estes:
- Tinha 4 colunas vazias (Unnamed: 10 ate Unnamed: 13), com 830.000 nulos cada uma. Eu tirei essas colunas.
- Tinha 3.650 linhas com a categoria "#N/D". Troquei por "Sem Categoria" usando uma funcao com if/else.
- Tinha 96.553 linhas duplicadas, iguais em tudo. Eu considerei que eram registros repetidos e tirei, porque elas aumentam as contagens.
  So que a base nao tem quantidade nem um id do item, entao nao da para ter certeza que nao eram unidades a mais do mesmo produto na mesma compra.
- A coluna DATA estava como texto (dd/mm/aaaa). Mudei para datetime e nenhuma data deu erro.
- Conferi a regra do CO_ID: cada compra tem que ter identificador, exatamente 1 cliente identificado e exatamente 1 data. Nenhuma compra quebrou a regra, entao 0 registros foram separados.
- Procurei colunas de peso, altura e largura, mas a base nao tem. Entao nao tinha nulo fisico para arrumar.
- A coluna CL_FHL nao tinha nulos.

Depois da limpeza sobraram 733.447 linhas e 10 colunas. Sao 1.000 clientes, 18.471 compras,
229 produtos e 7 categorias.

## Estatisticas do numero de filhos (CL_FHL)
Aqui eu usei so 1 linha por cliente (1.000 clientes), para nao contar o mesmo cliente varias vezes.
O codigo tambem mostra quantos clientes nao tem filhos: 527.

| Medida | Valor |
|---|---|
| Contagem | 1000 |
| Media | 1.14 |
| Mediana | 0 |
| Desvio padrao | 1.41 |
| Moda | 0 |
| Minimo | 0 |
| Maximo | 4 |

## Principais conclusoes
- O que mais aparece e ALIMENTOS, com 384.197 registros de produtos. Isso da mais ou menos 52% de tudo. Depois vem HIGIENE (18,8%) e LIMPEZA (17,5%).
- As mulheres fizeram um pouco mais de compras que os homens: 9.615 (F) contra 8.856 (M). Mas a quantidade de registros de produtos por compra e quase a mesma, uns 40 nos dois.
- Percebi que a maioria dos clientes nao tem filhos. A mediana e a moda deram 0, e 527 dos 1.000 clientes tem 0 filhos. A media ficou 1,14 e o maximo e 4.
- O segmento B e o que mais compra em todas as categorias (so de ALIMENTOS foram 245.501 registros). O segmento A e o que menos compra.
- As compras mudam bastante de um mes para outro. Os meses com mais compras foram 05/2019 e 10/2021 (711 cada). Ja 09/2022 (35) e 10/2022 (59) tem muito pouco. Pode ser que faltem dados nesses meses, ou pode ser que so teve menos movimento mesmo. Com essa base eu nao consigo confirmar a causa.

## O que ainda ficou faltando
- A base nao tem preco nem valor. Entao aqui eu contei registros de produtos, nao dinheiro.
- Por causa das duplicatas, pode ser que alguns produtos repetidos na mesma compra tenham sido tirados sem querer. Nao tem como conferir so com essa base.
- Nao deu para saber a categoria certa dos produtos com #N/D. Eles ficaram como "Sem Categoria".
- Os meses de setembro e outubro de 2022 tem poucas compras, e isso pode atrapalhar se alguem for ver a tendencia.
