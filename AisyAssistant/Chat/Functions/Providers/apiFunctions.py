import requests
import os
from dotenv import load_dotenv
from datetime import datetime



def api_enviar_correo(payload):

    try:
        URL = os.getenv('URL_API')  # Asegúrate de que la URL esté correctamente configurada

        _headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        # Realizar la solicitud POST
        response = requests.post(URL+"/api/sendEmailbyProvider",json =payload,headers=_headers)  # 'json' serializa automáticamente el dict en JSON
        return(response.text)
    except requests.RequestException as e:
        print(f"Excepción al enviar la solicitud: {e}")
        return False

def api_leer_eventos(uid):

    try:
       # Obtener la fecha actual
        fecha_actual = datetime.now().date()
        print("La fecha actual es:", fecha_actual)
        URL = os.getenv('URL_API')+"/api/pythonGetCalendarEventsbyDate" + f"?uid={uid}&date={fecha_actual}&endDate={fecha_actual}"  # Asegúrate de que la URL esté correctamente configurada

        # Realizar la solicitud get
        response = requests.get(URL)  # 'json' serializa automáticamente el dict en JSON
       
        return(response.text)
    except requests.RequestException as e:
        print(f"Excepción al enviar la solicitud: {e}")
        return False
def api_leer_correos(uid):

    try:
        URL = os.getenv('URL_API')+f"/api/pythonReadEmailbyProvider?uid={uid}"
        # Realizar la solicitud get
        response = requests.get(URL)  # 'json' serializa automáticamente el dict en JSON
        return(response.text)
    except requests.RequestException as e:
        print(f"Excepción al enviar la solicitud: {e}")
        return False