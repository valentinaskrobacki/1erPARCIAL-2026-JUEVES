class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)
    
    # -- 8.1 metodos de la lista enlazada --
    def append(self, dato):
        actual = self.header
        while actual._nxt:
            actual = actual._nxt
        actual._nxt = Nodo(dato)

    def remove(self, dato):
        actual = self.header
        while actual._nxt:
            if actual._nxt._elem == dato:
                actual._nxt = actual._nxt._nxt
                return True
            actual = actual._nxt
        return False

    # -- 8.2 iterador para la lista enlazada --
    def __iter__(self):
        actual = self.header._nxt
        while actual:
            yield actual._elem
            actual = actual._nxt

#traigo la clase kwikemart del ejercicio 7 pero ahora usando nuestra ListaEnlazada en vez de las listas comunes de python
#al tener implementado el __iter__ puedo recorrer los pasillos con un for directamente sin cambiar la logica
class KwikEMart:
    def __init__(self):
        #representamos los pasillos mediante un diccionario de listas de productos
        self.pasillos = {
            "Bebidas": ListaEnlazada(),
            "Snacks": ListaEnlazada(),
            "Conveniencia": ListaEnlazada()
        }
    def agregar_producto(self, pasillo, producto):
        #si el pasillo existe agregamos el producto a su lista
        if pasillo in self.pasillos:
            self.pasillos[pasillo].append(producto)
        else:
            #si no existe lo creamos con una nueva lista
            nueva_lista = ListaEnlazada()
            nueva_lista.append(producto)
            self.pasillos[pasillo] = nueva_lista

    def remover_producto(self, producto):
        #buscamos y removemos el producto en todos los pasillos
        for pasillo, lista_productos in self.pasillos.items():
                lista_productos.remove(producto)
    
    def actualizar_stock(self, producto, nuevo_stock):
        #actualizamos la propiedad stock del producto directamente
        producto.stock = nuevo_stock

    def remover_expirados_24hs(self):
        expirados = 0
        for pasillo, lista_productos in self.pasillos.items():
            #filtramos manteniendo los prod con dias de exp >=0
            productos_validos = ListaEnlazada()
            for p in lista_productos:
                #si calcular_dias_expiracion() da 0 o menos, expira en <=24hs o ya expiro
                if p.calcular_dias_expiracion() <= 0:
                    expirados += 1
                else:
                    productos_validos.append(p)
            #reemplazamos la lista por la de productos vigentes
            self.pasillos[pasillo] = productos_validos
        
        return expirados