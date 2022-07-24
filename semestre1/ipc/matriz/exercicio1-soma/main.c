#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A[2][3] = {{15,52,29}, {47,34,85}};
    int B[2][3] = {{5,13,11},{8,17,-10}};
    int C[2][3];
    int i, j;

    //fazendo a soma
    for (i=0; i<2; i++){
        for(j=0; j<3; j++){
            C[i][j] = A[i][j] + B[i][j];
        }
    }
    //imprimindo a soma
    for (i=0; i<2; i++){
        for(j=0; j<3; j++){
            printf(" %2d", C[i][j]);
        }
        printf("\n");
    }

    //printf("C[%d][%d]= ", C[i][j]);

    return 0;
}
