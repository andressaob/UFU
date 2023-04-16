/* Dupla:
Andressa Oliveira Bernardes, 12121BSI201
Rebeca Borges Pereira Reis, 12121BSI239*/

funcionarios(1598, angela, 7800).
funcionarios(2654, bruno, 4200).
funcionarios(3654, carlos, 8500).
funcionarios(4879, daniel, 6500).
funcionarios(5987, eduarda, 5600).

dependentes(2654, laura).
dependentes(2654, gabriel).
dependentes(3654, matheus).
dependentes(4879, patricia).
dependentes(4879, miguel).
dependentes(4879, helena).
dependentes(5987, valentina).

/* Consultas:

4. Mostrar os nomes e os salários de 2 funcionários, entrando com os seus
respectivos códigos.
funcionarios(3654, N, S).
forall((funcionarios(C, N, S), C >= 1598, C=<2654), writeln([N,S])).

5. Mostrar uma lista com o nome de um determinado funcionário e os nomes de
todos os seus dependentes.
forall((funcionarios(C, daniel, _), dependentes(C,N)), writeln([N])).
forall((funcionarios(C, daniel, _), dependentes(C,N)), writeln([daniel,N])).

6. Mostrar o nome do funcionário e o seu respectivo salário quando este estiver
dentro de uma faixa salarial.
funcionarios(_, N, S), S >= 4000, S=<5000.
forall((funcionarios(_, N, S), S >= 6000, S=<9000), writeln([N,S])).

7. Mostrar somente o nome do funcionário de quem uma determinada pessoa é
dependente.
funcionarios(4879, N, _), dependentes(4879, patricia).

*/