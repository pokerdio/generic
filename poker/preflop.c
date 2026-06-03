#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "poker.h"
#include "bitworks.h"

#define MAX_HAND 12
int play_count = 0;
int win[MAX_HAND * 2];
float tie_equity[MAX_HAND * 2]; //I need float to differentiate between two hands tie_equitying (score 0.5) and three or more
uint8_t hands[40] = {0};
int hands_count = 0;

void hu_win_test(uint8_t* cards, int n) {
    if (n != 5) {
	printf("BAD CARD NUMBER %d - needs FLOP TURN RIVER\n", n);
	exit(-1);
    }
    CardGroup c;

    int score[MAX_HAND] = {0};
    int best_score = 0;
    int best_score_count = 0;

    memcpy(c.cards, cards, 5);
    c.count = 7;
    play_count++;

    for (int i=0; i<hands_count; i++) {
	c.cards[5] = hands[i * 2];
	c.cards[6] = hands[i * 2 + 1];
	score[i] = cg_score(&c);
	if (score[i] == best_score) {
	    best_score_count++;
	} else if (score[i] > best_score) {
	    best_score = score[i];
	    best_score_count = 1;
	}
    }
    for (int i=0; i<hands_count; i++) {
	if (score[i] == best_score) {
	    if (best_score_count == 1) {
		win[i]++;
		break;
	    }
	    tie_equity[i] += 1.0 / best_score_count;
	}
    }
}

void usage_exit (const char* msg) {
    printf("arguments fail : %s\n", msg);
    printf("correct use examples:\n");
    printf("preflop AcAd KcKd\n");
    printf("preflop ac2d 5s5c jsts TCTD\n");
    exit(-1);
}

int main(int argc, char** argv) {
    if (argc < 3 || argc > 10) {
	usage_exit("bad argument count");
    }
    for (int i=1; i<argc; i++) {
	if (parse_hand(argv[i], &hands[(i - 1) * 2]) < 0) {
	    usage_exit("bad hand format");
	}
    }
    hands_count = (argc - 1);
    
    uint64_t hands_bitmap = cards_as_bit_filter(hands, hands_count * 2);
    if (bitcount(hands_bitmap) < hands_count * 2) {
	usage_exit("duplicate cards");
    }
    loop_card_combo(5, hands_bitmap, hu_win_test);

    for (int i=0; i<hands_count; i++) {
	print_cards(hands + i * 2, 2);
	printf(" win%.3f tie_equity%.3f total equity%.3f\n", 
	       win[i] * 100.0 / play_count, tie_equity[i] * 100.0 / play_count,
	       (win[i] + tie_equity[i]) * 100.0 / play_count);
    }
}
