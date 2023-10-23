#Actividad 1: Escribe un programa que capture la excepción división entre cero. Tendrá que mostar el mensaje del error capturado.

def calculoDivision(numUno:int,numDos:int) ->int:
    if numDos == 0:
        raise ValueError('El número debe ser mayor que 0.')
    return numUno % numDos

if __name__=="__main__":
    #proceso
    numeroCorrecto = False
    numUno = None
    numDos = None
    while not numeroCorrecto:
        try:
            #entrada
            numUno = int(input("Escribe un número: "))
            numDos = int(input("Escribe otro número: "))
            numUno = int
            numDos = int
            division = calculoDivision(numUno,numDos)
            numeroCorrecto = True
        except ValueError:   # Si no mete un int o es igual a 0
            if numUno == None and numDos == None:
                print('Por favor introduzca un número entero.')
            else:
                print('La división entre 0 no es posible.')

    print(division)

