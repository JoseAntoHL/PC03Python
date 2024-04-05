def obtener_calificaciones():
    while True:
        try:
            calificaciones_str = input("Ingrese las calificaciones(separadas por comas): ")
            calificaciones_lista = calificaciones_str.split(',')
            calificaciones_enteros = [int(calificacion.strip()) for calificacion in calificaciones_lista]
            return calificaciones_enteros
        except ValueError:
            print("Error: Por favor, ingrese calificaciones válidas.")

calificaciones = obtener_calificaciones()

print(f"Calificaciones ingresadas: {calificaciones}")
