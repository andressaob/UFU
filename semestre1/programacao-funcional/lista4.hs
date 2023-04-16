--Nome: Andressa Oliveira Bernardes
--Matrícula: 12121BSI201

import Data.Char

--exercicio 1
somaTuplas :: [(Int,Int)] -> [Int]
somaTuplas lista = [a+b | (a,b) <- lista]

--exercicio 2a
maiusculas :: [Char] -> [Char]
maiusculas [] = []
maiusculas (a:b) = toUpper a : (maiusculas b)

--OU

maiusculas2 :: [Char] -> [Char]
maiusculas2 (a:b)
    | b == [] = maiusculas2 []
    | otherwise = toUpper a : (maiusculas b)

--exercicio 2b
correspondente :: [Char] -> ([Char], [Char])
correspondente (a:b) = ((a:b), (maiusculas (a:b)))

--exercicio 3

indice :: [Int] -> Int -> Int -> Int
indice lista pos  elemento
    | pos == length lista = error "Erro"
    | (lista !! pos) == elemento = (pos+1)
    | otherwise = indice lista (pos+1) elemento 

maior :: [Int] -> (Int, Int)
maior lista = ((maximum lista), (indice lista 0 (maximum lista)))

--exercicio 4
iteraLista [] _ _ = []
iteraLista (x:xs) inicio indice
  | inicio == (indice-1) = iteraLista xs (inicio+1) indice
  | otherwise = x:iteraLista xs (inicio+1) indice

removeElemento [] _ = []
removeElemento lista indice = iteraLista lista 0 indice
    


--exercicio 5
type NomeAluno  = String
type MediaNota = Int
type Aluno = (NomeAluno, MediaNota)
type Turma = [Aluno]

aprovados :: Turma -> Int ->[NomeAluno]
aprovados turma nota = [a | (a,b) <- turma, b>=nota]