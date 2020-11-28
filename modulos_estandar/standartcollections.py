#contadores: sub-clase del diccionario que permiten contar cuantas veces se repitio x caracter 

from collections import Counter

list = [1,2,3,4,2,1,1,1,5,4,2,3,3]

Counter(list) 
print(Counter(list))

colores = "rojo verde azul lila lila azul rojo rojo"
print(Counter(colores))

print(Counter(colores.split()))

c = Counter(colores.split())

print(c.most_common(1)) #el numero son los elementos que se presentaran 

list2 = [10,20,30,40,10,20,30,10,20,10]
c = Counter(c)
print(c.items)
print(c.keys)
print(c.values)
print(sum(c.values())) 
dict(c)
# Creacion de diccionarios que cuando no se encuentre la clave no lance error
from collections import defaultdict

d = defaultdict(str)
d ['algo']
print(d)
# Los diccionarios son colecciones desordenadas 

n={}
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] ='three'

print(n)

from collections import OrderedDict

n2 = OrderedDict([('uno','one'),('dos','two')])
print(n2)
