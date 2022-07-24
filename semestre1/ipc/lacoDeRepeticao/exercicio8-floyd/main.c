#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, i, j, num=0;
    printf("Digite um valor para N: ", N); scanf("%d", &N);
    i=1; //i=linha
    //j=colunas

    while (i<=N) { //garante que N linhas serão puladas
        for (j=1; j<=i; j++){
            num++;
            //num=números que serão printados
            printf("%d ", num);
        }
        i++;
        printf("\n");
    }

    return 0;
}
