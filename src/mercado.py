from cidade import Cidade


class Mercado:
    """Compra e vende graos e terras a precos fixos.

    Nao guarda nenhuma Cidade: ela e recebida como parametro em cada operacao.
    """

    _PRECO_GRAO = 2
    _PRECO_TERRA = 10

    @property
    def preco_grao(self) -> int:
        return self._PRECO_GRAO

    @property
    def preco_terra(self) -> int:
        return self._PRECO_TERRA

    def comprar_graos(self, cidade: Cidade, quantidade: int) -> bool:
        if quantidade <= 0:
            return False
        custo = quantidade * self._PRECO_GRAO
        if not cidade.remover_florins(custo):
            return False
        cidade.adicionar_graos(quantidade)
        return True

    def vender_graos(self, cidade: Cidade, quantidade: int) -> bool:
        if quantidade <= 0:
            return False
        if not cidade.remover_graos(quantidade):
            return False
        receita = quantidade * self._PRECO_GRAO
        cidade.adicionar_florins(receita)
        return True

    def comprar_terras(self, cidade: Cidade, quantidade: int) -> bool:
        if quantidade <= 0:
            return False
        custo = quantidade * self._PRECO_TERRA
        if not cidade.remover_florins(custo):
            return False
        cidade.adicionar_terras(quantidade)
        return True

    def vender_terras(self, cidade: Cidade, quantidade: int) -> bool:
        if quantidade <= 0:
            return False
        if not cidade.remover_terras(quantidade):
            return False
        receita = quantidade * self._PRECO_TERRA
        cidade.adicionar_florins(receita)
        return True
