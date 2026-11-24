from cidade import Cidade


class Governo:
    """Arrecada impostos e define a taxa de imposto e o nivel de justica.

    Nao guarda nenhuma Cidade: ela e recebida como parametro em cada operacao.
    """

    _TAXA_MAXIMA = 50

    _NIVEL_JUSTA = "Justa"
    _NIVEL_MODERADA = "Moderada"
    _NIVEL_SEVERA = "Severa"

    _MULTIPLICADOR_JUSTA = 0.8
    _MULTIPLICADOR_MODERADA = 1.0
    _MULTIPLICADOR_SEVERA = 1.3

    @property
    def taxa_maxima(self) -> int:
        return self._TAXA_MAXIMA

    @property
    def niveis_justica(self) -> tuple:
        return (self._NIVEL_JUSTA, self._NIVEL_MODERADA, self._NIVEL_SEVERA)

    def arrecadar_impostos(self, cidade: Cidade) -> int:
        """Credita os impostos aos florins da cidade e devolve o valor."""
        base = cidade.servos * cidade.taxa_imposto // 100
        multiplicador = self._multiplicador_para(cidade.nivel_justica)
        arrecadado = int(base * multiplicador)
        cidade.adicionar_florins(arrecadado)
        return arrecadado

    def definir_taxa_imposto(self, cidade: Cidade, taxa: int) -> bool:
        """Define a taxa (0 a 50). Devolve False, sem alterar nada, se invalida."""
        if not 0 <= taxa <= self._TAXA_MAXIMA:
            return False
        cidade.taxa_imposto = taxa
        return True

    def definir_justica(self, cidade: Cidade, nivel: str) -> bool:
        """Define o nivel (Justa/Moderada/Severa). Devolve False se invalido."""
        if nivel not in self.niveis_justica:
            return False
        cidade.nivel_justica = nivel
        return True

    def _multiplicador_para(self, nivel: str) -> float:
        if nivel == self._NIVEL_JUSTA:
            return self._MULTIPLICADOR_JUSTA
        if nivel == self._NIVEL_SEVERA:
            return self._MULTIPLICADOR_SEVERA
        return self._MULTIPLICADOR_MODERADA
