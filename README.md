# Codo a Codo comision 24012

Proyecto de visualizacion de Estadisticas hecho en Python con el modulo Pandas.

Se crea una carpeta con el modulo de conexion al archivo de Google Sheets y obtencion de la lista con los datos y el modulo con los datos de configuracion de la conexion.

El programa principal main.py crea el Data Frame a partir de la lista enviada por el modulo y prepara los datos para hacer las Estadisticas. Con el modulo Matplotlib se hacen las visualizaciones.

Primero que nada hay que crearse en Google una cuenta de cloud para poder leer el googlesheet guardado en Drive,
crear las credenciales y la coneccin con la API de google. 
El archivo .json vacio esta para indicar en donde lo va a buscar el script pero siempre se puede cambiar el directorio con el modulo OS.
