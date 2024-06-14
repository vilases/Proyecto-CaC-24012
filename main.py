import pandas as pd
from modulos.obtenerDatos import cargar_sheet

data = cargar_sheet()
df = pd.DataFrame (data[1:], columns = data[0])
print (df)
