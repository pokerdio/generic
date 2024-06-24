const TILE_SIZE = 40;
const THICK = 5;
const TILE_SET = [0,1, 2, 3, 4];
//const TILE_SET = [2,3,4];
//const TILE_SET = [7, 8];
//const TILE_SET = [5, 6, 7, 8];
//const TILE_SET = [5, 6];

const DEBUG = false;

function setup() {
  createCanvas(1400, 800);
  myDraw();
}

function getRandomElement(arr) {
  const randomIndex = Math.floor(Math.random() * arr.length);
  return arr[randomIndex % arr.length];
}

function drawTile(x, y, type) {
    let S = TILE_SIZE;
    let dS = TILE_SIZE / 4;
    let x0 = x * S;
    let y0 = y * S;
    let x1 = x0 + S;
    let y1 = y0 + S;

    let x1q = x0 + dS;
    let x3q = x1 - dS;
    let y1q = y0 + dS;
    let y3q = y1 - dS;
    
    let xhalf = x0 + S / 2;
    let yhalf = y0 + S / 2;


    noFill();
    if (DEBUG) {
	stroke('red');
	strokeWeight(1);
	rect(x0, y0, S, S);
    }

    stroke(255);
    strokeWeight(THICK);
    switch (type) {
    case 0:
	arc(x0, y0, S, S, 0, HALF_PI);
	arc(x1, y1, S, S, HALF_PI * 2, HALF_PI * 3);
	break;
    case 1:
	arc(x1, y0, S, S, HALF_PI, HALF_PI * 2);
	arc(x0, y1, S, S, HALF_PI * 3, 0);
	break;
    case 2:
	line(x0 + S / 2, y0, x0 + S / 2, y1);
	line(x0, y0 + S / 2, x1, y0 + S / 2);
	break;
    case 3:
	line(x0 + S / 2, y0, x0 + S / 2, y1);
	point(x0, y0 + S / 2);
	point(x1, y0 + S / 2);
	break;
    case 4:
	point(x0 + S / 2, y0);
	point(x0 + S / 2, y1);
	line(x0, y0 + S / 2, x1, y0 + S / 2);
	break;

    case 5:
	line(x0, y1q, x3q, y1);
	line(x0, y3q, x1q, yhalf);
	line(x1q, y1, xhalf, y3q);

	line(x1q, y0, x1, y3q);
	line(xhalf, y1q, x3q, y0);
	line(x3q, yhalf, x1, y1q);
	break;

    case 6:
	line(x0, y3q, x3q, y0);
	line(x0, y1q, x1q, yhalf);
	line(x1q, y0, xhalf, y1q);

	line(x1q, y1, x1, y1q);
	line(xhalf, y3q, x3q, y1);
	line(x3q, yhalf, x1, y3q);

	break;


	//vertical weaving

    case 7:
	line(x1q, y0, x1q, y1);
	line(x3q, y0, x3q, y1);
	line(x0, y1q, x1q, y1q);
	line(x0, y3q, x1q, y3q);
	line(x3q, y1q, x1, y1q);
	line(x3q, y3q, x1, y3q);
	break;
    case 8:
	line(x0, y1q, x1, y1q);
	line(x0, y3q, x1, y3q);
	line(x1q, y0, x1q, y1q);
	line(x3q, y0, x3q, y1q);
	line(x1q, y3q, x1q, y1);
	line(x3q, y3q, x3q, y1);
	break;
    }
}

function myDraw() {
  background(75);
  for (let i=0; i*TILE_SIZE<width; ++i) {
    for (let j=0; j*TILE_SIZE<height; ++j) {
      drawTile(i, j, getRandomElement(TILE_SET));
    }
  }
}

function mouseClicked() {
  myDraw();
}

function draw() {
}
