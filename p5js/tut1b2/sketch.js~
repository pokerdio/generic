let cols; let rows;
let size = 25;
let blocks = [];
let img; 

function preload() {
    img = loadImage('https://upload.wikimedia.org/wikipedia/commons/7/7a/Cassius_Marcellus_Coolidge_-_Poker_Game_%281894%29.png');
}

function setup() {
    img.resize(605, 605 * img.height / img.width);
    createCanvas(img.width, img.height);
//    rectMode(CENTER);
    angleMode(DEGREES);
    cols = Math.floor(width / size);
    rows = Math.floor(height / size);

    for (let i=0 ; i<cols ; ++i) {
	blocks[i] = [];
	for (let j=0 ; j<rows ; ++j) {
	    blocks[i][j] = new Block(size/2 + i * size, size/2 + j * size, size * 0.65, 
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
    background(70);
    if (mouseX != pmouseX) {
	console.log("WAAAAAAAA")
    }
    stroke(125);
    for (let i=0 ; i<cols ; ++i) {
	for (let j=0 ; j<rows ; ++j) {
	    blocks[i][j].move();
	    blocks[i][j].display();
	}
    }
}

