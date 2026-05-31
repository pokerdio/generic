#include <stdint.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

#include "poker.h"


static void print_group(const CardGroup *g) {
    printf("{ count=%u, ranks=[", (unsigned)g->count);
    for (uint8_t i = 0; i < g->count; i++) {
        if (i) printf(" ");
        printf("%u", (unsigned)RANK(g->cards[i]));
    }
    printf("] }");
}


static int run_one_cg_filter_test(const CGFilterTest *test, void (*f) (const CardGroup *, CardGroup*), int verbose) {
    CardGroup src;
    CardGroup dest;
    cg_sort(&test->input, &src);
    f(&src, &dest);
    int pass = cg_same_cards(&dest, &test->expected);

    if (verbose || !pass) {
        printf("%s: %s\n", pass ? "PASS" : "FAIL", test->description);
        printf("  hand     = ");
        print_group(&test->input);
        printf("\n");
	printf("  expected = ");
	print_group(&test->expected);
        printf("  actual   = ");
	print_group(&dest);
	printf("\n");
    }

    return pass;
}

static int run_one_cg_test(const CGTest *test, int (*f) (const CardGroup *), int verbose) {
    int actual = f(&test->group);
    int pass = (actual == test->expected);

    if (verbose || !pass) {
        printf("%s: %s\n", pass ? "PASS" : "FAIL", test->description);
        printf("  hand     = ");
        print_group(&test->group);
        printf("\n");
        printf("  expected = %u\n", (unsigned)test->expected);
        printf("  actual   = %u\n", (unsigned)actual);
    }

    return pass;
}

int run_many_cg_tests(int verbose, const CGTest tests[], int total, int (*f) (const CardGroup *), const char* msg) {
    int passed = 0;

    for (int i = 0; i < total; i++) {
	if (run_one_cg_test(&tests[i], f, verbose)) {
	    passed++;
	}
    }
    printf("\n%s: %d/%d passed\n", msg, passed, total);
    return passed == total;
}

int run_many_cg_filter_tests(int verbose, const CGFilterTest tests[], int total, 
			     void (*f) (const CardGroup *, CardGroup *), const char* msg) {
    int passed = 0;

    for (int i = 0; i < total; i++) {
	if (run_one_cg_filter_test(&tests[i], f, verbose)) {
	    passed++;
	}
    }
    printf("\n%s: %d/%d passed\n", msg, passed, total);
    return passed == total;
}


int test_cg_pair_count(int verbose) {
  static const CGTest tests[] = {
    {"single card", CG(0), 0},
    {"two distinct cards", CG(0, 4), 0},
    {"one pair", CG(0, 1), 1},

    {"pair at start of three cards", CG(0, 1, 8), 1},
    {"pair at end of three cards", CG(0, 4, 5), 1},
    {"three of a kind", CG(0, 1, 2), 0},
    {"three distinct cards", CG(0, 4, 8), 0},

    {"four distinct cards", CG(0, 4, 8, 12), 0},
    {"one pair in four cards", CG(0, 1, 8, 12), 1},
    {"two pair in four cards", CG(0, 1, 8, 9), 2},
    {"trips plus kicker", CG(0, 1, 2, 12), 0},
    {"quads", CG(0, 1, 2, 3), 0},

    {"one pair plus kickers", CG(0, 1, 8, 12, 16), 1},
    {"two pair plus kicker", CG(0, 1, 8, 9, 16), 2},
    {"trips plus pair (full house)", CG(0, 1, 2, 8, 9), 1},
    {"pair plus trips", CG(0, 1, 8, 9, 10), 1},
    {"all distinct in five cards", CG(0, 4, 8, 12, 16), 0},

    {"three separate pairs in six cards", CG(0, 1, 8, 9, 16, 17), 3},
    {"quads plus pair in six cards", CG(0, 1, 2, 3, 8, 9), 1},
    {"trips plus pair plus kicker", CG(0, 1, 2, 8, 9, 16), 1},
    {"all distinct in six cards", CG(0, 4, 8, 12, 16, 20), 0},

    {"seven distinct cards", CG(0, 4, 8, 12, 16, 20, 24), 0},
    {"one pair in seven cards", CG(0, 1, 8, 12, 16, 20, 24), 1},
    {"two pair in seven cards", CG(0, 1, 8, 9, 16, 20, 24), 2},
    {"three separate pairs in seven cards", CG(0, 1, 8, 9, 16, 17, 24), 3},
    {"trips plus one pair in seven cards", CG(0, 1, 2, 8, 9, 16, 20), 1},
    {"trips plus two pairs in seven cards", CG(0, 1, 2, 8, 9, 16, 17), 2},
    {"quads plus pair in seven cards", CG(0, 1, 2, 3, 8, 9, 16), 1},
    {"quads plus trips in seven cards", CG(0, 1, 2, 3, 8, 9, 10), 0},
    {"one trips in seven cards", CG(0, 1, 2, 8, 12, 16, 20), 0}
  };
  return run_many_cg_tests(verbose, tests, ARRAY_SIZE(tests), cg_pair_count, "Pair count test");
}


int test_cg_trips_count(int verbose) {
  static const CGTest tests[] = {
    {"single card", CG (0), 0},
    {"two distinct cards", CG (0, 4), 0},
    {"one pair", CG (0, 1), 0},
    {"three of a kind (2s)", CG (0, 1, 2), 1},
    {"three of a kind (3s)", CG (4, 5, 6), 1},
    {"pair plus kicker", CG (0, 1, 4), 0},
    {"three distinct cards", CG (0, 4, 8), 0},
    {"pair plus two kickers", CG (0, 1, 4, 8), 0},
    {"four distinct cards", CG (0, 4, 8, 12), 0},
    {"two pair in four cards", CG (0, 1, 8, 9), 0},
    {"trips plus kicker", CG (0, 1, 2, 12), 1},
    {"trips plus two kickers", CG (0, 1, 2, 12, 16), 1},
    {"full house (trips plus pair)", CG (0, 1, 2, 12, 13), 1},
    {"trips plus pair plus kicker", CG (0, 1, 2, 12, 13, 16), 1},
    {"quads only", CG (0, 1, 2, 3), 0},
    {"quads plus kicker", CG (0, 1, 2, 3, 12), 0},
    {"quads plus pair", CG (0, 1, 2, 3, 12, 13), 0},
    {"two separate trips in six cards", CG (0, 1, 2, 4, 5, 6), 2},
    {"two separate trips in six cards, higher ranks", CG (0, 1, 2, 8, 9, 10), 2},
    {"two trips plus kicker in seven cards", CG (0, 1, 2, 8, 9, 10, 16), 2},
    {"trips plus quads", CG (0, 1, 2, 8, 9, 10, 11), 1},
    {"quads plus trips", CG (0, 1, 2, 3, 8, 9, 10), 1},
    {"one trips in seven cards", CG (0, 1, 2, 8, 12, 16, 20), 1},
    {"two pair in seven cards", CG (0, 1, 8, 9, 12, 16, 20), 0},
    {"seven distinct cards", CG (0, 4, 8, 12, 16, 20, 24), 0}
  };
  return run_many_cg_tests(verbose, tests, ARRAY_SIZE(tests), cg_trips_count, "Trips count test");
}

int test_cg_quads_count(int verbose) {
    static const CGTest tests[] = {
	{"single card", CG(0), 0},
	{"two cards", CG(0, 1), 0},
	{"three cards", CG(0, 1, 2), 0},

	{"four distinct cards", CG(0, 4, 8, 12), 0},
	{"one pair", CG(0, 1, 8, 12), 0},
	{"two pair", CG(0, 1, 8, 9), 0},
	{"trips", CG(0, 1, 2, 12), 0},

	{"exact quads", CG(0, 1, 2, 3), 1},

	{"quads + kicker", CG(0, 1, 2, 3, 12), 1},
	{"quads + two kickers", CG(0, 1, 2, 3, 12, 16), 1},
	{"quads + three kickers", CG(0, 1, 2, 3, 12, 16, 20), 1},

	{"trips + pair", CG(0, 1, 2, 8, 9), 0},
	{"two trips", CG(0, 1, 2, 8, 9, 10), 0},

	{"quads + pair", CG(0, 1, 2, 3, 8, 9), 1},
	{"quads + trips", CG(0, 1, 2, 3, 8, 9, 10), 1},

	{"no quads in 7 cards", CG(0, 1, 8, 9, 16, 17, 24), 0}
    };

    return run_many_cg_tests(verbose, tests, ARRAY_SIZE(tests), cg_quads_count, "Quads count test");
}

int cg_highcard_value_test_5 (const CardGroup *cg) {
    return cg_highcard_value_base13(cg, 5, 0);
}

int test_cg_highcard_value_base13_exact(int verbose) {
    static const CGTest tests[] = {
	{ "single deuce", CG(c2c), 0},
	{ "single ace", CG(cAc), 12},
	{ "five lowest cards", CG(c2c, c3c, c4c, c5c, c6c), ((((4 * 13 + 3) * 13 + 2) * 13 + 1) * 13 + 0) },
	{ "broadway high-card encoding", CG(cTc, cJc, cQc, cKc, cAc), 
	  ((((12 * 13 + 11) * 13 + 10) * 13 + 9) * 13 + 8) },
	{ "three high two low", CG(c2c, c3c, cQc, cKc, cAc), 
	  ((((12 * 13 + 11) * 13 + 10) * 13 + 1) * 13 + 0) },
	{ "seven cards uses top five only", CG(c2c, c3c, c4c, c9c, cTc, cJc, cAc), 
	  ((((12 * 13 + 9) * 13 + 8) * 13 + 7) * 13 + 2) },
	{ "seven cards uses top five only", CG(c2h, c3c, c4d, c7c, cTc, cJc, cKd),
	    ((((11 * 13 + 9) * 13 + 8) * 13 + 5) * 13 + 2) }
    };

    return run_many_cg_tests(verbose, tests, ARRAY_SIZE(tests),
			     cg_highcard_value_test_5,
			     "High-card base-13 exact value test");
}

int cg_sort_test_value(const CardGroup *g) {
    CardGroup sorted;
    cg_sort(g, &sorted);
  
    if (sorted.count != g->count) {
	return 0;
    }

    int ret = 1;
    for (int i = 0; i + 1 < sorted.count; i++) {
	if (sorted.cards[i] > sorted.cards[i + 1]) {
	    ret = 0;
	}
    }
    for (int i = 0; i<g->count; i++) {
	int ok = 0;
	for (int j = 0; j<g->count; j++) {
	    if (g->cards[i] == sorted.cards[j]) {
		ok = 1;
		break;
	    }
	}
	if (!ok) {
	    return 0;
	}
    }
    return ret;
}

int test_cg_sort(int verbose) {
    static const CGTest tests[] = {
	{"single card", CG(c2c), 1},

	{"two cards already sorted", CG(c2c, c3c), 1},
	{"two cards reversed", CG(c3c, c2c), 1},

	{"three cards already sorted", CG(c2c, c3c, c4c), 1},
	{"three cards reversed", CG(c4c, c3c, c2c), 1},
	{"three cards broken old bubble case", CG(c4c, c3c, c2c), 1},
	{"three cards middle disorder", CG(c2c, c4c, c3c), 1},

	{"seven cards already sorted", CG(c2c, c3c, c4c, c5c, c6c, c7c, c8c), 1},
	{"seven cards reversed", CG(c8c, c7c, c6c, c5c, c4c, c3c, c2c), 1},
	{"seven cards random order", CG(cAc, c2c, cTc, c5c, cKc, c3c, c8c), 1},

	{"same ranks different suits scrambled", CG(c2s, c2c, c2h, c2d), 1},
	{"mixed ranks and suits scrambled", CG(cAh, c2d, cTc, c5s, cKd, c3h, c8c), 1},

	{"duplicates by rank but distinct cards", CG(c5s, c2c, c5c, cAc, c2h, cTd, c5d), 1}
    };

    return run_many_cg_tests(verbose, tests, ARRAY_SIZE(tests),
			     cg_sort_test_value, "Sort test");
}


int test_cg_tuple_filters(int verbose) {
    int ret = 1;

    static const CGFilterTest highcard_tests[] = {
	{"empty", CG0(), CG0()},
        {"single card", CG(cAc), CG(cAc)},
        {"all highcards", CG(cAc, cKc, cQs), CG(cQs, cKc, cAc)},
        {"one pair removed", CG(cAc, cKc, cAs), CG(cKc)},
        {"two pair removed", CG(cAc, cAs, cKc, cKs, cQc), CG(cQc)},
        {"set removed", CG(cAc, cAs, cAd, cKc), CG(cKc)},
        {"quads removed", CG(cAc, cAs, cAd, cAh, cKc), CG(cKc)},
        {"mixed singles pairs set", CG(c2c, c2d, c3c, c4c, c4d, c4h, cAc),
         CG(c3c, cAc)},
        {"seven all distinct scrambled", CG(cAc, c2c, cKc, c3d, cQs, c7h, c9c),
         CG(c2c, c3d, c7h, c9c, cQs, cKc, cAc)}
    };

    static const CGFilterTest pair_tests[] = {
	{"empty", CG0(), CG0()},
        {"single card", CG(cAc), CG0()},
        {"no pair", CG(cAc, cKc, cQs), CG0()},
        {"one pair", CG(cAc, cAs, cKc), CG(cAc)},
        {"two pair", CG(cAc, cAs, cKc, cKs, cQc), CG(cKc, cAc)},
        {"three pair", CG(cAc, cAs, cKc, cKs, cQc, cQs), CG(cQc, cKc, cAc)},
        {"set ignored", CG(cAc, cAs, cAd, cKc), CG0()},
        {"quads ignored", CG(cAc, cAs, cAd, cAh, cKc), CG0()},
        {"pair plus set", CG(cAc, cAs, cAd, cKc, cKs), CG(cKc)},
        {"pair plus quads", CG(cAc, cAs, cAd, cAh, cKc, cKs), CG(cKc)},
        {"seven cards pair extraction", CG(c2c, c2d, c3c, c4c, c4d, c4h, cAc),
         CG(c2c)}
    };

    static const CGFilterTest set_tests[] = {
	{"empty", CG0(), CG0()},
        {"single card", CG(cAc), CG0()},
        {"no set", CG(cAc, cKc, cQs), CG0()},
        {"pair ignored", CG(cAc, cAs, cKc), CG0()},
        {"one set", CG(cAc, cAs, cAd, cKc), CG(cAc)},
        {"two sets", CG(cAc, cAs, cAd, cKc, cKs, cKd), CG(cKc, cAc)},
        {"quads ignored", CG(cAc, cAs, cAd, cAh, cKc), CG0()},
        {"set plus pair", CG(cAc, cAs, cAd, cKc, cKs), CG(cAc)},
        {"set plus quads", CG(cAc, cAs, cAd, cKc, cKs, cKd, cKh), CG(cAc)},
        {"seven cards mixed", CG(c2c, c2d, c2h, c4c, c4d, cAc, cKs),
         CG(c2c)}
    };

    static const CGFilterTest quad_tests[] = {
	{"empty", CG0(), CG0()},
        {"single card", CG(cAc), CG0()},
        {"no quads", CG(cAc, cKc, cQs), CG0()},
        {"pair ignored", CG(cAc, cAs, cKc), CG0()},
        {"set ignored", CG(cAc, cAs, cAd, cKc), CG0()},
        {"one quads", CG(cAc, cAs, cAd, cAh, cKc), CG(cAc)},
        {"quads plus pair", CG(cAc, cAs, cAd, cAh, cKc, cKs), CG(cAc)},
        {"quads plus set", CG(cAc, cAs, cAd, cAh, cKc, cKs, cKd), CG(cAc)},
        {"low quads", CG(c2c, c2d, c2h, c2s, cAc), CG(c2c)}
    };

    ret = ret && run_many_cg_filter_tests(verbose, highcard_tests,
                                          ARRAY_SIZE(highcard_tests),
                                          cg_filter_highcard,
                                          "Filter highcard test");

    ret = ret && run_many_cg_filter_tests(verbose, pair_tests,
                                          ARRAY_SIZE(pair_tests),
                                          cg_filter_pair,
                                          "Filter pair test");

    ret = ret && run_many_cg_filter_tests(verbose, set_tests,
                                          ARRAY_SIZE(set_tests),
                                          cg_filter_set,
                                          "Filter set test");

    ret = ret && run_many_cg_filter_tests(verbose, quad_tests,
                                          ARRAY_SIZE(quad_tests),
                                          cg_filter_quads,
                                          "Filter quads test");

    return ret;
}


int test_cg_top_straight(int verbose) {
    static const CGTest tests[] = {
	{"single card", CG(cAc), 0},
	{"four cards no straight yet", CG(c2c, c3c, c4c, c5c), 0},

	{"lowest non-wheel straight 23456", CG(c2c, c3d, c4h, c5s, c6c), 4},
	{"wheel straight A2345", CG(cAc, c2c, c3d, c4h, c5s), 3},
	{"broadway straight TJQKA", CG(cTc, cJd, cQh, cKs, cAc), 12},
	{"king-high straight 9TJQK", CG(c9c, cTd, cJh, cQs, cKc), 11},
	{"queen-high straight 89TJQ", CG(c8c, c9d, cTh, cJs, cQc), 10},

	{"no straight with gap", CG(c2c, c3d, c4h, c6s, c7c), 0},
	{"no straight with four-run plus ace", CG(cAc, c2c, c3d, c4h, c6s), 0},
	{"ace is not low without 2345", CG(cAc, c2c, c3d, c4h, cKs), 0},

	{"duplicates do not fake straight", CG(c2c, c2d, c3c, c4c, c5c), 0},
	{"pairs inside real straight", CG(c2c, c2d, c3c, c4c, c5c, c6c), 4},

	{"seven cards finds straight", CG(c2c, c3d, c4h, c5s, c6c, c9c, cAc), 4},
	{"seven cards chooses highest straight", CG(c2c, c3d, c4h, c5s, c6c, c7d, c8h), 6},
	{"seven cards wheel plus higher straight chooses higher", CG(cAc, c2c, c3d, c4h, c5s, c6c, c7c), 5},

	{"scrambled broadway", CG(cAc, cQc, cTc, cKc, cJc), 12},
	{"scrambled seven-card straight", CG(c9c, c2c, c6c, c5c, c3c, c4c, cAc), 4}
    };

    return run_many_cg_tests(verbose, tests, ARRAY_SIZE(tests),
			     cg_top_straight,
			     "Top straight test");
}

void print_base_13(int score) {
    if (score > 13) {
	print_base_13(score / 13);
    }
    printf ("%d ", score % 13);
}

void print_score (const char* prefix, int score) {
    int m = score / 1000000;
    int remainder = score % 1000000;
    printf ("%s %d -- %dM %d -- ", prefix, score, m, remainder);
    print_base_13 (remainder);
    printf ("\n");
}

int test_get_hand_score(const CardGroup *hand, int verbose) {
    int score = cg_score (hand);
    if (verbose) {
	printf ("SCORE FOR: ");
	print_group(hand);
	print_score ("  - ", score);
    }
    return score;
}

int test_cg_score(int verbose) {
    const CardGroup test[] = {
        /* high card */
        CG(c2c, c4d, c6h, c8s, cTc),
        CG(c2c, c4d, c6h, c8s, cJc),
        CG(c2c, c4d, c6h, c9s, cJc),
        CG(c2c, c4d, c7h, c9s, cJc),
        CG(c2c, c5d, c7h, c9s, cJc),
        CG(c3c, c5d, c7h, c9s, cJc),
        CG(cAc, cKc, cQc, c9d, c7h),

        /* one pair */
        CG(c2c, c2d, c4h, c6s, c8c),
        CG(c2c, c2d, c4h, c6s, c9c),
        CG(c2c, c2d, c4h, c7s, c9c),
        CG(c2c, c2d, c5h, c7s, c9c),
        CG(c3c, c3d, c2h, c4s, c6c),
        CG(cAc, cAd, cKc, cQc, cJd),

        /* two pair */
        CG(c2c, c2d, c3c, c3d, c4h),
        CG(c2c, c2d, c3c, c3d, c5h),
        CG(c2c, c2d, c4c, c4d, c3h),
        CG(c3c, c3d, c4c, c4d, c2h),

        /* three pair: should count as best two pair plus kicker */
        CG(c2c, c2d, c3c, c3d, c4c, c4d, c5h),
        CG(c2c, c2d, c3c, c3d, c5c, c5d, c4h),

        /* more two pair */	
        CG(cAc, cAd, cKc, cKd, c2h),
        CG(cAc, cAd, cKc, cKd, cQh),


        /* trips */
        CG(c2c, c2d, c2h, c4s, c6c),
        CG(c2c, c2d, c2h, c4s, c7c),
        CG(c2c, c2d, c2h, c5s, c7c),
        CG(c3c, c3d, c3h, c2s, c4c),
        CG(cAc, cAd, cAh, cKc, cQc),

        /* straights */
        CG(cAc, c2d, c3h, c4s, c5c), /* wheel */
        CG(c2c, c3d, c4h, c5s, c6c),
        CG(c3c, c4d, c5h, c6s, c7c),
        CG(c9c, cTd, cJh, cQs, cKc),
        CG(cTc, cJd, cQh, cKs, cAc),

        /* flushes */
        CG(c2c, c4c, c6c, c8c, cTc),
        CG(c2c, c4c, c6c, c8c, cJc),
        CG(c2c, c4c, c6c, c9c, cJc),
        CG(cAc, cKc, cQc, c9c, c7c),

        /* full houses */
        CG(c2c, c2d, c2h, c3c, c3d),
        CG(c2c, c2d, c2h, c4c, c4d),
        CG(c3c, c3d, c3h, c2c, c2d),
        CG(cTc, cTd, cTh, cKc, cKd),

        /* double trips: should use higher trips as trips, lower trips as pair */
        CG(c2c, c2d, c2h, cQc, cQd, cQh),
        CG(cKc, cKd, c4c, cKh, c4d, c4h),

        /* quads */
        CG(c2c, c2d, c2h, c2s, c3c),
        CG(c2c, c2d, c2h, c2s, cAc),
        CG(c3c, c3d, c3h, c3s, c2c),
        CG(cAc, cAd, cAh, cAs, cKc),

        /* straight flushes */
        CG(cAc, c2c, c3c, c4c, c5c),
        CG(c2c, c3c, c4c, c5c, c6c),
        CG(c3c, c4c, c5c, c6c, c7c),
        CG(c9c, cTc, cJc, cQc, cKc),
        CG(cTc, cJc, cQc, cKc, cAc)
    };
    test_get_hand_score(&test[12], 1);

    int n = ARRAY_SIZE(test);
    int okay = 0;
    int last_score = test_get_hand_score(&test[0], verbose);
    for (int i=1; i<n; i++) {
	int new_score = test_get_hand_score(&test[i], verbose);
	if (new_score >= last_score) {
	    okay++;
	} else {
	    printf ("FAIL --- DESCENDING SCORE DETECTED --- FAIL\n");
	}
	last_score = new_score;
    }
    printf ("CORRECT SORT ORDER %d/%d\n", okay, n-1);
    return okay == n - 1;
}


int main(void) {
    int pair_ok = test_cg_pair_count(1);
    int trips_ok = test_cg_trips_count(1);
    int quads_ok = test_cg_quads_count(1);
    int sort_ok = test_cg_sort(1);
    int highcard_val_ok = test_cg_highcard_value_base13_exact(1);
    int tuple_filter_ok = test_cg_tuple_filters(1);
    int score_ok = test_cg_score(1);
    TEST_OK(pair_ok);
    TEST_OK(trips_ok);
    TEST_OK(quads_ok);
    TEST_OK(sort_ok);
    TEST_OK(highcard_val_ok);
    TEST_OK(tuple_filter_ok);
    TEST_OK(score_ok);
    return 0;
}
