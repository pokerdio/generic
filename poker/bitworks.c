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


int bitcount(uint64_t x) {
    int ret = 0;
    while (x) {
	ret += x & 1;
	x >>= 1;
    }
    return ret;
}
