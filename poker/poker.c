#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "poker.h"



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
  for (uint8_t k = n; k<5; k++) {
    v = v * 13u;
  }
  return v;
}

int cg_pair_count (const CardGroup *sorted) {
  int n = sorted->count;
  int ret = 0;
  for (uint8_t k=0; k<n-1; k++) {
    if (RANK(sorted->cards[k]) != RANK(sorted->cards[k + 1])) {
      continue;
    }
    if (k>0 && RANK(sorted->cards[k - 1]) == RANK(sorted->cards[k])) {
      continue;
    }
    if (k<n-2 && RANK(sorted->cards[k + 1]) == RANK(sorted->cards[k + 2])) {
      continue;
    }
    ret++;
  }
  return ret;
}

int cg_trips_count (const CardGroup *sorted) {
  int n = sorted->count;
  int ret = 0;
  for (int k=0; k<n-2; k++) {
    if (RANK(sorted->cards[k]) != RANK(sorted->cards[k + 2])) {
      continue;
    }
    if (k>0 && RANK(sorted->cards[k - 1]) == RANK(sorted->cards[k])) {
      continue;
    }
    if (k<n-3 && RANK(sorted->cards[k + 2]) == RANK(sorted->cards[k + 3])) {
      continue;
    }
    ret++;
  }
  return ret;
}

static void print_group(const CardGroup *g) {
    printf("{ count=%u, ranks=[", (unsigned)g->count);
    for (uint8_t i = 0; i < g->count; i++) {
        if (i) printf(" ");
        printf("%u", (unsigned)RANK(g->cards[i]));
    }
    printf("] }");
}

#include "all_tests.c"
