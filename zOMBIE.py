import math as mt
import numpy as np
import matplotlib as np
from pprint import pprint
#El mundo está sumido en el caos, se ha desatado una pandemia, la cual provoca
# que los humanos infectados se transformen en muertos vivientes, es necesario
#sobrevivir, por lo cual la consigana es los humanos deben matar a los muertos
#vivientes, sin embargo este no es el unico problema, pues muchas veces y por
#sobrevivencia los humanos también matan a otros humanos, es necesario construir
#un algoritmo para clasificar a los miembros de los grupos de sobrevivientes,
#supongan las estadisticas de este grupo se encuentren en forma de diccionario,
#cuya clave es el nombre del miembro del grupo y un valor en forma de tupla,
# con la cantidad de no vivos y humanos que ha matado

# a)desarolle la función "total_grupo" que recibe como parametro un diccionario,
# retornando como una tupla el total de no vivos y el total de humanos eliminados

# b) Desarrolle la funcion puntaje_grupo que reciba el mismo diccionario y retorne un nuevo
#diccionario que le asigne un puntaje a cada miembro del grupo
#ptje=(z/(t_z+2))*(h/t_h)

# c)retorne una lista con los nombres ordenados de mayor a menor con los puntajes definidos
# en la funcion anterior.def total_grupo(diccionario):

def total_grupo(diccionario):
    lista=list(diccionario.keys())
    zombie=[]
    humanos=[]
    tuplas=()
    for i in lista:
        tuplas=diccionario.get(i)
        zombie+=[tuplas[0]]
        humanos+=[tuplas[1]]
    return(sum(zombie),sum(humanos))

def puntaje_grupo(diccionario):
    total=total_grupo(diccionario)
    lista=list(diccionario.keys())
    tuplas=()
    puntaje_dic={}
    for i in lista:
        tuplas=diccionario.get(i)
        puntaje=((tuplas[0]/(total[0]+2))*(tuplas[1]/total[1]))
        puntaje_dic[i]=(puntaje)
    return puntaje_dic
#
grupo={'Fran': (4,5),'Alex':(2,4),'Anton':(5,1),'Argoz':(4,2)}
print(total_grupo(grupo))
puntaje=puntaje_grupo(grupo)
lsit=sorted(puntaje.items(), key=lambda x: x[1])
print(lsit) #
