from __future__ import annotations

from cidade import Cidade
from nobreza import Nobreza


class Partida:
    """Guarda as cidades (1 a 4 jogadores), controla turnos, anos e vencedor."""

    MAXIMO_JOGADORES = 4
    ANO_FINAL = 1410

    def __init__(self) -> None:
        self._cidades: list[Cidade] = []
        self._indice_atual = 0

    @property
    def cidades(self) -> list[Cidade]:
        return list(self._cidades)

    @property
    def cidade_atual(self) -> Cidade:
        return self._cidades[self._indice_atual]

    @property
    def ano_atual(self) -> int:
        return self._cidades[0].ano_atual

    @property
    def ano_final(self) -> int:
        return self.ANO_FINAL

    def adicionar_cidade(self, cidade: Cidade) -> bool:
        if len(self._cidades) >= self.MAXIMO_JOGADORES:
            return False
        self._cidades.append(cidade)
        return True

    def passar_turno(self) -> bool:
        """Passa a vez. True quando o ultimo jogador encerrou (o ano acabou)."""
        self._indice_atual += 1
        if self._indice_atual >= len(self._cidades):
            self._indice_atual = 0
            return True
        return False

    def encerrar_ano(self, nobreza: Nobreza) -> list[Cidade]:
        """Avanca o ano de cada cidade e devolve as cidades promovidas."""
        promovidas = []
        for cidade in self._cidades:
            cidade.avancar_ano()
            if nobreza.verificar_promocao(cidade):
                promovidas.append(cidade)
        return promovidas

    def terminou(self) -> bool:
        if any(c.dono.eh_monarca() for c in self._cidades):
            return True
        return self.ano_atual > self.ANO_FINAL

    def determinar_vencedor(self, nobreza: Nobreza) -> Cidade:
        """Titulo mais alto; em caso de empate, maior prestigio."""
        return max(self._cidades,
                   key=lambda c: (c.dono.nivel_titulo,
                                  nobreza.calcular_prestigio(c)))
