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

/*Mostrar os nomes e os salários de 2 funcionários, entrando com os seus
respectivos códigos:
funcionarios(CODIGO, Nome, Salario).

Mostrar uma lista com o nome de um determinado funcionário e os nomes de
todos os seus dependentes:

Mostrar o nome do funcionário e o seu respectivo salário quando este estiver
dentro de uma faixa salarial:
funcionarios(_, Nome, Salario), Salario =< 6500, Salario >= 4000.

Mostrar somente o nome do funcionário de quem uma determinada pessoa é
dependente.
funcionarios(4879, Nome, _), dependentes(4879, patricia).
*/