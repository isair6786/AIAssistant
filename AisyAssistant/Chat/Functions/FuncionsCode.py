from datetime import datetime
def _getFecha():
    # Obtener la fecha y hora actual
    now = datetime.now()
    # Convertir la fecha y hora en una cadena de texto con el formato deseado
    cadena_fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
    return cadena_fecha_hora
    
def _sendMail(mensaje,correo):
    respuesta=f"""
    "correo":{correo},
    "mensaje":{mensaje},
    "resultado":"exitoso"
    """ 
    return respuesta