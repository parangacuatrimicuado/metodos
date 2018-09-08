def movimientos(x,y):
    allmov = []
    movs = [(-1,-2),(-1,2),(-2,-1),(-2,1),( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in movs:
        nuevoX = x + i[0]
        nuevoY = y + i[1]
        if movlegales(nuevoX) and movlegales(nuevoY):
            allmov.append((nuevoX,nuevoY))
    return allmov
def movlegales(x):
    if x >= 0 and x < 8:
        return True
    else:
        return False
x=int(input("ingrese posicion en x(entre 0 y 7):"))
y=int(input("ingrese posicion en y(entre 0 y 7):"))
print("El caballo se puede mover a las posiciones:",movimientos(x,y))
