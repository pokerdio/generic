let cols; let rows;
let size = 15;

let blocks = [];

function setup() {
    createCanvas(405, 405);
    rectMode(CENTER);
    angleMode(DEGREES);
    cols = Math.floor(width / size);
    rows = Math.floor(height / size);

    for (let i=0 ; i<cols ; ++i) {
	blocks[i] = [];
	for (let j=0 ; j<rows ; ++j) {
	    blocks[i][j] = new Block(size/2 + i * size, size/2 + j * size, size * 0.8);
	}
    }
}

function mouseMoved() {
    for (let i=0 ; i<cols ; ++i) {
	for (let j=0 ; j<rows ; ++j) {
	    blocks[i][j].initiate_move();
	}
    }
}

function draw() {
    background(220);
    if (mouseX != pmouseX) {
	console.log("WAAAAAAAA")
    }
    for (let i=0 ; i<cols ; ++i) {
	for (let j=0 ; j<rows ; ++j) {
	    blocks[i][j].move();
	    blocks[i][j].display();
	}
    }
}

