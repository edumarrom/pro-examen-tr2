class Soporte:
    """
    Representa un soporte multimedia USB, el cual contiene \
        una playlist de música.
    """
    def __init__(self, playlist = ('Baila Morena', 'Corazón Partío', 'Sultans of Swing')):
        """Constructor de la clase Soporte."""
        self.__set_playlist(playlist)

    def playlist(self):
        """Devuelve la playlist del soporte."""
        return self.__playlist

    def __set_playlist(self, playlist):
        """Modifica la playlist del soprte."""
        self.__playlist = playlist

    def reproducir(self, indice):
        """
        Reproduce la n-ésima pista de la playlist.

        Recibe: indice: int -> El índice de la pista.
        """
        return self.playlist()[indice]
