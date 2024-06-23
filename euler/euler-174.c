#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>

int L(int t) {
    int j, k, max; //a and b are the outter and inner widthes of the laminate

    max = sqrt(t); 
    k = 0;
    for(j=2 ; j<=max ; j += 2) { 
        if (t % j == 0 && (t / j) % 2 == 0 && j < (t / j)) {
            k ++;
        }
    }
    return k;
}

int main (int argc, char *argv[]) {
    int v = 0, v15 = 0, k;  

    for (int i=4 ; i<1000001 ; i+=4) {
        k = L(i);
        if (k > 0 && k < 11) {
            v++;
        }
    }
    
    printf("%d\n", v);
}
