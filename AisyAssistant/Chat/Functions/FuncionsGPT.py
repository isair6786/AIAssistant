functions = [
        {
            "type": "function",
            "function": {
            "name": "enviar_correo",
            "description": "Cuando el usuario confirme,se envia el correo a destinatarios, los correos deben ser separados por coma ",
            "parameters": {
               "type": "object",
                "properties": {
                    
                    "emails": {
                        "type": "string",
                        "description": "is the emails to send the email, ej. santiago@gmail.com o santiago@gmail.com,santiago@gmail.com,etc ",
                    },
                    "body": {
                        "type": "string",
                        "description": "Is the body of email to send",
                    },
                     "subject": {
                        "type": "string",
                        "description": "is the subject of email to send ",
                    },
                    "cc": {
                        "type": "string",
                        "description": "CC",
                    },
                    "bcc": {
                        "type": "string",
                        "description": "BCC",
                    }     
                    
                },
                "required": ["body","cc","bcc","emails","subject"],
            },
            }
        },
        {
            "type": "function",
            "function": {
            "name": "leer_agenda",
            "description": " Lee los eventos,agenda del calendario del usuario , de las cuentas asociadas",
            "parameters": {       

                }   ,
            }
        },
        {
            "type": "function",
            "function": {
            "name": "leer_correos",
            "description": " Lee los correos,emails de las cuentas del usuario , de las cuentas asociadas",
            "parameters": {            
            },
            }
        },
         {
            "type": "function",
            "function": {
            "name": "saludo_inicial",
            "description": "Responde al saludo inicial del usuario",
            "parameters": {            
            },
            }
        }
       
    ]


