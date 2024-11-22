functions = [
        {
            "type": "function",
            "function": {
            "name": "enviar_correo",
            "description": "Cuando el usuario confirme,se envia el correo a destinatarios, los correos deben ser separados por coma,como IA, el cuerpo debes formatearlo siempre en HTML ",
            "parameters": {
               "type": "object",
                "properties": {
                    
                    "emails": {
                        "type": "string",
                        "description": "is the emails to send the email, ej. santiago@gmail.com o santiago@gmail.com,santiago@gmail.com,etc ",
                    },
                    "body": {
                        "type": "string",
                        "description": "Is the body of email to send , must be in HTML FORMAT",
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
            "description": " Lee los eventos/agenda del calendario del usuario, el usuario debe indicar explicitamente palabras como ' Lee mi agenda , quiero ver mis eventos, mira mis horarios,etc'",
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
        #  {
        #     "type": "function",
        #     "function": {
        #     "name": "saludo_inicial",
        #     "description": "Responde al saludo inicial del usuario",
        #     "parameters": {            
        #     },
        #     }
        # }
       {
            "type": "function",
            "function": {
            "name": "agendar_evento",
            "description": "Crea/Agenda un evento en el calendario del usuario,obligatorio que el usuario verifique los datos y confirme antes de agendar, la año de fecha de inicio y fin debe ser mayor o igual al año actual  ",
            "parameters": {
               "type": "object",
                "properties": {
                    
                    "titulo": {
                        "type": "string",
                        "description": "Es el titulo del evento",
                    },
                    "descripcion_evento": {
                        "type": "string",
                        "description": "Es la descripcion del evento ",
                    },
                     "start": {
                        "type": "string",
                        "description": "el usuario brinda la Fecha de inicio  de la reunion (se formateará como este ejemplo 2024-11-26T20:00:00.000Z) ",
                    },
                     "end": {
                        "type": "string",
                        "description": "el usuario brinda la Fecha de finalizacion  de la reunion (se formateará como este ejemplo 2024-11-26T20:00:00.000Z ) ",
                    },
                    "isAllDay": {
                        "type": "boolean",
                        "description": "El usuario confirma si la reunion durará todo el dia o no",
                    },
                    "attendees": {
                        "type": "string",
                        "description": "correos de las personas invitadas separadas por coma",
                    }     
                    
                },
                "required": ["titulo","descripcion_evento","start","end","isAllDay","attendees"],
            }
            }
        },
         {
            "type": "function",
            "function": {
            "name": "analiza_agenda",
            "description": "Analiza la agenda del usuario y valida los horarios disponibles segun ya fea una fecha en especifico o un rango de fechas",
            "parameters": {
               "type": "object",
                "properties": {

                     "start": {
                        "type": "string",
                        "description": "el usuario brinda la Fecha de busqueda inicial (se formateará como este ejemplo 2024-11-26) ",
                    },
                     "end": {
                        "type": "string",
                        "description": "el usuario brinda la Fecha de busqueda final( formateará como este ejemplo 2024-11-26 ) ",
                    },
                    "esRangodeFechas": {
                        "type": "boolean",
                        "description": "El usuario confirma si se buscara solo en la fecha inicio o si se hará desde la fecha inicio a la fecha fin ",
                    }
                    
                },
                "required": ["start","end","esRangodeFechas"],
            }
            }
        }
    ]


