#include <stdio.h>
#include <stdlib.h>

int main()
{
    float h, idealF, idealM;
    char sexo;
    //sexo = getchar();

    printf("Escreva F para feminino ou M para masculino.\n");
    scanf("%c", &sexo);

    printf("Escreva a altura em metros: \n");
    scanf("%f", &h);

    idealF = (62.1 * h) - 44.7;
    idealM = (72.7 * h) - 58;

    if ((sexo =='M') || (sexo =='m')) {
        printf("Seu peso ideal é: %f", idealM);
    }else if ((sexo == 'F') || (sexo =='f')){
        printf("Seu peso ideal é: %f", idealF);
    }else {
        printf("Caractere não reconhecido.");
    }

    return 0;
}
