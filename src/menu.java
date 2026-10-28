package bolonhaemilano;

import java.util.Scanner;

public class Menu {

    private final Scanner scanner;
    private boolean emExecucao;

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
        System.out.println("0 - Sair");
        System.out.print("Escolha uma opcao: ");
    }

    // Le uma linha e converte para inteiro. Se for invalida, devolve -1.
    private int lerOpcao() {
        // Se a entrada acabou (Ctrl+D / fim do arquivo), encerra o menu sem travar.
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

    // Decide a acao conforme o numero lido.
    private void processarOpcao(int opcao) {
        switch (opcao) {
            case 1:
                System.out.println("\nNovo jogo sera implementado na Etapa 2.");
                break;
            case 2:
                exibirSobre();
                break;
            case 0:
                System.out.println("\nAte logo!");
                emExecucao = false;
                break;
            default:
                System.out.println("\nOpcao invalida! Digite 1, 2 ou 0.");
        }
    }

    // So e chamada quando processarOpcao recebe a opcao 2.
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
}