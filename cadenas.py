mayus = "hola mundo".upper()
minus = "hola mundo".lower()
#mayus solo la la primera letra de la cadena 
capi = "hola mundo".capitalize()
#mayus la primera letra de todas las palabras 
title = "hola mundo".title()
#Buscaruna en que posicion se encuentra un caracter
f = "hola mundo".find("mundo")
#find nos muestra la primera coincidencia 
# para buscar la ultima 
rf = "hola mundo mundo mundo".rfind("mundo")
#Para verificar si un dato es un digito 
d = 100
"hola mundo".islower()
"hola mundo".isspace()
"hola mundo".isalnum()

#mostrar la ultima palabra 
"contigo pipo dijo alex llorando enn el banio".split()[1]
#Separar la cadena en un arreglo
"contigo pipo dijo alex llorando enn el banio".split(',')
#Eliminar los espacios
"       ,      ".strip()
#Reemplazar palabras 
"hola mundo".replace("mundo", "marte")
"hola mundo mundo mundo mundo".replace("mundo","",3)
