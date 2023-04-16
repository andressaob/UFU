#include <stdio.h>
#include <stdlib.h>

int main()
{
    int quantidadeNum, num, i, maior, quantidadeMaior, contador;
    contador = 0;
    //o contador irá contar quantas vezes o maior número foi lido
    //posso usar o contador sempre que o enunciado pedir para contar algo
    maior = 0;
    quantidadeMaior = 0;
    printf("Coloque a quantidade de números que serão lidos: \n"); scanf("%d", &quantidadeNum);

    for (i=1; i<=quantidadeNum; i++) {
        printf("Digite o número: \n", num); scanf("%d", &num);
        if (num>maior){
            maior = num;
            contador=1;
            //contador ++ aqui conta quantas vezes o maior numero entrou no if
            //contador será incrementado (+1) toda vez que o maior número cair no if
        }
        else if (num==maior) {
            contador++;
        }
    }
    printf("O maior número é %d, ele foi repetido %d vezes.\n", maior, contador);

    return 0;
}
