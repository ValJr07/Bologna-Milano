from jogador import Jogador


class Cidade:

    def __init__(self, nome: str, dono: Jogador) -> None:
        self._nome = nome
        self._dono = dono
        self._ano_atual = 1400

    # Sera chamado apenas a partir da Etapa 7.
    def avancar_ano(self) -> None:
        self._ano_atual += 1

    def exibir_status(self) -> None:
        print()
        print("------------------------------------------")
        print("STATUS DA CIDADE")
        print("------------------------------------------")
        print(f"Cidade:     {self._nome}")
        print(f"Governante: {self._dono.titulo} {self._dono.nome}")
        print(f"Ano atual:  {self._ano_atual}")
        print("------------------------------------------")
