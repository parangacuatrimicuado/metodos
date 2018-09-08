n=int(input("Ingrese un número: "))
primos=[]
for i in range(2,n):
	primo=True
	for divisor in range (2,i):
		if i%divisor==0:
			primo=False
			break
	if primo:
		primos.append(i)
print("Hay",len(primos),"números primos antes de",n)

"""def es_primo(n): 
    for i in range(2,n):
        if (n%i == 0):
            return False
    return True """
