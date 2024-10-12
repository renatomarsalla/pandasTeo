# # %%

# import pandas as pd

# # %%
# df_customers = pd.read_csv("../data/customers.csv", sep=";")
# df_customers

# #%%
# df_customers.shape

# # %%
# df_customers.info(memory_usage='deep')

# # %%
# df_customers["Points"].describe()

# # %%
# condicao = df_customers["Points"] > 1000
# df_customers[condicao]

# # %%
# condicao = df_customers["Points"] == df_customers["Points"].max()
# df_customers[condicao]

# # %%
# condicao = df_customers["Points"] == df_customers["Points"].max()
# df_maior = df_customers[condicao]
# df_maior["Name"].iloc[0]

# # %%

# condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
# df_1000_2000 = df_customers[condicao].copy()


# # %%
# df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
# df_1000_2000
# # %%
# df_customers

# # %%
# df_customers[["UUID", "Name"]]

# # %%
# colunas = df_customers.columns.tolist()
# colunas.sort()

# df_customers = df_customers[colunas]
# df_customers

# # %%
# df_customers = df_customers.rename(columns={"Name": "Nome",
#                                             "Points": "Pontos"})

# df_customers

# # %%
# df_customers.rename(columns={"UUID":"Id"}, inplace=True)
# df_customers

#--------------------------------------------------------------------------------------------------------------------------------------
 
# %%
import pandas as pd
# %%
# importa arquivo csv local
df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers
# %%
# retorna quantidade de linhas e colunas em uma tupla
df_customers.shape
# %%
# retorna tamnaho real da memoria que esta sendo usada
df_customers.info(memory_usage="deep")

# %%
# retorna estatistica descritiva da coluna Points
df_customers["Points"].describe()
# %%
# foi verificado que a coluna Points estava como object porem devemos alterar para int
df_customers["Points"].astype(int)
# %%
# retorna estatistica descritiva da coluna Points
df_customers["Points"].describe()
# %%
# soma um valor para todos os elementos de uma serie
df_customers["Points"] + 1000
# %%

#-----------------------FILTROS------------------------------------------


#retorna uma serie booleana onde os points sao maisores que mill
condicao = df_customers["Points"] > 1000
# %%
df_customers[condicao]
# %%
maxima = df_customers["Points"].max()
condicao = df_customers["Points"] == maxima
df_customers[condicao]
# %%
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]
# %%
condicao = (df_customers["Points"]>=1000) & (df_customers["Points"]<=2000)
condicao
# %%
df_customers[condicao]

#------------------------------------------------------------------------
# %%

#selecionando duas colunas, passamos uma lista como argumento com os nomes desejados
df_customers[["UUID", "Name"]]

# %%
#colocando em ordem alfabetica
colunas = df_customers.columns.to_list()
colunas.sort()
df_customers[colunas]

#alterando o dataframe original
df_customers = df_customers[colunas]
df_customers
# %%

# renomear colunas sem alterar o dataframe original, rename gera um dataframe novo
df_customers.rename(columns={"Name":"Nome","Points":"Pontos"})
# %%
#inplace muda o nome das colunas no dataframe original
df_customers.rename(columns={"UUID":"Id"},inplace=True)
# %%
df_customers
# %%
