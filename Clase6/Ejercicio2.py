class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad=1):
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        total = 0
        for producto, cantidad in self.productos:
            total += producto.precio * cantidad
        return total

    def procesar_pago(self):
        total = self.calcular_total()
        print("Total de la compra del cliente:", total)
        

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = Carrito()



producto1 = Producto("Telefono", 370)
producto2 = Producto("Televisor", 230)
producto3 = Producto("Licuadora", 150)

    
cliente = Cliente("Juan")

    
cliente.carrito.agregar_producto(producto1, cantidad=2)
cliente.carrito.agregar_producto(producto2)
cliente.carrito.agregar_producto(producto3)

    
cliente.carrito.procesar_pago()