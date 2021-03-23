class Llave:
    """
    Representa una llave, que abrirá una
    puerta dependiendo de su color.
    """
    def __init__(self, color):
        """Constructor de la clase Llave."""
        self.__set_color(color)

    def __repr__(self):
        """Devuelve al forma normal de una llave."""
        return f"Llave('{self.color()}')"

    def color(self):
        """Devuelve el color de una llave."""
        return self.__color

    def __set_color(self, color):
        """
        Modifica el color de una llave.

        Recibe: color: String -> El color de la llave
        """
        self.__color = color
