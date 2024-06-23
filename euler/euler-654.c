#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define N 5002
typedef long long unsigned int bignumber; 
typedef unsigned int number; 

typedef number matrix[N][N];
typedef number vector[N];

void triangle(matrix v, int n) {
    int i, j; 
    for (i=0 ; i<n ; i++) {
        for (j=0 ; j<n ; j++) {
            v[i][j] = (j < n - i); 
        }
    }
}

void identity(matrix rez, number n) {
    number i, j;
    for (i=0 ; i<n ; ++i) {
        for (j=0 ; j<n ; ++j) {
            rez[i][j] = (i == j);
        }
    }
}

void vectorone(vector rez, number n) {
    number i;
    rez[0] = 1;
    for (i=1 ; i<n ; ++i) {
        rez[i] = 0;
    }
}

number vsum(vector v, number n, number mod) {
    number i;
    bignumber s = 0;
    for (i=0 ; i<n ; i++) {
        s += v[i];
    }
    return s % mod; 
}

void vcopy(vector dest, vector src, number n) {
    number i;
    for (i=0 ; i<n ; ++i) {
        dest[i] = src[i];
    }
}

void vmultiply(vector rez, matrix m, vector a, number n, number mod) {
    number i, j;
    vector tmp; 
    bignumber s; 
    for (i=0 ; i<n ; i++) {
        s = 0; 
        for (j=0 ; j<n ; j++) {
            s += (bignumber)a[j] * (bignumber)m[i][j];
            s %= mod;
        }
        tmp[i] = (number)s;
    }
    vcopy(rez, tmp, n);
}

void matrixcopy(matrix dest, matrix src, number n) {
    number i, j; 
    for (i=0 ; i<n ; i++) {
        for (j=0 ; j<n ; j++) {
            dest[i][j] = src[i][j];
        }
    }    
}


matrix multiply_tmp; 
vector multiply_tmp_v;

void multiply(matrix rez, matrix m1, matrix m2, number n, number mod) {
    number i, j, k; 
    bignumber s; 
    for (j=0 ; j<n ; j++) {
        fprintf(stderr, ".");
        for (k=0 ; k<n ; k++) {
            multiply_tmp_v[k] = m2[k][j]; 
        }
        for (i=0 ; i<n ; i++) {
            s = 0; 
            for (k=0 ; k<n ; k++) {
//                s += (m1[i][k] * m2[k][j]);
                s += ((bignumber)m1[i][k] * (bignumber)multiply_tmp_v[k]);
                s %= mod;
            }
            s %= mod;
            multiply_tmp[i][j] = (number)s; 
        }
    }
    matrixcopy(rez, multiply_tmp, n);
}

matrix matrixpow_tmp; 


/*changes v to be the result of m^power * v*/
void matrixpow_vmul(matrix m, vector v, number n, bignumber power, number mod) {
    bignumber i = 1; 
    matrixcopy(matrixpow_tmp, m, n); 
    while (1) {
        printf("\npower %llu\n", i);
        if (i & power) {
            vmultiply(v, matrixpow_tmp, v, n, mod); 
        }
        i *= 2; 
        if (i > power) {
            return; 
        }
        multiply(matrixpow_tmp, matrixpow_tmp, matrixpow_tmp, n, mod);
    }
}


void printmatrix(matrix m, number n) {
    number i, j;
    for (i=0 ; i<n ; i++) {
        for (j=0 ; j<n ; j++) {
            printf("%u ", m[i][j]);
        }
        printf("\n");
    }
}

void vprint(vector v, number n) {
    number i;
    for (i=0 ; i<n ; ++i) {
        printf("%u ", v[i]);
    }
    printf("\n");
}

matrix m1;

number T(number n, bignumber m, number mod) {
    vector a; 
    printf("T entering with m=%llu\n", m);
    triangle(m1, n - 1);
    vectorone(a, n - 1);
    matrixpow_vmul(m1, a, n - 1, m, mod);
    return vsum(a, n - 1, mod); 
}

void main (void) {
    assert(sizeof(number) == 4);

    printf("result(5,5)= %u\n", T(5, (number)5, (number)1000000007)); 
    printf("result(10,100)= %u\n", T(10, (number)100, (number)1000000007)); 
    printf("result(final)= %u\n", T(5000, 1000000000000, (number)1000000007)); 
}

