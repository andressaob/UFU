#include <stdio.h>
#include <stdlib.h>

int main()
{
    float salario;

    printf("Coloque o salário do funcionário: \n");
    scanf("%f", &salario);
    printf("salario", salario);

    float reajuste = salario * 1.075; //1.075 = salario * 0.75

    if (reajuste <= 1200) {
        printf("O reajuste do salário é igual a: %f", reajuste + 100);
    }else {
        printf("O reajuste do salário é igual a : %f", reajuste);
    }

    return 0;
}
