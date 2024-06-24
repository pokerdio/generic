#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#define N 100000000
void main(void){
    //we calculate just a single slice;  one sixth of the hexagon
    //we "square" the grid - think of the 60@ angle as 90@
    long int * v; //visible trees on the line index away from center (x+y=index)
    long int i, j, k;

    v = (long int*)malloc (sizeof(long int) * (N + 1));

    v[1] = 1;
    for (i=2 ; i <=N ; ++i) {
        v[i] = i - 1;
    }

    k = 10;
    for (i=2 ; i < N ; ++i) {

        if (i ==k) {
            printf("%ld\n", i);
            k = k * 2;
        }
        for (j=2 ; j<=N/i ; ++j) {
            assert(i * j <= N);
            v[i * j] -= v[i];
        }
    }

    j = 0;
    for (i=1 ; i<=N ; ++i) {
        j += (i - v[i]);
    }
    printf("%ld %ld\n", j, j * 6);
}
