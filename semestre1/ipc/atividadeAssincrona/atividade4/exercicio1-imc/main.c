#include <stdio.h>
#include <stdlib.h>

float imc (float massa, float alt){
    return  massa / (alt * alt);
}
int main(){
    float IMC, peso, altura;
    printf("Digite o seu peso em kg: "); scanf("%f", &peso);
    printf("Digite a sua altura em metros: "); scanf("%f", &altura);

    IMC = imc(peso, altura);
    printf("O seu índice de massa corporal (IMC) é: %.2f.", IMC);
    return 0;
}
