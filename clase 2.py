##from math import  sqrt
##a= 64
##raiz= sqrt(a)
##p(raiz)
##
##from math import sqrt
##b= 90
##gabito= sqrt(b)
##print(gabito)
##
####Funciones
##def operacion(persona,numero):
##    mayor_edad= numero>18
##    if mayor_edad == True:
##        return('si es mayor')
##    else:
##        return('menor de edad')
##
##def operacion(numero1,numero2):
##    R=numero1*numero2
##    return(R)
##print('ingresar primer valor')
##A= int(input())
##print('ingresar segundo valor')
##B= int(input())
##
##resultado= operacion(A,B)
##print('su resultado es:',resultado)


##nombre= 'Gabo'
##edad= 18
##resultado= operacion(nombre,edad)
##print(resultado)

from math import sqrt
import math
def manhattan (coord1,coord2):
    x0, y0 = coord1
    x1, y1 = coord2
    return(x1-x0) + (y1-y0)

def euclidiana (coord1, coord2):
    x0, y0 = coord1
    x1, y1 = coord2
    return math.sqrt(abs(x1-x0)**2 + abs(y1-y0)**2)

P1 = (8,10)
P2 = (15,23)

Resultado_Manhattan = manhattan(P1,P2)
Resultado_Euclidiana = euclidiana(P1,P2)
print("Distancia Manhattan:",Resultado_Manhattan)
print("Distancia Euclidiana:",Resultado_Euclidiana)




 







