import datetime

dt = datetime.datetime.now() #Ahora
print('impresion de la fecha actual')
print(dt)
print("{}:{}:{}".format(dt.hour,dt.minute, dt.second))
print("{}/{}/{}".format(dt.day,dt.month, dt.year))
#Creacion de una fecha
#La estructura que se emplea es la tupla
ndt = datetime.datetime(2000,1,1)
print(ndt)
ndt = ndt.replace(year=3000)
print(ndt)
#formateo segun las normas ISO
print(dt.isoformat())
#Formateo manual Clase 86
#libreria para gestionar el idioma local
import locale 
#locale.setlocale(locale.LC_ALL,'es-ES')
newdt = dt.strftime("%A %d %B %Y %I:%M")
print(newdt)
#Sumar tiempo
time = datetime.timedelta(days=14,hours=2,seconds=30)
twl = dt + time
print(twl)
#Zonas Horarias 
#Necesitas instalar un modulo manualmente
import pytz

pytz.all_timezones
dt2 = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
dt2 = dt2.strftime("%A %d %B %Y %I:%M")
print(dt2)

royer_age = datetime.datetime(1998,11,28)
print(dt - royer_age) 
royer_age = dt - royer_age
