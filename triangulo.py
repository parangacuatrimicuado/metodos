B = int(input("ingrese el largo de la base del triangulo (numero entero): "))
T=B
for i in range(B):
	for r in range(i):
		print(" ",end=" ")
	for j in range(T):
		print("* ",end=" ")
	print(" ")	
	T -= 1
