functions = [
        {
            "type": "function",
            "function": {
            "name": "obtener_fecha",
            "description": "Obtiene la fecha y hora actual",
            "parameters": {
            }
            }
        },
        {
            "type": "function",
            "function": {
            "name": "enviar_correo",
            "description": "Enviar Correo a destinatarios",
            "parameters": {
               "type": "object",
                "properties": {
                    "destinatarios": {
                        "type": "string",
                        "description": "El correo electrónico de los destinatarios, ej. santiago@gmail.com o santiago@gmail.com,santiago@gmail.com,etc",
                    },
                    "cuerpo": {
                        "type": "string",
                        "description": "El cuerpo del correo a enviar",
                    },
                    
                },
                "required": ["destinatarios","cuerpo"],
            },
            }
        }
    ]


