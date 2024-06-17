# Importacion de modulo pandas

import pandas as pd

# Funcion para cambiar los tipos de datos de las columnas
def modTypes(df):
    column_names = list(df.columns)

#Recorre los nombres de los dataframes y transforma los tipos dependiendo del encabezado de la columna
    for item in column_names:
        
        if item=='transactions':
            df[item]=df[item].astype(int) 
        
        elif item=='gross_margin' or item=='investment':
            df[item]= pd.to_numeric(df[item], errors='coerce')
        
        elif item=='date':
            df[item]= pd.to_datetime (df[item], format='%d/%m/%Y', errors='coerce')

        pass
    return df    

#Funcion para consolidar todos los dataframes en uno solo 
def mergeData(data_frame):
  
    df_merged= pd.merge (data_frame[0],data_frame[1], on='distributor_id') 
    df_merged= pd.merge (df_merged,data_frame[2], on='location_id')
    df_merged= pd.merge (df_merged,data_frame[3], on='id_country')
    df_merged= pd.merge (df_merged,data_frame[4], on='id_country')

    return df_merged
 
    
    