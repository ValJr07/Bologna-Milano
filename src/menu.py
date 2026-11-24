from __future__ import annotations

from agricultura import Agricultura
from cidade import Cidade
from construcoes import Construcoes
from governo import Governo
from jogador import Jogador
from mercado import Mercado
from nobreza import Nobreza
from partida import Partida


class Menu:

    def __init__(self) -> None:
        self._em_execucao = True
        self._partida: Partida | None = None
        self._cidade: Cidade | None = None
        self._mercado = Mercado()
        self._agricultura = Agricultura()
        self._governo = Governo()
        self._construcoes = Construcoes()
        self._nobreza = Nobreza()

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
        print("5 - Governo")
        print("6 - Construcoes")
        print("7 - Encerrar turno")
        print("8 - Ver classificacao")
        print("9 - Sobre o jogo")
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
            self._abrir_governo()
        elif opcao == 6:
            self._abrir_construcoes()
        elif opcao == 7:
            self._encerrar_turno()
        elif opcao == 8:
            self._exibir_classificacao()
        elif opcao == 9:
            self._exibir_sobre()
        elif opcao == 0:
            print("\nAte logo!")
            self._em_execucao = False
        else:
            print("\nOpcao invalida! Digite de 1 a 9 ou 0.")

    def _iniciar_novo_jogo(self) -> None:
        if self._partida is not None:
            print("\nAtencao: o jogo anterior sera substituido.")

        print()
        maximo = Partida.MAXIMO_JOGADORES
        quantidade = self._ler_inteiro(f"Quantos jogadores (1 a {maximo})? ")
        if quantidade is None:
            return
        if not 1 <= quantidade <= maximo:
            quantidade = 2
            print("Valor invalido: serao 2 jogadores.")

        partida = Partida()
        for numero in range(1, quantidade + 1):
            print(f"\n--- Jogador {numero} ---")
            nome_jogador = self._ler_texto("Digite o nome do jogador: ")
            if nome_jogador is None:
                return
            nome_cidade = self._ler_texto("Digite o nome da cidade: ")
            if nome_cidade is None:
                return
            partida.adicionar_cidade(Cidade(nome_cidade, Jogador(nome_jogador)))

        self._partida = partida
        self._cidade = partida.cidade_atual

        print()
        print(f"Novo jogo criado! A partida vai de {partida.ano_atual} "
              f"ate {partida.ano_final}.")
        self._anunciar_vez()

    def _anunciar_vez(self) -> None:
        cidade = self._cidade
        print(f"Agora e a vez de {cidade.dono.titulo} {cidade.dono.nome}, "
              f"governante de {cidade.nome} (ano {cidade.ano_atual}).")

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
        if hectares == -1:
            print("Sua cidade ja colheu neste ano. Encerre o turno.")
            return
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

    def _abrir_governo(self) -> None:
        cidade = self._cidade
        if cidade is None:
            print("\nNenhum jogo iniciado. Escolha 'Novo jogo' primeiro.")
            return

        no_governo = True
        while no_governo and self._em_execucao:
            self._exibir_opcoes_governo(cidade)
            opcao = self._ler_opcao()
            if opcao == 1:
                self._arrecadar_impostos(cidade)
            elif opcao == 2:
                self._definir_taxa_imposto(cidade)
            elif opcao == 3:
                self._definir_justica(cidade)
            elif opcao == 0:
                no_governo = False
            else:
                print("\nOpcao invalida! Digite 1, 2, 3 ou 0.")

    def _exibir_opcoes_governo(self, cidade: Cidade) -> None:
        print()
        print("------------------------------------------")
        print("GOVERNO")
        print("------------------------------------------")
        print(f"Seus florins:      {cidade.florins}")
        print(f"Seus servos:       {cidade.servos}")
        print(f"Taxa de imposto:   {cidade.taxa_imposto}%")
        print(f"Nivel de justica:  {cidade.nivel_justica}")
        print("------------------------------------------")
        print("1 - Arrecadar impostos")
        print("2 - Definir taxa de imposto")
        print("3 - Definir nivel de justica")
        print("0 - Voltar")
        print("Escolha uma opcao: ", end="", flush=True)

    def _arrecadar_impostos(self, cidade: Cidade) -> None:
        florins_antes = cidade.florins
        arrecadado = self._governo.arrecadar_impostos(cidade)
        print()
        if arrecadado == -1:
            print("Sua cidade ja arrecadou impostos neste ano. Encerre o turno.")
            return
        print(f"Impostos arrecadados: {arrecadado} florins.")
        print(f"Florins: {florins_antes} -> {cidade.florins}")

    def _definir_taxa_imposto(self, cidade: Cidade) -> None:
        maxima = self._governo.taxa_maxima
        taxa = self._ler_inteiro(f"Nova taxa de imposto (0 a {maxima}): ")
        if taxa is None:
            return
        if self._governo.definir_taxa_imposto(cidade, taxa):
            print(f"\nTaxa de imposto definida: {taxa}%.")
        else:
            print(f"\nTaxa invalida. Digite um valor de 0 a {maxima}.")

    def _definir_justica(self, cidade: Cidade) -> None:
        niveis = self._governo.niveis_justica
        print()
        print(f"Nivel de justica atual: {cidade.nivel_justica}")
        for numero, nivel in enumerate(niveis, start=1):
            print(f"{numero} - {nivel}")
        escolha = self._ler_inteiro("Escolha o nivel: ")
        if escolha is None:
            return
        if not 1 <= escolha <= len(niveis):
            print("\nOpcao invalida. O nivel de justica nao foi alterado.")
            return
        nivel = niveis[escolha - 1]
        if self._governo.definir_justica(cidade, nivel):
            print(f"\nNivel de justica definido: {nivel}.")
        else:
            print("\nNivel de justica invalido.")

    def _abrir_construcoes(self) -> None:
        cidade = self._cidade
        if cidade is None:
            print("\nNenhum jogo iniciado. Escolha 'Novo jogo' primeiro.")
            return

        na_construcoes = True
        while na_construcoes and self._em_execucao:
            self._exibir_opcoes_construcoes(cidade)
            opcao = self._ler_opcao()
            if opcao == 1:
                self._recrutar_soldados(cidade)
            elif opcao == 2:
                self._construir(cidade)
            elif opcao == 0:
                na_construcoes = False
            else:
                print("\nOpcao invalida! Digite 1, 2 ou 0.")

    def _exibir_opcoes_construcoes(self, cidade: Cidade) -> None:
        print()
        print("------------------------------------------")
        print("CONSTRUCOES")
        print("------------------------------------------")
        print(f"Custo do soldado:    {self._construcoes.preco_soldado} florins + 1 servo")
        print(f"Custo da construcao: {self._construcoes.preco_construcao} florins")
        print(f"Seus florins:        {cidade.florins}")
        print(f"Seus servos:         {cidade.servos}")
        print(f"Seus soldados:       {cidade.soldados}")
        print(f"Suas construcoes:    {cidade.construcoes}")
        print("------------------------------------------")
        print("1 - Recrutar soldados")
        print("2 - Construir")
        print("0 - Voltar")
        print("Escolha uma opcao: ", end="", flush=True)

    def _recrutar_soldados(self, cidade: Cidade) -> None:
        quantidade = self._ler_quantidade()
        if quantidade is None:
            return
        if quantidade <= 0:
            print("\nQuantidade invalida.")
        elif self._construcoes.recrutar_soldados(cidade, quantidade):
            custo = quantidade * self._construcoes.preco_soldado
            print(f"\nRecrutamento realizado: {quantidade} soldados por "
                  f"{custo} florins e {quantidade} servos.")
        else:
            print("\nFlorins ou servos insuficientes.")

    def _construir(self, cidade: Cidade) -> None:
        quantidade = self._ler_quantidade()
        if quantidade is None:
            return
        if quantidade <= 0:
            print("\nQuantidade invalida.")
        elif self._construcoes.construir(cidade, quantidade):
            custo = quantidade * self._construcoes.preco_construcao
            print(f"\nConstrucao realizada: {quantidade} construcoes "
                  f"por {custo} florins.")
        else:
            print("\nFlorins insuficientes.")

    def _encerrar_turno(self) -> None:
        partida = self._partida
        if partida is None:
            print("\nNenhum jogo iniciado. Escolha 'Novo jogo' primeiro.")
            return

        print()
        if not partida.passar_turno():
            self._cidade = partida.cidade_atual
            self._anunciar_vez()
            return

        print(f"O ano {partida.ano_atual} chegou ao fim.")
        promovidas = partida.encerrar_ano(self._nobreza)
        for cidade in promovidas:
            print(f"{cidade.dono.nome} foi promovido(a) a {cidade.dono.titulo}!")
        self._exibir_classificacao()

        if partida.terminou():
            self._encerrar_partida()
        else:
            self._cidade = partida.cidade_atual
            print()
            print(f"Comeca o ano {partida.ano_atual}.")
            self._anunciar_vez()

    def _exibir_classificacao(self) -> None:
        partida = self._partida
        if partida is None:
            print("\nNenhum jogo iniciado. Escolha 'Novo jogo' primeiro.")
            return

        print()
        print("------------------------------------------")
        print(f"CLASSIFICACAO - ano {partida.ano_atual}")
        print("------------------------------------------")
        ordenadas = sorted(
            partida.cidades,
            key=lambda c: (c.dono.nivel_titulo, self._nobreza.calcular_prestigio(c)),
            reverse=True)
        for posicao, cidade in enumerate(ordenadas, start=1):
            prestigio = self._nobreza.calcular_prestigio(cidade)
            necessario = self._nobreza.prestigio_para_proximo_titulo(cidade.dono)
            if necessario == -1:
                proximo = "titulo maximo"
            else:
                faltam = max(0, necessario - prestigio)
                proximo = f"faltam {faltam} para o proximo titulo"
            print(f"{posicao}. {cidade.nome} - {cidade.dono.titulo} "
                  f"{cidade.dono.nome} | prestigio {prestigio} | {proximo}")
        print("------------------------------------------")

    def _encerrar_partida(self) -> None:
        vencedor = self._nobreza_vencedor()
        print()
        print("==========================================")
        print("FIM DE JOGO")
        print("==========================================")
        print(f"Vencedor: {vencedor.dono.titulo} {vencedor.dono.nome}, "
              f"governante de {vencedor.nome}!")
        self._partida = None
        self._cidade = None

    def _nobreza_vencedor(self) -> Cidade:
        return self._partida.determinar_vencedor(self._nobreza)

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
