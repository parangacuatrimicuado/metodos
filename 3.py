import math
def es_primo(n): 
	for i in range(2,n): 
		if n%i==0: 
			return False 
	return True
num=int(input("Ingrese numero:"))
n=math.log2(num+1)
nlista=[]
nent=n-int(n)
print(nent)
if nent==0.0:
	print("Es un número de mersenne")
else:
	print("No es un número de mersenne")
"""USANDO LISTA
for i in str(n):
	nlista+=i
indice=nlista.index(".")
if nlista[indice+1:]==["0"] and es_primo(num):
	print("Es un número de mersenne")
else:
	print("No es un número de mersenne")"""
