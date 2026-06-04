#include <stdio.h>
#include <stdlib.h>
#include "bitworks.h"


int char_idx(char c, char* s) {
    for (int i=0; s[i]; i++) {
	if (c == s[i]) {
	    return i;
	}
    }
    return -1;
}

uint64_t cards_as_bit_filter(const uint8_t* c, int count) {
    uint64_t ret = 0;
    for (int i=0; i<count; i++)  {
	ret |= (UINT64_C(1) << c[i]);
    }
    return ret;
}

    /* int ret = 0; */
    /* while (x) { */
    /* 	ret += x & 1; */
    /* 	x >>= 1; */
    /* } */
    /* return ret; */

void bitPrint(uint64_t x) {
    printf("%19lu ", x);
    printf("%5d ", bitcount(x));
    for (int i=7; i>=0; i--) {
	for (int j=7; j>=0; j--) {
	    printf(x & (UINT64_C(1) << (i * 8 + j)) ? "1" : "0");
	}
	printf(" ");
    }
    printf("\n");
}
