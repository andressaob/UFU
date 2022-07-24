#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x = 1; // o valor 1 foi atribuido a variavel x
    int main() {

        printf("\n Valor de x = %d", x); // x = 1

        int x = 10; // o valor 10 foi atribuido a variavel x
        x++; // ++ = +1, portanto x = 10 + 1 = 11

        printf("\n Valor de x = %d", x);
        if (x > 0) { // 11 > 0?              //true
            printf("\n Valor de x = %d", x); // x = 11

            int x = 1000; // o valoe 1000 foi atribuido a variavel x
            ++x; // x = 1000 + 1 = 1001
            printf("\n Valor de x = %d", x++); //x = 1001 + 1 = 1002
        }
        printf("\n Valor de x = %d", ++x); // x = 11 + 1 = 12
    }

    return 0;
}
