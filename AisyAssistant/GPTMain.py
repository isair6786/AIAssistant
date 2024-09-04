from Chat.Chat import Chat
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

# Crear una instancia de la clase Chat
chat_instance = Chat()
app = FastAPI()

# Define el modelo de datos para la solicitud
class MessageRequest(BaseModel):
    contexto: str 

# Define el modelo de datos para la respuesta
class MessageResponse(BaseModel):
    responseMessage: str


"""
prompt_usuario = "Hola, ¿cómo estás? me llamo Kevin, quiero obtener la fecha y hora actual"
respuesta = chat_instance.realiza_peticion(prompt_usuario)
prompt_usuario = 'Ahora quiero enviar un correo a isair6786@gmail.com, y para el cuerpo creame un mensaje que le recuerde que tenemos una reunion el dia de mañana '
respuesta = chat_instance.realiza_peticion(prompt_usuario)
prompt_usuario = "puedes hacer una frase con mi nombre"
respuesta = chat_instance.realiza_peticion(prompt_usuario)
print(chat_instance.obtener_contexto())
print("fin") """

@app.post("/send-message/")
async def send_message(request: MessageRequest):
    try:
        print(request.contexto)

        
        respuesta = chat_instance.realiza_peticion_fe(json.loads(request.contexto))
        return MessageResponse(responseMessage=respuesta)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/google-auth/")
async def send_message(request: MessageRequest):
    try:
        print(request.contexto)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def send_message():
    return {"responseMessage": 'HolaMundo-Estado de API: Ejecucion'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)