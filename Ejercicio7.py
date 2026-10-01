class KwikEMart:
    def __init__(self):
        #representamos los pasillos mediante un diccionario de listas de productos
        self.pasillos = {
            "Bebidas": [],
            "Snacks": [],
            "Conveniencia": []
        }
    def agregar_producto(self, pasillo, producto):
        #si el pasillo existe agregamos el producto a su lista
        if pasillo in self.pasillos:
            self.pasillos[pasillo].append(producto)
        else:
            #si no existe lo creamos con una nueva lista
            self.pasillos[pasillo] = [producto]

    def remover_producto(self, producto):
        #buscamos y removemos el producto en todos los pasillos
        for pasillo, lista_productos in self.pasillos.items():
            if producto in lista_productos:
                lista_productos.remove(producto)
    
    def actualizar_stock(self, producto, nuevo_stock):
        #actualizamos la propiedad stock del producto directamente
        producto.stock = nuevo_stock

    def remover_expirados_24hs(self):
        expirados = 0
        for pasillo, lista_productos in self.pasillos.items():
            #filtramos manteniendo los prod con dias de exp >=0
            productos_validos = []
            for p in lista_productos:
                #si calcular_dias_expiracion() da 0 o menos, expira en <=24hs o ya expiro
                if p.calcular_dias_expiracion() <= 0:
                    expirados += 1
                else:
                    productos_validos.append(p)
            #reemplazamos la lista por la de productos vigentes
            self.pasillos[pasillo] = productos_validos
        
        return expirados