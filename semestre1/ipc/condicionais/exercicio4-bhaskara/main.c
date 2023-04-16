#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int a, b, c, delta, x1, x2;

    printf("Coloque os coeficientes 'a', 'b' e 'c', respectivamente de uma equação do segundo grau.\n");
    scanf("%d %d %d", &a, &b, &c);

    delta = (b*b) - 4 * a * c;

    x1 = ((-b) + sqrt(delta)) / 2 * a;
    x2 = ((-b) - sqrt(delta)) / 2 * a;

    if ( a == 0) {
        printf("Não é equação do 2º grau.");
    }else if (delta < 0) {
        printf("Não existe raíz.");
    }else if (delta == 0) {
        printf("Raíz única.");
    }else {
        printf(" As raízes são x1 = %d e x2 = %d", x1, x2);
    }

    return 0;
}
