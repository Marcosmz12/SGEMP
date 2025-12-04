class Lista:
    def __init__(self):
        self.lista = {}

    def anadir(self, nombre, telefono):
        if nombre in self.lista:
            if not telefono in self.lista[nombre]:
                self.lista[nombre].append(telefono)
        else:
            self.lista[nombre] = [telefono]

    def consultar(self, nombre):
        if nombre in self.lista:
            print(f'Lista de Telefonos de {nombre}: ')
            return self.lista[nombre]
        else:
            print(f'{nombre} no esta en nuestra base de datos')
            return[]

    def eliminar (self, nombre):
        if nombre in self.lista:
            del self.lista[nombre]
            print(f'Se ha eliminado correctamente a {nombre}')

def menu():
    opcion = 0
    while opcion < 1 or opcion > 5:
        print('1) Añadir telefonos')
        print('2) Consultar lista')
        print('3) Añadir otro telefono a una misma persona')
        print('4) Eliminar Persona de la lista')
        print('5) Salir')
        opcion = int(input('Escoge una opcion: '))
    return opcion

lista = Lista()

opcion = 0
while opcion != 5:
    opcion = menu()
    match opcion:
        case 1:
            nombre = input('Introduce el nombre: ')
            telefono = input('Introduce un número: ')
            lista.anadir(nombre, telefono)
            input('\nPulse intro para continuar: \n')
        case 2:
            nombre = input('Introduce el nombre: ')
            telefonos = lista.consultar(nombre)
            for i,telefono in enumerate(telefonos):
                print(f'{i + 1}: {telefono}')
            input('\nPulse intro para continuar: \n')
        case 3:
            mas = input('Desea añadir otro telefono (s/n): ')
            while mas == 's':
                nombre = input('Nombre: ')
                telefono = input('Telefono: ')
                lista.anadir(nombre, telefono)
                mas = input(f'Desea añadir otro telefono a {nombre} (s/n): ')
            input('\nPulse intro para continuar: \n')

        case 4:
            nombre = input('Introduce el nombre a eliminar: ')
            lista.eliminar(nombre)
            input('\nPulse intro para continuar: \n')
