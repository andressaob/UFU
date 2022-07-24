#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A, B, C, D;

    printf("Digite os numeros A, B, C e D, respectivamente\n");
    scanf("%d %d %d %d", &A, &B, &C, &D);

    printf("DIFERENÇA: %d",((A*C) - (B*D)));
    return 0;
}
