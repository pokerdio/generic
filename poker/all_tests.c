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


int main(void) {
  int pair_ok = test_cg_pair_count(1); 
  int trips_ok = test_cg_trips_count(1);
  int quads_ok = test_cg_quads_count(1);

  TEST_OK(pair_ok);
  TEST_OK(trips_ok);
  TEST_OK(quads_ok);

  return 0;
}
