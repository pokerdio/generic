var x;
let dx = 3;
let mult = 0.02; 
let pal; 
let color_reps = 24;

function mousePressed() {
    pal = getRandomPalette();

    // strokeWeight(5);
    // for (x=0 ; x<width ; x+=3) {
    // 	let c = lerpPalRot(pal, color_reps * x / width)
    // 	stroke(color(255-red(c), 255-green(c), 255-blue(c)), 255);
    // 	line(x, 0, x, height);
    // }
    background(90);
    x = 0;
    y = height / 2;
    noiseSeed(random(1000));
}

function setup() {
    createCanvas(800, 200);
    angleMode(DEGREES);
    mousePressed();
}

function flow(x0, y0, n, dir, len) {
    let x1, y1
    for (let i=0 ; i<n ; ++i) {
	angle = map(noise(x0 * mult, y0 * mult), 0, 1, 0, 720);
	if (dir) {
	    x1 = x0 + cos(angle) * len;
	    y1 = y0 + sin(angle) * len;
	} else {
	    x1 = x0 - cos(angle) * len;
	    y1 = y0 - sin(angle) * len;
	}
	line(x0, y0, x1, y1);
	x0 = x1;
	y0 = y1;
    }
}

function draw() {
    //    noStroke();
    strokeWeight(0.7);
    stroke(lerpPalRot(pal, color_reps *x/width));

    if (x > width){
	return;
    }
    for (let y=0 ; y<height ; y+=height/25) {
	let [x0, y0] = [x, y]
	flow(x0, y0, 50, false, 2);
	flow(x0, y0, 50, true, 2);
    }
    x += dx;
}

