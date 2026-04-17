CC = gcc
CFLAGS = -Wall -Wextra -Wpedantic -g -O0
TARGET = poker

all: $(TARGET)

$(TARGET): poker.c
	$(CC) $(CFLAGS) poker.c -o $(TARGET)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)
