import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante IV"
        elif self.x == 0 and self.y != 0:
            return "Sobre eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre eje X"
        else:
            return "Origen"

    def vector(self, otro_punto):
        vector_x = otro_punto.x - self.x
        vector_y = otro_punto.y - self.y
        return Punto(vector_x, vector_y)


punto1 = Punto(2, 6)
print(f"Coordenadas de punto1: {punto1}")
print(f"Cuadrante de punto1: {punto1.cuadrante()}")

punto2 = Punto(-1, 3)
print(f"Coordenadas de punto2: {punto2}")
print(f"Cuadrante de punto2: {punto2.cuadrante()}")

vector_resultante = punto1.vector(punto2)
print(f"Vector resultante entre punto1 y punto2: {vector_resultante}")

