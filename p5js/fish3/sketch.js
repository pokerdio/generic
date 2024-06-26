let fishs = [];
const nfishs = 125;

let gfx = [];

function strip1(col1, col2, vert) {
    return genStripes(vert, col1, col1, col2, col1, col1, col2, col1, col1);
}

function strip2(col1, col2, vert) {
    return genStripes(vert, col1, col2, col1);
}

function setup() {
    createCanvas(Fish.w, Fish.h);

    gfx.push(new FishGfx(false, ["red", "green", "red", "green"], "green"));
    gfx.push(new FishGfx(true, ["red", "orange", "yellow", "orange", "red"], "yellow"));
    gfx.push(new FishGfx(false, ["blue", "blue", "cyan"], "blue"));
    smooth();
    rectMode(CENTER);
    angleMode(DEGREES);
    // Fish.addColor(strip1("red", "yellow", true));
    // Fish.addColor(strip1("green", "yellow"));
    // Fish.addColor(strip2("black", "blue", true));

    smooth();
    for (let i=0 ; i<nfishs ; ++i) { 
	fishs.push(new Fish(gfx[floor(random(gfx.length * 0.999))]));
    }
}

function draw() {
    background("#ADD8E6");
    for (let i=0 ; i<fishs.length ; ++i) {
	fishs[i].update();
    }
    for (let i=0 ; i<fishs.length ; ++i) {
	fishs[i].display();
    }
//    gfx[floor(frameCount / 100) % gfx.length].display(1.0, width/2, height/2);
}

