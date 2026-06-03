#ifndef bitworks_h__
#define bitworks_h__

#include <stdint.h>

int bitcount(uint64_t x);
uint64_t cards_as_bit_filter(const uint8_t* c, int count);
int char_idx(char c, char* s);
#endif
