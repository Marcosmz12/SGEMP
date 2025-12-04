class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mayorDeEdad(self):
        if self.edad > 18:
             return"Es mayor de edad"
        else:
             return"Es menor de edad"

empleado1 = persona("Marcos", 21)
empleado2 = persona("Antonio", 15)

print(f"El empleado: {empleado1.nombre}", "tiene", empleado1.edad)
print(f"El empleado: {empleado1.nombre}. {empleado1.mayorDeEdad()}")
print(empleado2.nombre, "tiene", empleado2.edad)