import random
n=int(input("¿Cuántas veces quiere realizar el experimento? "))
cont=0
for i in range(n):
	a=random.randint(2,10)
	b=random.randint(2,10)
	print("*"*50)	
	print(a,"*",b)	
	c=a*b
	intento=int(input("¿Cuánto es la multiplicación de los dos números pseudoaleatorios? "))
	if intento==c:
		print("Has acertado!!")
		cont+=1
if cont/n==1.0:
	print("Guau!! has acertado todas!!")
elif cont/n>0.75:
	print("Guau!! tu porcentaje de acierto es mayor a 75%!!")

