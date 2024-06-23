#include <stdio.h>
#include <stdlib.h>

#define CYCLE 100

void seekxy(double* x, double* y, double (*f)(double, double), double delta) {
    double newx, newy, newf, bestx, besty, bestf, disx, disy;
    int dx, dy; 
    disx = *x;
    disy = *y;

    for (int i=0 ; i<CYCLE ; ++i) {
        bestx = disx; 
        besty = disy;
        bestf = f(bestx, besty);

        for (dx=-1;dx<2;dx+=2) {
            for(dy=-1;dy<2;dy+=2) {
                if ((dx || dy)) {
                    newx = disx + dx * delta;
                    newy = disy + dy * delta;
                    if (newx > 0.0 && newy > 0.0) {
                        newf = f(newx, newy);
                        if (newf < bestf){
                            bestf = newf;
                            bestx = newx;
                            besty = newy;
                        }
                    }
                }
            }
        }
        disx = bestx;
        disy = besty;

        delta = delta * 0.5783429;
        printf("%.2lf %.2lf best=%.16lf delta=%.16lf \n", disx, disy, bestf, delta);
    }

    *x = bestx;
    *y = besty;
}


double tritop_base, tritop_a, tritop_b;
double tritop(double x, double y) {
    double a_delta = y * y + x * x - tritop_a * tritop_a; 
    double b_delta = y * y  + (tritop_base - x) * (tritop_base - x) - \
        tritop_b * tritop_b;
    
    return a_delta * a_delta + b_delta * b_delta;
}


void get_tritop(double *x, double *y, int ra, int rb, int rc) {
    tritop_base = rb + rc;
    tritop_a = ra + rb;
    tritop_b = ra + rc;
    *x = tritop_base / 2.0;
    *y = *x + ra / 2.0;
    seekxy(x, y, tritop, ra + rb + rc);
}


void get_dxy(double *x, double *y, double ax, double ay, int ra, int rb, int rc) {
    double 
    
}



double tri_offcenter_x1, tri_offcenter_y1; 
double tri_offcenter_x2, tri_offcenter_y2;
double tri_offcenter_x3, tri_offcenter_y3;

double tri_offcenter(double x, double y) {
    double x1 = tri_offcenter_x1;
    double y1 = tri_offcenter_y1;
    double x2 = tri_offcenter_x2;
    double y2 = tri_offcenter_y2;
    double x3 = tri_offcenter_x3;
    double y3 = tri_offcenter_y3;

    return (x - x1) * (x - x1) + (y - y1) * (y - y1) +  \
        (x - x2) * (x - x2) + (y - y2) * (y - y2) + \
        (x - x3) * (x - x3) + (y - y3) * (y - y3);
}

void tri_center(double x1, double y1, double x2, double y2, double x3, double y3) {
    double x = (x1 + x2 + x3) / 3.0;
    double y = (y1 + y2 + y3) / 3.0;
    tri_offcenter_x1 = x1;
    tri_offcenter_y1 = y1;
    tri_offcenter_x2 = x2;
    tri_offcenter_y2 = y2;
    tri_offcenter_x3 = x3;
    tri_offcenter_y3 = y3;
    


    
}

void main(void) {
    double x, y;
    get_tritop(&x, &y, 1, 1, 1);
    printf("foo bar baz %.2lf %.2lf\n", x, y);
}
