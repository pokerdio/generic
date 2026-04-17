#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

enum {
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
} card;

#define SUIT(x) ((x) % 4)
#define RANK(x) (((x) / 4))


typedef struct {
  uint8_t cards[7];  // each is a card enum value
  uint8_t count;     // 0..7
} CardGroup;

_Static_assert(sizeof(CardGroup) == 8, "CardGroup must be exactly 8 bytes");

/* --- helpers --- */

static inline void cg_clear(CardGroup *g) {
     g->count = 0;
}

static inline void cg_push(CardGroup *g, uint8_t c) {
     if (g->count < 7) {
	  g->cards[g->count++] = c;
     }
}

/* Sort key: rank ascending, suit ascending (so grouped ranks; stable enough for eval work). */
static inline int card_less(uint8_t a, uint8_t b) {
     return a < b;
}

/* --- requested functions --- */

/* 1) Sort: src by reference, dst by reference. Does not modify src. */
void cg_sort(const CardGroup *src, CardGroup *dst) {
     *dst = *src; // copy count + bytes

     // insertion sort (n <= 7, simple and fast enough)
     for (uint8_t i = 1; i < dst->count; i++) {
	  uint8_t key = dst->cards[i];
	  int j = (int)i - 1;
	  while (j >= 0 && card_less(key, dst->cards[j])) {
	       dst->cards[j + 1] = dst->cards[j];
	       j--;
	  }
	  dst->cards[j + 1] = key;
     }
}

/* 2) Prune by rank: remove all cards of rank `rank_to_remove` from src into dst. */
void cg_prune_rank(const CardGroup *src, uint8_t rank_to_remove, CardGroup *dst) {
     cg_clear(dst);
     for (uint8_t i = 0; i < src->count; i++) {
	  uint8_t c = src->cards[i];
	  if (RANK(c) != rank_to_remove) cg_push(dst, c);
     }
}

/*
3) High-card value:
   - assumes `sorted` is sorted ascending by rank (as produced by cg_sort)
   - takes up to the 5 highest cards (or fewer if count < 5)
   - encodes ranks in base-13 with highest rank as most significant digit
   - ignores duplicates (caller promises non-paired groups)
*/
uint32_t cg_highcard_value_base13(const CardGroup *sorted) {
  uint8_t n = sorted->count;
  if (n > 5) n = 5;

  uint32_t v = 0;
  // take from the end (highest ranks) and build most-significant-first
  for (uint8_t k = 0; k < n; k++) {
    uint8_t c = sorted->cards[sorted->count - n + k]; // ascending slice of top n
    v = v * 13u + (uint32_t)RANK(c);
  }
  return v;
}

/* --- tiny demo --- */

int main(void) {
  CardGroup g = { .cards = { cTh, c2c, cKd, c7s, cJc, c9h, c3d }, .count = 7 };

  CardGroup s;
  cg_sort(&g, &s);

  printf("sorted ranks: ");
  for (uint8_t i = 0; i < s.count; i++) printf("%u ", (unsigned)RANK(s.cards[i]));
  printf("\n");

  CardGroup pr;
  cg_prune_rank(&s, RANK(cTh), &pr); // remove Tens' rank
  printf("after prune(T): count=%u\n", (unsigned)pr.count);

  uint32_t hv = cg_highcard_value_base13(&s);
  printf("highcard(base13)=%u\n", (unsigned)hv);

  return 0;
}
