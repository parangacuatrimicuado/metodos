import math as m

def primo(x):
	for i in range(2,x):
		if x%i == 0:
			return False
	return True

N = int(input("ingrese un numero: "))
n1 = N + 1
cont=0
while True:
	cont += 1
	S = 2**cont
	if n1 == S:
		n = m.log2(S)
		n = int(n)
		if primo(n):
			print("es un numero de mersenne!")
			break
		continue
	if S > N:
		print("no es un numero de mersenne")
		break	
