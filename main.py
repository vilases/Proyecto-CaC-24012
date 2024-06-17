'''Importacion de modulos panda para los dataframes
   Importacion de modulo obtenerDatos para cargar el sheet de Goggle Drive
   Importacion de matplotlib para los graficos
'''
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
transacciones= consolidado.groupby('country')['transactions'].sum().reset_index()

transacciones=transacciones.rename(columns={'country':'Pais','transactions':'Transacciones'})
print(transacciones.sort_values(by='Transacciones',ascending=False))
print('*'*40)
print()

print('2c) Ganancias Reales por País')
print('='*25)
ganancia_r_pais= consolidado.groupby('country')['revenue'].sum().reset_index()
ganancia_r_pais=ganancia_r_pais.rename(columns={'country':'Pais','revenue':'Ganancia_Real'})
print(ganancia_r_pais.sort_values(by='Ganancia_Real',ascending=False))
print('*'*40)
print()

print('3) Ganancias Reales por Mes')
print('='*25)
ganancia_r_mes= consolidado.groupby('mes')['revenue'].sum().reset_index()
ganancia_r_mes=ganancia_r_mes.rename(columns={'mes':'Mes','revenue':'Ganancia_Real'})
print(ganancia_r_mes.sort_values(by='Mes'))
print('*'*40)
print()

print('4) Ganancias Reales vs Inversiones por Pais')
print('='*40)
ganancia_r_vs_inv= consolidado.groupby('country').agg({'investment':'max','revenue':'sum'}).reset_index()
ganancia_r_vs_inv=ganancia_r_vs_inv.rename(columns={'country':'Pais','revenue':'Ganancia_Real','investment':'Inversion'}).reset_index()
print(ganancia_r_vs_inv.sort_values(by='Inversion',ascending=False))
print('*'*60)
print()
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

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.bar(transacciones['Pais'],transacciones['Transacciones'],color='skyblue')
plt.title('Transacciones por País')
plt.xlabel('País')
plt.ylabel('Transacciones')

plt.subplot(1,2,2)
plt.bar(ganancia_r_pais['Pais'],ganancia_r_pais['Ganancia_Real'],color='lightgreen')
plt.title('Ganancia Real por País')
plt.xlabel('País')
plt.ylabel('Ganancia Real')

'''
plt.subplot(2,1,1)
plt.bar(ganancia_r_mes['Mes'],ganancia_r_mes['Ganancia_Real'],color='magenta')
plt.title('Ganancia Real por Mes')
plt.xlabel('Mes')
plt.ylabel('Ganancia Real')

plt.subplot(2,2,2)
plt.plot(ganancia_r_vs_inv['Pais'],ganancia_r_vs_inv['Ganancia_Real'], marker='o', color='red', label='Revenue')

plt.twinx()
plt.plot(ganancia_r_vs_inv['Pais'],ganancia_r_vs_inv['Ganancia_Real'], marker='o', color='blue', label='Revenue')

plt.title('Ganancia Real vs Impuestos por Pais')
plt.xlabel('Pais')
plt.ylabel('Valores')

'''
plt.tight_layout()
plt.show()



