import pandas as pd
from modulos.obtenerDatos import cargar_sheet
import matplotlib.pyplot as plt

data = cargar_sheet()
df = pd.DataFrame (data[1:], columns = data[0])
df['transactions'] = df['transactions'].astype(int)
df['gross_margin'] = df['gross_margin'].astype(float)
print(df.dtypes)

df['gross_margin'].plot.hist(bins = 20)
print (df)
plt.show()