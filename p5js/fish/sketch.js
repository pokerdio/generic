let fishs = [];
const nfishs = 25;

function setup() {
    createCanvas(Fish.w, Fish.h);
    rectMode(CENTER);
    angleMode(DEGREES);

    for (let i=0 ; i<nfishs ; ++i) { 
	fishs.push(new Fish());
    }
    for (let i=0 ; i<nfishs ; ++i) {
//	fishs[i].setFollow(fishs[floor(random(nfishs-0.01))])
	fishs[i].setFollow(fishs[(i + 1) % nfishs])
    }

    // fishs[0] = new Fish(50, 200, "red", 1.0, 1.0);
    // fishs[1] = new Fish(600, 200, "lime", 0.0, 1.0);
    // fishs[0].setFollow(fishs[1]);
}

function draw() {
    background("#ADD8E6");
    if (random() < 0.1) {
	let fish = floor(random(nfishs - 0.01));
	let target = floor(random(nfishs - 0.01));
	fishs[fish].setFollow(fishs[target]);
    }
    for (let i=0 ; i<fishs.length ; ++i) {
	fishs[i].update();
    }
    for (let i=0 ; i<fishs.length ; ++i) {
	fishs[i].display();
    }
    fill(0);
    textSize(15);
    stroke(255);
    strokeWeight(2.5); 
    text(`fps:${frameRate().toFixed(2)}`, 10, 20);
}

