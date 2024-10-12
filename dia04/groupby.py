# %%
import pandas as pd

# read the excel archive
df = pd.read_excel("../data/transactions.xlsx")
df

# %%
# do a filter in IdCostumer by id number and sum the values.
condicao = df["IdCustomer"]=="5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user['Points'].sum()

# %%

pontos = {}
for i in df['IdCustomer'].unique():
    condicao = df["IdCustomer"]==i
    pontos[i] = df[condicao]["Points"].sum()

pontos

# %%

# agregar pelo idCustomer pela estatistica de points
# groupby IdCustomer using statistics of points
df_summary = df.groupby(["IdCustomer"])["Points"].sum()
df_summary.reset_index()

# %%

# groupby IdCustumer and aggregate Points by sum,UUID by count and DtTransactions by max value, rename the columns and reset the index.
(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": "max"})
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())

# %%
import datetime

data1 = df["DtTransaction"][0]
now = datetime.datetime.now()
(now - data1).days

# %%
# get the date now and substract the first line in DtTransaction date and get just days
(datetime.datetime.now() - df["DtTransaction"][0]).days


# %%
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days


(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": ['max', recencia]
          })
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())
# %%
