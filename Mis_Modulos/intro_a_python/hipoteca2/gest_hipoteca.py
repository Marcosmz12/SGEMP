import funciones 

def menu():
    while True:
        print('\nCálculos Hipoteca')
        print('-------------------------')
        print('1) Obtener cuota hipoteca')
        print('2) Obtener importe total')
        print('3) Salir')
        
        try:
            opcion = int(input('Seleccione una opcion: '))
            if 1 <= opcion <= 3:
                return opcion
            else:
                print("Por favor, seleccione 1, 2 o 3.")
        except ValueError:
            print("Error: Debe introducir un número entero.")

def gest_hipoteca():
    while True:
        opcion = menu()
        
        if opcion == 3:
            print("Saliendo del programa... ¡Hasta luego!")
            break 
            
        try:
            match opcion:
                case 1: 
                    print("\n--- Calcular Cuota ---")
                    hipoteca = int(input('Introduzca su hipoteca (entero): '))
                    anios = int(input("Introduzca los años (entero): "))
                    intereses = float(input("Introduzca los intereses (con punto): "))
                    
                    resultado = funciones.cuota(hipoteca, anios, intereses)
                    print(f"Su cuota es de: {resultado}")
                    input('Pulse intro para volver al menú...')
                    
                case 2:
                    print("\n--- Calcular Importe Total ---")
                    hipoteca = int(input('Introduzca su hipoteca (entero): '))
                    anios = int(input("Introduzca los años (entero): "))
                    intereses = float(input("Introduzca los intereses (con punto): "))
                    
                    resultado = funciones.importe_total(hipoteca, anios, intereses)
                    print(f"El importe total a pagar es: {resultado}")
                    input('Pulse intro para volver al menú...')

        except ValueError:
            print("Error de datos: Asegúrate de poner números (no letras).")
            input('Pulse intro para intentar de nuevo...')
        except Exception as e:
            print(f"Error inesperado: {e}")
            input('Pulse intro para continuar...')


gest_hipoteca()