# %% [markdown]
# ### European Exports 2019-2023 

# %%
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

# %% [markdown]
# ##### Carga de Datos

# %%
pd.set_option('display.max_rows', None)
f_exports_2019_2023 = pd.read_excel("FAOSTAT_data_en_2019_2023.xlsx", sheet_name= 'Hoja1')
f_exports_2019_2023.head(3)

# %%
pd.set_option('display.max_rows', None)
Socioeconomic_Data_2019_2023 = pd.read_excel("Socioeconomic_Data_2019_2023.xlsx", sheet_name= 'Data_2019_2023')
Socioeconomic_Data_2019_2023.head(3)

# %%
pd.set_option('display.max_rows', None)
dProduct = pd.read_excel("dProduct.xlsx", sheet_name= 'dProduct')
dProduct.head(3)

# %% [markdown]
# ##### Transformación y Iimpieza de datos

# %%
f_exports_2019_2023.info()

# %%
###Se elimina la columna Note porque no aporta valor.

f_exports_2019_2023.drop('Note', axis=1, inplace= True)


# %%
###Se eliminan todas las filas del dataframe que no contienen A de la columna Flag porque se tratan de estimaciones y 
# valores no oficiales que vamos a desechar.

f_exports_2019_2023.drop(f_exports_2019_2023[f_exports_2019_2023['Flag'] != 'A'].index, inplace= True)

# %%
f_exports_2019_2023.info()

# %%
## Creamos la columna Country-Year con la unión de las columnas Area Code (M49) y Year que nos va a servir para combinar ambos dataframes

f_exports_2019_2023['Area Code (M49)'] = f_exports_2019_2023['Area Code (M49)'].astype(str)
f_exports_2019_2023['Year'] = f_exports_2019_2023['Year'].astype(str)

f_exports_2019_2023['Country-Year'] = f_exports_2019_2023['Area Code (M49)'].str.cat(f_exports_2019_2023['Year'], sep='-')

# %%
f_exports_2019_2023.head(3)

# %% [markdown]
# #### Combinación de ambos dataframe

# %%
### Combinamos ambos dataframes con la columna Country-Year

f_exports_2019_2023 = f_exports_2019_2023.merge(Socioeconomic_Data_2019_2023, how='left', on = 'Country-Year')

# %%
f_exports_2019_2023.head(3)

# %%
f_exports_2019_2023 = f_exports_2019_2023.drop(['Area Code (M49)_y', 'Country', 'Year_y', 'Year_x'], axis=1)

# %%
f_exports_2019_2023.head(3)

# %%
f_exports_2019_2023 = f_exports_2019_2023.rename(columns={'Area Code (M49)_x': 'Country Code','Area': 'Country'})

# %%
f_exports_2019_2023.head(3)

# %% [markdown]
# ##### Limpieza de datos y gestión de nulos

# %%
f_exports_2019_2023.info()

# %%
###Porcentaje de nulos

Nulos = (f_exports_2019_2023.isnull().sum() / f_exports_2019_2023.shape[0] * 100).round(2)

df_nulos = pd.DataFrame(Nulos, columns=['porc_nulos'])

filtro = df_nulos['porc_nulos'] > 0

df_nulos[filtro].sort_values(by='porc_nulos', ascending = False)



# %%
### Se trata de un porcentaje pequeño de valores nulos que vamos a intentar imputar.
filas_nulas=f_exports_2019_2023[f_exports_2019_2023.isnull().any(axis=1)]
filas_nulas.head(3)





# %%
##Como los valores nules se encuentran en el primer Dataframe "Socioeconomic_Data_2019_2023" filtramos los valores nulos en este Dataframe para
## analizarlos detenidamente.

filas_nulas_Socioeconomic_Data_2019_2023 =Socioeconomic_Data_2019_2023[Socioeconomic_Data_2019_2023.isnull().any(axis=1)]
filas_nulas_Socioeconomic_Data_2019_2023


# %% [markdown]
# ##### GDP per capita (USD). Imputación de valores nulos

# %%
# Vamos a imputar los valores nulos en esta columna por un valor que será el cociente entre DGP total (Million USD) / Population

GDP_Norway = f_exports_2019_2023.loc[(f_exports_2019_2023['Country-Year'] == '578-2020') & (f_exports_2019_2023['GDP per capita (USD)'].isnull()), 'GDP per capita (USD)'] = (362000000000/5421241)
GDP_Croatia = f_exports_2019_2023.loc[(f_exports_2019_2023['Country-Year'] == '191-2023') & (f_exports_2019_2023['GDP per capita (USD)'].isnull()), 'GDP per capita (USD)'] = (72000000000/4000000)
GDP_Hungary = f_exports_2019_2023.loc[(f_exports_2019_2023['Country-Year'] == '348-2023') & (f_exports_2019_2023['GDP per capita (USD)'].isnull()), 'GDP per capita (USD)'] = (195000000000/9550000)



# %% [markdown]
# ##### Surface (km2). Imputación de valores nulos

# %%
# Vamos a imputar los valores nulos en esta columna por un valor investigado en internet para cada país.

Surface_Estonia = f_exports_2019_2023.loc[(f_exports_2019_2023['Country-Year'] == '233-2021') & (f_exports_2019_2023['Surface (km2)'].isnull()), 'Surface (km2)'] = 45227
Surface_Greece = f_exports_2019_2023.loc[(f_exports_2019_2023['Country-Year'] == '300-2021') & (f_exports_2019_2023['Surface (km2)'].isnull()), 'Surface (km2)'] = 131957
Surface_Luxembourg = f_exports_2019_2023.loc[(f_exports_2019_2023['Country-Year'] == '442-2021') & (f_exports_2019_2023['Surface (km2)'].isnull()), 'Surface (km2)'] = 2586
Surface_Albania = f_exports_2019_2023.loc[(f_exports_2019_2023['Country-Year'] == '8-2023') & (f_exports_2019_2023['Surface (km2)'].isnull()), 'Surface (km2)'] = 28749
Surface_Germany = f_exports_2019_2023.loc[(f_exports_2019_2023['Country-Year'] == '276-2023') & (f_exports_2019_2023['Surface (km2)'].isnull()), 'Surface (km2)'] = 357386





# %% [markdown]
# ##### Density (hab/km2). Imputación de valores nulos

# %%
# Vamos a imputar los valores nulos en esta columna por un valor investigado en internet para cada país que será el cociente entre la población y superficie.

Density_Sweden = f_exports_2019_2023.loc[(f_exports_2019_2023['Country-Year'] == '752-2022') & (f_exports_2019_2023['Density (hab/km2)'].isnull()), 'Density (hab/km2)'] = 23
Density_Czechia = f_exports_2019_2023.loc[(f_exports_2019_2023['Country-Year'] == '203-2023') & (f_exports_2019_2023['Density (hab/km2)'].isnull()), 'Density (hab/km2)'] = 136




# %%
#Despues de la imputación comprobamos que ya no existe porcentaje de nulos

Nulos = (f_exports_2019_2023.isnull().sum() / f_exports_2019_2023.shape[0] * 100).round(2)

df_nulos = pd.DataFrame(Nulos, columns=['porc_nulos'])

filtro = df_nulos['porc_nulos'] > 0

df_nulos[filtro].sort_values(by='porc_nulos', ascending = False)

# %%
#Para dProduct  reemplazamos los valores nulos por celdas vacías

dProduct.fillna("", inplace= True)
dProduct.head(3)

# %%
#### Cargamos los datos a Power Query

f_exports_2019_2023.info()


