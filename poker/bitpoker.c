#include <assert.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#include "bitworks.h"
#include "bitscore.h"
#include "poker.h"

void CG_Random7 (CardGroup * g) {
    int last = 0;
    for (int i=0; i<7; i++) {
	int delta = (NCARDS - last - (6 - i) - 2);
	if (delta > 5) {
	    delta = rand () % delta;
	    if (delta > 5) {
		delta = rand () % delta;
	    }
	}
	int next = last + 1 + delta;
	g->cards[i] = next;
	last = next;
    }
    g->count = 7;
}

BitCards CG_to_BC (const CardGroup * g) {
    BitCards ret = {0};
    for (int i=0; i<g->count; i++) {
	ret.suits[SUIT(g->cards[i])] |= 1 << (RANK(g->cards[i]));
    }
    return ret;
}

int test_count = 0;

void test(uint8_t* cards, int n) {
    assert(n == 7);
    CardGroup c;
    c.count = n;
    for (int i=0; i<n; i++) {
	c.cards[i] = cards[i];
    }
    
    BitCards b = CG_to_BC(&c);

    int score1 = (cg_score(&c));
    int score2 = bs_score(CG_to_BC(&c));
    if (score1 != score2) {
	print_cards(c.cards, c.count);
	printf(" %d ", (bitcount(b.all)));
	bitPrint(b.all);
	printf(" %d %d\n", score1, score2);
	exit(-1);
    }
}

long int global_test_sum = 0;

void test_old(uint8_t* cards, int n) {
    assert(n == 7);
    CardGroup c;
    c.count = n;
    for (int i=0; i<n; i++) {
	c.cards[i] = cards[i];
    }
    int score1 = (cg_score(&c));
    global_test_sum += score1;
    test_count++;
    if(test_count % 1000000 == 0) {
	printf("%d\n", test_count /  1000000);
    }

}


void test_new(uint8_t* cards, int n) {
    assert(n == 7);
    CardGroup c;
    c.count = n;
    for (int i=0; i<n; i++) {
	c.cards[i] = cards[i];
    }
    
    int score2 = bs_score(CG_to_BC(&c));
    global_test_sum += score2;
    test_count++;
    if(test_count % 1000000 == 0) {
	printf("%d\n", test_count /  1000000);
    }
}


double now(void)
{
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

int main (void) {
    double a = now();
    loop_card_combo(7, 0, test_old);
    double b = now();
    loop_card_combo(7, 0, test_new);
    double c = now();
    printf("old %.3lf new %.3lf %ld\n", b - a, c - b, global_test_sum);
    return 0;
}
