#include "raylib.h"
#include "rlgl.h"
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

#define PI2 6.28318530718f
#define LEVELS 6
#define X 20
#define Y 10
#define N 10

#define SPEED_MULTI 1.05

#define COUNT ((X) * (Y) * (N))

typedef struct {
    Vector2 center;
    float radius;
    float angle;
    float speed;
    int level;
} Triangle;

static Triangle tri[COUNT + 66];

static float randomf(float a, float b)
{
    return a + (b - a) * (float)rand() / RAND_MAX;
}

static void draw_triangle(Triangle t, float width, Color color)
{
    Vector2 p[3];

    for (int i = 0; i < 3; i++) {
        float a = t.angle + i * PI2 / 3.0f;
        p[i] = (Vector2){
            t.center.x + t.radius * cosf(a),
            t.center.y + t.radius * sinf(a)
        };
    }

    for (int i = 0; i < 3; i++)
        DrawLineEx(p[i], p[(i + 1) % 3], width, color);
}

int main(void)
{
    SetConfigFlags(FLAG_MSAA_4X_HINT | FLAG_WINDOW_RESIZABLE);
    InitWindow(1200, 800, "Triangle Field");
    SetTargetFPS(60);

    srand(42);

    int k = 0;

    for (int x=0; x<X; x++) {
        for (int y=0; y<Y; y++) {
	    if (k + N > COUNT) {
		break;
	    }
            Triangle *t = &tri[k];
	    t->center = (Vector2){ (0.5 + x) / X, (y + 0.5) / Y };
	    t->radius = randomf(0.045f, 0.125f);
	    t->angle = randomf(0, PI2);

            float direction = 1.0;
	    t->level = GetRandomValue (0, LEVELS - 1);
            t->speed = direction * randomf(0.155f, 0.165f) * (2.0f + t->level * 2.6f);
	    for (int i=1 ; i<N ; i++) {
		*(t+i) = *(t+i-1);
		(t+i)->speed *= SPEED_MULTI;
		if (++k >= COUNT) {
		    break;
		}
	    }
	}
    }

    printf ("k=%d", k);

    while (!WindowShouldClose()) {
        float dt = GetFrameTime();
        float w = (float)GetScreenWidth();
        float h = (float)GetScreenHeight();
        float scale = fminf(w, h);

	for (int i = 0; i < k; i++)
	    tri[i].angle += tri[i].speed * dt;

        BeginDrawing();
        ClearBackground((Color){5, 9, 20, 255});

        // Maximum blending: overlapping strokes retain
        // the strongest opacity instead of accumulating.
        BeginBlendMode(BLEND_CUSTOM_SEPARATE);
        rlSetBlendFactorsSeparate(
				  RL_ONE, RL_ONE,
				  RL_ONE, RL_ONE,
				  RL_MAX, RL_MAX
				  );

        // Draw distant blue layers first, foreground orange last.
	for (int i = 0; i < k; i++) {
	    Triangle t = tri[i];
	    int level = t.level;
            float shrink = powf(0.75f, (float)level);
            float radius = scale * 0.72f * shrink;
            float thickness = fmaxf(0.55f, 2.0f * shrink);

            Color color;
	    color = (Color){255 - level * 40, 125 - level * 15, 35 + level * 40, 55};

	    t.radius *= radius;
	    t.center.x *= w;
	    t.center.y *= h;
	    draw_triangle(t, thickness, color);
	}
	EndBlendMode();
	DrawFPS(10, 10);
	EndDrawing();
    }
    CloseWindow();
    return 0;
}

