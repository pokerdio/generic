#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 120000L

void main(void) {
    long int q, root, a2;
    for (long int pq=3 ; pq<=N ; ++pq) {
        for (long int p=1 ; p<pq ; ++p) {
            q = pq - p;
            if (q < p) {
                break;
            }
            a2 = pq * pq - p * q;
            root = (long int)floor(sqrt((double)a2));
            if (root * root == a2) {
                printf("%ld %ld\n", p, q);
            }
        }
    }
}
