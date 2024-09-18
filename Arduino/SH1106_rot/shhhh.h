//#define ROUND

#ifndef ROUND
#define SQUARE
#endif

#ifdef ROUND
#define ROT_A D2 //DT
#define ROT_B D1 //CLK
#define ROT_C D4 //MS
#endif

#ifdef SQUARE
#define ROT_A D1 //DT
#define ROT_B D2 //CLK
#define ROT_C D4 //MS
#define HALF_STEP
#endif
