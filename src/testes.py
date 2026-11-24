"""Testes automatizados das regras do jogo (sem bibliotecas externas).

Segundo ponto de entrada do projeto: nao faz parte do jogo, e nenhuma classe
do jogo conhece esta. Para rodar, na raiz do projeto:

    python src/testes.py

Padrao de cada teste: preparar, executar, verificar.
"""
import sys

from agricultura import Agricultura
from cidade import Cidade
from construcoes import Construcoes
from governo import Governo
from jogador import Jogador
from mercado import Mercado
from nobreza import Nobreza
from partida import Partida


class Testes:

    _aprovados = 0
    _reprovados = 0

    @staticmethod
    def main() -> None:
        print("===== TESTES BOLONHA E MILANO =====")
        Testes._testar_cidade()
        Testes._testar_mercado()
        Testes._testar_agricultura()
        Testes._testar_governo()
        Testes._testar_construcoes()
        Testes._testar_jogador_e_nobreza()
        Testes._testar_partida()
        print()
        print(f"Aprovados: {Testes._aprovados} | "
              f"Reprovados: {Testes._reprovados}")
        if Testes._reprovados > 0:
            sys.exit(1)

    @staticmethod
    def _verificar(descricao: str, condicao: bool) -> None:
        if condicao:
            Testes._aprovados += 1
            print(f"[OK]    {descricao}")
        else:
            Testes._reprovados += 1
            print(f"[FALHA] {descricao}")

    @staticmethod
    def _nova_cidade() -> Cidade:
        """Atalho para preparar: sempre com os valores iniciais."""
        return Cidade("Bolonha", Jogador("Teste"))

    @staticmethod
    def _testar_cidade() -> None:
        print("\n-- Cidade --")
        cidade = Testes._nova_cidade()
        Testes._verificar("cidade nasce com 1000 florins",
                          cidade.florins == 1000)
        Testes._verificar("cidade nasce no ano 1400", cidade.ano_atual == 1400)

        removeu = cidade.remover_florins(1001)
        Testes._verificar("remover_florins acima do saldo devolve False",
                          not removeu)
        Testes._verificar("... e nao altera o saldo", cidade.florins == 1000)

        cidade.marcar_colheita_feita()
        cidade.avancar_ano()
        Testes._verificar("avancar_ano soma 1 ao ano", cidade.ano_atual == 1401)
        Testes._verificar("avancar_ano libera a colheita de novo",
                          not cidade.colheita_feita())

    @staticmethod
    def _testar_mercado() -> None:
        print("\n-- Mercado --")
        mercado = Mercado()
        cidade = Testes._nova_cidade()
        comprou = mercado.comprar_graos(cidade, 100)
        Testes._verificar("comprar 100 graos da certo", comprou)
        Testes._verificar("... e custa 200 florins", cidade.florins == 800)
        Testes._verificar("... e soma 100 graos", cidade.graos == 600)

        cidade = Testes._nova_cidade()
        Testes._verificar("comprar quantidade negativa e recusado",
                          not mercado.comprar_graos(cidade, -5))

        cidade = Testes._nova_cidade()
        cidade.remover_florins(1000)
        Testes._verificar("comprar sem florins suficientes e recusado",
                          not mercado.comprar_graos(cidade, 100))

    @staticmethod
    def _testar_agricultura() -> None:
        print("\n-- Agricultura --")
        agricultura = Agricultura()
        cidade = Testes._nova_cidade()
        hectares = agricultura.processar_colheita(cidade)
        Testes._verificar("primeira colheita do ano cultiva 1000 hectares",
                          hectares == 1000)
        Testes._verificar("... e deixa 2000 graos (500 - 500 sementes + 2000)",
                          cidade.graos == 2000)
        Testes._verificar("segunda colheita no mesmo ano devolve -1",
                          agricultura.processar_colheita(cidade) == -1)

        cidade = Testes._nova_cidade()
        Testes._verificar("distribuir 10% e recusado (minimo 20%)",
                          not agricultura.distribuir_alimentos(cidade, 10))

    @staticmethod
    def _testar_governo() -> None:
        print("\n-- Governo --")
        governo = Governo()
        cidade = Testes._nova_cidade()
        Testes._verificar("taxa de 60% e recusada (maximo 50%)",
                          not governo.definir_taxa_imposto(cidade, 60))
        Testes._verificar('justica "Branda" e recusada',
                          not governo.definir_justica(cidade, "Branda"))

        governo.definir_justica(cidade, "Severa")
        arrecadado = governo.arrecadar_impostos(cidade)
        Testes._verificar("200 servos, 10%, Severa: arrecada 26 florins",
                          arrecadado == 26)
        Testes._verificar("segunda arrecadacao no mesmo ano devolve -1",
                          governo.arrecadar_impostos(cidade) == -1)

    @staticmethod
    def _testar_construcoes() -> None:
        print("\n-- Construcoes --")
        construcoes = Construcoes()
        # preparar: florins bastam (500 de 1000), servos nao (so 50)
        cidade = Testes._nova_cidade()
        cidade.remover_servos(150)
        # executar
        recrutou = construcoes.recrutar_soldados(cidade, 100)
        # verificar
        Testes._verificar("recrutar 100 soldados com so 50 servos e recusado",
                          not recrutou)
        Testes._verificar("... e NAO debita florins pela metade",
                          cidade.florins == 1000)

        cidade = Testes._nova_cidade()
        Testes._verificar("construir 10 da certo",
                          construcoes.construir(cidade, 10))
        Testes._verificar("... e custa 200 florins", cidade.florins == 800)

    @staticmethod
    def _testar_jogador_e_nobreza() -> None:
        print("\n-- Jogador e Nobreza --")
        nobreza = Nobreza()
        cidade = Testes._nova_cidade()
        Testes._verificar("jogador comeca como Cavaleiro",
                          cidade.dono.titulo == "Cavaleiro")
        Testes._verificar("prestigio inicial e 300 (200 servos + 10000/100 terras)",
                          nobreza.calcular_prestigio(cidade) == 300)
        Testes._verificar("com prestigio 300 nao sobe de titulo",
                          not nobreza.verificar_promocao(cidade))

        cidade.adicionar_construcoes(50)
        Testes._verificar("com 50 construcoes sobe para Barao",
                          nobreza.verificar_promocao(cidade)
                          and cidade.dono.titulo == "Barao")
        Testes._verificar("sobe no maximo um titulo por chamada",
                          cidade.dono.nivel_titulo == 1)

        jogador = Jogador("Rei")
        while jogador.promover():
            pass
        Testes._verificar("promover para alem de Rei/Rainha e recusado",
                          jogador.eh_monarca() and not jogador.promover())

    @staticmethod
    def _testar_partida() -> None:
        print("\n-- Partida --")
        nobreza = Nobreza()
        partida = Partida()
        bolonha = Cidade("Bolonha", Jogador("Ana"))
        milano = Cidade("Milano", Jogador("Bia"))
        partida.adicionar_cidade(bolonha)
        partida.adicionar_cidade(milano)
        milano.adicionar_construcoes(50)

        Testes._verificar("primeiro turno e de Bolonha",
                          partida.cidade_atual is bolonha)
        Testes._verificar("passar o turno de Bolonha NAO fecha o ano",
                          not partida.passar_turno())
        Testes._verificar("agora e a vez de Milano",
                          partida.cidade_atual is milano)
        Testes._verificar("passar o turno de Milano fecha o ano",
                          partida.passar_turno())

        partida.encerrar_ano(nobreza)
        Testes._verificar("encerrar_ano avanca todas as cidades",
                          bolonha.ano_atual == 1401 and milano.ano_atual == 1401)
        Testes._verificar("partida ainda nao terminou em 1401",
                          not partida.terminou())
        Testes._verificar("vencedor parcial e Milano (titulo mais alto)",
                          partida.determinar_vencedor(nobreza) is milano)

        for numero in range(2):
            partida.adicionar_cidade(Cidade(f"Extra{numero}", Jogador("X")))
        Testes._verificar("quinta cidade e recusada (maximo 4)",
                          not partida.adicionar_cidade(
                              Cidade("Quinta", Jogador("Y"))))


if __name__ == "__main__":
    Testes.main()
