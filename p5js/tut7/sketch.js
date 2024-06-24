var points = [];
let size = 50;
let mult = 0.002; 
let col; 

function mousePressed() {
    col = getRandomPalette();

    background(0);
    for (let x=0 ; x<width ; x+=size) {
	for (let y=0 ; y<height ; y+=size) {
	    let p = createVector(x + random(-size, size), y + random(-size, size));
	    points.push(p);
	    points.push(p.copy());
	}
    }
    noiseSeed(random(1000));

}

function setup() {
    createCanvas(400, 300);
    mousePressed();
}


function draw() {
    noStroke();
    let col_count = 0;
    for (let i=0 ; i<points.length ; ++i) {
	var angle = map(noise(points[i].x * mult, points[i].y * mult), 0, 1, 0, 720);
	if (i % 2) {
	    points[i].sub(createVector(cos(angle), sin(angle)));
	} else {
	    points[i].add(createVector(cos(angle), sin(angle)));
	}
	fill(col[(Math.trunc(i / 2)) % col.length]);
	ellipse(points[i].x, points[i].y, 1);

	if (points[i].x < 0 || points[i].x >= width || 
	    points[i].y < 0 || points[i].y >= height) {
	    points[i].x = random(0, width);
	    points[i].y = random(0, height);
	}
    }
}

