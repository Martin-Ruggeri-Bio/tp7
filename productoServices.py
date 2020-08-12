from repositorios import Repositorios


class ProductoService():

    def get_productosList(self):
        return Repositorios.productosList

    def add_producto(self, producto):
        lastKey = -1
        for i in Repositorios.productosList:
            lastKey = i
        productokey = lastKey + 1
        Repositorios.productosList[productokey] = producto.__dict__
        return productokey

    def delete_producto(self, key):
        lastKey = -1
        for i in Repositorios.productosList:
            lastKey = i
        maxkey = lastKey
        if key > maxkey:
            raise ValueError("no se puede eliminar si el id no existe")
        del Repositorios.productosList[key]
