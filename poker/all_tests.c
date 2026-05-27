#include "poker.h"

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

int test_cg_highcard_value_base13_exact(int verbose) {
    static const CGTest tests[] = {
	{ "single deuce", CG(c2c), 0},
	{ "single ace", CG(cAc), 12 * 13 * 13 * 13 * 13},
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
			     cg_highcard_value_base13,
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
int main (void) {
    test_cg_top_straight(1);
}

/* int main(void) { */

/*   int pair_ok = test_cg_pair_count(1); */
/*   int trips_ok = test_cg_trips_count(1); */
/*   int quads_ok = test_cg_quads_count(1); */
/*   int sort_ok = test_cg_sort(1); */
/*   int highcard_val_ok = test_cg_highcard_value_base13_exact(1); */

/*   TEST_OK(pair_ok); */
/*   TEST_OK(trips_ok); */
/*   TEST_OK(quads_ok); */
/*   TEST_OK(sort_ok); */
/*   TEST_OK(highcard_val_ok); */
/*   return 0; */
/* } */
