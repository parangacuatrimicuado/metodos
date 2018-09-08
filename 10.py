def es_primo(n): 
	for i in range(2,n): 
		if n%i==0: 
			return False 
	return True
#Primera pregunta:
cont=0
for i in range(2,10000):
	if es_primo(i):
		if str(i)[-1]=="7":
			cont+=1
print("Hay",cont,"numeros primos terminados en 7 antes que 10000")
#Segunda pregunta ¿Cual es la suma de los cuadrados de los numeros primos entre x e y?:
x=int(input("Ingrese primer valor: "))
y=int(input("Ingrese segundo valor: "))
sum=0
for i in range(x,y+1):
	if es_primo(i):
		sum+=i**2
print("La suma de los cuadrados de los numeros primos entre",x,"y",y,"es:",sum)
#Tercera pregunta ¿Cual es el producto de todos los primos menores que x que tengan algun digito 7?:
multi=1
cuentas=0
x=int(input("Ingrese x:"))
for i in range(2,x):
	if es_primo(i):
		if "7" in str(i):
			multi*=i
			cuentas+=1
if cuentas>0:
	print("La multiplicacion de los numeros primos que contienen al menos un digito 7 menores que",x,"es:",multi)
else:
	print("No existe la multiplicacion")
