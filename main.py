'''Importacion de modulos panda para los dataframes
   Importacion de modulo obtenerDatos para cargar el sheet de Goggle Drive
   Importacion de matplotlib para los graficos
'''
import numpy as np
import pandas as pd
from modulos.obtenerDatos import cargar_sheet
from modulos.consolidar import modTypes , mergeData
import matplotlib.pyplot as plt

# Se crea la constante RANGO para los rangos de las diferentes hojas a importar y la lista dataFrames que va a contener todos lod dfs

RANGO = ['consolidado!A1:E9607','distributors!A1:C1739','locations!A1:C564','countries!A1:B7','investments!A1:B7']
data_frames=[]

#Recorre los diferentes valores de RANGO
for item in RANGO:
    data = cargar_sheet(item) #Carga de la hoja de calculo el rango especificado

    df = pd.DataFrame (data[1:], columns = data[0]) #Crea el dataframe con los valores 

    df=modTypes(df) #Modifica los typos de datos ya que siempre los devuelve como tipo "object"

    data_frames.append(df) #Guarda en una lista todos los dataframes

consolidado= mergeData(data_frames) #La funcion toma la lista de dataframes y lo consolida en uno solo con todos los datos
consolidado['mes']=consolidado['date'].dt.strftime('%B')
consolidado['mes'].fillna('_Desconocido',inplace=True)
consolidado['tax']=consolidado['gross_margin']*3.5/100
consolidado['revenue'] = consolidado['gross_margin']-consolidado['tax']
  
#Inicio de muestra de datos del TP
print()
print('CaC Trabajo practico Parte 2')
print('='*28)
print()
print(f'1a) La cantidad de ciudades en las que opera la firma es de: {consolidado['city'].nunique()}')
print()
print(f'1b) La cantidad de distribuidores con los que opera la firma es de: {consolidado['distributor'].nunique()}')
print()
print(f'1c) El total de transacciones realizadas es de: {consolidado['transactions'].sum()}')
print()
print(f'1d) La ganancia Bruta toltal es de: {consolidado['gross_margin'].sum()}')
print()
print(f'1e) El total de impuestos a pagar es de: {consolidado['gross_margin'].sum()*3.5/100}')
print()
print('*'*40)
print()
print('2b) Transacciones por País')
print('='*21)

# Se hace el df de transacciones agrupando por pais
transacciones= consolidado.groupby('country')['transactions'].sum().reset_index()

transacciones=transacciones.rename(columns={'country':'Pais','transactions':'Transacciones'})
print(transacciones.sort_values(by='Transacciones',ascending=False))
print('*'*40)
print()

# Se hace el grafico usando matplotlib con el df anterior 
plt.figure(figsize=(10,6))
plt.bar(transacciones['Pais'],transacciones['Transacciones'], color='skyblue')
plt.xlabel('País')
plt.ylabel('Transacciones')
plt.title('Transacciones por país')
plt.show()

print('2c) Ganancias Reales por País')
print('='*25)
ganancia_r_pais= consolidado.groupby('country')['revenue'].sum().reset_index()
ganancia_r_pais=ganancia_r_pais.rename(columns={'country':'Pais','revenue':'Ganancia Real'})
print(ganancia_r_pais.sort_values(by='Ganancia Real',ascending=False))
print('*'*40)
print()

# Se hace el grafico usando matplotlib con el df anterior 
plt.figure(figsize=(10,6))
plt.bar(ganancia_r_pais['Pais'],ganancia_r_pais['Ganancia Real'], color='skyblue')
plt.xlabel('País')
plt.ylabel('Ganancia Real')
plt.title('Ganancia Real por país')
plt.show()

print('3) Ganancias Reales por Mes')
print('='*25)
ganancia_r_mes= consolidado.groupby('mes')['revenue'].sum().reset_index()
ganancia_desc = ganancia_r_mes.loc[ganancia_r_mes['mes'] == '_Desconocido', 'revenue'].values[0]

ganancia_r_mes=ganancia_r_mes.rename(columns={'mes':'Mes','revenue':'Ganancia Real'})
ganancia_r_mes=ganancia_r_mes[ganancia_r_mes['Mes'] != '_Desconocido']
print(ganancia_r_mes.sort_values(by='Mes'))
print (f'Se encuentra un valor de ganancia sin fecha el cual asciende a la cantidad de: {ganancia_desc}')
print('*'*40)
print()

# Se hace el grafico usando matplotlib con el df anterior 
plt.figure(figsize=(10,6))
plt.bar(ganancia_r_mes['Mes'],ganancia_r_mes['Ganancia Real'], color='skyblue')
plt.xlabel('Mes')
plt.ylabel('Ganancia Real')
plt.title('Ganancia Real por mes')
plt.ylim(1000000000000)
plt.show()

print('4) Ganancias Reales vs Inversiones por Pais')
print('='*40)
ganancia_r_vs_inv= consolidado.groupby('country').agg({'investment':'max','revenue':'sum'}).reset_index()
ganancia_r_vs_inv=ganancia_r_vs_inv.rename(columns={'country':'Pais','revenue':'Ganancia_Real','investment':'Inversion'}).reset_index()
print(ganancia_r_vs_inv.sort_values(by='Inversion',ascending=False))
print('*'*60)
print()

plt.figure(figsize=(10,6))

#Utilizando el df ya creado de ganancia real se acomoda de menor a mayor
ganancia_sorted= ganancia_r_pais.sort_values(by='Ganancia Real')

#Se hace el grafico con el df anterior
plt.plot (ganancia_sorted['Pais'],ganancia_sorted['Ganancia Real'],marker= 'o', color='blue', label = 'Ganancia Real')

# Se genera el df con las inversiones por pais usando los maximos paa cada uno y uego se acomoda de menor a mayor
inv_pais= consolidado.groupby('country')['investment'].max().reset_index()
inv_pais_sorted=inv_pais.sort_values(by='investment')
inv_pais_sorted=inv_pais.rename(columns={'country':'Pais','investment':'Inversion'})

# Se crea el grafico con el df anterior
plt.plot (inv_pais_sorted['Pais'],inv_pais_sorted['Inversion'],marker= '*', color='red', label = 'Inversion')

plt.xlabel('Paises')
plt.ylabel('Valores')

plt.title('Ganancia real vs Inversiones')

plt.show()

relacion= pd.merge (inv_pais_sorted,ganancia_sorted,on='Pais')

relacion['ROI']=(relacion['Ganancia Real']/relacion['Inversion']).round(2)

plt.figure(figsize=(10,6))
plt.bar(relacion['Pais'],relacion['ROI'], color='blue')
plt.xlabel('Pais')
plt.ylabel('ROI')
plt.title('Ganancia Real vs Inversiones')

plt.show()

print('''5) Recomendamos realizar una auditoría en las sucursales de:
- Paraguay porque observamos que la ganancia real generada por nuestras sucursales en Paraguay es significativamente baja en comparación 
      con la inversión realizada. Esto podría deberse a ineficiencias operativas, falta de controles internos efectivos o incluso 
      posibles irregularidades. También a que se debería evaluar si el bajo volumen de las transacciones se debe a que no se está 
      maximizando el potencial de negocio y podrían existir oportunidades para mejorar la rentabilidad. Sumado a que las regulaciones 
      paraguayas (Art. 33 de la Ley 2421/04) requieren que las empresas con una facturación anual igual o superior a 9.201.143.662 guaraníes 
      (U$S 1.343.037) cuenten con un dictamen de auditoría externa impositiva. Con lo cual sería ideal adelantarnos para evitar cualquier posible desviación. 
- Uruguay porque su relación ganancia neta-inversión alta (12,81) indica que la empresa está generando una ganancia significativa en relación 
      con la cantidad de recursos invertidos. Esto podría ser positivo y sugerir una gestión eficiente de los activos y operaciones, la auditoría 
      nos permitiría conocer el contexto y el modelo de gestión que se podría aplicar a otros países. ''')


