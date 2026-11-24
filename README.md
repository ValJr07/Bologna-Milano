# Bolonha e Milano

Jogo de estratégia econômica medieval em Python, jogado pelo console. O jogador comanda uma cidade da Itália medieval, começando no ano de 1400 com o título de Cavaleiro.

> Projeto em desenvolvimento (SPOTDES). Por enquanto existem o menu, a criação do jogador e da cidade e o mercado de grãos e terras.

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

Nenhuma operação deixa florins, terras ou grãos negativos: se faltar saldo ou estoque, a operação é recusada e nada muda.

## Etapas

- **Etapa 1**: estrutura inicial, módulo `main` e classe `Menu`.
- **Etapa 2**: classes `Jogador` e `Cidade`, novo jogo e status da cidade.
- **Etapa 3**: economia. `Cidade` ganha florins, terras e grãos; nova classe `Mercado` (preços fixos) e novo menu "Mercado" com compra e venda de grãos e terras.
