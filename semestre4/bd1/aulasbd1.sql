--Isto é um comentário
/*
 * comentário
 * de bloco
 */

--Acessando dados de um banco de dados
--A cláusula select nos permite acessar/consultar dados armazendos em tabelas no banco de dados
--1) O resultado do select é uma tabela

INSERT INTO cliente VALUES (8, 'Jessica Gomes', 'Rua das rosas, 1206', '(21) 5555-1234', NULL, 2); --jessica tinha sido
--na aula do dia 21/11

set search_path to locadora; --define que locadora será o esquema padrão
select 8*7;
--retorna uma tabela agora renomeado a primeira coluna para conta
select 8*7 as conta;
--podemos obter tabelas de múltiplas colunas
select 6*7 as conta1, 9*8 as conta2, 'josefina';

/* 
 * Primeira forma geral:
 * select <lista de atributos> from <lista de tabelas>;
 */

select nomereal, nomeartistico from ator;

--SELECT SEMPRE RETORNA UMA TABELA COMO RESULTADO. No caso acima, retorna uma tabela com os atributos
-- nomereal e nomeartistico

--outra forma de rodar a consulta acima é especificando a origem de cada coluna
select ator.nomereal, ator.nomeartistico from ator;

--podemos rodar o comando acima definindo um ALIAS (apelido), para as tabelas
select a.nomereal, a.nomeartistico from ator a;

--podemos obter todas as colunas de uma tabela com o operador *
select a.* from ator a;

--evitar usar asterisco no "mundo real" para evitar tráfego desnecessário de dados e para se previnir
-- contra futuras alterações nas tabelas

/*
 * Segunda forma geral:
 * select <lista de atributos> from <lista de tabela> where <condição de seleção>
 */

--consultando apenas os dados do Marlon Brando
select a.* from ator a where a.nomeartistico = 'Marlon Brando';

--sempre utilizar como condição uma chave primária
select a.* from ator a where a.cod = 1;

--exibindo os atores americanos
select  a.* from ator a where a.nacionalidade = 'USA';

--exibindo os atores americanos e canadenses
select  a.* from ator a where  a.nacionalidade = 'USA' or a.nacionalidade = 'Canadá';

--reescrevendo a consulta acima usando o operador IN							
select  a.* from ator a where a.nacionalidade in ('USA', 'Canadá');

--exibindo os atores que não são nem americanos nem canadenses com o operador IN
select  a.* from ator a where not(a.nacionalidade in ('USA', 'Canadá'));

--podemos também usar o operador NOT IN
select a.* from ator a where a.nacionalidade not in ('USA', 'Canadá');

--exibindo os atores que não são nem americanos nem canadenses com o operador lógico OR
select  a.* from ator a where not (a.nacionalidade = 'USA' or a.nacionalidade = 'Canadá');

-- exibindo os atores americanos cujo nome artístico tenha mais de 10 caracteres
select a.* from ator a where a.nacionalidade = 'USA' and length(a.nomeartistico) > 10;

-- exibindo o comprimento do nomeartistico no resultado
select a.*, length(a.nomeartistico) as tamanhonome from ator a where a.nacionalidade = 'USA' and 
length(a.nomeartistico) > 10;

--a cláusula order by ordena a ordem em que as linhas vão aparecer
select a.* from ator a order by datanasc;

--para ordenar de forma crescente é só usar a cláusula ASC
select a.* from ator a order by datanasc asc ;

--para ordenar de forma decrescente é só usar a cláusula DESC
select a.* from ator a order by datanasc desc;

--a cláusula DISTINCT força a exibição apenas de resultados distintos
select a.nacionalidade from ator a;--valores repetidos
select distinct a.nacionalidade from ator a;--valores distintos

--quando duas colunas são puxadas, a cláusula distinct não funciona com o exemplo abaixo, 
--pois não tem nenhuma linha com os dois campos iguais
select distinct a.nacionalidade from ator a;

/*
 * Cláusula LIKE para casamento de padrões
 * A cláusula LIKE 	permite casar padrões em uma string utilizando dois caracteres especiais reservados
 * reservados.
 * %: casa com qualquer sequência de 0 ou mais caracteres
 * _: casa com um único caracter
 */

--obtendo atores que nasceram em países começados com 'U' e que tenham exatamente 3 caracteres
select a.* from ator a where a.nacionalidade like 'U__';

--obtendo atores que nasceram em países começados com 'U'
select a.* from ator a where a.nacionalidade like 'U%';

--obtendo os atores cujo nome tenha o caracter a (exceção de quem começa com A)
select a.* from ator a where a.nomereal like '%a%';

--obtendo os atores cujo nome tenha o caracter a
select a.* from ator a where a.nomereal like '%a%' or a.nomereal like 'A%';

--clientes que possuem o sobrenome Silva no meio
select c.* from cliente c where c.nome like '%Silva%';

--podemos converter o nome para minúsuculo para facilitar o casamento de padrões
--utilizando a função LOWER
select a.* from ator a where lower(a.nomereal) like '%a%';

--calculando a idade de cada ator
select a.nomereal, age(now(), a.datanasc) as idade from ator a;

--ordenando pela coluna idade
select a.nomereal, age(now(), a.datanasc) as idade from ator a order by idade;

--mostrando a idade apenas em anos
select a.nomereal, date_part('year', age(now(), a.datanasc)) as idade from ator a;

--atores com menos de 45 anos
select a.nomereal, date_part('year', age(now(), a.datanasc)) as idade from ator a where 
date_part('year', age(now(), a.datanasc)) < 45;

select e.*, age(e.datedev, e.dataret) as tempoEmprestimo from emprestimo e;

--podemos fazer casting (conversão de tipos) utilizando a cláusula CAST
select cast(a.datanasc as char(10)) from ator a;




--aula 9/10
select e.* from emprestimo e;
--o postgreesql tem uma forma de fazer conversão de tipos obtendo a coluna dataret como CHAR[10] em 
--vez de DATE
select e.dataret from emprestimo e;--

/*
 * Operações de conjuntos
 * Podemos fazer operações de conjuntos (UNIÃO, INTERSEÇÃO E DIFERENÇA) sobre os resultados de dois ou
 * mais selects, desde que o número de colunas e seus respectivos tipos sejam compatíveis.
 * Usamos as cláusulas:
 * UNION: operação de união
 * INTERSECT: operação de interseção
 * EXCEPT: operação de diferença
 * */
select c.nome from cliente c;
select a.nomeArtistico from ator a;

--quero uma tabela com nome de clientes e atores
select c.nome from cliente c
union
select a.nomeArtistico from ator a;--
--deu certo pois o número de colunas e o tipo das tabelas é o mesmo

--nas operações de conjunto, as linhas no resultado são todas distintas, ou seja, não aparecem duas 
--linhas iguais

--podemos ordenar o resultado
select c.nome from cliente c
union
select a.nomeArtistico from ator a 
order by nome;

--listando os atores que são americanos
select a.* from ator a where a.nacionalidade = 'USA'; 

--usando except para listar os atores que não são americanos
select a.* from ator a
except
select a.* from ator a where a.nacionalidade = 'USA';

--outro jeito
select a.* from ator a where a.nacionalidade != 'USA';
--com a cláusula in
select a.* from ator a where a.nacionalidade not in ('USA');

--atores americanos que nasceram depois de 198-01-01 (utilizando cláusula intersect)
select a.* from ator a where a.datanasc <= '1980-01-01'
intersect 
select a.* from ator a where a.nacionalidade = 'USA';

--A cláusula LIMIT nos permite limitar o número de linhas (tuplas) exibidas no resultado
select a.* from ator a limit 5;

--em geral, a cláusula LIMIT é utilizada com a cláusula ORDER BY para evitar que sgbd mostre os
--resultados em qualquer ordem
select a.* from ator a order by datanasc asc limit 5;
--
 define um ponto de partida, obtendo os 5 atores mais velhos a partir da posição 10
select a.* from ator a order by datanasc asc limit 5 offset 10;

--podemos gerar gerar uma tabela física no banco de dados com o resultado de um select
--usamos para isso INTO 
--exemplo: gerando uma tabela só com atores americanos
select a.* into AtorAmericano from ator a where a.nacionalidade = 'USA';

--a consulta acima gera uma nova tabela chamada AtorAmericano
select aa.* from atoramericano aa;

/*
 * Funções de agregação
 * 
 * Resumir informação de várias linhas em uma única linha
 * As funções mais comuns são:
 * COUNT: contagem de linhas (NOT NULL)
 * SUM: soma de valores númericos em uma coluna
 * MIN: valor mínimo em uma coluna
 * MAX: valor máximo em uma coluna
 * AVG: média dos valores de uma coluna
 */

--obtendo o número de linhas da tabela cliente
select count(c.*) from cliente c;

--contando quantos valores preenchidos na coluna fonecel da tabela cliente
select count(c.fonecel) from cliente c;

--contanto os tipos e emprestimos
select count(e.tipo) from emprestimo e;

--contando os tipos distintos de emprestimo
select count(distinct e.tipo) from emprestimo e;

--soma dos valores pagos nos emprestimos
select sum(e.valor_pg) from emprestimo e;

--média dos valores pagos nos emprestimos
select sum(e.valor_pg)/count(e.valor_pg)  from emprestimo e;
select avg(e.valor_pg) from emprestimo e;

--podemos usar várias funções de agregação na mesma consulta
select min(e.valor_pg), max(e.valor_pg), avg(e.valor_pg) from emprestimo e;

--contando o número de empréstimos de VHS
select count(e.tipo) from emprestimo e where e.tipo = 'VHS';

--contando quantos empréstimos de VHS e de DVD
select count(e.tipo) from emprestimo e where e.tipo in ('VHS', 'DVD');

--fazendo a contagem separada (DVD e VHS) com o que aprendemos hoje
select 'DVD', count(e.tipo) from emprestimo e where e.tipo = 'DVD'
union
select 'VHS', count(e.tipo) from emprestimo e where e.tipo = 'VHS';

--aula 17/10

--numeros de celular terminam em 1
select c.fonecel from cliente c where c.fonecel like '%1';

--numeros de celular tem 1
select c.fonecel from cliente c where c.fonecel like '%1%';

--contando quantos numeros de celular terminam em 1
select count(c.fonecel) from cliente c where c.fonecel like '%1';

--contando celulares que contenham o dígito 4 de clientes cujo nome comece com A
select count(c.fonecel) from cliente c where c.fonecel like '%4%' and c.nome like 'A%';

--o select é um operador de tabela e além disso pode-se dar um select sobre o resultado de outro select

/*
 * Agregação com agrupamento
 * A agregação com agrupamento consiste em aplicar as funções de agregação a subgrupos de tuplas, 
 * onde os subgrupos são baseados em valores de atributos.
 * Especificamos esses subgrupos (agrupamentos) com as cláusulas especiais GROUP BY e HAVING. 
 */

--contando os empréstimos de cada tipo
select e.tipo, count(*) from emprestimo e group by e.tipo; --GROUP BY separa os grupos

--contanto os emprestimos de cada tipo feitos pelo cliente 1
select e.tipo, count(*) from emprestimo e where e.cliente = 1 group by e.tipo;

--podemos criar os agrupamentos baseados em mais de uma coluna
select e.tipo, e.cliente, count(e.*) from emprestimo e group by e.tipo, e.cliente order by e.tipo;

/* sempre que listamos um ou mais atributos na cláusula GROUP BY, TODOS esses atributos têm que aparecer
 * junto com o resultado da função de agregação (após a cláusula SELECT e antes da cláusula WHERE)
 * EM OUTRAS PALAVRAS
 * sempre que listarmos um ou mais atributos junto com a função de agregação, TODOS esses atributos 
 * devem ser listados após a cláusula GROUP BY*/

/*
 * A cláusula HAVING permite especificar condições que cada agrupamento deve satisfazer para aparecer
 * no resultado. Essas condições devem ser construídas sobre alguma das funções de agregação 
 * utilizadas.
 */

--exibindo a contagem de emprestimos por tipo
select e.tipo, count(*) from emprestimo e group by e.tipo;

--exibindo apenas os tipos de emprestimo onde a contagem é maior que 6
select e.tipo, count(*) from emprestimo e where count(e.*) > 6 group by e.tipo; --NÃO FUNCIONA
select e.tipo, count(*) from emprestimo e group by e.tipo having count(e.*) > 6;

--a função count não pode ser usada na cláusula WHERE, pois a mesma é aplicada antes da contagem 
-- ser realizada; para isso, utilizamos a cláusula HAVING

--a cláusula HAVING se destina a especificar condições para filtrar grupos inteiros

select t.* from (select c.* from cliente c) t;

--podemos então obter os tipos de emprestimos com contagem maior que 6 sem usar o HAVING com SELECT's
-- aninhados
select t.* from (select e.tipo, count(e.*) from emprestimo e group by e.tipo) t where t.count > 6;

--obtendo emprestimo com o maior valor pago
select max(e.valor_pg) from emprestimo e; --obtem o maior valor_pg de emprestimo

--podemos saber que emprestimo foi esse fazendo:
select e.* from emprestimo e where e.valor_pg = 63675; --JEITO ERRADO

select e.* from emprestimo e where e.valor_pg = (select max(e.valor_pg) from emprestimo e); --JEITO CERTO

--no caso acima, o subselect foi usado na cláusula WHERE para fazer uma comparação e só deu certo pq 
--esse subselect retorna apenas uma linha e uma coluna, portanto pode ser encarado como um valor escalar

--outro jeito sem subselect
select e.* from emprestimo e order by e.valor_pg desc limit 1;
--só mostra uma linha no resultado, diferente da forma anterior, que mostraria duas linhas caso elas
--tivessem empatado


--aula 23/10
select c.* from cliente c;

--listando clientes que foram indicados por outros clientes (ou seja, que tem a coluna numclienteindicador preenchida)
select c.* from cliente c where c.numclienteindicador is not null;
--ou
select c.* from cliente c where not(c.numclienteindicador is null);

--Consultas sobre duas relações
 select c.* from cliente c; --lista o conteúdo da tabela cliente

select e.* from emprestimo e; --lista o conteúdo da tabela emprestimo

--como listar cada emprestimo junto com os dados do respectivo cliente que fez o emprestimo?
--podemos especificar mais de uma tabela na cláusula FROM
select e.*, c.* from emprestimo e, cliente c; --forma errada
/*
 * gerou tuplas falsas por que combinou cada empreśtimo com todos os clientes ao invés de ter combinado cada empréstimo com seu
 * respectivo cliente;
 * cada linha da tabela cliente foi combinada com cada linha com a tabela emprestimo (foi feito o produto cartesiano das linhas
 * das duas tabelas), por isso que foram geradas 160 linhas. 
 */

--para eliminar as tuplas falsas do resultado, é preciso impor o relacionamento entre as tabelas que estão sendo listadas na 
--cláusula from
select e.*, c.* from emprestimo e, cliente c where e.cliente = c.numcliente;

--listando os emprestimos com suas respectivas mídias
select e.* from emprestimo e;
select m.* from midia m; --na tabela midia, temos 3 campos atuando simultaneamente com chave primária

--o mesmo acontece com chave primária composta
select e.*, m.* from emprestimo e, midia m where e.numfilme = m.numfilme and e.tipo = m.tipo and e.numero = m.numero;

--listar cada ator com o filmes que ele trabalhou
select a.* from ator a;
select f.* from filme f;

--listando os atores com cada filme que eles trabalharam
select a.nomeartistico, f.titulo_pt from ator a, filme f, estrela e where a.cod = e.codator and f.numfilme = e.numfilme;

--incluindo a tabela classificação no relatório anterior
select a.nomeartistico, f.titulo_pt, c.nome from ator a, filme f, estrela e, classificacao c where a.cod = e.codator and 
f.numfilme = e.numfilme and f.classificacao = c.cod;

--contar quantos filmes cada ator fez
select a.nomeartistico, count(*) from ator a, estrela e where a.cod = e.codator group by a.nomeartistico;

--listando emprestimo e clientes
select e.*, c.* from emprestimo e, cliente c where e.cliente = c.numcliente;

--podemos realizar a consulta acima utilizando o conceito de junção interna (utilizando a cláusula JOIN)
select e.*, c.* from emprestimo e join cliente c on e.cliente = c.numcliente;
--a cláusula JOIN tem sintaxe própria, nela é utilizado a cláusula ON (ao invés de WHERE) para impor o relacionamento/especificar
--o relacionamento (ELE TEM QUE SER ESPECIFICADO)

--o uso das cláusulas JOIN/ON não anula o uso da cláusula WHERE
select e.*, c.* from emprestimo e join cliente c on e.cliente = c.numcliente where e.valor_pg < 10;

--podemos fazer a junção de várias tabelas
select a.nomeartistico, f.titulo_pt from ator a join estrela e on a.cod = e.codator join filme f on f.numfilme = e.numfilme;

--para especificar a junção interna, pode-se usar JOIN ou INNER JOIN
select e.*, c.* from emprestimo e inner join cliente c on e.cliente = c.numcliente;

--existe ainda a junção natural, que não é muito recomendada; é uma junção interna onde o próprio sistema impõe o relacionamento
--automaticamente a partir do nome das colunas.
--todas as colunas com nome em comum entre as duas tabelas serão usadas automaticamente
--NÃO USAR 
select f.*, e.* from filme f natural join estrela e; --NÃO USAR


--aula 24/10

--mostrando os clientes que fizeram empréstimos
select distinct c.nome from emprestimo e join cliente c on e.cliente = c.numcliente;
--analisando o resultado acima, percebemos que há um cliente sem nenhum emprestimo, pois a junção interna faz com que só linhas de 
--uma tabela que estejam relacionadas com alguma linha da outra apareçam no resultado

/*
 * Como listar os clientes que não tem emprestimo na junção entre as tabelas emprestimo e cliente?
 * Resolvemos esse problema com o conceito da junção externa.
 * O conceito de junção interna combina apenas as linhas das tabelas envolvidas onde o relacionamento é atendido, mas pode acontecer 
 * de uma linha em uma das tabelas não se combinar com nenhuma das linhas da outra tabela e mesmo assim precisar ser listada.
 * Exemplo: clientes que não fizeram empréstimo ou empréstimos sem cliente (caso fizesse sentido); para essas situações, existe a 
 * junção externa.
 */

--aqui faremos a junção externa à direita, ou seja, queremos que as linhas da tabela à direita (cliente c) que não têm 
--correspondência com emprestimo
select e.*, c.* from emprestimo e right outer join cliente c on e.cliente = c.numcliente;

--usamos a junção externa à direita porque queríamos que as linhas da tabela à direita que não tem relação com a outra tabela
--também aparecessem no resultado
--caso quiséssemos listar os empréstimos sem cliente, usaríamos a junção externa à esquerda
select e.*, c.* from emprestimo e left outer join cliente c on e.cliente = c.numcliente;
--nesse caso em específico, como não há empréstimo sem cliente, o resultado é o mesmo da junção interna

select e.*, c.* from cliente c left outer join emprestimo e on e.cliente = c.numcliente;
--se trocarmos as tabelas de lugar, aí sim podemos usar a junção externa à esquerda

--e se quisermos listar tanto clientes sem empréstimo quanto empréstimos sem clientes? em outras palavras, queremos a junção 
--externa à direita e ao mesmo tempo a junção externa à esquerda
select e.*, c.* from emprestimo e full outer join cliente c on e.cliente = c.numcliente;

--vamos criar uma cópia da tabela emprestimo para colocar um empréstimo sem cliente
select e.* into emprestimo2 from emprestimo e;
--inserindo um emprestimo sem cliente
insert into emprestimo2 values (5, 1, 'Blue-ray', null, null, null, 7);
select e2.* from emprestimo2 e2;

--agora podemos visualizar o resultado da nossa junção externa completa
select e2.*, c.nome from cliente c full outer join emprestimo2 e2 on e2.cliente = c.numcliente;

--contando o número de empréstimos de cada cliente
select c.nome, count(e.*) from cliente c join emprestimo e on c.numcliente = e.cliente group by c.nome;
--note que os clientes sem emprestimos não aparecem na contagem

--usando a junção externa para mostrar a contagem com os clientes sem emprestimos
select c.nome, count(e.*) from cliente c left outer join emprestimo e on c.numcliente = e.cliente group 
by c.nome order by 2 desc;-- ORDEM by 2 significa ordenar pela segunda coluna do resultado
select e.* from emprestimo e;
--agora sim a jessica aparece com a quantidade de empréstimos ela tem (0)

--contando só os empréstimos feitos no mês de março
--vamos usar o operador BETWEEN que serve para testar se um valor pertence a um intervalo
select c.nome, count(e.*) from cliente c left outer join emprestimo e on c.numcliente = e.cliente where 
e.dataret between '2013-03-01' and '2013-03-31' group by c.nome order by 2 desc;

/*
 * Funções LEAST e GREATEST
 * 
 * A função LEAST retorna o menor entre uma lista de elementos
 * A função GREATEST retorna o maior entre uma lista de elementos
 */

select least(7, -6, 2, 100, -30);
select greatest (7, -6, 2, 100, -30);

select greatest ('Andressa', 'lucas', 'wendel', 'guilherme');

--mostrando os filmes pelo título original ou título em português de acordo com o que vier primeiro na ordem alfabética
select least (f.titulo_original, f.titulo_pt) from filme f;
--comparando as colunas

/*
 * Consultas aninhadas
 * 
 * O resultado de um SELECT também é uma tabela. Podemos então dar um select sobre o resultado de outro.
 */

select t.* from (select f.* from filme f) t;

--exemplo: descobrindo o maior valor de emprestimo pago por cada cliente
select e.cliente, max(e.valor_pg) from emprestimo e group by e.cliente;

select c.nome, vc.max from cliente c join (select e.cliente, max(e.valor_pg) from emprestimo e group by
e.cliente) vc on c.numcliente = vc.cliente;

--outro jeito
select c.nome, max(e.valor_pg) from cliente c left outer join emprestimo e on c.numcliente = e.cliente  group by c.nome;



--aula 30/10
--Exemplo: obtendo os emprestimos maiores do que a média
select e.* from emprestimo e;
--Passo 1: obtendo a média dos valores pagos nos emprestimos
select avg(e.valor_pg) from emprestimo e; --3197.25
--set search_path to locadora;
--Passo 2 : os emprestimos cujo valor pago ficou acima da média
select e.* from emprestimo e where e.valor_pg >= 3197.25; --dá o resultado certo, mas está LOGICAMENTE ERRADO, pois se 
--alguém acrescentar um novo valor a média será alterada

--podemos resolver isso substituindo a constante 3197.25 pela expressão que resulta nela

select e.* from emprestimo e where e.valor_pg >= (select avg(e.valor_pg) from emprestimo e); --LOGICAMENTE CORRETO, pois
--como o select de dentro retorna apenas um valor (uma célula) podemos interpretar ele como um valor escalar

/* No exemplo acima, nós temos um SELECT aninhado. O SELECT dentro dos parênteses é executado primeiro para então compor
 * a condição de seleção do segundo.*/

--Exemplo: listar emprestimos de filmes estrelados por britânicos
--Podemos usar o operador IN

--Passo 1: obtendo os atores britânicos
select a.* from ator a where a.nacionalidade = 'UK';

--Passo 2: códigos de filmes estrelados por atores britânicos
--código dos atores britânicos: 12, 22, 25, 32 e 33
select e.numfilme from estrela e where e.codator in (10, 11, 12, 22, 25, 32, 33); --LOGICAMENTE ERRADO

--para tornar a consulta logicamente certa, substituimos as constantes usadas no operador IN pela expressão que as
--originou

select e.numfilme from estrela e where e.codator in (select a.cod from ator a where a.nacionalidade = 'UK'); --LOGICAMENTE
--CORRETO
--podemos usar o SELECT interno no contexto do operador IN porque ele retorna apenas uma coluna

--outra forma: fazendo junção interna
select e.numfilme from estrela e join ator a on a.cod = e.codator where a.nacionalidade = 'UK';

--as consultas acima nos retornam os números 4, 8, 9 e 11 como sendo estrelados por britânicos
--precisamos obter os emprestimos desses filmes
select e.* from emprestimo e where e.numfilme in (4, 8, 9, 11); --LOGIMENTE ERRADO

--para a consulta ficar logicamente correta, substituímos as constantes usadas no operador IN por uma das consultas que 
--as originam

select e.* from emprestimo e where e.numfilme in (select e.numfilme from estrela e where e.codator in (select a.cod from 
ator a where a.nacionalidade = 'UK')); --LOGICAMENTE CORRETO

--OU

select e.* from emprestimo e where e.numfilme in (select e.numfilme from estrela e join ator a on a.cod = 
e.codator where a.nacionalidade = 'UK'); --TAMBÉM LOGICAMENTE CORRETO

/*Além de IN e NOT, existem outros operadores que trabalham com uma lista de valores, como ANY ou SOME e ALL. Estes últimos
 * operadores devem ser utilizados em conjunto com os operadores de comparação: >, <, >=, <=, =, !=
 */

--exemplo: lista de atores que nasceram antes de todos os filmes serem lançados
--Passo 1: obter as datas de lançamento dos filmes
select f.data_lancamento from filme f;
select a.datanasc from ator a; 

--Passo 2: obtendo os atores que nasceram antes das datas retornadas pelo SELECT acima
select a.* from ator a where a.datanasc <= all(select f.data_lancamento from filme f);

--Exemplo: obtendo a lista de emprestimos dos clientes que tem o atributo numcliente indicador preenchido
select c.* from cliente c;

--Passo 1: obtendo os numeros de clientes com numclienteindicador preenchido
select c.numcliente from cliente c where c.numclienteindicador is not null;

--Passo 2: obtendo os emprestimos desses clientes
select e.* from emprestimo e where e.cliente in (select c.numcliente from cliente c where c.numclienteindicador is 
not null);

--outra forma é usando o ANY ao invés de IN. Dizemos que e.cliente deve ser igual a algum valor da lista. Poderíamos 
--usar SOME ao invés de ANY também (são sinônimos)
select e.* from emprestimo e where e.cliente = any (select c.numcliente from cliente c where c.numclienteindicador is 
not null);

--outra forma é usando junção
select e.* from emprestimo e join cliente c on e.cliente = c.numcliente where c.numclienteindicador is not null;


--aula 31/10
/*
 * Consultas Aninhadas Correlacionadas
 * 
 * Uma consulta (SELECT) interna é dita correlacionada à externa se, para cada linha computada na consulta externa, é 
 * necessário executar a consulta interna. Em geral isso ocorre se, na cláusula WHERE da consulta interna é usado
 * algum atributo declarado na consulta externa.
 */

insert into ator values (44, '1981-04-26', 'Brasil', 'Mariana Ximenes de Prado Nuzzi', 'Mariana Ximenes');

--Exemplo: listar os atores com a quantidade de filmes que cada um estrelou
select a.* from ator a;

--Passo 1: saber quantos filmes determinado ator estrelou, ex.: Marlon Brando (cod = 1)
select count(e.numfilme) from estrela e where e.codator = 1;

--Passo 2: rodar essa mesma consulta para todos os atores (utilizamos a mesma lógica do select acima)
select a.nomeartistico, (select count(e.numfilme) from estrela e where e.codator = a.cod) from ator a;
--nesse caso, se o ator não fez nenhum filme, ele vai aparecer no resulta com um 0

/*
 * No exemplo acima temos SELECTs correlacionados. Note que o SELECT de dentro dos parênteses usa o valor a.cod, que vem
 * do escopo do SELECT de fora. Ou seja, o SELECT interno tem correlação com o SELECT externo. Nesse caso, é necessário
 * rodar o SELECT externo para cada linha do resultado do SELECT interno
 */

--Outro jeito
select a.nomeartistico, count(e.numfilme) from ator a join estrela e on a.cod = e.codator group by a.nomeartistico;
--nesse caso, se o ator não fez nenhum filme ele não aparecerá no resultado

--Usando a junção externa, consertamos esse problema (a junção externa faz o papel da junção interna e também pega as 
--linhas de uma tabela que não tem relação com a outra)
select a.nomeartistico, count(e.numfilme) from ator a left outer join estrela e on a.cod = e.codator group by a.nomeartistico;
--Agora a Mariana Ximenes aparece no resultado com 0 filmes estrelados

--Exemplo: vamos listar cada emprestimo com o nome do cliente que o fez:

--usando junção
select e.*, c.nome from emprestimo e join cliente c on e.cliente = c.numcliente;

--usando SELECTs aninhados
select e.*, (select c.nome from cliente c where c.numcliente = e.cliente) from emprestimo e;

--outro exemplo: listar os clientes onde a média do valor pago nos emprestimos ficou abaixo da média geral dos valores 
--pagos nos emprestimos

--Passo 1: obter a média geral dos valores pagos nos emprestimos
select avg(e.valor_pg) from emprestimo e;

--Passo 2: obter a média dos valores pagos nos emprestimos de um determinado cliente, ex.: cliente 1
select avg(e.valor_pg) from emprestimo e where e.cliente = 1;

--Passo 3: listar os clientes e usar os passos 1 e 2 para fazer a filtragem 
select c.* from cliente c where (select avg(e.valor_pg) from emprestimo e where e.cliente = c.numcliente) <
(select avg(e.valor_pg) from emprestimo e);
--fazer essa mesma consulta sem usar select aninhado:


--Outro exemplo: obtendo o nome de cada cliente e, se for o caso, o nome do cliente que o indicou (observando o atributo
--numclienteindicador)
select c1.nome, (select c2.nome from cliente c2 where c2.numcliente = c1.numclienteindicador) from cliente c1;
--fazer de outro jeito:


--aula 07/11
/*
 * Visões (VIEWS)
 * 
 * No contexto de SQL, uma visão (view) é uma tabela derivada de outras tabelas.
 * Essas outras tabelas podem ser tabelas da base, ou mesmo outras visões.
 * 
 * Views também são denominadas tabelas virtuais, pois não necessariamente são armazenadas de forma física no banco de
 * dados, ao contrário das tabelas da base.
 * 
 * O SGBD se compromete a manter as visões sempre atualizadas, isto é, se as tabelas que deram origem a uma view sofrerem
 * alteração em seus dados, a View deve refletir essa atualização automaticamente.
 * 
 * Em geral, pode-se fazer qualquer consulta SELECT sobre uma view como com qualquer outra tabela. No entanto, as operações
 * que envolvem atualizações dos dados ficam mais restritas.
 * 
 * Views costumam ser utilizadas quando é preciso referenciar, com certa frequência, tabelas construídas com consultas que
 * exigem algum nível de complexidade.
 */

--ex.: consulta para listar emprestimos e clientes
select e.*, c.* from emprestimo e join cliente c on e.cliente = c.numcliente;

--podemos criar uma visão sobre o resultado de qualquer SELECT:
create or replace view VisaoEmprCliente as select e.*, c.* from emprestimo e full outer join cliente c on 
e.cliente = c.numcliente;

/*o código acima cria uma visão que foi chamada de VisaoEmprCliente com o resultado do SELECT anterior. Podemos dar um 
 * SELECT na nossa visão normalmente.*/
select v.* from visaoemprcliente v;

/*O SGBD se responsabiliza por manter as visões sempre com dados atualizados em relação às tabelas originais. Por exemplo,
 * se algum novo cliente for inserido na tabela cliente, automaticamente a nossa visão visaoemprcliente refletirá a 
 * alteração.*/

-- inserindo um novo cliente
INSERT INTO Cliente 
	VALUES (19, 'Carol', 'XXX', '(21) 555-3333', NULL, NULL);

-- agora a nova cliente inserida na tabela Cliente automaticamente
-- aparece na minha visão.
SELECT v.* FROM visaoemprcliente v;

/* não consundir VIEW com SELECT INTO, que armazena um backup dos dados gerados (naquele instante) em um nova tabela 
 * física no disco */

/* SELECT CASE: podemos usar a cláusula SELECT CASE para impor uma espécie de condicional no resultado de uma coluna 
 * de um SELECT.
 * 
 * sintaxe:
 * 
 * SELECT <colunas>
 * 
 *   CASE
 * 		WHEN <condição 1> THEN <resultado 1>
 * 		WHEN <condição 2> THEN <resultado 2>
 * 		...
 * 		WHEN <condição n> THEN <resultado n>
 * 		ELSE <resultado n+1>
 * END
 * ...
 */

/*O SELECT CASE tem um funcionamento semelhante à cláusula SWITCH na linguagem C. Aqui, podemos especificar uma série de 
 * condições (com a cláusula WHEN) e resultados associados.
 * A primeira condição que resultar em verdadeiro, terá o respectivo resultado calculado. Temos ainda a cláusula ELSE que
 * tem a função similar ao DEFAULT no SWITCH em C.*/

INSERT INTO Cliente VALUES (21, 'Lucas', 'Av Ayrton Sena, Barra', NULL, NULL, NULL);

/*exemplo: listar o nome e o contato de cada cliente.
 * Se o cliente possuir telefone celular, listamos o celular.
 * Se o cliente não possuir celular, mostramos o telefone residencial.
 * Se o cliente não possuir nenhum dos dois, mostramos o endereço.*/

select c.nome, 
	case
		when (c.fonecel is not null) then c.fonecel
		when (c.foneres is not null) then c.foneres
		else c.endereco 
	end as Contato
	from cliente c;

--exemplo: vamos colocar uma multa de 20% para os emprestimos atrasados em mais de 2 dias
select e.*, 
	case
		when e.datedev - e.dataret >= 2 then e.valor_pg * 1.2
		else 0
	end as multa
from emprestimo e;

/*ROW_NUMBER
 * 
 * No postgreesql, podemos usar a função ROW_NUMBER para gerar uma coluna que atribuirá um número inteiro sequencial para
 * cada linha do resultado de um SELECT.
 * Para usar ROW_NUMBER, podemos especificar uma ordem para numeração, que pode ser a do próprio resultado da consulta, 
 * ou uma ordenação específica.
 */

--numerando as linhas seguindo a ordem padrão
select c.nome, c.endereco, row_number() over() from cliente c;

--observe que o número de linha não muda se usarmos a cláusula ORDER BY
select c.nome, c.endereco, row_number() over() from cliente c order by c.nome;

/* Como uma função aplicada na "janela de resultados" (window function), ROW_NUMBER() é calculado após a aplicação das 
 * cláusulas JOIN, WHERE, GROUP BY e HAVING, e antes da aplicação de ORDER BY.
 */

--podemos especificar uam ordem para atribuir o número de linhas
select c.nome, c.endereco, row_number() over(order by c.nome) from cliente c;

--listando o ranking de clientes que mais gastaram na locadora
select c.nome, sum(e.valor_pg) from cliente c left outer join emprestimo e on c.numcliente = e.cliente group by 
c.numcliente, c.nome;

/* Note que clientes sem emprestimo acabam aparecendo com soma NULL em vez de 0. Para corrigir isso, podemos usar o SELECT
 * CASE , ou usar uma gambiarra, com a função COALESCE, que retorna o primeiro valo não NULL em sua lista de 
 * argumentos.
 */
select coalesce(null, null, 7, 8);

--usando a função COALESCE para zerar a soma dos clientes sem emprestimo
select c.numcliente, c.nome, coalesce(sum(e.valor_pg), 0) as soma from cliente c left outer join emprestimo e on
c.numcliente = e.cliente  group by c.numcliente, c.nome;

--usando a função ROW_NUMBER para gerar o ranking
select c.numcliente, c.nome, coalesce(sum(e.valor_pg), 0) from cliente c as soma, from cliente c left outer join emprestimo e on 
c.numcliente = e.cliente group by c.numcliente, c.nome;


--aula 14/11
begin;--inicia uma transação

select * from cliente c;

insert into cliente values (30, 'Isabela', null, '(21) 555 3333');

insert into cliente values (31, 'Natalie', null, '(62) 555 3333');

insert into cliente values (32, 'Matheus', null, '(32) 555 3333');

select * from cliente c; --os novovs clientes aparecem na tabela
/*Porém se abrirmos outra conexão com o banco em outra aba, e dermos SELECT na tabela Cliente, os novos clientes não aparecerão lá.*/

rollback; --desfaz tudo que a transação fez
/*Após o ROLLBACK ou COMMIT a transação acaba*/

end; --erro, pois a transação já foio encerrada pelo ROLLBACK


begin;

insert into filme values (16, 'The Terminator', 'O Exterminador do Futuro', 107);

insert into filme values (17, 'Die Hard', 'Duro de Matar', 132);

--os filmes inseridos só aparecem no escopo local dessa transação, pois ainda não demos o COMMIT (se abrir outra conexão com o SGBD e rodar 
--o mesmo SELECT abaixo, os novos filmes não serão listados)
select * from filme f;

commit; --commita a transação, e as alterações passam a valer fora do escopo da transação
--a execução do commit encerra a transação por si só. Se rodar o END abaixo, ele dará erro, pois não há mais transação em aberto
end;


/*A cláusula SAVEPOINT permit definir um ponto de salvamento (ponto de recuperação) para desfazer as operações feitas após esse ponto*/
begin;

delete from filme f where f.numfilme = 16;

select * from filme f;

savepoint pontoRecuperacao1;

delete from filme f where f.numfilme = 17;

select * from filme f;

rollback to pontoRecuperacao1; --volta para o estado em que estávamos quando o pontoRecuperacao1 foi criado

end; --encerra a transação. Nesse caso, a remoção do filme 16 será efetivada fora do escopo da transação


begin;

/*bloqueia a tabela Filme para uso fora do escopo dessa transação*/
lock table filme in access exclusive mode nowait;
--operações aqui envolvendo a tabela Filme

end;


--aula 21/11
--vamos criar um gatilho para, quando alguém remover um cliente da tabela Cliente, o mesmo ser inserido em uma tabela chamada
--ClienteInativo

create table ClienteInativo(
	numcliente serial4 not null,
	nome varchar(50) not null,
	endereco varchar(50) null,
	foneres varchar(50) null,
	fonecel varchar(50) null,
	numClienteIndicador int4 null,
	dataInativacao date,
	constraint pk_cliente2 primary key (numCLiente)
	);

select c.* from cliente c;

select ci.* from clienteInativo ci;

--criando uma função para, quando o cliente for removido, inserir seus dados na tabela ClienteInativo
create or replace function bef_removeCliente()
	returns trigger as --dizendo o que a função retorna
$$ --início do corpo da função
begin
	insert into ClienteInativo values(
		old.numcliente,
		old.nome, 
		old.endereco,
		old.foneres,
		old.fonecel,
		old.numclienteindicador,
		now() );
return old; --o que realmente a funçãp retorna	
end
$$ --final do corpo da função
language 'plpgsql';

/*agora criamos o gatilho a ser executado quando se apaga um cliente. Vamos chamar a função bef_removeCliente*/

create trigger gatilhoRemoveCliente before delete on Cliente for each row execute procedure bef_removeCliente();

select * from clienteinativo c;

select * from cliente;

--agora magicamente o cliente cujo numcliente é 8 aparece na tabela ClienteInativo
delete from cliente where numcliente = 8;

--para remover o gatilho, usamo DROP
drop trigger gatilhoRemoveCliente on Cliente;

/*	Consultas Recursivas
 * 
 * Podemos gerar consultas recursivas, que são úteis em situações, onde, por exemplo, temos uma tabela referenciando a si 
 * própria (a tabela tem uma chave estrangeira para ela mesma).
 * 
 * FORMA GERAL
 * 
 * WITH RECURSIVE <Resultado Recursivo> AS ( <Consulta Base da Recursão> UNION | UNION ALL <Consulta Recursiva Envolvendo
 * <Resultado Recursivo>> ) <Consulta Envolvendo <Reusultado Recursivo>>
 * 
 * A recursão termina quando a consulta recursiva retorna uma tabela vazia (ou o máximo de chamadas recursivas do SGBD é 
 * alcançado)
 */

--exemplo: contando até 10

with recursive Contagem as (select 1 as "k"
	union
	select c.k+1 from Contagem c where c.k < 10)
select * from Contagem;





