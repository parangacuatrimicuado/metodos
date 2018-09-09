def binario(x):
	
	valores = {
	'1001' : 9,	
	'1000' : 8,	
	'0111' : 7,        
	'0110' : 6,
        '0101' : 5,
        '0100' : 4,
        '0011' : 3,
        '0010' : 2,
        '0001' : 1,
        '0000' : 0
	}
	
	lx = list(x)
	r = len(lx)
	L = ""
	Lb = ""
	N = ""
	for i in range(r):
		try:
			L += str(int(lx[i]))
			if i == r-1:
				for j in range(4-len(L)):
					Lb += "0"
				Lb += L
				N += str(valores[Lb])
				continue
		except:
			for k in range(4-len(L)):
				Lb += "0"
			Lb += L
			N += str(valores[Lb])
			L = ""
			Lb= ""
			continue
	return N

n = input("ingrese el numero binario separando con un _ entre cuartetos binarios:")
print("el numero es: ",binario(n))
