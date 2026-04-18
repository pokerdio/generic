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
    uint32_t expected;
} CGTest;

//test entry in an array of CGTest  
#define CG(...) { .cards = { __VA_ARGS__ }, .count = sizeof((uint8_t[]){ __VA_ARGS__ }) / sizeof(uint8_t) }


#endif 
