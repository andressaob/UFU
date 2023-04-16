#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, ult, pen, i, atual;
    pen = 0;
    ult = 1;

    printf("Coloque um valor para 'N': "); scanf("%d", &N);
   // printf("%d %d ", pen, ult);

    for (i=0; i<N; i++){
        atual = pen + ult;
        ult = pen;
        pen = atual;
        printf("%d\n", atual);
    }
    return 0;
}
