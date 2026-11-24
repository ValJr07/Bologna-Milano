from cidade import Cidade
from jogador import Jogador


class Nobreza:
    """Calcula o prestigio da cidade e promove o governante.

    Nao guarda nenhuma Cidade: ela e recebida como parametro em cada operacao.
    """

    _PESO_CONSTRUCAO = 10
    _PESO_SOLDADO = 2
    _PESO_SERVO = 1
    _HECTARES_POR_PONTO = 100
    # Prestigio minimo para cada nivel de titulo (Cavaleiro ... Rei/Rainha).
    _PRESTIGIO_MINIMO = (0, 400, 550, 700, 850, 1000)

    def calcular_prestigio(self, cidade: Cidade) -> int:
        """Florins nao entram na conta: para subir e preciso investir."""
        return (cidade.construcoes * self._PESO_CONSTRUCAO
                + cidade.soldados * self._PESO_SOLDADO
                + cidade.servos * self._PESO_SERVO
                + cidade.terras // self._HECTARES_POR_PONTO)

    def prestigio_para_proximo_titulo(self, jogador: Jogador) -> int:
        """Prestigio exigido pelo proximo titulo, ou -1 se ja for Rei/Rainha."""
        if jogador.eh_monarca():
            return -1
        return self._PRESTIGIO_MINIMO[jogador.nivel_titulo + 1]

    def verificar_promocao(self, cidade: Cidade) -> bool:
        """Promove o dono em no maximo UM titulo por chamada."""
        dono = cidade.dono
        necessario = self.prestigio_para_proximo_titulo(dono)
        if necessario == -1:
            return False
        if self.calcular_prestigio(cidade) < necessario:
            return False
        return dono.promover()
