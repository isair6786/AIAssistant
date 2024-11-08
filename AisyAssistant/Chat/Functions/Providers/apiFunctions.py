import requests
import os
from dotenv import load_dotenv


def api_enviar_correo(payload):

    try:
        URL = os.getenv('URL_API')  # Asegúrate de que la URL esté correctamente configurada

        print(payload)
        _headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        # Realizar la solicitud POST
        response = requests.post(URL+"/api/sendEmailbyProvider",json =payload,headers=_headers)  # 'json' serializa automáticamente el dict en JSON
        return(response.text)
    except requests.RequestException as e:
        print(f"Excepción al enviar la solicitud: {e}")
        return False

def api_leer_eventos(fecha_desde,fecha_hasta,uid):

    try:
        URL = os.getenv('URL_API')+"/api/getCalendarEventsbyDate" + f"?uid={uid}&date={fecha_desde}&endDate={fecha_hasta}"  # Asegúrate de que la URL esté correctamente configurada
        print(f" {fecha_desde},{fecha_hasta},{uid}")
        # Realizar la solicitud get
        response = requests.get(URL)  # 'json' serializa automáticamente el dict en JSON
        return(response.text)
    except requests.RequestException as e:
        print(f"Excepción al enviar la solicitud: {e}")
        return False
def api_leer_correos(uid):

    try:
        URL = os.getenv('URL_API')+f"/api/readEmailbyProvider?uid={uid}"
        # Realizar la solicitud get
        response = requests.get(URL)  # 'json' serializa automáticamente el dict en JSON
        return(response.text)
    except requests.RequestException as e:
        print(f"Excepción al enviar la solicitud: {e}")
        return False