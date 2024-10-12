# %%
import pandas as pd #importa o pandas e cria um alias (apelido) para o panda
# %%

# criando uma serie a partir de uma lista
idades = [12,34,56,78,90,23,56]

#serie é um objeto pandas de 1 coluna
series_idades = pd.Series(idades)
series_idades
# %%
series_idades.mean() #media
# %%
series_idades.var() #variancia

# %%
series_idades.median() #mediana
# %%
series_idades.describe()

# %%
series_idades.shape
# %%
series_idades[0]
# %%
series_idades.index

# %%
series_idades.index = ["a","b","c","d","e","f","g"]
# %%
series_idades
# %%
series_idades.iloc[0] #pega pela posição

# %%
series_idades.loc["c"] #pega pelo valor do indice
# %%

series_idades.name = "idades"
# %%
series_idades
# %%



# %%
a = 10

# %%
b = 10
# %%
