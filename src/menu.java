package bolonhaemilano;

import java.util.Scanner;

public class Menu {

    private final Scanner scanner;
    private boolean emExecucao;
    private Jogador jogador;
    private Cidade cidade;

    public Menu() {
        this.scanner = new Scanner(System.in);
        this.emExecucao = true;
    }

    public void executar() {
        while (emExecucao) {
            exibirOpcoes();
            int opcao = lerOpcao();
            processarOpcao(opcao);
        }
        scanner.close();
    }

    private void exibirOpcoes() {
        System.out.println();
        System.out.println("==========================================");
        System.out.println("            BOLONHA E MILANO");
        System.out.println("  Um jogo de estrategia economica medieval");
        System.out.println("==========================================");
        System.out.println("1 - Novo jogo");
        System.out.println("2 - Sobre o jogo");
        System.out.println("3 - Ver status da cidade");
        System.out.println("0 - Sair");
        System.out.print("Escolha uma opcao: ");
    }

    private int lerOpcao() {
        if (!scanner.hasNextLine()) {
            return 0;
        }
        String linha = scanner.nextLine().trim();
        try {
            return Integer.parseInt(linha);
        } catch (NumberFormatException e) {
            return -1;
        }
    }

    private void processarOpcao(int opcao) {
        switch (opcao) {
            case 1:
                iniciarNovoJogo();
                break;
            case 2:
                exibirSobre();
                break;
            case 3:
                exibirStatusCidade();
                break;
            case 0:
                System.out.println("\nAte logo!");
                emExecucao = false;
                break;
            default:
                System.out.println("\nOpcao invalida! Digite 1, 2, 3 ou 0.");
        }
    }

    private void iniciarNovoJogo() {
        if (cidade != null) {
            System.out.println("\nAtencao: o jogo anterior sera substituido.");
        }

        System.out.println();
        String nomeJogador = lerTexto("Digite o nome do jogador: ");
        if (nomeJogador == null) {
            return;
        }
        String nomeCidade = lerTexto("Digite o nome da cidade: ");
        if (nomeCidade == null) {
            return;
        }

        jogador = new Jogador(nomeJogador);
        cidade = new Cidade(nomeCidade, jogador);

        System.out.println();
        System.out.println("Novo jogo criado! " + jogador.getTitulo() + " "
                + jogador.getNome() + ", bem-vindo a " + nomeCidade + ".");
    }

    private void exibirStatusCidade() {
        if (cidade == null) {
            System.out.println("\nNenhum jogo iniciado. Escolha 'Novo jogo' primeiro.");
        } else {
            cidade.exibirStatus();
        }
    }

    private void exibirSobre() {
        System.out.println();
        System.out.println("------------------------------------------");
        System.out.println("SOBRE O JOGO");
        System.out.println("------------------------------------------");
        System.out.println("Bolonha e Milano e um jogo de estrategia");
        System.out.println("economica ambientado na Italia medieval.");
        System.out.println("Voce comanda um comerciante que viaja entre");
        System.out.println("as cidades de Bolonha e Milano, comprando e");
        System.out.println("vendendo mercadorias para enriquecer.");
        System.out.println("------------------------------------------");
    }

    private String lerTexto(String pergunta) {
        while (true) {
            System.out.print(pergunta);
            if (!scanner.hasNextLine()) {
                emExecucao = false;
                return null;
            }
            String texto = scanner.nextLine().trim();
            if (!texto.isEmpty()) {
                return texto;
            }
            System.out.println("O nome nao pode ficar vazio.");
        }
    }
}