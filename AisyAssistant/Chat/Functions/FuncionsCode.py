from datetime import datetime
import Chat.Functions.Providers.apiFunctions as FuncionsCode
import json

def _sendMail(bcc,body,cc,emails,subject,uid,correoUid):

    payload = {
    "uid":uid,
    "correoUid":correoUid,
    "subject":subject, 
    "body":body, 
    "toRecipients":emails,
    "toCCRecipients":cc, 
    "toBCCRecipients":bcc
    }

    respuesta=FuncionsCode.api_enviar_correo(payload)
    
    return respuesta
def _readEvents(fecha_desde,fecha_hasta,uid,correoUid):

    respuesta=FuncionsCode.api_leer_eventos(fecha_desde,fecha_hasta,uid)
    
    return respuesta
def _readEmails(uid,correoUid):

    respuesta=FuncionsCode.api_leer_correos(uid)
    
    return respuesta
def _sayHiChat(uid,correoUid):

    respuesta=F"Hola! Soy Shedzy! Tu asistente virtual , ¿Cómo puedo ayudarte hoy?"
    
    return respuesta