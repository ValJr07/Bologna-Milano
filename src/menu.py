from __future__ import annotations

from agricultura import Agricultura
from cidade import Cidade
from jogador import Jogador
from mercado import Mercado


class Menu:

    def __init__(self) -> None:
        self._em_execucao = True
        self._jogador: Jogador | None = None
        self._cidade: Cidade | None = None
        self._mercado = Mercado()
        self._agricultura = Agricultura()

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
        print("2 - Ver status da cidade")
        print("3 - Mercado")
        print("4 - Agricultura")
        print("5 - Sobre o jogo")
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
            self._exibir_status()
        elif opcao == 3:
            self._abrir_mercado()
        elif opcao == 4:
            self._abrir_agricultura()
        elif opcao == 5:
            self._exibir_sobre()
        elif opcao == 0:
            print("\nAte logo!")
            self._em_execucao = False
        else:
            print("\nOpcao invalida! Digite 1, 2, 3, 4, 5 ou 0.")

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

    def _exibir_status(self) -> None:
        if self._cidade is None:
            print("\nNenhum jogo iniciado. Escolha 'Novo jogo' primeiro.")
        else:
            self._cidade.exibir_status()

    def _abrir_mercado(self) -> None:
        cidade = self._cidade
        if cidade is None:
            print("\nNenhum jogo iniciado. Escolha 'Novo jogo' primeiro.")
            return

        no_mercado = True
        while no_mercado and self._em_execucao:
            self._exibir_opcoes_mercado(cidade)
            opcao = self._ler_opcao()
            if opcao == 1:
                self._comprar_graos(cidade)
            elif opcao == 2:
                self._vender_graos(cidade)
            elif opcao == 3:
                self._comprar_terras(cidade)
            elif opcao == 4:
                self._vender_terras(cidade)
            elif opcao == 0:
                no_mercado = False
            else:
                print("\nOpcao invalida! Digite 1, 2, 3, 4 ou 0.")

    def _exibir_opcoes_mercado(self, cidade: Cidade) -> None:
        print()
        print("------------------------------------------")
        print("MERCADO")
        print("------------------------------------------")
        print(f"Preco do grao:  {self._mercado.preco_grao} florins")
        print(f"Preco da terra: {self._mercado.preco_terra} florins")
        print(f"Seus florins:   {cidade.florins}")
        print(f"Seus graos:     {cidade.graos}")
        print(f"Suas terras:    {cidade.terras} hectares")
        print("------------------------------------------")
        print("1 - Comprar graos")
        print("2 - Vender graos")
        print("3 - Comprar terras")
        print("4 - Vender terras")
        print("0 - Voltar")
        print("Escolha uma opcao: ", end="", flush=True)

    def _ler_quantidade(self) -> int | None:
        return self._ler_inteiro("Quantidade: ")

    def _ler_inteiro(self, pergunta: str) -> int | None:
        print(pergunta, end="", flush=True)
        try:
            linha = input().strip()
        except EOFError:
            self._em_execucao = False
            return None
        try:
            return int(linha)
        except ValueError:
            return -1

    def _comprar_graos(self, cidade: Cidade) -> None:
        quantidade = self._ler_quantidade()
        if quantidade is None:
            return
        if quantidade <= 0:
            print("\nQuantidade invalida.")
        elif self._mercado.comprar_graos(cidade, quantidade):
            custo = quantidade * self._mercado.preco_grao
            print(f"\nCompra realizada: {quantidade} graos por {custo} florins.")
        else:
            print("\nFlorins insuficientes.")

    def _vender_graos(self, cidade: Cidade) -> None:
        quantidade = self._ler_quantidade()
        if quantidade is None:
            return
        if quantidade <= 0:
            print("\nQuantidade invalida.")
        elif self._mercado.vender_graos(cidade, quantidade):
            receita = quantidade * self._mercado.preco_grao
            print(f"\nVenda realizada: {quantidade} graos por {receita} florins.")
        else:
            print("\nGraos insuficientes.")

    def _comprar_terras(self, cidade: Cidade) -> None:
        quantidade = self._ler_quantidade()
        if quantidade is None:
            return
        if quantidade <= 0:
            print("\nQuantidade invalida.")
        elif self._mercado.comprar_terras(cidade, quantidade):
            custo = quantidade * self._mercado.preco_terra
            print(f"\nCompra realizada: {quantidade} hectares por {custo} florins.")
        else:
            print("\nFlorins insuficientes.")

    def _vender_terras(self, cidade: Cidade) -> None:
        quantidade = self._ler_quantidade()
        if quantidade is None:
            return
        if quantidade <= 0:
            print("\nQuantidade invalida.")
        elif self._mercado.vender_terras(cidade, quantidade):
            receita = quantidade * self._mercado.preco_terra
            print(f"\nVenda realizada: {quantidade} hectares por {receita} florins.")
        else:
            print("\nTerras insuficientes.")

    def _abrir_agricultura(self) -> None:
        cidade = self._cidade
        if cidade is None:
            print("\nNenhum jogo iniciado. Escolha 'Novo jogo' primeiro.")
            return

        na_agricultura = True
        while na_agricultura and self._em_execucao:
            self._exibir_opcoes_agricultura(cidade)
            opcao = self._ler_opcao()
            if opcao == 1:
                self._colher(cidade)
            elif opcao == 2:
                self._distribuir_alimentos(cidade)
            elif opcao == 0:
                na_agricultura = False
            else:
                print("\nOpcao invalida! Digite 1, 2 ou 0.")

    def _exibir_opcoes_agricultura(self, cidade: Cidade) -> None:
        print()
        print("------------------------------------------")
        print("AGRICULTURA")
        print("------------------------------------------")
        print(f"Suas terras:    {cidade.terras} hectares")
        print(f"Seus servos:    {cidade.servos}")
        print(f"Seus graos:     {cidade.graos}")
        print("------------------------------------------")
        print("1 - Colher (processar safra)")
        print("2 - Distribuir alimentos")
        print("0 - Voltar")
        print("Escolha uma opcao: ", end="", flush=True)

    def _colher(self, cidade: Cidade) -> None:
        graos_antes = cidade.graos
        hectares = self._agricultura.processar_colheita(cidade)
        print()
        if hectares == 0:
            print("Nenhum hectare foi cultivado. "
                  "E preciso ter terras, servos e graos para a semente.")
            return
        variacao = cidade.graos - graos_antes
        print("Colheita realizada!")
        print(f"Hectares cultivados: {hectares}")
        print(f"Graos: {graos_antes} -> {cidade.graos} ({variacao:+d})")

    def _distribuir_alimentos(self, cidade: Cidade) -> None:
        minimo = self._agricultura.percentual_minimo
        maximo = self._agricultura.percentual_maximo
        percentual = self._ler_inteiro(
            f"Percentual de graos a distribuir ({minimo} a {maximo}): ")
        if percentual is None:
            return

        graos_antes = cidade.graos
        servos_antes = cidade.servos
        if not self._agricultura.distribuir_alimentos(cidade, percentual):
            print(f"\nPercentual invalido. Digite um valor de {minimo} a {maximo}.")
            return

        distribuido = graos_antes - cidade.graos
        print()
        print(f"Foram distribuidos {distribuido} graos a populacao.")
        if cidade.servos > servos_antes:
            print(f"Comida de sobra: a populacao cresceu de "
                  f"{servos_antes} para {cidade.servos} servos.")
        elif cidade.servos < servos_antes:
            print(f"Faltou comida: a populacao caiu de "
                  f"{servos_antes} para {cidade.servos} servos.")
        else:
            print(f"A populacao se manteve em {cidade.servos} servos.")

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
