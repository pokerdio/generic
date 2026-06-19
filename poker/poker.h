#ifndef poker_h__
#define poker_h__

#include <stdint.h>

#define SUIT(x) ((x) % 4)
#define RANK(x) (((x) / 4))
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

typedef enum {
    SCORE_HIGHCARD = 0,
    SCORE_PAIR = 1000000,
    SCORE_TWO_PAIR = 2000000,
    SCORE_TRIPS = 3000000,
    SCORE_STRAIGHT = 4000000,
    SCORE_FLUSH = 5000000,
    SCORE_FULL_HOUSE = 6000000,
    SCORE_QUADS = 7000000,
    SCORE_STRAIGHT_FLUSH = 8000000
} score_t;

typedef enum {
c2c, c2d, c2h, c2s, 
c3c, c3d, c3h, c3s, 
c4c, c4d, c4h, c4s, 
c5c, c5d, c5h, c5s, 
c6c, c6d, c6h, c6s, 
c7c, c7d, c7h, c7s, 
c8c, c8d, c8h, c8s, 
c9c, c9d, c9h, c9s, 
cTc, cTd, cTh, cTs, 
cJc, cJd, cJh, cJs, 
cQc, cQd, cQh, cQs, 
cKc, cKd, cKh, cKs, 
cAc, cAd, cAh, cAs, 
} card_t;

#define NCARDS 52
#define NRANKS 13

typedef struct {
  uint8_t cards[7];  // each is a card enum value
  uint8_t count;     // 0..7
} CardGroup;

typedef struct {
    const char *description;
    CardGroup group;
    int expected;
} CGTest;

typedef struct {
    const char *description;
    CardGroup input;
    CardGroup expected;
} CGFilterTest;

//test entry in an array of CGTest  
#define CG(...) { .cards = { __VA_ARGS__ }, .count = sizeof((uint8_t[]){ __VA_ARGS__ }) / sizeof(uint8_t) }
#define CG0() {.cards = {0}, .count = 0}
#define PRINT_VAR(x) printf("%s = %d\n", #x, (x))
#define TEST_OK(x) \
    do { printf("Test %s: %s\n", #x, (x) ? "OLL KORRECT" : "FAIL"); } while (0)

#define ARRAY_SIZE(rrr) (int)(sizeof(rrr) / sizeof((rrr)[0]))

int cg_score (const CardGroup *g);
int cg_straight_flush_score(const CardGroup *sorted);
int cg_quads_score(const CardGroup *sorted);
int cg_full_house_score(const CardGroup *sorted);
int cg_set_score(const CardGroup *sorted);
int cg_two_pair_score(const CardGroup *sorted);
int cg_pair_score (const CardGroup *sorted);
void cg_filter_quads(const CardGroup *sorted, CardGroup *dest);
void cg_filter_set(const CardGroup *sorted, CardGroup *dest);
void cg_filter_pair(const CardGroup *sorted, CardGroup *dest);
void cg_filter_highcard(const CardGroup *sorted, CardGroup *dest);
void cg_filter_tuple(const CardGroup *sorted, CardGroup *dest, int wanted_count);
int cg_filter_flush(CardGroup *g);
int cg_top_straight (const CardGroup *g);
int cg_quads_count (const CardGroup *sorted);
int cg_trips_count (const CardGroup *sorted);
int cg_pair_count (const CardGroup *sorted);
int cg_highcard_value_base13(const CardGroup *sorted, int topn, int seed);
void cg_sort(const CardGroup *src, CardGroup *dst);
int cg_same_cards_sorted(const CardGroup *sorted_src, const CardGroup *sorted_dst);
int cg_same_cards (const CardGroup *src, const CardGroup *dst);
int cg_count (const CardGroup *src, uint8_t card);

int parse_hand(const char* s, uint8_t *dest);
int parse_card(const char* s);
void print_cards (uint8_t * cards, int n);
void print_card (uint8_t card);
void print_cards_ascii (uint8_t * cards, int n);
void print_card_ascii (uint8_t card);
void loop_card_combo (int n, uint64_t forbid_bitmask, void (*f) (uint8_t*, int));
void loop_card_combo_bit (int n, uint64_t forbid_bitmask, void (*f) (BitCards));
uint64_t gospers_hack(const uint64_t n);


static inline uint64_t bs_13bit_contract(BitCards hand) {
    return hand.all & (((UINT64_C(1) << 13) - 1) |
	(hand.all & (((UINT64_C(1) << 13) - 1) << 16)) >> 3 |
	(hand.all & (((UINT64_C(1) << 13) - 1) << 32)) >> 6 | 
	(hand.all & (((UINT64_C(1) << 13) - 1) << 48)) >> 9);
}

static inline BitCards bs_13bit_expand(uint64_t x) {
    BitCards ret = {0};
    ret.clubs = x & ((UINT64_C(1) << 13) - 1);
    ret.diamonds = (x & (((UINT64_C(1) << 13) - 1) << 16)) >> 16;
    ret.hearts = (x & (((UINT64_C(1) << 13) - 1) << 32)) >> 16;
    ret.spades = (x & (((UINT64_C(1) << 13) - 1) << 48)) >> 16;
    return ret;
}


#endif 
