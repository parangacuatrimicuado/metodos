a=str(input("Ingrese numero: "))
lista=[]
listainv=[]
for i in a:
	lista.append(int(i))
	listainv.append(int(i))
#print(lista)
#print(listainv[::-1])
if lista==listainv[::-1]:
	print("Es palindromo")
else:
	print("No es palindromo")
