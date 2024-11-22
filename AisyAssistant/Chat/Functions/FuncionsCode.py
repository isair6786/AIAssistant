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

def _readEvents(uid,correoUid):
    respuesta=FuncionsCode.api_leer_eventos(uid)
    return respuesta
def _readEmails(uid,correoUid):
    respuesta=FuncionsCode.api_leer_correos(uid)
    return respuesta

def _sheduleEvent(attendees,descripcion_evento,end,isAllDay,start,titulo,uid,correoUid):
    respuesta=FuncionsCode.api_agendar_evento(attendees,descripcion_evento,end,isAllDay,start,titulo,uid,correoUid)
    return respuesta

def _viewShedule(end,esRangodeFechas,start,uid,correoUid):
    respuesta=FuncionsCode.api_validar_horarios(end,esRangodeFechas,start,uid,correoUid)
    return respuesta