from funciones import cuota
from funciones import importe_total
def menu():
    opcion = 0
    while opcion < 1 or opcion > 3:
        print('Cálculos Hipoteca')
        print('-------------------------')
        print('1) Obtener cuota hipoteca')
        print('2) Obtener importe total')
        print('3) Salir')
        opcion = int(input('Seleccione una opcion: '))
    return opcion

opcion = 0
while opcion != 3:
    opcion = menu()
    match opcion:
        case 1: 
            hipoteca = int(input('Introduzca su hipoteca: '))
            anios = int(input("Introduzca los años: "))
            intereses = float(input("Introduzca los intereses: "))
            print(f"Su cuota es de : {cuota(hipoteca, anios, intereses)}")
            input('\nPulse intro para continuar: \n')
        case 2:
            hipoteca = int(input('Introduzca su hipoteca: '))
            anios = int(input("Introduzca los años: "))
            intereses = float(input("Introduzca los intereses: "))
            print(f"El importe total a pagar es {importe_total(hipoteca,anios,intereses)}")
            input('\nPulse intro para continuar: \n')