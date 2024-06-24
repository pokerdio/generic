let size = 40
let grid;
let color_pal; 
let w, h;

function myDraw() {
    
    let x, y, col

    noStroke();
    for (let i=0 ; i<w ; i++) {
	for (let j=0 ; j<h ; j++) {	
	    fill(grid[i][j]);
	    rect(i * size, j * size, size, size);
	}
    }
    noFill();
    stroke(0);
    strokeWeight(3);
    rect(0, 0, size * w, size * h)

    for (let i=0 ; i<w ; i++) {
	for (let j=0 ; j<h ; j++) {	
	    x = i * size;
	    y = j * size;
	    if (j > 0 && grid[i][j] != grid[i][j - 1]) {
		line(x, y, x + size, y);
	    }
	    if (i > 0 && grid[i][j] != grid[i - 1][j]) {
		line(x, y, x, y + size);
	    }
	}
    }

    stroke('black');
    fill('white')
    textSize(18);
    text(getRandomPalette.col_name, 10, 20)
}

function myInit1() {
    color_pal = getRandomPalette();

    w = Math.floor(width / size);
    h = Math.floor(height / size);
    
    grid = [];
    for (let i=0 ; i<w ; i++) {
	grid[i] = []
	for (let j=0 ; j<h ; j++) {	
	    grid[i][j] = random(color_pal)
	}
    }
}

function subRange(start, stop) {
    let a = start + Math.floor(Math.random() * (stop + 0.999 - start));
    let b = start + Math.floor(Math.random() * (stop + 0.999 - start));
    return [min(a, b), max(a, b)]
}

function myInit2() {
    color_pal = getRandomPalette();

    w = Math.floor(width / size);
    h = Math.floor(height / size);
    
    grid = [];
    for (let i=0 ; i<w ; i++) {
	grid[i] = []
	for (let j=0 ; j<h ; j++) {	
	    grid[i][j] = random(color_pal)
	}
    }

    for (let n=0 ; n<w ; ++n) {
	let [x1, x2] = subRange(0, w - 3);
	let [y1, y2] = subRange(0, h - 3);
	let c = random(color_pal);
	for (let i=x1 ; i<=x2 ; ++i) {
	    for (let j=y1 ; j<=y2 ; ++j) {
		grid[i][j] = c;
	    }
	}
    }
}


function mousePressed() {
    myInit2();
    myDraw();
}

function setup() {
    createCanvas(400, 320);
    angleMode(DEGREES);
    myInit1();
    myDraw();
}


function draw() {
}

