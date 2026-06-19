#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "poker.h"
#include "bitworks.h"

int win[13][13][13][13] = {0};
int lose[13][13][13][13] = {0};
int tie[13][13][13][13] = {0};

uint8_t hands[4];
uint8_t hands_13[4];

BitCards CG_to_BC (const CardGroup * g) {
    BitCards ret = {0};
    for (int i=0; i<g->count; i++) {
	ret.suits[SUIT(g->cards[i])] |= 1 << (RANK(g->cards[i]));
    }
    return ret;
}

void hu_win_test_bit(uint8_t* cards, int n) {
    if (n != 5) {
	printf("BAD CARD NUMBER %d - needs FLOP TURN RIVER\n", n);
	exit(-1);
    }
    CardGroup c;

    int score1, score2;

    memcpy(c.cards, cards, 5);
    c.count = 7;
    
    c.cards[5] = hands[0];
    c.cards[6] = hands[1];
    score1 = bs_score (CG_to_BC(&c));

    c.cards[5] = hands[2];
    c.cards[6] = hands[3];
    score2 = bs_score (CG_to_BC(&c));

    if (score1 > score2) {
	 win[hands_13[0]][hands_13[1]][hands_13[2]][hands_13[3]]++;
	 lose[hands_13[2]][hands_13[3]][hands_13[0]][hands_13[1]]++;
    } else if (score1 == score2) {
	 tie[hands_13[0]][hands_13[1]][hands_13[2]][hands_13[3]]++;
	 tie[hands_13[2]][hands_13[3]][hands_13[0]][hands_13[1]]++;
    } else {
	 win[hands_13[2]][hands_13[3]][hands_13[0]][hands_13[1]]++;
	 lose[hands_13[0]][hands_13[1]][hands_13[2]][hands_13[3]]++;
    }
}


void hu_win_test(uint8_t* cards, int n) {
    if (n != 5) {
	printf("BAD CARD NUMBER %d - needs FLOP TURN RIVER\n", n);
	exit(-1);
    }
    CardGroup c;

    int score1, score2;

    memcpy(c.cards, cards, 5);
    c.count = 7;
    
    c.cards[5] = hands[0];
    c.cards[6] = hands[1];
    score1 = cg_score (&c);

    c.cards[5] = hands[2];
    c.cards[6] = hands[3];
    score2 = cg_score (&c);

    if (score1 > score2) {
	 win[hands_13[0]][hands_13[1]][hands_13[2]][hands_13[3]]++;
	 lose[hands_13[2]][hands_13[3]][hands_13[0]][hands_13[1]]++;
    } else if (score1 == score2) {
	 tie[hands_13[0]][hands_13[1]][hands_13[2]][hands_13[3]]++;
	 tie[hands_13[2]][hands_13[3]][hands_13[0]][hands_13[1]]++;
    } else {
	 win[hands_13[2]][hands_13[3]][hands_13[0]][hands_13[1]]++;
	 lose[hands_13[0]][hands_13[1]][hands_13[2]][hands_13[3]]++;
    }
}

void usage_exit (const char* msg) {
    printf("arguments fail : %s\n", msg);
    printf("correct use examples:\n");
    printf("preflop AcAd KcKd\n");
    printf("preflop ac2d 5s5c jsts TCTD\n");
    exit(-1);
}

void loop_hands_all_flops (int i, int j, int k, int q) {
    hands[0] = (uint8_t) i;
    hands[1] = (uint8_t) j;
    hands[2] = (uint8_t) k;
    hands[3] = (uint8_t) q;

    if (SUIT(i) == SUIT(j) || RANK(i) == RANK(j)) {
	hands_13[0] = (uint8_t)RANK(i); //suited hands get upward order
	hands_13[1] = (uint8_t)RANK(j);
    } else {
	hands_13[0] = (uint8_t)RANK(j);//offsuit hands get downward order
	hands_13[1] = (uint8_t)RANK(i);
    }

    if (SUIT(k) == SUIT(q) || RANK(k) == RANK(q)) {
	hands_13[2] = (uint8_t)RANK(k);
	hands_13[3] = (uint8_t)RANK(q);
    } else {
	hands_13[2] = (uint8_t)RANK(q);
	hands_13[3] = (uint8_t)RANK(k);
    }

    if (k == 50 && q == 51) {
	fprintf (stderr, "%d %d\n", i, j);
    }
    BitCards forbid = {0};
    
    loop_card_combo_bit(5, UINT64_C(1) << i | UINT64_C(1) << j | 
			UINT64_C(1) << k | UINT64_C(1) << q, hu_win_test_bit);
}

void loop_hands() {
     for(int i=0; i<51; i++) {
	  for(int j=i+1; j<52; j++) {
	       for(int k=i+1; k<51; k++) {
		    if (i == k || j == k) {
			 continue;
		    }
		    for(int q=k+1; q<52; q++) {
			 if (i == q || j == q) {
			      continue;
			 }
			 loop_hands_all_flops(i, j, k, q);
		    }
	       }
	  }
     }
}

void display_data(void) {
     const char *s = "23456789TJQKA";
     for (int i=0; i<13; i++) {
	  for (int j=0; j<13; j++) {
	       for (int k=0; k<13; k++) {
		    for (int q=0; q<13; q++) {
			 printf("%c%c%s %c%c%s %d %d %d\n",
				(i>j?s[i]:s[j]), (i>j?s[j]:s[i]), (i>j?"o":(i==j?"":"s")), 
				(k>q?s[k]:s[q]), (k>q?s[q]:s[k]), (k>q?"o":(k==q?"":"s")), 
				win[i][j][k][q], lose[i][j][k][q], tie[i][j][k][q]);
		    }
	       }
	  }
     }
}

int main(void) {
    //     loop_hands();
    loop_hands_all_flops(0, 0, 12, 12);
    display_data();
    return 0;
}
