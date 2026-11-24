# Bolonha e Milano

Jogo de estratégia econômica medieval em Python, jogado pelo console. O jogador comanda uma cidade da Itália medieval, começando no ano de 1400 com o título de Cavaleiro.

> Projeto em desenvolvimento (SPOTDES). Por enquanto existem o menu, a criação do jogador e da cidade, o mercado de grãos e terras, a agricultura com a população e o governo com os impostos.

## Como executar

Requer Python 3.8 ou superior. Na raiz do projeto:

```
python src/main.py
```

## Economia

A cidade começa com **1000 florins**, **10000 hectares** de terra e **500 unidades** de grãos. No menu **Mercado** é possível comprar e vender grãos e terras a preços fixos:

| Mercadoria | Preço (florins) |
|------------|-----------------|
| Grão       | 2               |
| Hectare    | 10              |

Nenhuma operação deixa florins, terras, grãos ou servos negativos: se faltar saldo ou estoque, a operação é recusada e nada muda.

## Agricultura e população

A cidade começa com **200 servos**. No menu **Agricultura**:

- **Colher**: cultiva `min(terras, servos × 5)` hectares. Gasta 1 grão de semente a cada 2 hectares (se faltar grão, planta só o que o estoque permite) e produz 2 grãos por hectare.
- **Distribuir alimentos**: o jogador escolhe um percentual do estoque de grãos, entre 20 e 80. A necessidade mínima é `servos ÷ 5`. Se o alimento distribuído cobre a necessidade, a população cresce 5%; se não, perde o déficit em servos (nunca abaixo de zero).

## Impostos e governo

A cidade começa com **imposto de 10%** e justiça **Moderada**. No menu **Governo**:

- **Arrecadar impostos**: `base = servos × taxa ÷ 100`, multiplicada pelo fator da justiça (**Justa** 0,8 · **Moderada** 1,0 · **Severa** 1,3) e truncada para inteiro. O valor é somado aos florins.
- **Definir taxa de imposto**: aceita de 0 a 50.
- **Definir nível de justiça**: Justa, Moderada ou Severa.

Taxa e justiça são configurações da cidade (não recursos acumuláveis), então são apenas lidas e definidas, nunca somadas ou subtraídas.

## Etapas

- **Etapa 1**: estrutura inicial, módulo `main` e classe `Menu`.
- **Etapa 2**: classes `Jogador` e `Cidade`, novo jogo e status da cidade.
- **Etapa 3**: economia. `Cidade` ganha florins, terras e grãos; nova classe `Mercado` (preços fixos) e novo menu "Mercado" com compra e venda de grãos e terras.
- **Etapa 4**: agricultura e população. `Cidade` ganha servos; nova classe `Agricultura` (colheita e distribuição de alimentos) e novo menu "Agricultura".
- **Etapa 5**: impostos e governo. `Cidade` ganha taxa de imposto e nível de justiça; nova classe `Governo` (arrecadação, validação de taxa e justiça) e novo menu "Governo".
