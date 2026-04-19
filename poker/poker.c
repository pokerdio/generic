#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
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

//sort a card group to a new card group, or in place
void cg_sort(const CardGroup *src, CardGroup *dst) {
  if (dst != src) {
     *dst = *src; // copy count + bytes
  }
  for (int i=0; i<dst->count; ++i) {
    for (int j=0; j<i; j++) {
      if (dst->cards[j] > dst->cards[j+1]) {
	uint8_t tmp = dst->cards[j];
	dst->cards[j] = dst->cards[j+1];
	dst->cards[j+1] = tmp;
      }
    }
  }
}

//removes all cards of a rank, preserves order, can do in place if src==dest
void cg_prune_rank(const CardGroup *src, uint8_t rank_to_remove, CardGroup *dst) {
  int j = 0;
  for (int i = 0; i < src->count; i++) {
    uint8_t c = src->cards[i];
    if (RANK(c) != rank_to_remove) {
      dst->cards[j++] = c;
    }
  }
  dst->count = j;
}

//removes duplicates of the same rank except one; presumes sorted, fails otherwise; can do in place
void cg_prune_dup(const CardGroup *src_sorted, CardGroup *dst) {
  int last_rank = -1;
  int n = src_sorted->count;
  int j = 0;
  for (int i=0; i<n; i++) {
    uint8_t card = src_sorted->cards[i];
    int r = RANK(card);
    assert(r >= last_rank);
    if (r != last_rank) {
      dst->cards[j++] = card;
      last_rank = r;
    }
  }
  dst->count = j;
}

//removes cards not of the most popular suit, can do in place
void cg_one_suit(const CardGroup *src, CardGroup *dst) {
  int suit_count[4] = {0};
  int n = src->count;
  int max_count = 0;
  int best_suit = 0;
  for (int i=0; i<n; i++) {
    int suit = SUIT(src->cards[i]);
    suit_count[suit]++;
    if (suit_count[suit] > max_count) {
      max_count = suit_count[suit];
      best_suit = suit;
    }
  }
  int j = 0;
  for (int i=0; i<n; i++) {
    if (SUIT(src->cards[i]) == best_suit) {
      dst->cards[j++] = src->cards[i];
    }
  }
  assert(j == max_count);
  dst->count = j;
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
  for (int k=0; k<n-1; k++) {
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

int cg_quads_count (const CardGroup *sorted) {
  int n = sorted->count;
  for (int k=0; k+3<n; k++) {
    if (RANK(sorted->cards[k]) == RANK(sorted->cards[k + 3])) {
      return 1;
    }
  }
  return 0;
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
