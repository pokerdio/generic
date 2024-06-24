let cols; let rows;
let size = 25;
let blocks = [];
let x_coords, y_coords;
let img, imgs; 
let img_idx = 0;

function preload() {
    imgs = [loadImage('https://upload.wikimedia.org/wikipedia/commons/7/7a/Cassius_Marcellus_Coolidge_-_Poker_Game_%281894%29.png'),
	    loadImage('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Pieter_Bruegel_the_Elder_-_Children%E2%80%99s_Games_-_Google_Art_Project.jpg/1280px-Pieter_Bruegel_the_Elder_-_Children%E2%80%99s_Games_-_Google_Art_Project.jpg')]
    img = imgs[0];
}


function mousePressed () {
    img = imgs[(++img_idx) % imgs.length]
    clear();
    setup();
}

function setup() {
    img.resize(1400, 1400 * img.height / img.width);
    createCanvas(img.width, img.height);
//    rectMode(CENTER);
    angleMode(DEGREES);
    cols = Math.floor(width / size);
    rows = Math.floor(height / size);

    x_coords = Array(cols + 1).fill(0);
    y_coords = Array(rows + 1).fill(0);
    for (let i=0 ; i<cols ; ++i) {
	blocks[i] = [];
	for (let j=0 ; j<rows ; ++j) {
	    blocks[i][j] = new Block(img, [i * size, j * size, size, size]);
	}
    }
}

function makeZoomCoords(count, size, mouse) {
    let widths = Array(count - 1).fill(0);
    for (let i=0 ; i<count-1 ; ++i) {
	let d = abs(((i + 0.5) * size) - mouse) / size + 0.001
	d = 5 / d;
	if (d > 3) {
	    d = 3;
	}
	widths[i] = d;
    }
    let s = widths.reduce((x, y) => x + y, 0);
    let wanted_s = (count - 1) * size
    let ret = Array(count).fill(0);
    for (let i=0 ; i<count-1 ; ++i) {
	ret[i + 1] = ret[i] + (widths[i] * wanted_s / s)
    }
    return ret;
}

function draw() {
    if (mouseX <= 2 || mouseX >= width - 2 || mouseY <= 2 || mouseY > height - 2) {
	for (let i=0 ; i<=cols ; ++i) {
	    x_coords[i] = i * size;
	}
	for (let i=0 ; i<=rows ; ++i) {
	    y_coords[i] = i * size;
	}
    } else {
	x_coords = makeZoomCoords(cols, size, mouseX);
	y_coords = makeZoomCoords(rows, size, mouseY);
    }
    
    background(70);
    stroke(125);
    for (let i=0 ; i<cols ; ++i) {
	for (let j=0 ; j<rows ; ++j) {
	    blocks[i][j].display(x_coords[i], y_coords[j], x_coords[i + 1] + 1, y_coords[j + 1] + 1);
	}
    }
}

