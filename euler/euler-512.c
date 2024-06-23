#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <stdint.h>

#define N 500000000
//#define N 5000

unsigned short div[N + 1] = {0};

int toti(int n) {
    int d = div[n], m = 1, mm;
    if (!d) {
        if (n > 1) {
            return (n - 1);
        } else {
            return 1;
        }
    }

    mm = d - 1;
    while (n % d == 0) {
        n /= d;
        m *= mm;
        mm = d;
    }

    if (n == 1) {
        return m;
    } else {
        return m * toti(n);
    }
}

#define big uint64_t


void m2print(big *m) {
    printf("[%lu %lu] \n[%lu %lu]\n\n", m[0], m[1], m[2], m[3]);
}

void m2printv(big *v) {
    printf("[%lu] \n[%lu]\n\n", v[0], v[1]);
}

void m2mul(big *ret, big *m1, big *m2, big mod) {
    ret[0] = m1[0] * m2[0] + m1[1] * m2[2];
    ret[1] = m1[0] * m2[1] + m1[1] * m2[3];

    ret[2] = m1[2] * m2[0] + m1[3] * m2[2];
    ret[3] = m1[2] * m2[1] + m1[3] * m2[3];
    
    if (mod) {
        ret[0] %= mod;
        ret[1] %= mod;
        ret[2] %= mod;
        ret[3] %= mod;
    }
}

void m2copy(big *dest, big*m) {
    for (int i=0 ; i<4 ; ++i) {
        dest[i] = m[i];
    }
}

void m2mulv(big *ret, big*m, big*v, big mod) {
    ret[0] = m[0] * v[0] + m[1] * v[1];
    ret[1] = m[2] * v[0] + m[3] * v[1];
    if (mod) {
        ret[0] %= mod;
        ret[1] %= mod;
    }
}

void m2identity(big *ret) {
    ret[0] = 1;
    ret[1] = 0;
    ret[2] = 0;
    ret[3] = 1;
}

void m2pow(big *ret, big *m, int pow, big mod) {
    big two_pow[32][4];
    big buf[4];
    int i = 2, k = 1;

    m2identity(ret);
    if (pow <= 0) {
        return;
    }

    m2copy(two_pow[0], m);
    while (i <= pow) {
        m2mul(two_pow[k], two_pow[k - 1], two_pow[k - 1], mod);
        i *= 2;
        k += 1;
    }

    i = 1; k = 0;
    while (i <= pow) {
        if (i & pow) {
            m2copy(buf, ret);
            m2mul(ret, buf, two_pow[k], mod);
        }
        i *= 2;
        k += 1;
    }
}



big f(big n) {
    big tt = toti(n);
    big v[2] = {1, 1};
    big vret[2];
    big m[4] = {n, 1, 0, 1};

    big mn1[4];
    m2pow(mn1, m, n - 1, n + 1);
    m2mulv(vret, mn1, v, n + 1);
    return (tt * vret[0]) % (n + 1);
}


big g(int n) {
    big sum = 0;
    big fval;
    for (int i=1 ; i<=n ; i+=2) {
        if (i % 1000000 == 1) {
            printf("i=%d sum=%lu\n", i, sum);
        }
        fval = toti(i);
//      fval = f(i); <- used to be  this but the power series 1+n+n**2+...
// just adds up to i%2 (n mod n+1 is -1 mod n+1 is a sum of 1 -1 +1 -1 ....)
        sum += fval;
//        printf("f(%d)=%lu\n", i, fval);
    }
    return sum;
}

void main(void) {
    int n2 = (int)(sqrt(N) + 2.0);
    assert(sizeof(unsigned short) == 2);
    for(int i=2 ; i<=n2 ; ++i) {
        if (!div[i]) {
            printf("%d\n", i);
            for(int j=2*i ; j<=N ; j += i) {
                div[j] = i;
            }
        }
    }

    printf("gggggg %lu\n", g(N));
}

