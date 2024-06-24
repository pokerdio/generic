#include <stdio.h>
#include <stdlib.h>
#include <assert.h>


int sevens_factorial(int n) {
    int i, s = 0;
    for (i=7 ; i<=n ; i*=7) {
        s += n / i; 
    }
    return s;
}


int sevens_number(int n) {
    int s = 0;
    while (n % 7 == 0) {
        n /= 7; 
        s += 1;
        if (n == 0)
            break;
    }
    return s;
}

int go(int n) {
    int num_sevens = 0;
    int a, b = 0, father;
    int i, j, k; 

    int s = 0; 
    long long c = 1;
    int backup_sevens; 

    for (i=1 ; i<n ; ++i) {
        k = sevens_number(i);
        j = sevens_number(n + 1 - i); 
        num_sevens += j - k;


        c *= n + 1 - i;
        c /= i;

        backup_sevens = sevens_number(c);
        printf("multiply by %d divide by %d; sevens %d; c = %lld; backup sevens %d\n", 
               n + 1 - i, i, num_sevens, c, backup_sevens);

        assert(backup_sevens == num_sevens);
        assert(num_sevens >= 0);
        if (num_sevens > 0) {
            s += 1;
        }
    }
    printf("\n");
    return s;
}

int main (int argc, char *argv[]) {
    int x, i;
    int s = 0;
    assert(argc == 2);
    x = atoi(argv[1]);

    go(x);
    exit(0);

    for (i=3 ; i<=x ; ++i) {
        s += go(i);
    }


    i = x * (x + 1) / 2;
    printf("%d %d\n", s, i - s);
}
