#reutilizamos el codigo del ejercicio 5 y le agregamos la sobrecarga de metodos requerida (__str__ y __eq__)
from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento 
        self.precio = precio
        self.stock = stock

    def actualizar_datos(self, descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock
    
    def calcular_dias_expiracion(self):
        hoy = date.today()
        dias_restantes = (self.fecha_vencimiento - hoy).days

        if dias_restantes < 0:
            print(f"El producto '{self.descripcion}' ha expirado")
            self.stock = 0
            return 0
        return dias_restantes

    def __str__(self):
        #usamos :.2f en precio para que muestre dos decimales como en el $1.50 del ejemplo
        return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio:.2f} | Stock:{self.stock}"

    def __eq__(self, otro):
        #verificamos que el objeto a comparar sea de la misma clase
        if not isinstance(otro, ProductoKwikE):
            return False
        #compara coincidencia de id_producto y descripcion
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion
