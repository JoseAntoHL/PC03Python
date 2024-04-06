class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        for producto in productos_filtrados:
            print(producto)

    def buscar_por_nombre(self, nombre):
        productos_encontrados = [producto for producto in self.productos if producto.nombre.lower() == nombre.lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'")


catalogo = Catalogo()
catalogo.agregar_producto(Producto("Lunas", 100, 2020))
catalogo.agregar_producto(Producto("Motor", 150, 2019))
catalogo.agregar_producto(Producto("Aire acondicionado", 20, 2021))
catalogo.agregar_producto(Producto("Gasolina", 30, 2021))


print("Todos los productos:")
catalogo.mostrar_productos()

print("\nProductos del año 2020:")
catalogo.filtrar_por_año(2020)

print("\nBuscar producto por nombre:")
catalogo.buscar_por_nombre("Lunas")
catalogo.buscar_por_nombre("Gasolina")
