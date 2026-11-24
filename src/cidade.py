from jogador import Jogador


class Cidade:

    def __init__(self, nome: str, dono: Jogador) -> None:
        self._nome = nome
        self._dono = dono
        self._ano_atual = 1400
        self._florins = 1000
        self._terras = 10000
        self._graos = 500
        self._servos = 200
        self._taxa_imposto = 10
        self._nivel_justica = "Moderada"
        self._soldados = 0
        self._construcoes = 0

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def dono(self) -> Jogador:
        return self._dono

    @property
    def ano_atual(self) -> int:
        return self._ano_atual

    @property
    def florins(self) -> int:
        return self._florins

    @property
    def terras(self) -> int:
        return self._terras

    @property
    def graos(self) -> int:
        return self._graos

    @property
    def servos(self) -> int:
        return self._servos

    @property
    def soldados(self) -> int:
        return self._soldados

    @property
    def construcoes(self) -> int:
        return self._construcoes

    # Taxa de imposto e nivel de justica sao configuracoes, nao recursos
    # acumulaveis: getter/setter simples (a validacao fica no Governo).
    @property
    def taxa_imposto(self) -> int:
        return self._taxa_imposto

    @taxa_imposto.setter
    def taxa_imposto(self, taxa: int) -> None:
        self._taxa_imposto = taxa

    @property
    def nivel_justica(self) -> str:
        return self._nivel_justica

    @nivel_justica.setter
    def nivel_justica(self, nivel: str) -> None:
        self._nivel_justica = nivel

    # Sera chamado apenas a partir da Etapa 7.
    def avancar_ano(self) -> None:
        self._ano_atual += 1

    # Para cada recurso: adicionar sempre funciona; remover devolve False
    # (sem alterar nada) se nao houver saldo suficiente, nunca deixando o
    # recurso negativo.
    def adicionar_florins(self, qtd: int) -> None:
        self._florins += qtd

    def remover_florins(self, qtd: int) -> bool:
        if qtd > self._florins:
            return False
        self._florins -= qtd
        return True

    def adicionar_terras(self, qtd: int) -> None:
        self._terras += qtd

    def remover_terras(self, qtd: int) -> bool:
        if qtd > self._terras:
            return False
        self._terras -= qtd
        return True

    def adicionar_graos(self, qtd: int) -> None:
        self._graos += qtd

    def remover_graos(self, qtd: int) -> bool:
        if qtd > self._graos:
            return False
        self._graos -= qtd
        return True

    def adicionar_servos(self, qtd: int) -> None:
        self._servos += qtd

    def remover_servos(self, qtd: int) -> bool:
        if qtd > self._servos:
            return False
        self._servos -= qtd
        return True

    def adicionar_soldados(self, qtd: int) -> None:
        self._soldados += qtd

    def remover_soldados(self, qtd: int) -> bool:
        if qtd > self._soldados:
            return False
        self._soldados -= qtd
        return True

    def adicionar_construcoes(self, qtd: int) -> None:
        self._construcoes += qtd

    def remover_construcoes(self, qtd: int) -> bool:
        if qtd > self._construcoes:
            return False
        self._construcoes -= qtd
        return True

    def exibir_status(self) -> None:
        print()
        print("------------------------------------------")
        print("STATUS DA CIDADE")
        print("------------------------------------------")
        print(f"Cidade:      {self._nome}")
        print(f"Governante:  {self._dono.titulo} {self._dono.nome}")
        print(f"Ano atual:   {self._ano_atual}")
        print(f"Florins:     {self._florins}")
        print(f"Terras:      {self._terras} hectares")
        print(f"Graos:       {self._graos} unidades")
        print(f"Servos:      {self._servos}")
        print(f"Imposto:     {self._taxa_imposto}%")
        print(f"Justica:     {self._nivel_justica}")
        print(f"Soldados:    {self._soldados}")
        print(f"Construcoes: {self._construcoes}")
        print("------------------------------------------")
