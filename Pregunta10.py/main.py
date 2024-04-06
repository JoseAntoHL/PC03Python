from Circulo import Circulo
from Rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

def mostrar_menu():
    print("\n1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir\n")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.area()}")
        elif opcion == "2":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            rectangulo = Rectangulo(base, altura)
            print(f"El área del rectángulo es: {rectangulo.area()}")
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print(f"El área del cuadrado es: {cuadrado.area()}")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
