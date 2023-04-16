#include <stdio.h>
#include <stdlib.h>

int main()
{
    float fahrenheit, kelvin;
    int celsius;

    fahrenheit = 0;
    celsius = 0;

    do {
        kelvin = celsius + 273.15;
        fahrenheit = 9 * celsius / 5.0 + 32;
        printf("A temperatura em Celsius é %d, em Kelvin é de %.2f e em Fahrenheit é de %.2f.\n", celsius, kelvin, fahrenheit);
        celsius ++;
    }

    while (fahrenheit = 9 * celsius / 5.0 + 32 < 200);

    return 0;
}
