#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

long long foo[1100][1100];
long long bar[1100][1100];

int fill(int n) {
    long long t = 0;
    int k = 0;
    int i = 0, j = 0;
    long long min = 1048576;
    
    int totaln = n * (n + 1) / 2;
    printf("%d\n", n);
    for (k=0 ; k<totaln ; ++k) {
        t = (615949 * t + 797807) % 1048576;
        foo[i][j] = t - 524288;
        if (foo[i][j] < min) {
            min = foo[i][j];
        }
        j += 1;
        if (j > i) {
            i += 1;
            j = 0;
        }
    }
    assert(j == 0 && i == n);
    return min;
}

long long base(int n) {
    int i, j;
    long long best = 1048576; 

    for (j=0 ; j<=n ; ++j) {
        bar[n][j] = foo[n][j];
    }
    for (i=n-1 ; i>=0 ; --i) {
        for (j=0 ; j<=i ; ++j) {
            bar[i][j] = foo[i][j] + bar[i+1][j] + bar[i+1][j+1];
            if (i < n - 1) {
                bar[i][j] -= bar[i + 2][j + 1];
            }
            if (bar[i][j] < best){
                best = bar[i][j];
            }
//            printf("i=%d j=%d n=%d sum=%lld\n", i, j, n, bar[i][j]);
        }
    }
    return best;
}

int fill2(void) {
    foo[0][0] = 15;
    foo[1][0] = -14; foo[1][1] = -7;
    foo[2][0] = 20; foo[2][1] = -13; foo[2][2] = -5; 
    foo[3][0] = -3; foo[3][1] = 8; foo[3][2] = 23; foo[3][3] = -26; 
    foo[4][0] = 1; foo[4][1] = -4; foo[4][2] = -5; foo[4][3] = -18; foo[4][4] = 5; 
    foo[5][0] = -16; foo[5][1] = 31; foo[5][2] = 2; foo[5][3] = 9; foo[5][4] = 28; foo[5][5] = 3; 
    return -26;
}

void main(void) {
    int n = 1000; 
    long long best = fill(n), new;
    for (int i=1 ; i<n ; ++i) {
        new = base(i);
        printf("%d %lld\n", i, new);
        if (new < best) {
            best = new;
        }
    }
    printf("finall result: %lld\n", best);
}
