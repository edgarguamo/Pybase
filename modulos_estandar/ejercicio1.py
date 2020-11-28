def suma(a,b):
    try:
        r = a+b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return r

def subtraction(a,b):
    try:
        r = a-b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return r
 
def multiplicaction(a,b):
    try:
        r = a*b
    except TypeError:
        print("Error: Tipo de dato no valido")
    else:
        return r
def divide(a,b):
    try:
        r = a/b
    except TypeError:
        print("Error: Tipo de dato no valido")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    else:
        return r 


