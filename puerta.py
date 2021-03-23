from llave import Llave

CERRADA = 1
ABIERTA = 0

class Puerta:
    """
    Representa una puerta, identificada con su color.
    Ésta puede estar abierta o cerrada. Para abrirse, se
    requiere de una llave del mismo color que la puerta.
    La llave se coloca en la cerradura.
    """
    def __init__(self, color):
        """Constructor de la clase Puerta."""
        self.__set_color(color)
        self.__cerradura = None
        self.__cerrada = CERRADA

    def __repr__(self):
        """Devuelve la forma normal de una puerta."""
        return f"Puerta('{self.color()}')"

    def color(self):
        """Devuelve el color de una llave."""
        return self.__color

    def __set_color(self, color):
        """
        Modifica el color de una llave.

        Recibe: color: String -> El color de la llave
        """
        self.__color = color

    def cerradura(self):
        """Devuelve el el estado de la cerradura."""
        return self.__cerradura

    def __set_cerradura(self, cerradura):
        """
        Modifica la cerradura de una puerta.

        La cerradura sólo puede recibir
        instancias de la clase llave, o devolverá una \
            excepción TypeError.
        Recibe: cerradura: Llave -> El cerradura de la puerta
        """
        if cerradura == None or isinstance(cerradura, Llave):
            self.__cerradura = cerradura
        else: raise TypeError('La cerradura sólo recibe llaves.')

    def cerrada(self):
        """Devuelve 1 si la puerta cerrada, 0 en caso contrario."""
        return self.__cerrada

    def __set_cerrada(self, cerrada):
        """
        Modifica el estado del atributo cerrada de una puerta.
        Sólo puede recibir 1 ó 0., o devolverá una \
            excepción ValueError.

        Recibe: cerrada: Bool -> El nuevo estado de cerrada.
        """
        if cerrada in (ABIERTA, CERRADA):
            self.__cerrada = cerrada
        else: raise ValueError('La cerrada sólo recibe '\
            f'ABIERTA({ABIERTA}) o CERRADA({CERRADA}).')

    def poner(self, llave):
        """
        Pone una llave en la cerradura.
        Devuelve el propio objeto puerta.

        El ejercicio no especificaba que hacer en caso \
            de que la cerradura no estuviese vacía.
        """
        self.__set_cerradura(llave)
        return self

    def quitar(self):
        """
        Quita la llave de la puerta.

        Devuelve la llave que estaba puesta, o None \
            si no había ninguna.
        """
        llave = None
        if self.cerradura() != None:
            llave = self.cerradura()
            self.__set_cerradura(None)
        return llave

    def abrir(self):
        """
        Abre la puerta, si es posible.

        Devuelve True si se ha poddo abrir
        (o si ya estaba abierta) o False en caso contrario.
        """
        if self.cerradura() == None:
            return False
        else:
            if self.color() == self.cerradura().color():
                self.__set_cerrada(ABIERTA)
                return True
            else: return False

    def cerrar(self):
        """
        Cierra la puerta, si está abierta.

        No recuerdo si debía devolver algo, o nada.
        """
        if self.cerrada() == ABIERTA:
            self.__set_cerrada(CERRADA)

if __name__ == '__main__':
    print(Puerta('rojo').poner(Llave('rojo')).abrir())  # True
    print(Puerta('rojo').poner(Llave('verde')).abrir()) # False
    print(Puerta('rojo').abrir())                       # False
