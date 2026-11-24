from cidade import Cidade


class Construcoes:
    """Recruta soldados e constroi edificios sobre uma Cidade.

    Nao guarda nenhuma Cidade: ela e recebida como parametro em cada operacao.
    """

    _PRECO_SOLDADO = 5
    _SERVOS_POR_SOLDADO = 1
    _PRECO_CONSTRUCAO = 20

    @property
    def preco_soldado(self) -> int:
        return self._PRECO_SOLDADO

    @property
    def preco_construcao(self) -> int:
        return self._PRECO_CONSTRUCAO

    def recrutar_soldados(self, cidade: Cidade, quantidade: int) -> bool:
        """Recruta soldados: cada um custa florins e servos.

        Os DOIS recursos sao validados antes de alterar qualquer um deles;
        se faltar um, devolve False e nada muda.
        """
        if quantidade <= 0:
            return False
        custo = quantidade * self._PRECO_SOLDADO
        servos_necessarios = quantidade * self._SERVOS_POR_SOLDADO

        if cidade.florins < custo or cidade.servos < servos_necessarios:
            return False

        cidade.remover_florins(custo)
        cidade.remover_servos(servos_necessarios)
        cidade.adicionar_soldados(quantidade)
        return True

    def construir(self, cidade: Cidade, quantidade: int) -> bool:
        """Constroi edificios pagando so florins. False se faltar saldo."""
        if quantidade <= 0:
            return False
        custo = quantidade * self._PRECO_CONSTRUCAO
        if not cidade.remover_florins(custo):
            return False
        cidade.adicionar_construcoes(quantidade)
        return True
