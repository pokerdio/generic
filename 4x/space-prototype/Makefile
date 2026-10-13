CC = gcc
CFLAGS = -std=c11 -O2 -Wall -Wextra 
LDLIBS = -lraylib -lGL -lm -lpthread -ldl -lrt -lX11 -lm
all: space
space: main.c
	$(CC) $(CFLAGS) -o $@ $< $(LDLIBS)
clean:
	rm -f space
.PHONY: all clean
