let fishs = [];
const nfishs = 75;


function genStripes(vert, ...cols) {
    let d = 64
    let ret = createGraphics(d, d);
    ret.noStroke();
    for (let i=0 ; i<cols.length ; ++i) {
	ret.fill(cols[i]);
	if (vert) {
	    ret.rect(i * d / cols.length, 0, (i + 1) * d / cols.length, d);
	} else {
	    ret.rect(0, i * d / cols.length, d, (i + 1) * d / cols.length);
	}
    }
    return ret; 
}

function strip1(col1, col2, vert) {
    return genStripes(vert, col1, col1, col2, col1, col1, col2, col1, col1);
}

function strip2(col1, col2, vert) {
    return genStripes(vert, col1, col2, col1);
}

function setup() {
    createCanvas(Fish.w, Fish.h, WEBGL);
    rectMode(CENTER);
    angleMode(DEGREES);
    Fish.addColor(strip1("red", "yellow", true));
    Fish.addColor(strip2("blue", "purple"));
    Fish.addColor(strip1("green", "yellow"));
    Fish.addColor(strip2("black", "blue", true));


    smooth();
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
    if (random() < 0.01) {
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

