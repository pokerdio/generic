const TILE_SIZE = 40;
const THICK = 8;
const NX = 30;
const NY = 20;
const TILE_TYPE = 5;

function preload() {
}

function myDraw () {
    background(75);
    for (let i=0 ; i<NX ; ++i) {
	for (let j=0; j<NY ; ++j) {
	    drawTile(i, j, Math.floor(random() * TILE_TYPE));
	}
    }
}


function setup() {
    createCanvas(windowWidth, windowHeight);
    myDraw();
}

function mouseClicked() {
    myDraw();
}

function drawTile(x, y, type) {
    x0 = x * TILE_SIZE;
    y0 = y * TILE_SIZE;
    x1 = x0 + TILE_SIZE;
    y1 = y0 + TILE_SIZE;

    noFill();
    stroke(255, 0, 0);
    strokeWeight(1);
    rect(x0, y0, TILE_SIZE, TILE_SIZE);

    stroke(255);
    strokeWeight(THICK);
    switch(type) {
    case 0:
	arc(x0, y0, TILE_SIZE, TILE_SIZE, 0, HALF_PI);
	arc(x1, y1, TILE_SIZE, TILE_SIZE, 
	    HALF_PI * 2, HALF_PI * 3);
	break;
    case 1:
	arc(x1, y0, TILE_SIZE, TILE_SIZE, HALF_PI, HALF_PI * 2);
	arc(x0, y1, TILE_SIZE, TILE_SIZE, 
	    HALF_PI * 3, 0);
	break;
    case 2:
	line(x0 + TILE_SIZE / 2, y0, x0 + TILE_SIZE / 2, y1);
	line(x0, y0 + TILE_SIZE / 2, x1, y0 + TILE_SIZE / 2);
	break;
    case 3: 
	line(x0 + TILE_SIZE / 2, y0, x0 + TILE_SIZE / 2, y1);
	point(x0, y0 + TILE_SIZE / 2);
	point(x1, y0 + TILE_SIZE / 2);
	break;
    case 4:
	point(x0 + TILE_SIZE / 2, y0); 
	point(x0 + TILE_SIZE / 2, y1);
	line(x0, y0 + TILE_SIZE / 2, x1, y0 + TILE_SIZE / 2);
	break;
    }
}

function draw() {
}

