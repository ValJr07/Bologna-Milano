from __future__ import annotations

from cidade import Cidade
from jogador import Jogador


class Menu:

    def __init__(self) -> None:
        self._em_execucao = True
        self._jogador: Jogador | None = None
        self._cidade: Cidade | None = None

    def executar(self) -> None:
        while self._em_execucao:
            self._exibir_opcoes()
            opcao = self._ler_opcao()
            self._processar_opcao(opcao)

    def _exibir_opcoes(self) -> None:
        print()
        print("==========================================")
        print("            BOLONHA E MILANO")
        print("  Um jogo de estrategia economica medieval")
        print("==========================================")
        print("1 - Novo jogo")
        print("2 - Sobre o jogo")
        print("3 - Ver status da cidade")
        print("0 - Sair")
        print("Escolha uma opcao: ", end="", flush=True)

    def _ler_opcao(self) -> int:
        try:
            linha = input().strip()
        except EOFError:
            return 0
        try:
            return int(linha)
        except ValueError:
            return -1

    def _processar_opcao(self, opcao: int) -> None:
        if opcao == 1:
            self._iniciar_novo_jogo()
        elif opcao == 2:
            self._exibir_sobre()
        elif opcao == 3:
            self._exibir_status_cidade()
        elif opcao == 0:
            print("\nAte logo!")
            self._em_execucao = False
        else:
            print("\nOpcao invalida! Digite 1, 2, 3 ou 0.")

    def _iniciar_novo_jogo(self) -> None:
        if self._cidade is not None:
            print("\nAtencao: o jogo anterior sera substituido.")

        print()
        nome_jogador = self._ler_texto("Digite o nome do jogador: ")
        if nome_jogador is None:
            return
        nome_cidade = self._ler_texto("Digite o nome da cidade: ")
        if nome_cidade is None:
            return

        self._jogador = Jogador(nome_jogador)
        self._cidade = Cidade(nome_cidade, self._jogador)

        print()
        print(f"Novo jogo criado! {self._jogador.titulo} "
              f"{self._jogador.nome}, bem-vindo a {nome_cidade}.")

    def _exibir_status_cidade(self) -> None:
        if self._cidade is None:
            print("\nNenhum jogo iniciado. Escolha 'Novo jogo' primeiro.")
        else:
            self._cidade.exibir_status()

    def _exibir_sobre(self) -> None:
        print()
        print("------------------------------------------")
        print("SOBRE O JOGO")
        print("------------------------------------------")
        print("Bolonha e Milano e um jogo de estrategia")
        print("economica ambientado na Italia medieval.")
        print("Voce comanda um comerciante que viaja entre")
        print("as cidades de Bolonha e Milano, comprando e")
        print("vendendo mercadorias para enriquecer.")
        print("------------------------------------------")

    def _ler_texto(self, pergunta: str) -> str | None:
        while True:
            print(pergunta, end="", flush=True)
            try:
                linha = input()
            except EOFError:
                self._em_execucao = False
                return None
            texto = linha.strip()
            if texto:
                return texto
            print("O nome nao pode ficar vazio.")
