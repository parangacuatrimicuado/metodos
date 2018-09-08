#12 Escriba un programa que determine el numero de dias que hay entre dos fechas con estructura de funcion (suponiendo que todos los años tienen 365 dias)
def transfecha(x):
	#ejemplo 06/06/1666 -->dia/mes/año
	#    bin:0123456789
	#hacer cortes al string x ingresado por teclado quitando los "/"     
	dia=int(x[:2])/365
	mes=int(x[3:5])/12
	ano=int(x[6:])
	fechareal=dia+mes+ano
	return fechareal
print("Ingrese dos fechas en formato DD/MM/AAAA pls donde la segunda fecha es mayor que la primera")
fecha1=str(input("Primera fecha: "))
fecha2=str(input("Segunda fecha: "))
diffechas=transfecha(fecha2)-transfecha(fecha1)
print("Hay",diffechas*365,"dias entre la fecha",fecha1,"y la fecha",fecha2)

