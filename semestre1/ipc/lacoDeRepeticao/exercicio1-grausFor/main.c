#include <stdio.h>
#include <stdlib.h>

int main()
{
    float fahrenheit, kelvin;
    int celsius;

    for (celsius=-10 ; celsius<=100; celsius++) {
        fahrenheit = 9 * celsius / 5.0 + 32;
        kelvin = celsius + 273.15;
        printf("A temperatura atual em Celsius é de %d, em Fahrenheit é de %.2f graus e em Kelvin é de %.2f graus.\n",
        celsius, fahrenheit, kelvin);
    }

    return 0;
}
