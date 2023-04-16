#include <stdio.h>
#include <stdlib.h>

int main()
{
    float a, *b, **c, ***d, i;
    printf("Digite o valor da variável 'a': "); scanf("%f", &a);

    b=&a;
    c=&b;
    d=&c;

    printf("\na = %.0f, dobro de a = %.0f, triplo de a = %.0f e quádruplo de a = %.0f", a, *b * 2, **c * 3, ***d * 4);

    return 0;
}
