class Jogador:

    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._titulo = "Cavaleiro"

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def titulo(self) -> str:
        return self._titulo
