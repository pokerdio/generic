#include "raylib.h"
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 10000
#define MAX_NAME 40
#define INPUT_MAX 256
#define ROW_H 19
#define PANEL 590

typedef struct { float x,y,t,m; char name[MAX_NAME]; bool selected; } Planet;
typedef struct { float x0,y0,x1,y1; } Rect;
static Planet planets[N];
static int order[N], count_selected=N;
static Rect view={-1,-1,1,1};
static char command[INPUT_MAX]="", status[256]="Type a sector, a resource filter, z SECTOR, or d ...";
static int input_len=0, sort_key=0, sort_reverse=0;
static double anchor=0; // 0 = first row at top; 1 = last row at bottom
static uint32_t rng=0x12345678;
static uint32_t random32(void) { rng ^= rng<<13; rng ^= rng>>17; rng ^= rng<<5; return rng; }
static double uniform(void) { return ((double)random32()+0.5)/4294967296.0; }
static float position(void) { double v=2*uniform()-1; return (float)copysign(pow(fabs(v),1.3),v); }
static float resource(void) { return (float)-log10(uniform()); }
static int cmp(const void *a,const void *b) {
    const Planet *p=&planets[*(const int*)a], *q=&planets[*(const int*)b];
    int r=0;
    if(sort_key==0) r=strcmp(p->name,q->name);
    else { float x=sort_key==1?p->t:sort_key==2?p->m:sort_key==3?p->x:p->y;
           float y=sort_key==1?q->t:sort_key==2?q->m:sort_key==3?q->x:q->y;
           r=(x>y)-(x<y); }
    return sort_reverse?-r:r;
}
static void rebuild(void) {
    count_selected=0;
    for(int i=0;i<N;i++) if(planets[i].selected) order[count_selected++]=i;
    qsort(order,count_selected,sizeof(int),cmp);
}
static int coord_index(float v,float lo,float hi) {
    int k=(int)floorf(8*(v-lo)/(hi-lo));
    return k<0?0:k>7?7:k;
}
static void name_group(int *ids,int n,Rect r,const char *prefix,int depth) {
    if(n<10 || depth>=12) {
        for(int j=0;j<n;j++) {
            // A suffix is needed for both two-planet and larger leaf cells to keep names unique.
            if(n==1) snprintf(planets[ids[j]].name,MAX_NAME,"%s",prefix);
            else snprintf(planets[ids[j]].name,MAX_NAME,"%s%d",prefix,j+1);
        }
        return;
    }
    int bins[64]={0};
    for(int j=0;j<n;j++) {
        Planet *p=&planets[ids[j]];
        int x=coord_index(p->x,r.x0,r.x1), y=coord_index(p->y,r.y0,r.y1);
        bins[y*8+x]++;
    }
    int starts[64],at[64],total=0;
    for(int b=0;b<64;b++) { starts[b]=at[b]=total; total+=bins[b]; }
    int *tmp=malloc((size_t)n*sizeof(int));
    if(!tmp) { fprintf(stderr,"Out of memory\n"); exit(1); }
    for(int j=0;j<n;j++) {
        Planet *p=&planets[ids[j]];
        int x=coord_index(p->x,r.x0,r.x1), y=coord_index(p->y,r.y0,r.y1);
        tmp[at[y*8+x]++]=ids[j];
    }
    float w=(r.x1-r.x0)/8, h=(r.y1-r.y0)/8;
    for(int b=0;b<64;b++) if(bins[b]) {
        int x=b%8,y=b/8;
        char next[MAX_NAME]; snprintf(next,sizeof(next),"%s%c%c",prefix,'A'+x,'J'+y);
        Rect sub={r.x0+x*w,r.y0+y*h,r.x0+(x+1)*w,r.y0+(y+1)*h};
        name_group(tmp+starts[b],bins[b],sub,next,depth+1);
    }
    free(tmp);
}
static void generate(void) {
    int ids[N];
    for(int i=0;i<N;i++) {
        planets[i]=(Planet){.x=position(),.y=position(),.t=resource(),.m=resource(),.selected=true};
        ids[i]=i;
    }
    name_group(ids,N,(Rect){-1,-1,1,1},"",0);
    rebuild();
}
static bool sector_bounds(const char *s,Rect *out) {
    size_t len=strlen(s);
    if(len<1 || len>24) return false;
    // A single column (A-H) is a full-height strip. Complete pairs subdivide 8x8.
    Rect r={-1,-1,1,1};
    for(size_t i=0;i<len;) {
        char x=toupper((unsigned char)s[i++]);
        if(x<'A'||x>'H') return false;
        float w=(r.x1-r.x0)/8;
        float left=r.x0+(x-'A')*w; r.x0=left; r.x1=left+w;
        if(i==len) break;
        char y=toupper((unsigned char)s[i++]);
        if(y<'J'||y>'Q') return false;
        float h=(r.y1-r.y0)/8;
        float bottom=r.y0+(y-'J')*h; r.y0=bottom; r.y1=bottom+h;
    }
    *out=r; return true;
}
static bool area_bounds(const char *s,Rect *out) {
    char copy[100]; if(strlen(s)>=sizeof(copy)) return false;
    strcpy(copy,s);
    char *dash=strchr(copy,'-');
    if(!dash) return sector_bounds(copy,out);
    *dash=0;
    Rect a,b;
    if(!sector_bounds(copy,&a)||!sector_bounds(dash+1,&b)) return false;
    *out=(Rect){fminf(a.x0,b.x0),fminf(a.y0,b.y0),fmaxf(a.x1,b.x1),fmaxf(a.y1,b.y1)};
    return true;
}
static bool matches(int i,const char *expr,bool *valid) {
    Rect r;
    if(area_bounds(expr,&r)) {
        Planet *p=&planets[i];
        return p->x>=r.x0&&p->x<=r.x1&&p->y>=r.y0&&p->y<=r.y1;
    }
    char field,op; float v; int used=0;
    if(sscanf(expr," %c %c %f %n",&field,&op,&v,&used)==3 && used==(int)strlen(expr)
       && (op=='>'||op=='<') && (field=='t'||field=='m'||field=='x'||field=='y')) {
        Planet *p=&planets[i];
        float value=field=='t'?p->t:field=='m'?p->m:field=='x'?p->x:p->y;
        return op=='>'?value>v:value<v;
    }
    *valid=false; return false;
}
static void filter(const char *s) {
    char buf[INPUT_MAX]; snprintf(buf,sizeof(buf),"%s",s);
    bool next_or=false,first=true;
    char *p=buf;
    while(*p) {
        bool op_or=false,op_and=false;
        if(*p=='+') { op_or=true; p++; }
        else if(*p=='&') { op_and=true; p++; }
        char *end=p;
        while(*end && *end!='+' && *end!='&') end++;
        char saved=*end; *end=0;
        if(!*p) { snprintf(status,sizeof(status),"Empty filter"); return; }
        bool valid=true;
        // Validate expression once, including when the galaxy has zero selected objects.
        (void)matches(0,p,&valid);
        if(!valid) { snprintf(status,sizeof(status),"Invalid filter: %.180s",p); return; }
        for(int i=0;i<N;i++) {
            bool hit=matches(i,p,&valid);
            if(first && !op_or && !op_and) planets[i].selected=hit;
            else if(first && op_and && count_selected==0) planets[i].selected=hit; // empty selection starts with all
            else if(op_or || (first && next_or)) planets[i].selected |= hit;
            else planets[i].selected &= hit;
        }
        first=false; next_or=false;
        if(!saved) break;
        p=end+1;
        if(saved=='+') { // the next token is a union operation
            next_or=true;
            // Keep operator with the token, so the next iteration knows its meaning.
            if(*p) { memmove(p+1,p,strlen(p)+1); *p='+'; }
        }
    }
    rebuild(); anchor=0;
    snprintf(status,sizeof(status),"Filter: %.190s (%d planets)",s,count_selected);
}
static bool parse_anchor(const char *s,double *a) {
    char *end; double n=strtod(s,&end);
    if(end==s) return false;
    if(*end=='/') { char *end2; double den=strtod(end+1,&end2);
        if(*end2 || den==0) return false;
        n=n/den;
    } else if(*end) return false;
    if(n==0) return false;
    if(strchr(s,'/')) *a=n>0?n:1+n;
    else if(n>0) *a=10000+n; // top-aligned 1-based row
    else *a=-10000+n; // bottom-aligned 1-based row counted from bottom
    return true;
}
static void execute(const char *s) {
    while(isspace((unsigned char)*s)) s++;
    if(!*s) return;
    if(s[0]=='z' && isspace((unsigned char)s[1])) {
        while(isspace((unsigned char)*++s));
        Rect r;
        if(area_bounds(s,&r)) { view=r; snprintf(status,sizeof(status),"Map zoom: %s",s); }
        else snprintf(status,sizeof(status),"Invalid zoom area: %s",s);
    } else if(!strcmp(s,"z")) { view=(Rect){-1,-1,1,1}; strcpy(status,"Map zoom: entire galaxy"); }
    else if(s[0]=='d' && (s[1]==0||isspace((unsigned char)s[1]))) {
        char buf[INPUT_MAX]; snprintf(buf,sizeof(buf),"%s",s+1);
        char *tok=strtok(buf," \t"); bool got_anchor=false;
        while(tok) {
            if(!strcmp(tok,"t")||!strcmp(tok,"m")||!strcmp(tok,"x")||!strcmp(tok,"y")||
               !strcmp(tok,"-t")||!strcmp(tok,"-m")||!strcmp(tok,"-x")||!strcmp(tok,"-y")||!strcmp(tok,"name")) {
                sort_reverse=tok[0]=='-';
                char c=sort_reverse?tok[1]:tok[0];
                sort_key=c=='t'?1:c=='m'?2:c=='x'?3:c=='y'?4:0;
            } else {
                double a;
                if(!parse_anchor(tok,&a)) { snprintf(status,sizeof(status),"Invalid display argument: %s",tok); return; }
                anchor=a; got_anchor=true;
            }
            tok=strtok(NULL," \t");
        }
        (void)got_anchor;
        rebuild(); snprintf(status,sizeof(status),"Display: %s",s);
    } else filter(s);
}
static int first_row(int visible) {
    if(count_selected<=visible) return 0;
    double a=anchor;
    int row,screen;
    if(a>=10000) { row=(int)(a-10000)-1; screen=0; }
    else if(a<=-10000) { row=count_selected+(int)(a+10000); screen=visible-1; }
    else { row=(int)floor(a*(count_selected-1)+0.5);
           screen=(int)floor(a*(visible-1)+0.5); }
    int first=row-screen;
    if(first<0) first=0;
    if(first>count_selected-visible) first=count_selected-visible;
    return first;
}
int main(void) {
    SetConfigFlags(FLAG_WINDOW_RESIZABLE);
    InitWindow(1240,720,"Space - raylib prototype");
    SetTargetFPS(60);
    generate();
    while(!WindowShouldClose()) {
        int ch;
        while((ch=GetCharPressed())!=0) if(ch>=32&&ch<127&&input_len<INPUT_MAX-1) {
            command[input_len++]=(char)ch; command[input_len]=0;
        }
        if(IsKeyPressed(KEY_BACKSPACE)&&input_len) command[--input_len]=0;
        if(IsKeyPressed(KEY_ENTER)) { execute(command); input_len=0; command[0]=0; }
        int W=GetScreenWidth(),H=GetScreenHeight();
        int margin=12, bottom=82, content_h=H-bottom-2*margin;
        int side=(W-3*margin)/2;
        int map_side=fminf(side,content_h);
        int map_x=margin, map_y=margin+(content_h-map_side)/2;
        int table_x=map_x+map_side+margin,table_w=W-table_x-margin;
        int visible=(content_h-56)/ROW_H; if(visible<1) visible=1;
        int first=first_row(visible);
        BeginDrawing(); ClearBackground((Color){13,17,24,255});
        DrawRectangle(map_x,map_y,map_side,map_side,(Color){5,8,16,255});
        DrawRectangleLines(map_x,map_y,map_side,map_side,GRAY);
        for(int i=0;i<N;i++) {
            Planet *p=&planets[i];
            if(p->x<view.x0||p->x>view.x1||p->y<view.y0||p->y>view.y1) continue;
            int x=map_x+(int)((p->x-view.x0)/(view.x1-view.x0)*map_side);
            int y=map_y+(int)((view.y1-p->y)/(view.y1-view.y0)*map_side);
            DrawCircle(x,y,p->selected?2.4f:1.3f,p->selected?RED:RAYWHITE);
        }
        DrawText("GALAXY",map_x+8,map_y+8,18,LIGHTGRAY);
        DrawRectangle(table_x,margin,table_w,content_h,(Color){20,25,34,255});
        DrawText(TextFormat("PLANETS  %d / %d",count_selected,N),table_x+8,margin+8,20,RAYWHITE);
        DrawText(status,table_x+8,margin+33,13,LIGHTGRAY);
        int header_y=margin+55;
        DrawText("NAME",table_x+8,header_y,14,SKYBLUE);
        DrawText("X",table_x+150,header_y,14,SKYBLUE);
        DrawText("Y",table_x+230,header_y,14,SKYBLUE);
        DrawText("TRIT",table_x+310,header_y,14,SKYBLUE);
        DrawText("MOLY",table_x+390,header_y,14,SKYBLUE);
        BeginScissorMode(table_x,header_y+ROW_H,table_w,content_h-55-ROW_H);
        for(int j=0;j<visible&&first+j<count_selected;j++) {
            Planet *p=&planets[order[first+j]];
            int y=header_y+ROW_H*(j+1);
            if(j%2==0) DrawRectangle(table_x,y,table_w,ROW_H,(Color){27,33,43,255});
            DrawText(p->name,table_x+8,y+2,14,RAYWHITE);
            DrawText(TextFormat("%+.3f",p->x),table_x+150,y+2,14,LIGHTGRAY);
            DrawText(TextFormat("%+.3f",p->y),table_x+230,y+2,14,LIGHTGRAY);
            DrawText(TextFormat("%.3f",p->t),table_x+310,y+2,14,LIGHTGRAY);
            DrawText(TextFormat("%.3f",p->m),table_x+390,y+2,14,LIGHTGRAY);
        }
        EndScissorMode();
        DrawText(TextFormat("Rows %d-%d of %d",count_selected?first+1:0,
            count_selected?fminf(first+visible,count_selected):0,count_selected),table_x+8,H-bottom-10,14,GRAY);
        DrawRectangle(margin,H-60,W-2*margin,46,(Color){29,35,47,255});
        DrawText(">",margin+10,H-48,23,GREEN);
        DrawText(command,margin+40,H-46,21,RAYWHITE);
        if(((int)(GetTime()*2))%2==0) DrawRectangle(margin+40+MeasureText(command,21),H-47,2,23,RAYWHITE);
        EndDrawing();
    }
    CloseWindow(); return 0;
}
