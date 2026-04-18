
/* ----------------- test suite ----------------- */

/*
  These tests assume the cards are already sorted by your cg_sort logic,
  i.e. increasing enum value / increasing rank.
  
  I am writing cards as raw enum-like integers:
    rank 0 suit 0 -> 0
    rank 0 suit 1 -> 1
    rank 1 suit 0 -> 4
    rank 2 suit 0 -> 8
  etc.
  
  Since cg_pair_count only uses RANK(), the exact suit values do not matter,
  as long as cards of same rank differ by 0..3 inside that rank block.
*/

static int run_one_pair_count_test(const char *name,
                                   const CardGroup *g,
                                   uint32_t expected,
                                   int verbose) {
    uint32_t actual = cg_pair_count(g);
    int pass = (actual == expected);

    if (verbose || !pass) {
        printf("%s: ", pass ? "PASS" : "FAIL");
        printf("%s\n", name);
        printf("  hand     = ");
        print_group(g);
        printf("\n");
        printf("  expected = %u\n", (unsigned)expected);
        printf("  actual   = %u\n", (unsigned)actual);
    }

    return pass;
}

void test_cg_pair_count(int verbose) {
    int total = 0;
    int passed = 0;

    CardGroup tests[] = {
        /* empty */
        { .cards = {0}, .count = 0 },

        /* one card */
        { .cards = {0}, .count = 1 },

        /* two unrelated */
        { .cards = {0, 4}, .count = 2 },   /* 2,3 */

        /* exactly one pair */
        { .cards = {0, 1}, .count = 2 },   /* 2,2 */

        /* three cards, one pair at start */
        { .cards = {0, 1, 8}, .count = 3 },   /* 2,2,4 */

        /* three cards, one pair at end */
        { .cards = {0, 4, 5}, .count = 3 },   /* 2,3,3 */

        /* trips should NOT count as one pair */
        { .cards = {0, 1, 2}, .count = 3 },   /* 2,2,2 */

        /* four distinct */
        { .cards = {0, 4, 8, 12}, .count = 4 },   /* 2,3,4,5 */

        /* one pair + kickers */
        { .cards = {0, 1, 8, 12}, .count = 4 },   /* 2,2,4,5 */

        /* two pair */
        { .cards = {0, 1, 8, 9}, .count = 4 },    /* 2,2,4,4 */

        /* trips + kicker -> 0 single pairs */
        { .cards = {0, 1, 2, 12}, .count = 4 },   /* 2,2,2,5 */

        /* quads -> 0 single pairs */
        { .cards = {0, 1, 2, 3}, .count = 4 },    /* 2,2,2,2 */

        /* full house -> should count 1 pair? no: only the pair part counts */
        { .cards = {0, 1, 2, 8, 9}, .count = 5 }, /* 2,2,2,4,4 */

        /* pair + trips -> one single pair */
        { .cards = {0, 1, 8, 9, 10}, .count = 5 }, /* 2,2,4,4,4 */

        /* two pair + kicker */
        { .cards = {0, 1, 8, 9, 16}, .count = 5 }, /* 2,2,4,4,6 */

        /* one pair only, later in hand */
        { .cards = {0, 4, 8, 9, 16}, .count = 5 }, /* 2,3,4,4,6 */

        /* three separate pairs in 6 cards */
        { .cards = {0, 1, 8, 9, 16, 17}, .count = 6 }, /* 2,2,4,4,6,6 */

        /* pair + pair + trips */
        { .cards = {0, 1, 8, 9, 16, 17, 18}, .count = 7 }, /* 2,2,4,4,6,6,6 */

        /* all distinct in 7 cards */
        { .cards = {0, 4, 8, 12, 16, 20, 24}, .count = 7 },

        /* one pair in 7 cards */
        { .cards = {0, 1, 8, 12, 16, 20, 24}, .count = 7 },

        /* two pair in 7 cards */
        { .cards = {0, 1, 8, 9, 16, 20, 24}, .count = 7 },

        /* trips + two pair-looking overlap should still be handled right */
        { .cards = {0, 1, 2, 8, 9, 16, 20}, .count = 7 }, /* 2,2,2,4,4,6,7 */

        /* full house + extra pair => two separate pairs plus trips? no:
           trips ignored, each exact pair counted */
        { .cards = {0, 1, 2, 8, 9, 16, 17}, .count = 7 }, /* 2,2,2,4,4,6,6 */

        /* quads + pair */
        { .cards = {0, 1, 2, 3, 8, 9}, .count = 6 }, /* 2,2,2,2,4,4 */
    };

    uint32_t expected[] = {
        0, /* empty */
        0, /* one card */
        0, /* two unrelated */
        1, /* exactly one pair */
        1, /* pair at start */
        1, /* pair at end */
        0, /* trips */
        0, /* four distinct */
        1, /* one pair + kicker */
        2, /* two pair */
        0, /* trips + kicker */
        0, /* quads */
        1, /* full house => one exact pair */
        1, /* pair + trips => one exact pair */
        2, /* two pair + kicker */
        1, /* one pair only */
        3, /* three separate pairs */
        2, /* pair + pair + trips */
        0, /* all distinct */
        1, /* one pair */
        2, /* two pair */
        1, /* trips + one pair */
        2, /* trips + pair + pair */
        1, /* quads + pair */
    };

    const char *names[] = {
        "empty hand",
        "single card",
        "two distinct cards",
        "one pair in two cards",
        "pair at start of three cards",
        "pair at end of three cards",
        "three of a kind",
        "four distinct cards",
        "one pair in four cards",
        "two pair in four cards",
        "trips plus kicker",
        "four of a kind",
        "full house",
        "pair plus trips",
        "two pair plus kicker",
        "single pair later in hand",
        "three separate pairs",
        "two pairs plus trips",
        "seven distinct cards",
        "one pair in seven cards",
        "two pair in seven cards",
        "trips plus one pair in seven cards",
        "trips plus two separate pairs",
        "quads plus pair"
    };

    size_t num_tests = sizeof(tests) / sizeof(tests[0]);

    for (size_t i = 0; i < num_tests; i++) {
        total++;
        if (run_one_pair_count_test(names[i], &tests[i], expected[i], verbose)) {
            passed++;
        }
    }

    printf("\nPair-count tests: %d/%d passed\n", passed, total);
}
