# %%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

df.dtypes


# %%

df["Points_dobble"] = df["Points"] * 2

# %%
df[["Points", "Points_dobble"]].astype(float)

# %%
df[["UUID", "Name"]].astype(int)

# %%

df["Lista"] = [[ 1,2 ] for i in df.index ]
df

# %%

df.dtypes
# %%

idEx = df['UUID'] == 'aa3eaf74-6d9c-4859-b733-5a18a3b2f71b'

# %%
df[idEx]['Name']
# %%
