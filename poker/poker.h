#ifndef poker_h__
#define poker_h__

#define SUIT(x) ((x) % 4)
#define RANK(x) (((x) / 4))


enum {
c2c, c2d, c2h, c2s, 
c3c, c3d, c3h, c3s, 
c4c, c4d, c4h, c4s, 
c5c, c5d, c5h, c5s, 
c6c, c6d, c6h, c6s, 
c7c, c7d, c7h, c7s, 
c8c, c8d, c8h, c8s, 
c9c, c9d, c9h, c9s, 
cTc, cTd, cTh, cTs, 
cJc, cJd, cJh, cJs, 
cQc, cQd, cQh, cQs, 
cKc, cKd, cKh, cKs, 
cAc, cAd, cAh, cAs, 
} card;

typedef struct {
  uint8_t cards[7];  // each is a card enum value
  uint8_t count;     // 0..7
} CardGroup;


typedef struct {
    const char *description;
    CardGroup group;
    int expected;
} CGTest;

//test entry in an array of CGTest  
#define CG(...) { .cards = { __VA_ARGS__ }, .count = sizeof((uint8_t[]){ __VA_ARGS__ }) / sizeof(uint8_t) }
#define PRINT_VAR(x) printf("%s = %d\n", #x, (x))
#define TEST_OK(x) \
    do { printf("Test %s: %s\n", #x, (x) ? "OLL KORRECT" : "FAIL"); } while (0)


#define ARRAY_SIZE(rrr) (int)(sizeof(rrr) / sizeof((rrr)[0]))

#endif 
