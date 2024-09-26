// Constants
const CANVAS_SIZE = 500;
const MOVE_AMOUNT = 1.2; // How much the slime moves in its heading direction
const DISTANCE = 5;   // Distance to the three points from the slime
const SIDE_ANGLE = 3.14159 / 4; // Angle to the side points in radians (30 degrees)
const SLIME_COUNT = 5000; 
const ROTATION_AMOUNT = 0.15; 
const STROKE_WEIGHT = DISTANCE * 0.8; 

var slime = [];


function getCol(x, y) {
    // Calculate the index of the pixel in the pixels array
    x = floor(x);
    y = floor(y);
    const index = (x + y * width) * 4; // Each pixel has 4 values (RGBA)

    // Check if coordinates are within bounds
    if (index >= 0 && index < pixels.length) {
	const r = pixels[index];     // Red value
	const g = pixels[index + 1]; // Green value
	const b = pixels[index + 2]; // Blue value

	return (r + g + b) / 3.0;
    } else {
	return 0;
    }
}

// Slime class
class Slime {
    constructor() {
	this.x = random(width);     // Random x position within the canvas
	this.y = random(height);    // Random y position within the canvas
	this.heading = random(TWO_PI); // Random heading (angle) in radians
	this.computePoints(); 
    }

    // Update function: moves the slime in its heading direction
    update() {
	this.computePoints();

	let f = getCol(this.frontX, this.frontY)
	let r = getCol(this.rightX, this.rightY)
	let l = getCol(this.leftX, this.leftY)

	if (f < r || f < l) {
	    if (r > l) {
		this.heading += ROTATION_AMOUNT; 
	    } else {
		this.heading -= ROTATION_AMOUNT; 
	    }
	}
	this.x += MOVE_AMOUNT * cos(this.heading);
	this.y += MOVE_AMOUNT * sin(this.heading);

	// Wrapping around the canvas
	this.x = (this.x + width) % width;
	this.y = (this.y + height) % height;
    }

    // Function to compute the three points in front and to the sides
    computePoints() {
	// Calculate the front point
	let frontX = this.x + DISTANCE * cos(this.heading);
	let frontY = this.y + DISTANCE * sin(this.heading);
	
	// Calculate the left point (angle shifted by SIDE_ANGLE to the left)
	let leftX = this.x + DISTANCE * cos(this.heading - SIDE_ANGLE);
	let leftY = this.y + DISTANCE * sin(this.heading - SIDE_ANGLE);
	
	// Calculate the right point (angle shifted by SIDE_ANGLE to the right)
	let rightX = this.x + DISTANCE * cos(this.heading + SIDE_ANGLE);
	let rightY = this.y + DISTANCE * sin(this.heading + SIDE_ANGLE);

	// Wrap around the points if they go outside the canvas bounds
	this.frontX = (frontX + width) % width;
	this.frontY = (frontY + height) % height;
	this.leftX = (leftX + width) % width;
	this.leftY = (leftY + height) % height;
	this.rightX = (rightX + width) % width;
	this.rightY = (rightY + height) % height;
    }

    // Display the slime and its points for visualization
    display() {


	point(this.x, this.y)

	// Draw the points (front, left, right)
	// fill(255, 0, 0, 255); // Red color for points

	// ellipse(this.frontX, this.frontY, 3, 3);
	// ellipse(this.leftX, this.leftY, 3, 3);
	// ellipse(this.rightX, this.rightY, 3, 3);
    }
}


function setup() {
    createCanvas(CANVAS_SIZE, CANVAS_SIZE); // Creates a 400x400 canvas
    background(255);        // Sets the background to white
    for (let i=0 ; i<SLIME_COUNT ; ++i) {
	slime.push(new Slime());
    }
}

function draw() {
    loadPixels();
    strokeWeight(STROKE_WEIGHT);
    stroke(255);

    for (let i=0 ; i<slime.length ; ++i) {
	slime[i].update();
	slime[i].display(); 
    }
    fill(0, 5);            // Sets the fill to black with 10 alpha (transparency)
    noStroke(); 
    rect(0, 0, width, height); // Draws a rectangle covering the entire canvas
}

