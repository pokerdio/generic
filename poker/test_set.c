static int run_one_trips_test(const CGTest *test, int verbose) {
    uint32_t actual = cg_trips_count(&test->group);
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

void test_cg_trips_count(int verbose) {
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

    int total = (int)(sizeof(tests) / sizeof(tests[0]));
    int passed = 0;

    for (int i = 0; i < total; i++) {
        if (run_one_trips_test(&tests[i], verbose)) {
            passed++;
        }
    }

    printf("\nTrips-count tests: %d/%d passed\n", passed, total);
}


