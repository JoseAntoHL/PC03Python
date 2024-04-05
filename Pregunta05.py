class Alumno:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, 1):
                print(f"Nota {i}: {nota}")

    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, notas):
        self.notas = notas

nombre = "Jose"
numero = "15200022"
alumno = Alumno(nombre, numero)
alumno.setAge(29)
alumno.setNota([11, 8, 18])
alumno.display()
