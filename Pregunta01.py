def porcentaje(fraccion):
    x,y = fraccion.split('/')
    x,y = int(x), int(y)

    if x <= 0 or y <= 0 or x > y:
        raise ValueError("X y Y deben ser números enteros y X debe ser menor o igual a Y")

    porcent = (x / y) * 100

    if porcent < 1:
        return 'E'
    elif porcent > 99:
        return 'F'
    else:
        return f"{round(porcent)}%"

def main():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            print(f"La cantidad de combustible en el tanque es: {porcentaje(fraccion)}")
            break
        except ValueError as e:
            print(f"Error: {e} Inténtelo nuevamente")
        except ZeroDivisionError:
            print("Error: Y no puede ser 0 Inténtelo nuevamente")

if __name__ == "__main__":
    main()
