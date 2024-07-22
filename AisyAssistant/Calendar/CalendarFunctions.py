import datetime
import os.path
from Class.Response import Response
from dateutil import parser

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


#Para el uso de diferentes chats , se debe crear una funcion
#para guardar las credenciales de cada usuario luego de loguearse con google desde flutter 
class CalendarFunctions:
    
    def __init__(self):
        self._creds = None
        script_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        credencials_path=os.path.join(script_dir, "Calendar","Secret", "credentials.json")
        token_path=os.path.join(script_dir, "Calendar","Secret", "token.json")
        if os.path.exists(token_path):
            self._creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self._creds or not self._creds.valid:
         if self._creds and self._creds.expired and self._creds.refresh_token:
            self._creds.refresh(Request())
         else:
            script_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            credencials_path=os.path.join(script_dir, "Calendar","Secret", "credentials.json")
            print(credencials_path)
            flow = InstalledAppFlow.from_client_secrets_file(
                credencials_path, SCOPES
            )
            self._creds = flow.run_local_server(port=8530)
            # Save the credentials for the next run
            with open(token_path, "w") as token:
                token.write(self._creds.to_json())
        try:
            self._service = build("calendar", "v3", credentials=self._creds)
        except HttpError as error:
            print(f"An error occurred: {error}") 
            
    def _get_service(self):
        return self._service
    
    #region Funciones Busqueda y obtencion de datos de los calendarios    
    def get_list_calendars(self):
        service=self._get_service()
        print("Aca estamos")
        page_token = None
        while True:
            calendar_list = service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                print(calendar_list_entry['summary'])
                page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
    #Funcion que devuelve el dato del calendario buscado por id       
    def get_by_calendar_id(self,id='primary'):
        service=self._get_service()
        print("imprimiendo calendario")
        calendar_list_entry = service.calendarList().get(calendarId=id).execute()
        data = [{"TimeZone":calendar_list_entry['timeZone'],
                 "Id":calendar_list_entry['id'],
                 "Summary":calendar_list_entry['summary']}]
        print(data)
    ##Funcion que devuelve los id de calendarios buscado por nombre
    def get_id_calendar_by_summary(self,summary):
        print("Aca estamos")
        service=self._get_service()
        page_token = None
        encontrado= False
        id=''
        while True:
            calendar_list = service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                if calendar_list_entry['summary'].upper()== summary.upper():
                    encontrado=True
                    id=calendar_list_entry['id']
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
            if encontrado:
                break 
        return id
    #endregion
    #region Funciones CRUD calendario
    def create_calendar(self,dataCalendar):
        service=self._get_service()
        id=""
        exito=False
        mensaje=""
        id=self.get_id_calendar_by_summary(dataCalendar["nombre"])
        try:
           if id=="":
            calendar = {
                'summary': dataCalendar["nombre"],
                'timeZone': 'America/El_Salvador'
            }
            created_calendar = service.calendars().insert(body=calendar).execute()
            id =created_calendar['id']
            mensaje=f"Se creo el id: {id}"
            exito=True
           else:
            mensaje=f"ya existe un calendario con este nombre"  
        except Exception as e:
            exito=False
            mensaje=e
        # end try
        
        response = Response("Exito" if exito else "Error","create_calendar",f"{mensaje}")
        return response.obtener_respuesta()
    #endregion
    #region Eventos 
    #Crea un evento en el calendario
    def create_event(self,nombreCalendario,titulo,direccion, descripcion, correos,fechainicio, fechafin):
        service=self._get_service()
        id=""
        exito=False
        mensaje=""
        id=self.get_id_calendar_by_summary(nombreCalendario)
        
        try:
            if id!="":
                fechainicio = self.convertir_formato_fecha(fechainicio)
                fechafin = self.convertir_formato_fecha(fechafin)
                correos_formateados=self.convertir_a_formato_deseado(correos)
                print(correos_formateados)
                if fechainicio is not None and fechafin is not None:
                    event = {
                        'summary': titulo,
                        'location': direccion,
                        'description': descripcion,
                        'start': {
                            'dateTime': fechainicio,
                            'timeZone': 'America/El_Salvador',
                        },
                        'end': {
                            'dateTime': fechafin,
                            'timeZone': 'America/El_Salvador',
                        },
                        'recurrence': [
                            'RRULE:FREQ=DAILY;COUNT=1'
                        ],
                        'attendees': 
                            correos_formateados
                        ,
                        'reminders': {
                            'useDefault': False,
                            'overrides': [
                            {'method': 'email', 'minutes': 24 * 60},
                            {'method': 'popup', 'minutes': 10},
                            ],
                        },
                    }
                    event = service.events().insert(calendarId=id, body=event).execute()
                    id = event.get('htmlLink')
                    mensaje=f"Se creo el Evento solicitado , la url es : {id}"
                    exito=True
                else:
                    mensaje=f"No se pudo convertir la fecha."  
            else:
                mensaje=f"No existe el calendario para crear el evento"  
        except Exception as e:
            exito=False
            mensaje=e
        # end try
        
        response = Response("Exito" if exito else "Error","create_calendar",f"{mensaje}")
        return response.obtener_respuesta()
    #Este metodo se usa en create_event para formatear la cadena de correos 
    # que se reciben 
    def convertir_a_formato_deseado(self,correos):
        correos_lista = correos.split(';')  # Dividir la cadena en una lista de correos electrónicos
        correos_formateados = []
        for correo in correos_lista:
            nombre, dominio = correo.split('@')  # Dividir el correo en nombre de usuario y dominio
            correo_formateado = {'email': f'{nombre}@{dominio}'}  # Formatear en el formato deseado
            correos_formateados.append(correo_formateado)
        return correos_formateados
    
    #Metodo para conversion de fecha en formato esperado 
    def convertir_formato_fecha(self,cadena_fecha):
        try:
            # Intenta analizar la cadena de fecha en el formato dado
            fecha = datetime.datetime.strptime(cadena_fecha, "%d/%m/%Y %H:%M:%S")
            # Luego formatea la fecha al formato deseado
            fecha_formateada = fecha.strftime("%Y-%m-%dT%H:%M:%S%z")
            return fecha_formateada
        except ValueError:
            print("La cadena de fecha no está en el formato esperado.")
            return None
        
    ## Falta proceso para eventos recurrentes , para cancelar eventos ,
    # para modificar eventos ,y estados fuera de oficina 
    
    #Metodo para eventos recurrentes
    def create_recurrent_event(self,nombreCalendario,titulo,direccion, descripcion, correos,fechainicio, fechafin):
        service=self._get_service()
        id=""
        exito=False
        mensaje=""
        id=self.get_id_calendar_by_summary(nombreCalendario)
        
        try:
            if id!="":
                fechainicio = self.convertir_formato_fecha(fechainicio)
                fechafin = self.convertir_formato_fecha(fechafin)
                correos_formateados=self.convertir_a_formato_deseado(correos)
                print(correos_formateados)
                if fechainicio is not None and fechafin is not None:
                    event = {
                        'summary': titulo,
                        'location': direccion,
                        'description': descripcion,
                        'start': {
                            'dateTime': fechainicio,
                            'timeZone': 'America/El_Salvador',
                        },
                        'end': {
                            'dateTime': fechafin,
                            'timeZone': 'America/El_Salvador',
                        },
                        'recurrence': [
                            'RRULE:FREQ=WEEKLY;UNTIL=20110701T170000Z',
                        ],
                        'attendees': 
                            correos_formateados
                        ,
                        'reminders': {
                            'useDefault': False,
                            'overrides': [
                            {'method': 'email', 'minutes': 24 * 60},
                            {'method': 'popup', 'minutes': 10},
                            ],
                        },
                    }
                    event = service.events().insert(calendarId=id, body=event).execute()
                    id = event.get('htmlLink')
                    mensaje=f"Se creo el Evento solicitado , la url es : {id}"
                    exito=True
                else:
                    mensaje=f"No se pudo convertir la fecha."  
            else:
                mensaje=f"No existe el calendario para crear el evento"  
        except Exception as e:
            exito=False
            mensaje=e
        # end try
        
        response = Response("Exito" if exito else "Error","create_recurrent_event",f"{mensaje}")
        return response.obtener_respuesta()
    
    def armar_recurrencia():
        recurrencia ="RRULE:FREQ=WEEKLY;COUNT=5;BYDAY=TU,FR"
        
        return recurrencia
    #endregion
    
    