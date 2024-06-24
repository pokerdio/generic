let f = []; 
let n_picture = 4;
let picture = 0;

function mousePressed() {
    picture = (picture + 1) % n_picture; 
    init(picture);
}

function init(picture) {
    let n = 15;

    switch(picture) {
    case 0:
	for (let i=0 ; i<n ; ++i) {
	    f[n-1-i] = new Flower(80 + i * 5, 2 + i, 12, -1 + i * 0.1, 
				  ["red", "white", "black", "yellow"][i % 4])
	}
	f.length = n;
	break;
    case 1:
	n = 12;
	for (let i=0 ; i<n ; ++i) {
	    f[n-1-i] = new Flower(80 + i * 5, 2 + i, 6 + i * 2, -1 + i * 0.15, 
				  ["red", "white", "black", "yellow"][i % 3])
	}
	f.length = n;
	break;
    case 2:
	for (let i=0 ; i<n ; ++i) {
	    f[n-1-i] = new Flower(80 + i * 5, 2 + i, 6 + i, -1 + i * 0.1, 
				  ["red", "white", "black", "yellow"][i % 4])
	}
	f.length = n;
	break;
    case 3:
	n = 10;
	for (let i=0 ; i<n ; ++i) {
	    f[n-1-i] = new Flower(80 + i * 5, 18, 8, -1 + i * 0.2, 
				  ["blue", "orange", "black", "yellow"][i % 4])
	}
	f.length = n;
	break;
    }
}


function setup() {
    createCanvas(400, 400);
    angleMode(DEGREES);
    init(picture);
}

function draw() {
    background(220);
    translate(width/2, height/2);

    push();
//    blendMode(EXCLUSION);
    for (let i=0 ; i<f.length ; ++i) {
	f[i].display();
    }
    pop();
}

