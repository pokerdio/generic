let img;
let img_count = 1; 

const PARTICLE_SIZE_INPUT = 5;
const PARTICLE_SIZE_OUTPUT = 7;
const MIN_FORCE = 0.0;
const MAX_FORCE = 10.0;
const WARP_RADIUS = 100;


let particles = [];

function myImageLoad() {
    let name = "./" + img_count + ".jpg";
    img_count = (img_count % 6) + 1;
    console.log("loading image " + name);
    img = loadImage(name, spawnParticles);
}

function preload() {
    myImageLoad();
}

function setup() {
    createCanvas(windowWidth, windowHeight);
    spawnParticles();
}

function mouseClicked() {
    myImageLoad();
    spawnParticles();
}

function draw() {
    background(40);
    // image(img, 0, 0, 
    // 	  img.width * PARTICLE_SIZE_OUTPUT / PARTICLE_SIZE_INPUT,
    // 	  img.height * PARTICLE_SIZE_OUTPUT / PARTICLE_SIZE_INPUT);

    noStroke();
    
    particles.forEach((p => {
	p.update();
	p.draw();
    }));
}

function imgGet(x, y) {
    let ret = [0, 0, 0];
    let n = 0;
    for (let dx=-1 ; dx<=1 ; ++dx) {
	for (let dy=-1 ; dy<=1 ; ++dy) {
	    n += 1;
	    let col = img.get(x + dx, y + dy);
	    for (let k=0 ; k<3 ; ++k) {
		ret[k] += col[k];
	    }
	}
    }
    return [ret[0] / n, ret[1] / n, ret[2] / n, 255]
}

function spawnParticles () {
    console.log("spawning " + img.width + " " + img.height);
    particles = [];

    let half = PARTICLE_SIZE_INPUT / 2;
    for (let i=half ; i<img.width ; i+=PARTICLE_SIZE_INPUT) {
	for (let j=half ; j<img.height ; j+=PARTICLE_SIZE_INPUT) {
	    particles.push(new Particle(i / PARTICLE_SIZE_INPUT, 
					j / PARTICLE_SIZE_INPUT, 
					imgGet(i, j)));
	}
    }
}

class Particle {
    constructor (x, y, color) {
	x = x * PARTICLE_SIZE_OUTPUT;
	y = y * PARTICLE_SIZE_OUTPUT;
	this.x = x;
	this.y = y;
	this.targetX = x;
	this.targetY = y;
	this.color = color; 
    }

    update () {
	let mouseVector = createVector(mouseX, mouseY);
	let currentVector = createVector(this.x, this.y);
	let targetVector = createVector(this.targetX, this.targetY);
	let fromMouseToParticle = p5.Vector.sub(currentVector, mouseVector);
	let distanceToMouse = fromMouseToParticle.mag();
	let fromParticleToTarget = p5.Vector.sub(targetVector, currentVector);
	let distanceToTarget = fromParticleToTarget.mag();

	let totalForce = createVector(0, 0);
	if (distanceToMouse < WARP_RADIUS) {
	    let repulsion = map(distanceToMouse, 0, WARP_RADIUS, 
				MAX_FORCE, MIN_FORCE); 
	    fromMouseToParticle.setMag(repulsion);
	    totalForce.add(fromMouseToParticle);
	} 
	if (distanceToMouse > 0) {
	    let attraction = map(distanceToTarget, 0, WARP_RADIUS, 
				 MIN_FORCE, MAX_FORCE);
	    fromParticleToTarget.setMag(attraction);
	    totalForce.add(fromParticleToTarget);
	}
	this.x += totalForce.x;
	this.y += totalForce.y;
    }
    draw () {
	fill(this.color);
	ellipse(this.x, this.y, PARTICLE_SIZE_OUTPUT);
    }
}
