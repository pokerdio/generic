#include <stdio.h>
#include <stdlib.h>


void main(void) {
    long double a = 1.0;
    int k = 0;
    int q = 0;

    while (1) {
        a = a * 2;
        q += 1;
        if (a > 1000)
            a /= 10.0;

        if ((int)a == 123) {
            k++;
            if (k % 100 == 0) {
                printf("%d\n", k);
            }
            if (k == 678910) {
                printf("winner %d\n", q);
                exit(0);
            }
        }
    }
}
