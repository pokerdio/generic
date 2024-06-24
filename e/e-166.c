#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

int v[4][4];
int count = 10;

void update_minmax(int* min, int* max, int sum, int partial, int free) {
    int newmin = sum - partial - free * 9;
    int newmax = sum - partial;

    if (newmin > *min)
        *min = newmin;
    if (newmax < *max)
        *max = newmax;
}

void minmax(int y, int x, int* min, int* max) {
    int s, i, j, ret = 0;
    int sum=0;
    *min = 0;
    *max = 9;

    if (y == 0) {  //first row unrestricted
        return;
    }

    sum = v[0][0] + v[0][1] + v[0][2] + v[0][3];

    for (i=s=0 ; i<x ; ++i) {
        s += v[y][i];
    }
    update_minmax(min, max, sum, s, 3 - x); 

    for (i=s=0 ; i<y ; ++i) {
        s += v[i][x];
    }
    update_minmax(min, max, sum, s, 3 - y); 

    if (x == y) {
        for (i=s=0 ; i<x ; ++i) {
            s += v[i][i];
        }
        update_minmax(min, max, sum, s, 3 - y); 
    }

    if (x == 3 - y) {
        for (i=s=0 ; i<y ; ++i) {
            s += v[i][3-i];
        }
        update_minmax(min, max, sum, s, 3 - y); 
    }
}

void init_test_case(void) {
    v[0][0] = 6; v[0][1] = 3; v[0][2] = 3; v[0][3] = 0;
    v[1][0] = 5; v[1][1] = 0; v[1][2] = 4; v[1][3] = 3;
    v[2][0] = 0; v[2][1] = 7; v[2][2] = 1; v[2][3] = 4;
    v[3][0] = 1; v[3][1] = 2; v[3][2] = 4; v[3][3] = 5;
}

void init_test_zero(void) {
    memset(v, 0, sizeof(v));
}

void test_minmax() {
    int i, j, min, max;
    
    init_test_zero();
    for (i=0 ; i<4 ; ++i) {
        for (j=0 ; j<4 ; ++j) {
            minmax(i, j, &min, &max);
            printf("%d(%d %d)  ", v[i][j], min, max);
        }
        printf("\n");
    }
}

void printv() {
    for (int i=0 ; i < 4 ; ++i){
        printf("%d %d %d %d\n", v[i][0], v[i][1], v[i][2], v[i][3]);
    }
    printf("\n");
}

long int go(int level) {
    int i, y = level / 4, x = level % 4;
    int min, max;
    long int s = 0; 

    if (level == 3) {
        printf("%d %d %d\n", v[0][0], v[0][1], v[0][2]);
    }
    if (level == 16) {
        return 1;
    }

    minmax(y, x, &min, &max);
    for(i=min ; i<=max ; ++i) {
        v[y][x] = i;
        s += go(level + 1);
    }
    return s;
}


int main (int argc, char *argv[]) {
    int i, j;

//    test_minmax();
    
    printf("%ld\n", go(0));

    return 0;
}
