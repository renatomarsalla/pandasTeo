# # %%
# import pandas as pd
# # %%

# data = {
#     "nome":["teo", "nah", "lara", "maria"],
#     "sobrenome": ["calvo", "ataide", "calvo", "calvo"],
#     "idade": [31, 32, 31, 2]
# }

# #%%
# data["idade"][0]

# # %%
# df = pd.DataFrame(data)
# df
# #%%
# df["idade"].iloc[0]

# # %%
# df['sobrenome'].iloc[0]

# # %%
# df.iloc[0]

# # %%
# df['idade']

# # %%

# df.index=[3,2,1,0]
# df
# # %%
# df["idade"][0]

# # %%
# df.index

# # %%
# df.columns

# # %%
# df.info(memory_usage='deep')

# # %%
# df.dtypes

# # %%

# df['peso'] = [80, 53, 65, 14]

# sumario = df.describe()

# sumario['peso']['mean']

# # %%
# df.head(2)

# # %%
# df.tail(2)

#------------------------------------------------------------
# %%
import pandas as pd
# %%
data = {
    "nome":["teo", "nah","lara","maria"],
    "sobrenome":["calvo","ataide","calvo","calvo"],
    "idade":[31,32,31,2]
}
# %%
data["idade"][0]
# %%
df = pd.DataFrame(data) #cria dataframe
#datarfame pode ser representado por um conjunto de series
# %%

df
# %%
df["idade"].iloc[1]

# %%
df.iloc[0]
# %%
df.columns
# %%
df.info()
# %%
df.info(memory_usage='deep')

# %%
df.dtypes
# %%
df.describe()
# %%

df['peso']= [80,66,77,100]
df.describe()
# %%
sumario = df.describe()
# %%
sumario["peso"]["mean"]

# %%
sumario["peso"].iloc[1]

# %%
df.head()#mostra 5 primeiras linha ou especificar um numero
# %%

df.tail()#mostra 5 ultimas linha ou especificar um numero
# %%
