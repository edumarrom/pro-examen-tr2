from soporte import Soporte

class Televisor:
    """Representa un televisor y su funcionamiento."""
    def __init__(self, canal = 1, volumen = 20, encendido = False):
        self.__set_canal(canal)
        self.__set_volumen(volumen)
        self.__set_encendido(encendido)
        self.__soporte = None

    def __repr__(self):
        """Devuelve la forma normla de un televisor."""
        return f"Televisor({self.canal()}, "\
            f"{self.volumen()}, {self.encendido()})"

    def canal(self):
        """
        Devuelve el canal actualmente sintonizado.
        """
        return self.__canal

    def __set_canal(self, canal):
        """
        Modifica el canal de un televisor.
        Un canal sólo puede estar comprendido entre
            el 1 y el 100.

        Recibe: canal: Int -> El canal a sintonizar
        """
        if canal in range(1, 101):
            self.__canal = canal
        else: raise ValueError('Un canal sólo puede '\
            'estar comprendido entre el 1 y el 100')

    def sintonizar(self, num_canal):
        """
        Sintoniza un canal, de entre los 100 disponibles.

        Devuelve el propio objeto televisor.
        """
        self.__set_canal(num_canal)
        return self

    def volumen(self):
        """
        Devuelve el volumen del televisor.
        """
        return self.__volumen

    def __set_volumen(self, volumen):
        """
        Modifica el volúmen de un televisor.
        El volúmen sólo puede estar comprendido entre
            el 0 y el 30.

        Recibe: volúmen: Int -> El volúmen a sintonizar
        """
        if volumen in range(30):
            self.__volumen = volumen
        else: raise ValueError('El volúmen sólo puede '\
            'estar comprendido entre el 0 y el 30')

    def subir_volumen(self, cantidad = 1):
        """
        Sube el volúmen de uno en uno si el televisor está encendido.
        Si está apagado no hace nada.

        Devuelve el propio objeto televisor.
        """
        if self.encendido():
            self.__set_volumen(self.volumen() + cantidad)
        return self

    def bajar_volumen(self, cantidad = 1):
        """
        Baja el volúmen de uno en uno si el televisor está encendido.
        Si está apagado no hace nada.

        Devuelve el propio objeto televisor.
        """
        if self.encendido():
            self.__set_volumen(self.volumen() - cantidad)
        return self

    def encendido(self):
        """
        Devuelve True si está encendido, False en caso contrario.
        """
        return self.__encendido

    def __set_encendido(self, encendido):
        """
        Modifica el estado del atributo encendido de un televisor.
        El estado sólo puede recibir True o False.

        Recibe: encendido: Bool -> El nuevo estado de encendido.
        """
        if encendido in (True, False):
            self.__encendido = encendido
        else: raise ValueError('El atributo encendido sólo puede '\
            'recibir True o False.')

    def encender(self):
        """
        Enciende el televisor.
        Devuelve el propio objeto Televidor.
        """
        if self.encendido() == False:
            self.__set_encendido(True)
        return self

    def apagar(self):
        """
        Apaga el televisor.
        Devuelve el propio objeto Televidor.
        """
        if self.encendido() == True:
            self.__set_encendido(False)
        return self

    def soporte(self):
        """Devuelve el estado del soporte."""
        return self.__soporte

    def __set_soporte(self, soporte):
        """
        Modifica el soporte de un televisor.

        soporte sólo puede recibir
        instancias de la clase Soporte
        Recibe: soporte: Soporte -> El soporte del televisor.
        """
        if soporte == None or isinstance(soporte, Soporte):
            self.__soporte = soporte
        else: raise TypeError('El soporte sólo recibe soportes válidos.')

    def conectar(self, soporte):
        """
        Conecta un soporte al puerto USB.

        Devuelve el propio objeto Televisor.
        """
        self.__set_soporte(soporte)


    def desconectar_si_conectado(self):
        """
        Desconecta el soporte que tuviera conectado \
            en el puerto USB.
        Si no hubiera ninguno no hace nada

        Devuelve el propio objeto Televisor.
        """
        if self.soporte() != None:
            self.__set_soporte(None)
        return self

    def reproducir_si_conectado(self):
        """
        Reproduce, de uno en uno, todo el contenido \
            multimedia que hay en el soporte conectado.

        Devuelve una tupla con los nombres de los archivos.
        """
        reproducido = []
        if self.encendido():
            if self.soporte() != None:
                for t in self.soporte().playlist():
                    reproducido.append(t)
        return tuple(reproducido)

if __name__ == '__main__':
    tv = Televisor()
    pendrive = Soporte()
    tv.conectar(pendrive)
    tv.encender()
    print(tv.reproducir_si_conectado())
    tv.desconectar_si_conectado()
    print(tv.soporte())
    print(tv.reproducir_si_conectado())
