from CalendarFunctions import CalendarFunctions


calendar_instance = CalendarFunctions()
calendar_instance.get_by_calendar_id()
response=calendar_instance.create_calendar({"nombre":"PruebaCalendario"})
print(response)
response=calendar_instance.create_event("PruebaCalendario","Evento Prueba","Test","Prueba de evento","isair6786@gmail.com;kevinmendoza261@gmail.com","11/05/2024 19:30:00","11/05/2024 20:00:00")
print(response)
response=calendar_instance.create_recurrent_event("PruebaCalendario","Evento Prueba","Test","Prueba de evento","isair6786@gmail.com;kevinmendoza261@gmail.com","16/07/2024 19:30:00","16/07/2024 20:00:00")
print(response)