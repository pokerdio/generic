let x, y;
let angle = 0;
let r = 150;

function setup() {
    createCanvas(400, 400);
    rectMode(CENTER);
    angleMode(DEGREES);
}

function draw() {
    background(220);
    angle = angle + 1;
    let amouse = angle + map(mouseX, 0, width, 0, 360)
    x = r * cos(amouse);
    y = r * sin(amouse);
    translate(width/2, height / 2);
    fill(255);
    ellipse(0, 0, r * 2, r * 2);

    fill(75, 75, 75, 255);
    for (let a=0 ; a<180 ; a+=10) {
	push();
	rotate(-a);
	line(-r, 0, r, 0);
	pop();
    }
    for (let a=0 ; a<180 ; a+=10) {
	push();
	rotate(-a);
	ellipse(r * cos(amouse + a), 0, 20, 20);
	pop();
    }

    fill(255, 0, 0, 255);
    ellipse(x, y, 20, 20);
}

