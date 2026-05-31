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

int cg_count (const CardGroup *src, uint8_t card) {
    int ret = 0;
    for (int i=0; i<src->count; i++) {
	if (src->cards[i] == card) {
	    ret++;
	}
    }
    return ret;
}

int cg_same_cards (const CardGroup *src, const CardGroup *dst) {
    if (src->count != dst->count) {
	return 0;
    }
    int n = src->count;
    for (int i=0; i<n; i++) {
	assert(cg_count(src, src->cards[i]) == 1);
	assert(cg_count(dst, dst->cards[i]) == 1);
	if (cg_count(dst, src->cards[i]) != 1) {
	    return 0;
	}
    }
    return 1;
}


int cg_same_cards_sorted(const CardGroup *sorted_src, const CardGroup *sorted_dst) {
    if (sorted_src == sorted_dst) {
	return 1;
    }
    if (sorted_src->count != sorted_dst->count) {
	return 0;
    }
    for (int i=0; i<sorted_src->count; i++) {
	if (sorted_src->cards[i] != sorted_dst->cards[i]) {
	    return 0;
	}
    }
    return 1;
}

//sort a card group to a new card group, or in place
void cg_sort(const CardGroup *src, CardGroup *dst) {
    if (dst != src) {
	*dst = *src; // copy count + bytes
    }
    for (int i=0; i<dst->count; ++i) {
	int ok=1;
	for (int j=0; j<dst->count-i-1; j++) {
	    if (dst->cards[j] > dst->cards[j+1]) {
		uint8_t tmp = dst->cards[j];
		dst->cards[j] = dst->cards[j+1];
		dst->cards[j+1] = tmp;
		ok = 0;
	    }
	}
	if (ok) {
	    break;
	}
    }
}

/*
3) High-card value:
   - assumes `sorted` is sorted ascending by rank (as produced by cg_sort)
   - takes up to the topn highest cards (or fewer if count too small)
   - encodes ranks in base-13 with highest rank as most significant digit, starting
   - from the argument zero
   - ignores duplicates (caller promises non-paired groups)
*/
int cg_highcard_value_base13(const CardGroup *sorted, int topn, int seed) {
    uint8_t n = sorted->count;
    if (n > topn) {
	n = topn;
    }
    int v = seed;
    // take from the end (highest ranks) and build most-significant-first

    for (int k=n-1; k>=0; k--) {
	uint8_t c = sorted->cards[sorted->count - n + k]; // ascending slice of top n
	v = v * 13u + (uint32_t)RANK(c);
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

//returns the highcard in a straight, or 0 if there's no straight
//the bycicle straight returns 3, which is the code of rank 5 cards
int cg_top_straight (const CardGroup *g) {
    int bit = 0;
    for (int i=0; i<g->count ; ++i) {
	bit |= (1 << RANK(g->cards[i]));
    }
    int top = 12;
    int count = 0;
    for (int i=12; i>=0; i--) {
	if (bit & (1 << i)) {
	    if (5 == ++count) {
		return top;
	    }
	} else {
	    top = i - 1;
	    count = 0;
	}
    }
    if (count == 4 && bit & (1 << 12)) { //bycicle
	return 3;
    }
    return 0;
}

int cg_filter_flush(CardGroup *g) {
    int suit[4] = {0};
    for (int i=0; i<g->count; i++) {
	suit[SUIT(g->cards[i])]++;
    }
    for (int i=0; i<4; i++) {
	if (suit[i] >= 5) {
	    int k=0;
	    for (int j=0; j<g->count; j++) {
		if (i == SUIT(g->cards[j])) {
		    g->cards[k++] = g->cards[j];
		}
	    }
	    g->count = k;
	    return 1;
	}
    }
    g->count = 0;
    return 0;
}

void cg_filter_tuple(const CardGroup *sorted, CardGroup *dest, int wanted_count) {
    int k = 0;
    int n = sorted->count;

    for (int i = 0; i < n; ) {
        int start = i;
        int r = RANK(sorted->cards[i]);

        while (i < n && RANK(sorted->cards[i]) == r) {
            i++;
        }

        if (i - start == wanted_count) {
            dest->cards[k++] = sorted->cards[start];
        }
    }
    dest->count = k;
}

void cg_filter_highcard(const CardGroup *sorted, CardGroup *dest) {
    cg_filter_tuple (sorted, dest, 1);
}

void cg_filter_pair(const CardGroup *sorted, CardGroup *dest) {
    cg_filter_tuple (sorted, dest, 2);
}

void cg_filter_set(const CardGroup *sorted, CardGroup *dest) {
    cg_filter_tuple (sorted, dest, 3);
}

void cg_filter_quads(const CardGroup *sorted, CardGroup *dest) {
    cg_filter_tuple (sorted, dest, 4);
}


int cg_pair_score (const CardGroup *sorted) {
    CardGroup p, h;
    cg_filter_pair(sorted, &p);
    assert(p.count == 1);
    cg_filter_highcard(sorted, &h);
    return SCORE_PAIR + cg_highcard_value_base13(&h, 3, RANK(p.cards[0]));
}

int cg_two_pair_score(const CardGroup *sorted) {
    CardGroup p, h;
    cg_filter_pair(sorted, &p);
    assert(p.count >= 2 && p.count < 4);
    cg_filter_highcard(sorted, &h);

    // allow the lowest pair of the "tree pair hand" to contribute to the highcard value
    if (p.count == 3) {
	h.cards[h.count++] = p.cards[0];
	cg_sort(&h, &h); 
    }

    return SCORE_TWO_PAIR + cg_highcard_value_base13(&h, 1, cg_highcard_value_base13(&p, 2, 0)); 
}

int cg_set_score(const CardGroup *sorted) {
    CardGroup t, h;
    cg_filter_set(sorted, &t);
    assert(t.count == 1);
    cg_filter_highcard(sorted, &h);
    return SCORE_TRIPS + cg_highcard_value_base13(&h, 2, cg_highcard_value_base13(&t, 1, 0)); 
}

int cg_full_house_score(const CardGroup *sorted) {
    CardGroup t, p;
    cg_filter_set(sorted, &t);
    if (t.count == 2) {
	return SCORE_FULL_HOUSE + cg_highcard_value_base13(&t, 2, 0);
    }
    assert (t.count == 1);
    cg_filter_pair(sorted, &p);
    assert (p.count >= 1);
    return SCORE_FULL_HOUSE + cg_highcard_value_base13(&p, 1, cg_highcard_value_base13(&t, 1, 0)); 
}

int cg_quads_score(const CardGroup *sorted) {
    CardGroup q, h;
    cg_filter_quads(sorted, &q);
    assert(q.count == 1);
    cg_filter_highcard(sorted, &h);
    return SCORE_QUADS + cg_highcard_value_base13(&h, 1, cg_highcard_value_base13(&q, 1, 0)); 
}

int cg_straight_flush_score(const CardGroup *sorted) {
    int top_str = cg_top_straight(sorted);
    CardGroup flush = *sorted;
    cg_filter_flush(&flush);

    if (top_str > 0) {
	int top_str_flush = cg_top_straight (&flush);

	if (top_str_flush > 0) {
	    return SCORE_STRAIGHT_FLUSH + top_str_flush;
	}
    }
    if (flush.count >= 5) {
	return SCORE_FLUSH + cg_highcard_value_base13(&flush, 5, 0);
    }

    if (top_str > 0) {
	return SCORE_STRAIGHT + top_str;
    }
    return 0;
}

int cg_score (const CardGroup *g) {
    CardGroup sorted;
    cg_sort(g, &sorted);
    int rank_score = 0;

    int quads = cg_quads_count(&sorted);
    if (quads >= 1) {
	return cg_quads_score(&sorted); //quads excludes a straight flush in a seven card hand
    }

    int pairs = cg_pair_count(&sorted);
    int trips = cg_trips_count(&sorted);

    if (trips == 2 || (trips == 1 && pairs > 0)) {
	return cg_full_house_score(&sorted); //if full house, no straight/flush potential in seven cards
    } else if (trips == 1 && pairs == 0) {
	rank_score = cg_set_score(&sorted);
    } else if (pairs >= 2) {
	rank_score = cg_two_pair_score(&sorted);
    } else if (pairs == 1) {
	rank_score = cg_pair_score (&sorted);
    } else {
	rank_score = SCORE_HIGHCARD + cg_highcard_value_base13(&sorted, 5, 0);
    }

    int straight_flush_score = cg_straight_flush_score(&sorted);
    if (straight_flush_score > rank_score) {
	return straight_flush_score;
    } 
    return rank_score;
}

