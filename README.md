# Relatório com a experiência de TDD

Nesse mini EP vou me propor a fazer uma calculadora de média de dados. Ou seja, um programa que recebe uma string representando resultados de dados e calcula a esperança do resultado dos dados.

Por exemplo,

`1d6` representa o lançamento de um dado de seis lados.

`XdN` representa o lançamento de `X` dados de `N` lados. O resultado final desse lançamento é a soma das faces viradas para cima de cada dado.

Podemos também somar lançamentos de dados diferentes. Sejam `N` e `M` dois números inteiros, então podemos ter a fórmula:
`XdN + YdM`, onde `X` e `Y` também são números inteiros. Nesse caso, estamos fazendo um lançamento com `X` dados de `N` lados e `Y` dados de `M` lados. Se `N=M`, então a fórmula é equivalente a `Xd2N`.

Por fim, além de somar dados, podemos somar ou multiplicar valores inteiros.
`XdN + Y` representa fazer um lançamento de `X` dados de `N` lados e somar `Y` ao resultado final.

O programa será feito em `python` e utilizaremos os _framework_ de testes `unittest`.

## Experiência

Comecei testando apenas uma fórmula simples. Isso fez com que fossemos obrigados a criar a classe mencionada no `setUp` e também o método `get_mean_for_die_formula`, que recebe uma `string` e retorna um `float`.

Entretanto, ao testar apenas uma fórmula, resolvi isso facilmente retornando `3.5` na função criada, o que claramente não é o esperado.

Portanto, foram adicionados mais testes para verificar se o programa está calculando a média corretamente (ainda com strings do tipo `1dN`). Assim, basta retornar `(N+1)/2` e passamos esse teste também.

Para os próximos passos, queremos criar funções que recebam strings do tipo `XdN` e retornem ou `X` ou `N` (dependendo da função). Para isso, fizemos mais dois testes.

Depois, fazemos novamente testes de várias fórmulas simples, mas do tipo `XdN`. O programa não necessariamente usará as funções que o forçamos a criar nos testes anteriores, mas isso seria o ideal (de fato não há forma de assegurar que o programa as usará usando TDD).

Agora é hora de testar somas de dados. Para começar, vamos somar apenas dois dados, mas vamos testar com várias fórmulas e com uma quantidade de espaços variada entre cada um dos dados.

Em sequência, temos os testes mais complexos, que envolvem somas de vários dados.

E, por fim, vamos testar também a média somando valores que não são dados (valores inteiros normais, que são chamados no programa de escalares).

E ao final desse processo, temos um programa funcionando da forma como gostaríamos =).

## Possíveis adições futuras

- **Melhorar os testes**: existem alguns códigos repetidos entre os testes. Poderíamos melhorar essa classe para deixar os testes um pouco mais robustos. Além disso, poderíamos realizar mais testes (por exemplo, testar o comportamento de quando passamos apenas um número inteiro para o programa);
- **Subtração**: seria legal se pudéssemos também subtrair dados ou inteiros, isso seria uma boa _feature_ para o futuro;
- **Verificação de input**: atualmente não estamos tratando os possíveis erros de inputs inválidos, o `unittest` permite testar o lançamento de exceções e isso seria algo interessante de se fazer em uma versão futura.