## coding: utf-8
def es_primo(n): 
    for i in range(2,n): # bucle i=2,3,...,n-1 
        if (n%i == 0):   # Si el resto al dividir n entre 
            return False # cualquier valor de i es 0, 
                         # n no es primo, devolvemos False
                         # y la rutina se acaba.
    
    # Si hemos llegado aqui, n no es divisible entre 
    # ningun valor de i, y por lo tanto es primo.
    return True 
"""for i in range(3,n-2):                           # Para i=3,4,...,n-3
    if ( (es_primo(i)) and (es_primo(n-i)) ):    # Si tanto i como n-i son primos
        print(n,"=",i,"+",n-i)           # Imprimimos y salimos
"""
def primos(n):
	primos=[]
	for i in range(2,n):
		primo=True
		for divisor in range (2,i):
			if i%divisor==0:
				primo=False
				break
		if primo:
			primos.append(i)
	return primos
while True:#filtro de numero par mayor que 2
	try:
		n = int(input("Ingrese un número:"))
		if (n%2==0) and (n>2):
			break
		int("x")#se fuerza error
	except:
		print("Se necesita un número entero par mayor que 2.")
 
print("Se monstrarán todas las combinaciones de suma de dos numeros primos que dan como resultado el numero ingresado")
l = 0
for i in primos(n):
	for j in primos(n):
		if i+j==n:
			if i==l:
				exit=True
				break
			l=j
			print(i,"+",j,"=",n)
	if exit==True:
		break
