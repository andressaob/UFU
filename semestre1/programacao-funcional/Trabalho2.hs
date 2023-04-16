--Nome: Andressa Oliveira Bernardes
--Matrícula: 12121BSI201

type Codigo = Int
type Nome = String
type Preco = Float

type Produto = (Codigo, Nome, Preco)

tabelaProdutos :: [Produto]
tabelaProdutos = [(001, "Chocolate", 5.25), (002, "Biscoito", 10.10), (003, "Laranja", 4.60)
                 , (004, "Sabao", 2.10), (005, "Batata Chips", 6.90), (006, "Doritos", 8.90)]

isCodigo :: Codigo -> Produto -> Bool
isCodigo codigo (c, i, p)
    | codigo == c = True
    | otherwise = False

getPreco :: Produto -> Preco
getPreco (c, i, p) = p

getNome :: Produto -> Nome
getNome (c, i, p) = i

buscaPrecoPorCodigo :: Codigo -> Preco
buscaPrecoPorCodigo codigo = getPreco (head (filter (isCodigo codigo) tabelaProdutos))

buscaNomePorCodigo :: Codigo -> Nome
buscaNomePorCodigo codigo = getNome (head (filter (isCodigo codigo) tabelaProdutos))

calculaPrecos :: [Codigo] -> Float
calculaPrecos lstCodigo = foldr (+) 0 (map buscaPrecoPorCodigo lstCodigo)

formataStrProduto :: Codigo -> String
formataStrProduto codigo = buscaNomePorCodigo codigo ++ replicate (30 - length (buscaNomePorCodigo 
    codigo ++ (show (buscaPrecoPorCodigo codigo)))) '.' ++ (show (buscaPrecoPorCodigo codigo)) ++ "\n"

geraNotaFiscal :: [Codigo] -> IO()
geraNotaFiscal lsCodigo = writeFile "notaFiscal.txt" ((foldr (++) [] (map formataStrProduto lsCodigo)) 
    ++ "Total" ++ replicate (30 - length ("Total" ++ (show (calculaPrecos lsCodigo)))) '.' ++ 
    (show (calculaPrecos lsCodigo)))