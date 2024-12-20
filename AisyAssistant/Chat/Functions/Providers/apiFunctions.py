import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from Chat.Functions.Providers.functionsExtra  import Chat
gpt = Chat()
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
        fecha_actual = datetime.now().date() - timedelta(days=3)
        fecha_futura = fecha_actual + timedelta(weeks=1)
        print("La fecha actual es:", fecha_actual)
        print("La fecha fin es:", fecha_futura)
        URL = os.getenv('URL_API') + "/api/pythonGetCalendarEventsbyDate" + f"?uid={uid}&date={fecha_actual}&endDate={fecha_futura}"  # Asegúrate de que la URL esté correctamente configurada

        # Realizar la solicitud get con un timeout de 180 segundos (3 minutos)
        response = requests.get(URL, timeout=(30,90))  # Agregamos el timeout
        # Devuelve el contenido de la respuesta si es exitosa
        if response.text=="[]":
           return "agenda esta vacia"
        return response.text
    except requests.Timeout:
        print("Error al consultar los correos, el servicio no esta disponible por el momento , intente nuevamente ")
        return "Error al consultar los correos, el servicio no esta disponible por el momento , intente nuevamente "
    except requests.RequestException as e:
        print(f"Excepción al enviar la solicitud: {e}")
        return f"Error al realizar la solicitud: {e}"
def api_leer_correos(uid):

    try:
        URL = os.getenv('URL_API')+f"/api/pythonReadEmailbyProvider?uid={uid}"
        # Realizar la solicitud get
        response = requests.get(URL,timeout=(30,90))  # 'json' serializa automáticamente el dict en JSON
        return(response.text)
    except requests.Timeout:
        print("Error al consultar los correos, el servicio no esta disponible por el momento , intente nuevamente ")
        return "Error al consultar los correos, el servicio no esta disponible por el momento , intente nuevamente "
    except requests.RequestException as e:
        print(f"Excepción al enviar la solicitud: {e}")
        return f"Error al realizar la solicitud: {e}"

def api_validar_horarios(end,esRangodeFechas,start,uid,correoUid):
    print(end,esRangodeFechas,start,uid,correoUid)

    esRango=0
    if esRangodeFechas:
        esRango=1
    else:
       end = datetime.strptime(end, "%Y-%m-%d").date() + timedelta(days=1)
    try:
        URL = os.getenv('URL_API')+f"/api/getOnlyInfoShedule?uid={uid}&date={start}&endDate={end}&esRango={esRango}"
        # Realizar la solicitud get
        info = requests.get(URL,timeout=(60,120))  # 'json' serializa automáticamente el dict en JSON
        data = json.loads(info.text)
        response_calendar = data.get("response", None)  # Devuelve None si "response" no está presente

        response=gpt.realiza_peticion_interna(response_calendar)
        return(response)
    except requests.Timeout:
        print("Error al consultar agenda, el servicio no esta disponible por el momento , intente nuevamente ")
        return "Error al consultar agenda, el servicio no esta disponible por el momento , intente nuevamente "
    except requests.RequestException as e:
        print(f"Excepción al enviar la solicitud: {e}")
        return f"Error al realizar la solicitud: {e}"

def api_agendar_evento(attendees, descripcion_evento, end, isAllDay, start, titulo, uid, correoUid):
    try:
        URL = os.getenv('URL_API') + "/api/pythonSheduleEvent"
        payload = {
            "uid":uid,
            "correoUid":correoUid,
            "titulo":titulo,
            "descripcion_evento":descripcion_evento,
            "start":start,
            "end":end,
            "isAllDay":isAllDay,
            "attendees":attendees
        }
        print(payload)
        # Realizar la solicitud POST con los datos del evento
        response = requests.post(URL, json=payload)  # 'json' serializa automáticamente el dict en JSON
        print(response.text)
        return response.text
    except requests.RequestException as e:
        print(f"Excepción al enviar la solicitud: {e}")
        return False