let angle = 0

function setup() {
    createCanvas(800, 600);
    angleMode(DEGREES);
}


function draw() {
    background(0);
    translate(width/2, height/2);
    for (let i=10 ; i<400 ; i+=8) {
	stroke(100, 255, 150);
	strokeWeight (0.75);
	noFill();
	ellipse(cos(angle * 2 + i * 3) * 5, 30 * sin(angle - i - (i / 55) ** 2.2), i, i/2);
    }
    angle += 1.5;
}

