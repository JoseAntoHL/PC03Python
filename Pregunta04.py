class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo*self.ancho

largo = 11
ancho = 12
rectangulo = Rectangulo(largo,ancho)
print(f"El área del rectangulo con radio es: {rectangulo.area()}")