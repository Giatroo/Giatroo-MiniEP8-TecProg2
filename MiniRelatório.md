# Relatório com a experiência de TDD

Nesse mini EP vou me propor a fazer uma calculadora de média de dados. Ou seja, um programa que recebe uma string representando resultados de dados e calcula a esperança do resultado dos dados.

Por exemplo,

`1d6` representa o lançamento de um dado de seis lados.

`XdN` representa o lançamento de `X` dados de `N` lados. O resultado final desse lançamento é a soma das faces viradas para cima de cada dado.

Podemos também somar lançamentos de dados diferentes. Sejam `N` e `M` dois números inteiros, então podemos ter a fórmula:
`XdN + YdM`, onde `X` e `Y` também são números inteiros. Nesse caso, estamos fazendo um lançamento com `X` dados de `N` lados e `Y` dados de `M` lados. Se `N=M`, então a fórmula é equivalente a `Xd2N`.

Por fim, além de somar dados, podemos somar ou multiplicar valores inteiros.
`XdN + Y` representa fazer um lançamento de `X` dados de `N` lados e somar `Y` ao resultado final.

O programa será feito em `python`.