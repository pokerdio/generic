#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 1000050

char c[MAXN];
int v[MAXN][26];


void step(int poz) {
    int x = v[poz - 1][c[poz - 1]];
    for (int letter=0 ; letter<26 ; ++letter) {
        if (c[x] == letter) {
            v[poz][letter] = x + 1;
        } else {
            v[poz][letter] = v[x][letter];
        }
    }
}

void dec_a(char* c) {
    while(*c > 0) {
        *c -= 'a';
        ++c;
    }
}

int main (void) {
    int nquery, i, n2;
    scanf ("%s", c);
    int n = strlen(c); 
    dec_a(c);


    for (i=0 ; i<26 ; ++i) {
        v[0][i] = 0;

        if (n > 1) {
            v[1][i] = (i == c[0]) ? 1 : 0;
        }
    }

    for (i=2 ; i<n ; ++i) {
        step(i);
    }

    scanf ("%d", &nquery);
    for (int query=0 ;  query<nquery ; ++query) {
        scanf ("%s", c + n);
        n2 = n + strlen(c + n);
        dec_a(c + n);

        for (i=n ; i<n2 ; ++i) {
            step(i);
            printf("%d%s", v[i][c[i]], i<n2-1?" ":"");
        }
        printf("\n");
    }

    return 0;
}
