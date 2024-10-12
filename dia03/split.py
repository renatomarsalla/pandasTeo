# %%

# split é utilizado para dividir o conteúdo de uma string em uma lista com um ou vários elementos

list_name = ['renato_marsalla_toscano','otavio_miranda_nunes','maria_bethania-gal']

# nome = []
for i in list_name:
    print(i.upper().split('_')[0])
    # nome.append(i.upper)
# %%
endereco = '/data/ipea/homicidio-de-jovens-por-armas-de-fogo.csv'
name1 = endereco.split('/')[-1]
name2 = name1.split('.')[0]
name2

# %%
