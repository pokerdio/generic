#include <assert.h>
#include "bitscore.h"
#include "bitworks.h"

const uint16_t bs_straights[] = {(1 << 12) + 15, 31, 31 << 1, 31 << 2, 31 << 3, 31 << 4, 31 << 5,
				 31 << 6, 31 << 7, 31 << 8};

int bs_highcard_score(uint16_t ranks, int count, int seed) {
    assert(bitcount(ranks) >= count);
    while (count-- > 0) {
	int high = msb_index(ranks);
	seed = seed * 13 + high;
	ranks ^= (1 << high);
    }
    return seed;
}


int bs_straight(uint16_t ranks) {
    for (int i=9; i>=0; i--) {
	if ((ranks & bs_straights[i]) == bs_straights[i]) {
	    return i + 3;
	}
    }
    return 0;
}

int bs_flushed_score(uint16_t flush_ranks) {
    int str = bs_straight(flush_ranks);
    if (str > 0) {
	return SCORE_STRAIGHT_FLUSH + str;
    }
    return SCORE_FLUSH + bs_highcard_score(flush_ranks, 5, 0);
}


int bs_score(BitCards hand) {
    assert(bitcount(hand.all) == 7);
    if (bitcount (hand.clubs) >= 5) {
	return bs_flushed_score (hand.clubs); // if there's a flush boats are impossible
    }
    if (bitcount (hand.diamonds) >= 5) {
	return bs_flushed_score (hand.diamonds); 
    }
    if (bitcount (hand.hearts) >= 5) {
	return bs_flushed_score (hand.hearts); 
    }
    if (bitcount (hand.spades) >= 5) {
	return bs_flushed_score (hand.spades); 
    }
    uint16_t ranks = hand.clubs | hand.diamonds | hand.hearts | hand.spades;
    
    //actually paired masks ranks that are at least paired, including trips, quads
    uint16_t paired = (hand.clubs & hand.diamonds) | (hand.clubs & hand.hearts) | (hand.clubs & hand.spades) | 
	(hand.diamonds & hand.hearts) | (hand.diamonds & hand.spades) | (hand.hearts & hand.spades); 

    if (!paired) {
	int str = bs_straight(ranks);
	if (str > 0) {
	    return SCORE_STRAIGHT + str;
	} else {
	    return SCORE_HIGHCARD + bs_highcard_score(ranks, 5, 0);
	}
    }

    //actually tripped masks ranks that are tripped or quadded
    uint16_t tripped = (hand.clubs & hand.diamonds & hand.hearts) |
	(hand.clubs & hand.diamonds & hand.spades) |
	(hand.clubs & hand.hearts & hand.spades) |
	(hand.diamonds & hand.hearts & hand.spades);

    if (!tripped) { //
	int str = bs_straight(ranks);
	if (str > 0) {
	    return SCORE_STRAIGHT + str;
	}
	int pair_count = bitcount(paired);
	if (1 == pair_count) {
	    return SCORE_PAIR + bs_highcard_score(ranks & (~paired), 3, bs_highcard_score(paired, 1, 0));
	} else if (2 == pair_count) {
	    return SCORE_TWO_PAIR + bs_highcard_score(ranks & (~paired), 1, bs_highcard_score(paired, 2, 0));
	} else { // if (3 == pair_count) {
	    int top_pair_rank = msb_index(paired);
	    int second_pair_rank = msb_index(paired & ~(1 << top_pair_rank));
	    int kicker = msb_index(ranks & ~((1 << top_pair_rank) | (1 << second_pair_rank)));
	    return SCORE_TWO_PAIR + 169 * top_pair_rank + 13 * second_pair_rank + kicker;
	}
    }
    uint16_t quadded = (hand.clubs & hand.diamonds & hand.hearts & hand.spades);

    if (quadded) {
	return SCORE_QUADS + msb_index(quadded) * 13 + msb_index(ranks & (~quadded));
    }

    int pair_count = bitcount(paired);
    if (pair_count == 1) {
	int str = bs_straight(ranks);
	if (str > 0) {
	    return SCORE_STRAIGHT + str;
	}
	return SCORE_TRIPS + bs_highcard_score(ranks & (~paired), 2, msb_index(paired));
    }

    int top_trips = msb_index(tripped);
    return SCORE_FULL_HOUSE + top_trips * 13 + msb_index(paired & ~(1 << top_trips));
}
