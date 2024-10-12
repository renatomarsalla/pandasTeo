# %%
import pandas as pd

# %%
df = pd.read_csv("../data/customers.csv", sep=';')
df

# %%
# ordenando pontos de forma decrescente e nomes de forma crescente

df = (df.sort_values( by=["Points", "Name"],
                      ascending=[False, True] )
        .rename(columns={"Name":"Nome", "Points":"Pontos"}))

df
# %%
df["Pontos"].max()
# %%
condicao = df["Pontos"] == 4304
# %%
df[condicao]

# %%
df[condicao]["Nome"]
# %%
