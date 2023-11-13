import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from urllib.request import urlretrieve


# Contingut original.
filepath: str = "incidence-rate-2021-raw.csv"

# Et donem el contingut ja preprocessat, a partir de la q3.
filepath_q3: str = "incidence-rate-2021-new.csv"

def q0_read_raw_data():
    df_orig = pd.read_csv(filepath, sep=';', decimal=".")
    print(df_orig.iloc[0])
    return df_orig

def q0_read_correct_data():
    df_orig = pd.read_csv(filepath_q3, sep=';', decimal=".")
    # print(df_orig.iloc[0])
    return df_orig

# Pregunta 1. Mostra la següent info: 
#               El número de files en total 
#               Informació sobre totes les columnes
#               Les 20 primeres files 
def q1_basic_info(df: pd.DataFrame):
    print(len(df))
    print(df.info())
    print(df.info(20))

# Pregunta 2. Preprocessament dataframe.
#               Mostra els valors únics del camp DENOMINATOR
#               Crea un nou dataframe que:
#                 Elimina la columna DISEASE_DESCRIPTION
#                 De la columna 'GROUP' només volem les files 
#                   que tinguin el valor 'COUNTRIES'
#                 De la columna 'DENOMINATOR' Només tingui el valor
#                   'per 1,000,000 total population'.
#                   per tal d'unificar criteris.
#               Guarda-ho en un fitxer anomenat:
#                  incidence-rate-2021-new.csv
def q2_preprocessing(df: pd.DataFrame):
    df_new = df
    mask_countries = df_new.loc[:,"GROUP"] == "COUNTRIES"
    df_new = df_new.loc[mask_countries,:]
    df_new = df_new.drop(columns=['GROUP'])
    df_new.to_csv(filepath_q3, index=False, sep=';', decimal=".")
    return df_new

# Pregunta 3. Analitzem NaN i outliers.
#               Mostra els valors NaN que hi ha en cada columna.
#               Mostra el nom, enfermetat, inc_rate i any de les 10 files que tenen valors més
#               alts d'INCIDENCE_RATE.
def q3_outliers(df_new: pd.DataFrame):
    print(df_new.isna().sum())
    df_outliers = df_new.sort_values(by='INCIDENCE_RATE', ascending=False).head(5)
    #CODE;NAME;YEAR;DISEASE;DISEASE_DESCRIPTION;DENOMINATOR;INCIDENCE_RATE
    print(df_outliers[['NAME','YEAR','DISEASE','INCIDENCE_RATE']])
    return df_new

# Pregunta 4. Gràfic distribució casos enfermetats.
#               Mostra un gràfic plotbox o similar dels casos d'enfermetats d'un país
#               (el que et toqui) agrupats per enfermetats.
def q4_grafic_distribucio(df_new: pd.DataFrame):
    df_new_spa = df_new.query("NAME == 'Spain'")
    plt.figure(figsize=(20,12))
    sns.boxplot(data=df_new_spa, x='INCIDENCE_RATE', y='DISEASE').get_figure().savefig('output/q42_outliers.png')


if __name__ == "__main__":
    # df = q0_read_raw_data()
    # q1_basic_info(df)
    # df_new = q2_preprocessing(df)
    df_new = pd.read_csv(filepath, sep=';', decimal=".")
    q3_outliers(df_new)
    q4_grafic_distribucio(df_new)