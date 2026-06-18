let cols; let rows;
let size = 15;
let blocks = [];
let config = {spawn_chance: 10.0, dy: 3.5, max_size: 66};

function setup() {
    createCanvas(405, 405);
    rectMode(CENTER);
    angleMode(DEGREES);
}

function mouseMoved() {
}

function draw() {
    background(220);
    if (random (100) < config.spawn_chance) {
	blocks.push(new Block())
    }
    if (mouseX != pmouseX) {
	console.log("WAAAAAAAA")
    }
    for (let i=0 ; i<blocks.length ; ++i) {
	blocks[i].move();
    }
    for (let i=0 ; i<blocks.length ; ++i) {
	blocks[i].display();
    }
    new_blocks = [];
    for (let i=0 ; i<blocks.length ; ++i) {
	if (blocks[i].y - blocks[i].size < height) {
	    new_blocks.push(blocks[i])
	}
    }
    blocks = new_blocks;

    push();
    translate( mouseX, height - 10);
    strokeWeight(1.5);
    stroke(0, 0, 0);
    fill(255, 100, 100);
    triangle(0, -10, -10, 0, 10, 0);
    pop();
}

