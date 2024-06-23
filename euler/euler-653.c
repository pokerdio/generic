#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

long int rlast = 6563116;

void rr(void){ // reset r
    rlast = 6563116;
}

int r(void) {
    int ret = rlast;
    rlast = rlast * rlast % 32745673;
    return ret;
}

#define BALLS 10000005


signed char dir[BALLS];
int x[BALLS], t[BALLS];


int main(int argc, char* argv[]) {
    int L = 5000, N=3, J=2;
    int i, k, x0, delta;


    if (argc == 4) {
        sscanf(argv[1], "%d", &L);
        sscanf(argv[2], "%d", &N);
        sscanf(argv[3], "%d", &J);
    }
    fprintf(stderr, "L=%d N=%d J=%d\n", L, N, J);

    assert(N<BALLS);


    x0 = 0;
    for (i=0 ; i<N ; ++i) {

        k = r();
        x[i] = x0 + k % 1000 + 1;
        x0 = x[i] + 20;

        dir[i] = (k <= 10000000) ? 1 : -1;
        t[i] = 0;

    }


    while(N > 0) {
        if (N % 100 == 0) {
            printf("%d remaining\n", N-J);
        }
        if (dir[0]== -1) {
            t[0] += x[0];
            x[0] = 0;
            dir[0] = 1;
        }
        i=N-2;
        delta = -1;
        while(i<N-1) {
            if (dir[i] == 1 && dir[i + 1] == -1) {
                if (t[i] < t[i + 1])  {
                    x[i] += t[i + 1] - t[i];
                    t[i] = t[i + 1];
                } else {
                    x[i + 1] -= t[i] - t[i + 1];
                    t[i + 1] = t[i];
                }
                k = x[i + 1]- x[i] - 20;
                assert(k >= 0);
                x[i] += k / 2;
                x[i + 1] -= k / 2;

                t[i] += (k + 1) / 2; // trick here: if the distance is odd, the balls do
                t[i + 1] +=  (k + 1) / 2; // half a step in to the mid and half a step out
                // for an extra +1 travel distance

                dir[i] = -1;
                dir[i + 1] = 1; 
                delta = 1;
            }
            i += delta;
            if (i < 0) {
                break;
            }
        }

        for (i=N-1 ; i>=0 ; --i) {
            if (dir[i] == 1) {
                t[i] += L - x[i] - 10;
                if (i == J - 1) {
                    fprintf(stderr, "FINAL ANSWER %d\n", t[i]);
                    exit(0);
                }
                N -= 1;
            } else {
                break;
            }
        }
    }
}
