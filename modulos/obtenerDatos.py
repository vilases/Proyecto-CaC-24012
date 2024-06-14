from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from modulos.config import CON

# SCOPES=['https://www.googleapis.com/auth/spreadsheets']
# KEY= 'proyecto-cac-24012-f9cb5f939850.json'
# SPREADSHEETS_ID='1u2IO5cPIJ_d6vYp4oQHQ7fBq7pxB0Wy3U9aIATfrGOY'
def cargar_sheet():
    creds= None
    creds= service_account.Credentials.from_service_account_file(CON['KEY'],scopes=CON['SCOPES']) 

    service = build('sheets', 'v4', credentials=creds)
    sheet= service.spreadsheets()

    result = sheet.values().get(spreadsheetId=CON['SPREADSHEET_ID'],range='consolidado!A1:E9607').execute()
    consolidado=result.get('values',[])
    # print (consolidado)

    return consolidado

# a=cargar_sheet()
# \