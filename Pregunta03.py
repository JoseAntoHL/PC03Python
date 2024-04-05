import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi*self.radio**2

radio = 7
circulo = Circulo(radio)
print(f"El área del circulo con radio {radio} es: {circulo.area()}")
