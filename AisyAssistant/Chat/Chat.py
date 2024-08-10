import openai
import Chat.Functions.FuncionsGPT as FuncionsGPT 
import json
import Chat.Functions.FuncionsCode as FuncionsCode 
import os
from dotenv import load_dotenv

class Chat:
    def __init__(self):
        # Obtener la ruta del directorio del script actual
        script_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        load_dotenv()
        # Construir la ruta al archivo token.txt
        #token_file = os.path.join(script_dir,  "token.txt")
        self._context=[]
        #with open(token_file) as f:
        openai.api_key = os.getenv('API_KEY')

            
    def obtener_contexto(self):
        return self._context
    
    #Metodo Privado
    def _obtener_completion(self,mensajes, model="gpt-3.5-turbo-0125"):
        respuesta = openai.chat.completions.create(
            model=model,
            messages=mensajes,
            tools=FuncionsGPT.functions,
            tool_choice="auto"
        )
        return respuesta.choices[0].message
    
    def _obtener_completion_function(self,mensajes, model="gpt-3.5-turbo-0125"):
        respuesta = openai.chat.completions.create(
            model=model,
            messages=mensajes
        )
        return respuesta.choices[0].message
     #Metodo Privado
    def _concatenar_chat(self,chat):
        self._context.append(chat)
   
    def realiza_peticion(self,prompt_user):
        self._concatenar_chat({'role':'user', 'content':f"{prompt_user}"})
        respuesta=self._analiza_respuesta(self._obtener_completion(self.obtener_contexto()))
        return respuesta
    #Esta funcion recibe el contexto de los mensajes con el ultimo 
    #mensaje del usuario para obtener la respuesta 
    def realiza_peticion_fe(self,mensajes):
        respuesta=self._analiza_respuesta(self._obtener_completion(mensajes))
        return respuesta
    
    def _analiza_respuesta(self,respuesta):
        
        message=respuesta.content
        llamadas_funciones = respuesta.tool_calls
        if llamadas_funciones:
            available_functions = {
            "obtener_fecha": FuncionsCode._getFecha,
            "enviar_correo": FuncionsCode._sendMail,
            }  
            
            for funcion in llamadas_funciones:
                function_name = funcion.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(funcion.function.arguments)
                if len(function_args)>0:
                    sorted_args = [function_args[arg_name] for arg_name in sorted(function_args.keys())]
                    function_response = function_to_call(*sorted_args)
                else:
                    function_response = function_to_call()
            #Concatenamos tollcalls
            self._concatenar_chat(
                {
                    "tool_calls": llamadas_funciones,
                    "role": "assistant",
                }
            ) 
            # Enviamos la respuesta de la función a GPT
            self._concatenar_chat(
                {
                    "tool_call_id": funcion.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # Contenido de la funciónno
            response_message = self._obtener_completion_function(self.obtener_contexto())
            message=response_message.content
        #Si no hay funcion a invocar solo guardamos lo que ya respondio
        self._concatenar_chat({'role':'assistant', 'content':f"{message}"})
        return message
    
   