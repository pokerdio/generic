CC = gcc
WARN = -Wall -Wextra -Wpedantic

DEBUG_CFLAGS = $(WARN) -g -O0
PREFLOP_CFLAGS ?= $(WARN) -O3 -march=native -DNDEBUG

TEST_TARGET = poker-tests
PREFLOP_TARGET = preflop
BIT_TARGET = bit
GEN_TARGET = gen

.PHONY: all test run preflop clean

all: $(TEST_TARGET) $(PREFLOP_TARGET) $(GEN_TARGET) $(BIT_TARGET)

$(BIT_TARGET): bitpoker.c poker.c poker.h bitworks.c bitworks.h
	$(CC) $(PREFLOP_CFLAGS) bitpoker.c poker.c bitworks.c bitscore.c -o $(BIT_TARGET)

$(TEST_TARGET): all_tests.c poker.c poker.h bitworks.c bitworks.h
	$(CC) $(DEBUG_CFLAGS) all_tests.c poker.c bitworks.c -o $(TEST_TARGET)

$(PREFLOP_TARGET): preflop.c poker.c poker.h bitworks.c bitworks.h
	$(CC) $(PREFLOP_CFLAGS) preflop.c poker.c bitworks.c -o $(PREFLOP_TARGET)

$(GEN_TARGET): gen.c poker.c poker.h bitworks.c bitworks.h 
	$(CC) $(PREFLOP_CFLAGS) gen.c poker.c bitworks.c bitscore.c -o $(GEN_TARGET)


test_run: $(TEST_TARGET)
	./$(TEST_TARGET)

preflop_run: $(PREFLOP_TARGET)
	./$(PREFLOP_TARGET)

clean:
	rm -f $(TEST_TARGET) $(PREFLOP_TARGET)


# CC = gcc
# CFLAGS = -Wall -Wextra -Wpedantic -g -O0
# TARGET = poker

# all: $(TARGET)

# $(TARGET): poker.c all_tests.c poker.h
# 	$(CC) $(CFLAGS) poker.c -o $(TARGET)

# run: $(TARGET)
# 	./$(TARGET)

# clean:
# 	rm -f $(TARGET)
