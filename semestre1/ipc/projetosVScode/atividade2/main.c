#include <stdio.h>
#include <stdlib.h>

int main() {
    int celsius = 0;
    float kelvin, fahrenheit = 0;

    while ((fahrenheit = 9 * celsius) < 200){
        kelvin = celsius + 273.15;
        printf("A temperatura em Celsius é de %d, em Fahrenheit é de %.2f graus e em Kelvin é de %.2f graus.\n",
        celsius, fahrenheit, kelvin);
        celsius++;
    }
    return 0;
}
