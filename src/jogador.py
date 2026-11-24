class Jogador:

    _TITULOS = ("Cavaleiro", "Barao", "Conde", "Marques", "Duque", "Rei/Rainha")

    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._nivel_titulo = 0

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def titulo(self) -> str:
        return self._TITULOS[self._nivel_titulo]

    @property
    def nivel_titulo(self) -> int:
        return self._nivel_titulo

    def promover(self) -> bool:
        """Sobe um nivel de titulo. False se ja for Rei/Rainha."""
        if self.eh_monarca():
            return False
        self._nivel_titulo += 1
        return True

    def eh_monarca(self) -> bool:
        return self._nivel_titulo == len(self._TITULOS) - 1
