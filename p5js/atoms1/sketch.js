let atoms = [];
const natoms = 25;

function setup() {

    createCanvas(Atom.w, Atom.h);
    rectMode(CENTER);
    angleMode(DEGREES);


    for (let i=0 ; i<natoms ; ++i) { 
	atoms.push(new Atom());
    }
}

function draw() {
    background(0);
    for (let i=0 ; i<atoms.length ; ++i) {
	atoms[i].update();
    }
    for (let i=0 ; i<atoms.length ; ++i) {
	atoms[i].display();
    }


    fill(0);
    textSize(15);
    stroke(255);
    strokeWeight(2.5);
    text("mouse:" + mouseX + mouseY);
}

