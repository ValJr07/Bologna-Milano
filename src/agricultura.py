from cidade import Cidade


class Agricultura:
    """Processa a colheita do ano e a distribuicao de alimentos.

    Nao guarda nenhuma Cidade: ela e recebida como parametro em cada operacao.
    """

    _HECTARES_POR_SERVO = 5
    _HECTARES_POR_SEMENTE = 2
    _RENDIMENTO_POR_HECTARE = 2
    _SERVOS_POR_GRAO = 5
    _CRESCIMENTO_PERCENTUAL = 5
    _PERCENTUAL_MINIMO = 20
    _PERCENTUAL_MAXIMO = 80

    @property
    def percentual_minimo(self) -> int:
        return self._PERCENTUAL_MINIMO

    @property
    def percentual_maximo(self) -> int:
        return self._PERCENTUAL_MAXIMO

    def processar_colheita(self, cidade: Cidade) -> int:
        """Planta, gasta a semente e produz graos novos.

        Devolve o numero de hectares cultivados, ou -1 (sem alterar nada)
        se a cidade ja colheu neste ano.
        """
        if cidade.colheita_feita():
            return -1
        hectares = min(cidade.terras, cidade.servos * self._HECTARES_POR_SERVO)
        sementes = hectares // self._HECTARES_POR_SEMENTE
        if sementes > cidade.graos:
            # Sem semente suficiente: planta so o que o estoque permite.
            sementes = cidade.graos
            hectares = sementes * self._HECTARES_POR_SEMENTE
        cidade.remover_graos(sementes)
        producao = hectares * self._RENDIMENTO_POR_HECTARE
        cidade.adicionar_graos(producao)
        cidade.marcar_colheita_feita()
        return hectares

    def distribuir_alimentos(self, cidade: Cidade, percentual: int) -> bool:
        """Distribui um percentual do estoque de graos a populacao.

        Devolve False (sem alterar nada) se o percentual estiver fora do
        intervalo permitido. Se o alimento cobrir a necessidade minima, a
        populacao cresce; senao, perde o deficit em servos.
        """
        if not self._PERCENTUAL_MINIMO <= percentual <= self._PERCENTUAL_MAXIMO:
            return False

        alimento_distribuido = cidade.graos * percentual // 100
        cidade.remover_graos(alimento_distribuido)

        necessidade = cidade.servos // self._SERVOS_POR_GRAO
        if alimento_distribuido >= necessidade:
            crescimento = cidade.servos * self._CRESCIMENTO_PERCENTUAL // 100
            cidade.adicionar_servos(crescimento)
        else:
            deficit = necessidade - alimento_distribuido
            cidade.remover_servos(min(deficit, cidade.servos))
        return True
