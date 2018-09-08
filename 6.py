a=int(input("Ingrese primer año:"))
b=int(input("Ingrese segundo año año:"))
cont=0
for i in range(a,b+1):
	if i%4==0 and i%100!=0 or i%400==0:
		cont+=1
print("Hay",cont,"años bisiestos entre los años",a,"y",b)
