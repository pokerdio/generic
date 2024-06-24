var vline;

function mousePressed() {
    background(0);
    stroke(255);
}

function setup() {
    createCanvas(1600, 900);
    rectMode(CENTER);
    //angleMode(DEGREES);
    vline = gen1(0.03, x=>sin(x * PI * 4))
}



function draw() {
    fill("red");
    for (let o of vline) {
	circle(o.x * width, height * 0.5 - o.f * height * 0.4, 3);
    }
}
