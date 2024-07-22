class Response: 
    def __init__(self,respuesta,funcion,resultado):
        self._Response={"respuesta":respuesta,"funcion":funcion,"resultado":resultado}
    
    def obtener_respuesta(self):
        return self._Response