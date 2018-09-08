lista=[]
hora=input("Ingrese hora: ")
for i in range(0,len(hora),5):
	lista+=[hora[i:i+4]]
#print(lista)
if "1111" in lista:
	lista2=lista[lista.index("1111")+1:]
	#print(lista2)
	#print(len(lista2))
	if "1111" in lista2 or len(lista2)>4:
		print("Hora no valida")
	else:
		a=lista2[0]
		al=[]
		for i in a:
			al+=i
		hora1=int(al[0])*8+int(al[1])*4+int(al[2])*2+int(al[3])
		if hora1>=0 and hora1<=2:
			b=lista2[1]
			bl=[]
			for i in b:
				bl+=i
			hora2=int(bl[0])*8+int(bl[1])*4+int(bl[2])*2+int(bl[3])
			if hora1==2 and hora2>4:
				print("Hora no valida")
			elif hora2>=0 and hora2<=9:
				c=lista2[2]
				cl=[]
				for i in c:
					cl+=i
				min1=int(cl[0])*8+int(cl[1])*4+int(cl[2])*2+int(cl[3])
				if min1>=0 and min1<6:
					d=lista2[3]
					dl=[]
					for i in d:
						dl+=i
					min2=int(dl[0])*8+int(dl[1])*4+int(dl[2])*2+int(dl[3])
					if min2>=0 and min2<10:
						print("Iniciar las observaciones a las ",hora1,hora2,":",min1,min2)
					else:
						print("Hora no valida")
				else:
					print("Hora no valida")
			else:
				print("Hora no valida")
		else:
			print("Hora no valida")
else:
	print("Hora no valida")
