#ifndef bitscore_h__
#define bitscore_h__
#include "poker.h"

typedef union {
    struct {
        uint16_t clubs;
        uint16_t diamonds;
        uint16_t hearts;
        uint16_t spades;
    };
    uint16_t suits[4];
    uint64_t all;
} BitCards;

#define BS_CARD(rank, suit) (UINT64_C(1)<<((rank) + 16 * (suit)))

#define bs_twos (BS_CARD(0, 0) | BS_CARD(0, 1) | BS_CARD(0, 2) | BS_CARD(0, 3))
#define bs_threes (BS_CARD(1, 0) | BS_CARD(1, 1) | BS_CARD(1, 2) | BS_CARD(1, 3))
#define bs_fours (BS_CARD(2, 0) | BS_CARD(2, 1) | BS_CARD(2, 2) | BS_CARD(2, 3))
#define bs_fives (BS_CARD(3, 0) | BS_CARD(3, 1) | BS_CARD(3, 2) | BS_CARD(3, 3))
#define bs_sixes (BS_CARD(4, 0) | BS_CARD(4, 1) | BS_CARD(4, 2) | BS_CARD(4, 3))
#define bs_sevens (BS_CARD(5, 0) | BS_CARD(5, 1) | BS_CARD(5, 2) | BS_CARD(5, 3))
#define bs_eights (BS_CARD(6, 0) | BS_CARD(6, 1) | BS_CARD(6, 2) | BS_CARD(6, 3))
#define bs_nines (BS_CARD(7, 0) | BS_CARD(7, 1) | BS_CARD(7, 2) | BS_CARD(7, 3))
#define bs_tens (BS_CARD(8, 0) | BS_CARD(8, 1) | BS_CARD(8, 2) | BS_CARD(8, 3))
#define bs_jacks (BS_CARD(9, 0) | BS_CARD(9, 1) | BS_CARD(9, 2) | BS_CARD(9, 3))
#define bs_queens (BS_CARD(10, 0) | BS_CARD(10, 1) | BS_CARD(10, 2) | BS_CARD(10, 3))
#define bs_kings (BS_CARD(11, 0) | BS_CARD(11, 1) | BS_CARD(11, 2) | BS_CARD(11, 3))
#define bs_aces (BS_CARD(12, 0) | BS_CARD(12, 1) | BS_CARD(12, 2) | BS_CARD(12, 3))

extern const uint64_t bs_ranks[];

int bs_score(BitCards hand);

#endif
