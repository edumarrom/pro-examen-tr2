class Soporte:
    """Representa un soporte multimedia USB."""
    def __init__(self, playlist = ('Baila morena', 'Corazón Partío', 'Sultans of Swing')):
        self.__set_playlist(playlist)

    def playlist(self):
        return self.__playlist

    def __set_playlist(self, playlist):
        self.__playlist = playlist

    def reproducir(self, indice):
        return self.playlist()[indice]
