# Mini-Projeto - Analise Exploratoria da base Varejo

Visualizacao de Dados e BI [T4] - Mini-Projeto Avaliativo Modulo 1 Semana 07
Aluno: Isaias Moreno

## Sobre o projeto
Neste projeto eu fiz uma analise exploratoria da base Varejo do Kaggle usando Python e pandas.
Carreguei a base, procurei os problemas, fiz a limpeza (nulos, duplicatas, tipos e datas),
calculei as estatisticas do numero de filhos (CL_FHL) e fiz alguns agrupamentos.
No final salvei a base limpa no arquivo df_limpo.

Base usada: https://www.kaggle.com/datasets/namespaiva/base-varejo/data

## Arquivos
- `Miniprojeto_IsaiasMoreno_T4/Miniprojeto_IsaiasMoreno_T4.ipynb` - notebook do Colab com as saidas
- `Miniprojeto_IsaiasMoreno_T4/Miniprojeto_IsaiasMoreno_T4.py` - o mesmo codigo em .py
- `Miniprojeto_IsaiasMoreno_T4/df_limpo.zip` - base limpa (df_limpo.csv dentro do zip, porque o csv passa de 25 MB)
- `Miniprojeto_IsaiasMoreno_T4/README_IsaiasMoreno_T4.md` - instrucoes para rodar

## Como executar
Abrir no Google Colab, subir o arquivo Base Varejo.csv e rodar todas as celulas.
Tambem da para rodar no computador com `python Miniprojeto_IsaiasMoreno_T4.py`,
com o Base Varejo.csv na mesma pasta (precisa ter o pandas instalado).

## Reflexao: ETL e qualidade de dados
Fazendo o projeto deu para entender melhor o que e ETL. O Extrair foi ler o CSV, com o pandas
e tambem com o csv.DictReader. O Transformar foi a parte maior: tirar as colunas vazias,
arrumar o texto, trocar o #N/D por "Sem Categoria", tirar as linhas duplicadas, converter a data
de texto para datetime e conferir a regra do CO_ID. O Carregar foi salvar o df_limpo, que pode ser
usado depois em um dashboard. A qualidade dos dados importa porque se eu nao tirasse as
96.553 linhas duplicadas, todas as contagens de itens iam sair maiores do que sao de verdade,
e a conclusao ia ficar errada. Dado sujo gera conclusao errada.

## Problemas encontrados e tratamento
A base original tinha 830.000 linhas e 14 colunas.
- 4 colunas vazias (Unnamed: 10 ate Unnamed: 13), com 830.000 nulos cada. Removi essas colunas.
- 3.650 linhas com categoria "#N/D". Troquei por "Sem Categoria" com uma funcao if/else.
- 96.553 linhas duplicadas (iguais em tudo). Removi porque elas aumentam as contagens.
- A coluna DATA estava como texto (dd/mm/aaaa). Converti para datetime; nenhuma data ficou invalida.
- Regra do CO_ID (cada compra com 1 cliente e 1 data): conferi e nenhuma compra quebrou a regra.
- Dimensoes fisicas (peso, altura, largura): a base nao tem essas colunas, entao nao tinha nulos fisicos para tratar.
- CL_FHL nao tinha nulos.

Depois da limpeza ficaram 733.447 linhas e 10 colunas, com 1.000 clientes, 18.471 compras,
229 produtos e 7 categorias.

## Estatisticas do numero de filhos (CL_FHL)
Calculado com 1 linha por cliente (1.000 clientes), para nao contar o mesmo cliente varias vezes.

| Medida | Valor |
|---|---|
| Contagem | 1000 |
| Media | 1.14 |
| Mediana | 0 |
| Desvio padrao | 1.41 |
| Moda | 0 |
| Minimo | 0 |
| Maximo | 4 |

## Principais insights
- ALIMENTOS e a categoria que mais vende: 384.197 itens, mais ou menos 52% de tudo. Depois vem HIGIENE (18,8%) e LIMPEZA (17,5%).
- As mulheres fizeram um pouco mais de compras: 9.615 compras (F) contra 8.856 (M). Mas o numero de itens por compra e quase igual, perto de 40 nos dois.
- A maioria dos clientes nao tem filhos: a mediana e a moda sao 0 e 527 dos 1.000 clientes tem 0 filhos. A media e 1,14 e o maximo e 4.
- O segmento B e o que mais compra em todas as categorias (por exemplo 245.501 itens de ALIMENTOS), o segmento A e o que menos compra.
- As compras por mes variam bastante. Os meses com mais compras foram 05/2019 e 10/2021 (711 cada). Os meses 09/2022 (35) e 10/2022 (59) tem muito pouco, parece que faltam dados nesse periodo.

## Problemas que ainda ficaram
- A base nao tem preco nem valor, por isso aqui "vendas" quer dizer quantidade de itens e nao dinheiro.
- Nao da para saber qual era a categoria certa dos produtos com #N/D, ficaram como "Sem Categoria".
- Os meses de set/out 2022 com poucas compras podem atrapalhar uma analise de tendencia.
