let cols; let rows;
let size = 25;
let blocks = [];
let x_coords, y_coords;
let img, imgs; 
let angle = 0; 
let img_idx = 0;

function preload() {
    imgs = [loadImage('https://upload.wikimedia.org/wikipedia/commons/7/7a/Cassius_Marcellus_Coolidge_-_Poker_Game_%281894%29.png'),
	    loadImage('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Ships_Riding_on_the_Seine_at_Rouen_by_Claude_Monet%2C_1872.jpg/1024px-Ships_Riding_on_the_Seine_at_Rouen_by_Claude_Monet%2C_1872.jpg'),
	    loadImage('https://upload.wikimedia.org/wikipedia/commons/f/f5/Ducks%2C_Guinea_Pigs_and_a_Rabbit_in_a_Wooded_Landscape_Beside_a_Lake_by_David_de_Coninck.jpg')]
    img = imgs[0];
}



function mousePressed () {
    img = imgs[(++img_idx) % imgs.length]
    clear();
    setup();
}

function setup() {
    img.resize(1205, 1205 * img.height / img.width);
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

function draw() {
    angle = angle + 1.5;
    for (let i=0 ; i<=cols ; ++i) {
	x_coords[i] = i * size + size / 3 * sin(angle + i * 40);
    }
    for (let i=0 ; i<=rows ; ++i) {
	y_coords[i] = i * size + size / 3 * cos(angle + i * 40);
    }
    
    background(70);
    stroke(125);
    for (let i=0 ; i<cols ; ++i) {
	for (let j=0 ; j<rows ; ++j) {
	    blocks[i][j].display(x_coords[i], y_coords[j], x_coords[i + 1] + 1, y_coords[j + 1] + 1);
	}
    }
}

