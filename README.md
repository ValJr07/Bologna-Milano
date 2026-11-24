# Bolonha e Milano

Jogo de estratégia econômica medieval em Python, jogado pelo console. O jogador comanda uma cidade da Itália medieval, começando no ano de 1400 com o título de Cavaleiro.

> Projeto em desenvolvimento (SPOTDES). Por enquanto existem o menu, a criação do jogador e da cidade, o mercado de grãos e terras, a agricultura com a população e o governo com os impostos e as construções com soldados e edifícios, e a partida com rodadas, vários jogadores e vitória.

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

## Construções e soldados

A cidade começa com **0 soldados** e **0 construções**. No menu **Construções**:

- **Recrutar soldados**: cada soldado custa **5 florins + 1 servo**. Florins e servos são validados *antes* de alterar qualquer um; se faltar um dos dois, nada muda.
- **Construir**: cada construção custa **20 florins**.

Soldados e construções são recursos acumuláveis (voltam ao padrão `adicionar_*`/`remover_*`) e aparecem em "Ver status da cidade".

## Rodadas, jogadores e vitória

Uma partida tem de **1 a 4 jogadores** (cada um com a sua cidade). Cada jogador joga o seu turno e usa **Encerrar turno** (opção 7); quando o último encerra, o ano fecha e todos avançam um ano. Começa em 1400 e termina em 1410.

- **Colher** e **Arrecadar impostos** valem **uma vez por ano** por cidade.
- **Prestígio** = construções × 10 + soldados × 2 + servos + terras ÷ 100 (florins não contam). Uma cidade nova começa com 300.
- **Títulos** (prestígio mínimo): Cavaleiro (início) · Barão 400 · Conde 550 · Marquês 700 · Duque 850 · Rei/Rainha 1000. A promoção é checada ao fechar o ano, no máximo **um título por ano**.
- **Vitória**: quem virar Rei/Rainha primeiro, ou o melhor colocado ao fim de 1410 (título mais alto; empate, maior prestígio).
- **Ver classificação** (opção 8) mostra o ranking a qualquer momento. "Sobre o jogo" passa a ser a opção 9.

## Etapas

- **Etapa 1**: estrutura inicial, módulo `main` e classe `Menu`.
- **Etapa 2**: classes `Jogador` e `Cidade`, novo jogo e status da cidade.
- **Etapa 3**: economia. `Cidade` ganha florins, terras e grãos; nova classe `Mercado` (preços fixos) e novo menu "Mercado" com compra e venda de grãos e terras.
- **Etapa 4**: agricultura e população. `Cidade` ganha servos; nova classe `Agricultura` (colheita e distribuição de alimentos) e novo menu "Agricultura".
- **Etapa 5**: impostos e governo. `Cidade` ganha taxa de imposto e nível de justiça; nova classe `Governo` (arrecadação, validação de taxa e justiça) e novo menu "Governo".
- **Etapa 6**: construções e soldados. `Cidade` ganha soldados e construções; nova classe `Construcoes` (recrutar soldados validando florins e servos, construir) e novo menu "Construções" (opção 6; "Sobre o jogo" passa a ser a 7).
- **Etapa 7**: rodadas, múltiplos jogadores e vitória. Novas classes `Partida` (turnos, anos, fim de jogo, vencedor) e `Nobreza` (prestígio e promoção); `Jogador` troca `titulo` por `nivel_titulo`; `Cidade` ganha os indicadores de colheita e impostos do ano; novos menus "Encerrar turno" e "Ver classificação".
