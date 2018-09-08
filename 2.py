romanos={"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
num=input("Ingrese numero que quiere transformar:").upper()
print(num)
letras=list(num)
resultado = 0
anterior=0
for i in letras:
	if i in romanos:
		actual=romanos[i]
		if anterior >= actual:
			resultado+=actual
		else:
			#resultado=(resultado-anterior)+(actual-anterior)
			resultado+=actual-2*anterior
	else:
		print("numero invalido")
	
print(resultado)
