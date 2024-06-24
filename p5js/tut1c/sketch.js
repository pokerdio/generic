let cols; let rows;
let size = 25;
let blocks = [];
let img; 

function preload() {
  img = loadImage('https://upload.wikimedia.org/wikipedia/commons/8/86/Eurasian_blue_tit_Lancashire.jpg');
}

function setup() {
    img.resize(600, 600 * img.height / img.width);
    createCanvas(img.width, img.height);
//    rectMode(CENTER);
    angleMode(DEGREES);
    cols = Math.floor(width / size);
    rows = Math.floor(height / size);

    for (let i=0 ; i<cols ; ++i) {
	blocks[i] = [];
	for (let j=0 ; j<rows ; ++j) {
	    blocks[i][j] = new Block(size/2 + i * size, size/2 + j * size, size * 0.85, 
				     img, [i * size, j * size, size, size]);
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

