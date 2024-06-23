#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define N 500050

typedef struct Point {
	char type; 
	int x;
	int y;
} Point;

Point xy[N];
Point white_king; 
int nblack;

int manhattan(Point * p) {
	return abs(p->x - white_king.x) + abs(p->y - white_king.y);
}

int maxdelta(Point *p) {
	int dx = abs(p->x - white_king.x);
	int dy = abs(p->y - white_king.y);
	if (dx > dy) {
		return dx;
	} else {
		return dy;
	}
}

int compare(const void * a, const void * b) {
	int va = maxdelta((Point*)a);
	int vb = maxdelta((Point*)b);
	return va - vb;
}

void print_points(void) {
	for (int i=0 ; i<nblack ; ++i) {
		printf("point %d %c %d %d\n", i, xy[i].type, xy[i].x, xy[i].y);
	}
}

int main(int argc, char* argv[]) {
	int diagpp = 1;
	int diagpm = 1;
	int diagmp = 1;
	int diagmm = 1;
	int vertp=1,vertm=1;
	int horizp=1,horizm=1;


	int dx, dy; 

	scanf("%d\n", &nblack);
	scanf("%d %d\n", &white_king.x, &white_king.y);

	assert(N > nblack);

	for (int i=0 ; i<nblack ; ++i) {
		scanf("%c %d %d\n", &xy[i].type, &xy[i].x, &xy[i].y);
	}
	//print_points();
	qsort(xy, nblack, sizeof(Point), compare);
	//print_points();
	for (int i=0; i<nblack ; ++i) {
		dx = xy[i].x - white_king.x;
		dy = xy[i].y - white_king.y;
		if (abs(dx) == abs(dy)) {
			if (dx < 0 && dy < 0) {
				if (diagmm && (xy[i].type == 'B' || xy[i].type=='Q')) {
					printf("YES\n");
					exit(0);
				}
				diagmm = 0;
			}
			if (dx > 0 && dy < 0) {
				if (diagpm && (xy[i].type == 'B' || xy[i].type=='Q')) {
					printf("YES\n");
					exit(0);
				}
				diagpm = 0;
			}
			if (dx < 0 && dy > 0) {
				if (diagmp && (xy[i].type == 'B' || xy[i].type=='Q')) {
					printf("YES\n");
					exit(0);
				}
				diagmp = 0;
			}
			if (dx > 0 && dy > 0) {
				if (diagpp && (xy[i].type == 'B' || xy[i].type=='Q')) {
					printf("YES\n");
					exit(0);
				}
				diagpp = 0;
			}
		}
		if (dx == 0) {
			if (dy < 0) {
				if (vertm && (xy[i].type == 'R' || xy[i].type=='Q')) {
					printf("YES\n");
					exit(0);
				}
				vertm = 0;
			}
			if (dy > 0) {
				if (vertp && (xy[i].type == 'R' || xy[i].type=='Q')) {
					printf("YES\n");
					exit(0);
				}
				vertp = 0;
			}
		}
		if (dy == 0) {
			if (dx < 0) {
				if (horizm && (xy[i].type == 'R' || xy[i].type=='Q')) {
					printf("YES\n");
					exit(0);
				}
				horizm = 0;
			}
			if (dx > 0) {
				if (horizp && (xy[i].type == 'R' || xy[i].type=='Q')) {
					printf("YES\n");
					exit(0);
				}
				horizp = 0;
			}
		}
	}
	printf("NO\n");
}
