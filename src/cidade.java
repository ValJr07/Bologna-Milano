package bolonhaemilano;

public class Cidade {

    private final String nome;
    private final Jogador dono;
    private int anoAtual;

    public Cidade(String nome, Jogador dono) {
        this.nome = nome;
        this.dono = dono;
        this.anoAtual = 1400;
    }

    // Sera chamado apenas a partir da Etapa 7.
    public void avancarAno() {
        anoAtual++;
    }

    public void exibirStatus() {
        System.out.println();
        System.out.println("------------------------------------------");
        System.out.println("STATUS DA CIDADE");
        System.out.println("------------------------------------------");
        System.out.println("Cidade:     " + nome);
        System.out.println("Governante: " + dono.getTitulo() + " " + dono.getNome());
        System.out.println("Ano atual:  " + anoAtual);
        System.out.println("------------------------------------------");
    }
}