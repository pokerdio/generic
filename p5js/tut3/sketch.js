let size = 50;
let space_size = 80;
let margin = space_size / 2;
let rows, cols;

let angleX = 0;
let angleY = 0;

function setup() {
    createCanvas(500, 400, WEBGL);
    cols = Math.floor(width / space_size);
    rows = Math.floor(height / space_size);
    angleMode(DEGREES);
}

function myBox(size) {
    // Draw the front face
    fill(255, 0, 0);
    beginShape();
    vertex(-size, -size, size);
    vertex(size, -size, size);
    vertex(size, size, size);
    vertex(-size, size, size);
    endShape(CLOSE);

    // Draw the back face
    fill(0, 255, 0);
    beginShape();
    vertex(-size, -size, -size);
    vertex(size, -size, -size);
    vertex(size, size, -size);
    vertex(-size, size, -size);
    endShape(CLOSE);

    // Draw the top face
    fill(0, 0, 255);
    beginShape();
    vertex(-size, -size, size);
    vertex(size, -size, size);
    vertex(size, -size, -size);
    vertex(-size, -size, -size);
    endShape(CLOSE);

    // Draw the bottom face
    fill(255, 255, 0);
    beginShape();
    vertex(-size, size, size);
    vertex(size, size, size);
    vertex(size, size, -size);
    vertex(-size, size, -size);
    endShape(CLOSE);

    // Draw the left face
    fill(0, 255, 255);
    beginShape();
    vertex(-size, -size, size);
    vertex(-size, size, size);
    vertex(-size, size, -size);
    vertex(-size, -size, -size);
    endShape(CLOSE);

    // Draw the right face
    fill(255, 0, 255);
    beginShape();
    vertex(size, -size, size);
    vertex(size, size, size);
    vertex(size, size, -size);
    vertex(size, -size, -size);
    endShape(CLOSE);    
}

function draw() {
    background(220);
    smooth();
    stroke(0);
    strokeWeight(1.5);
    let x = map(mouseX, 0, width, 0, 360);
    let y = map(mouseY, 0, height, 0, 360);


    for (let i=0 ; i<cols ; ++i) {
	for (let j=0 ; j<rows ; ++j) {
	    push();
	    translate((i - cols/2) * space_size + margin, (j - rows/2) * space_size + margin);
	    rotateX(angleX * (1.0 + i * 0.1));
	    rotateY(angleY * (1.0 + j * 0.1));
	    myBox(size / 2);
	    pop();
	}
    }


    angleX += 1;
    angleY += 0.13;
}

