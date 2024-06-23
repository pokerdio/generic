#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>

typedef long long unsigned int number; 

void main (void) {
    number x, k, kroot; 

    number total = 0; 
// x x x+1
    for (x=2 ; x<=333333333 ; ++x) {
        k = (3 * x + 1) * (x - 1); 
        kroot = (int)sqrt(k);
        if (kroot * kroot == k) {
            k = kroot * (x + 1);
            if (k % 4 == 0) {
                total += (x + x + x + 1); 
            }
        }
    }
// x x x-1
    for (x=2 ; x<=333333333 ; ++x) {
        k = (3 * x - 1) * (x + 1); 
        kroot = (int)sqrt(k);
        if (kroot * kroot == k) {
            k = kroot * (x - 1);
            if (k % 4 == 0) {
                total += (x + x + x - 1); 
            }
        }
    }

    printf("%llu", total); 
}

