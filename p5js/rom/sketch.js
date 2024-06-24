let img; // Declare variable 'img'.
let diameter = 200;

function preload() {
  // Load the image
  //img = loadImage('https://upload.wikimedia.org/wikipedia/commons/f/f5/Missolonghi.jpg');
}

function drawEllipseWithTexture(x, y, w, h, textureImage) {
    beginShape();
    texture(textureImage);
    for (let angle = 0; angle < TWO_PI; angle += 0.7) {
	let xPos = x + cos(angle) * w / 2;
	let yPos = y + sin(angle) * h / 2;
	let u = map(cos(angle), -1, 1, 0, w);
	let v = map(sin(angle), -1, 1, 0, h);
	vertex(xPos, yPos, 0, u, v);
    }
    endShape(CLOSE);
}

function setup() {
    // Draw the ellipse with the texture
    createCanvas(700, 700, WEBGL);

    let d = 64;
    img = createGraphics(d, d);
    img.noStroke();
    let k = 0;
    let c = ["red", "yellow", "blue", "green", "black", "pink", "purple", "cyan"];
    for (let i=0 ; i<6 ; ++i) {
	for (let j=0 ; j<6 ; ++j) {
	    img.fill(c[k % c.length]);
	    img.rect(d * i / 6, d * j / 6, d / 6, d / 6);
	    k++;
	}
    }
    img.fill(255);
    img.ellipse(25, 25, 5, 5);
    noFill();

    textureWrap(REPEAT);
    texture(img);
    stroke(0);
    strokeWeight(1.6);
    smooth();
}

function draw() {
    textureWrap(REPEAT);

    background(255);
    push();
//    ellipse(sin(frameCount * 0.051) * 60, 0, 150 , 50);      
    drawEllipseWithTexture(sin(frameCount * 0.051) * 60, 0, 150 , 50, img);
    translate(sin(frameCount * 0.049) * 120, -250)
    rotate(frameCount * 0.015)  
//    ellipse(0, 0, 50 , 150);        
    drawEllipseWithTexture(0, 0, 50, 150, img)
    pop();
}
