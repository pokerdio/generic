#ifndef bitworks_h__
#define bitworks_h__

#include <stdint.h>

static inline int bitcount(uint64_t x) {
    return __builtin_popcountll(x);
}

static inline int lsb_index(uint64_t x) {
    return __builtin_ctzll(x);     // count trailing zeros
} 

static inline int msb_index(uint64_t x) {
    return 63 - __builtin_clzll(x); // index of highest set bit    
}

uint64_t cards_as_bit_filter(const uint8_t* c, int count);
int char_idx(char c, char* s);
void bitPrint(uint64_t x);

#endif
