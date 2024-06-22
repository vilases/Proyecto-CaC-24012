# Importacion de librerias para trabajar con API de Goggle
# Importacion de constante del modulo config

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from modulos.config import CON

# Funcion que conecta con la API y devuelve una lista con los valores de la hoja de Google Sheets indicada en el rango pedido 
# (mas adelante tanto los rangos como las hojas podran ser ingresados por el usuario)

def cargar_sheet(rango):
    creds= None
    creds= service_account.Credentials.from_service_account_file(CON['KEY'],scopes=CON['SCOPES']) # Crea la variable con los datos de la "key" para conectar la API

    service = build('sheets', 'v4', credentials=creds) #Conecta con el servicio
    sheet= service.spreadsheets() #Genera el objeto de "sheet"

    result = sheet.values().get(spreadsheetId=CON['SPREADSHEET_ID'],range=rango).execute() # Carga en el objeto los datos de la sheet de Google pedido con la constante
    consolidado=result.get('values',[]) # Guarda los valores en una lista que es lo que retorna la funcion
    #print (consolidado)

    return consolidado

# \