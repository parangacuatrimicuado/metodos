def codigo_palabra(codigo):
	a=codigo[-1::-2]
	return a
def codigo_ra(codigo):
	grados=codigo[:codigo.find(":")]#corta la palabra hasta la posicion del caracter :
	decimales=codigo[codigo.find(":")+1:]	
	sum1=0
	sum2=0	
	for i in grados:
		sum1+=int(i)
	gradosfinal=sum1%24
	for i in decimales:
		sum2+=int(i)
	decimalesfinal=sum2%60
	return gradosfinal, decimalesfinal
#####programa hecho solo para UNA palabra y UNA ascension recta OJO!!
while True:
	palabra=input("Ingrese codigo:")
	asra=input("Ingrese codigo:")
	a=input("ente gatillante:")
	if a=="astro":
		break
print("palabra desencriptada:",codigo_palabra(palabra),",","ascension recta desencriptada:",codigo_ra(asra)[0],":",codigo_ra(asra)[1])

