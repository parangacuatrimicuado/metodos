import math
#a
def factorial(x):
	fact=1
	while x>0:
		fact=x*fact
		x-=1
	return fact
def seno(x,m)
	sums=0
	for i in range(1,m+1):
		sums+=((-1)**(i-1))*(x**(2i-1))/(factorial(2i-1))
	return sums
def coseno(x,m)
	sumc=0
	for i in range(1,m+1):
		sums+=((-1)**(i-1))*(x**(2i))/(factorial(2i))
	return sumc
#b
def errorsen(x)
	error=abs((seno(x,m)-math.sin(x))/math.sin(x))*100
	return error
def errorcos(x)
	error=abs((seno(x,m)-math.sin(x))/math.sin(x))*100
	return error
