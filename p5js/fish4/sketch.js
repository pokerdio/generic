const nfishs = 75;

let gfx = [];

function strip1(col1, col2, vert) {
    return genStripes(vert, col1, col1, col2, col1, col1, col2, col1, col1);
}

function strip2(col1, col2, vert) {
    return genStripes(vert, col1, col2, col1);
}

function getRnd() {
    if (arguments.length === 0) {
	return undefined; // If no parameters passed, return undefined
    }
    
    var randomIndex = floor(random() * arguments.length);

    return arguments[randomIndex];
}

function setup() {
    createCanvas(Fish.w, Fish.h);

    gfx.push(new FishGfx(false, ["red", "green", "red", "green"], "green"));
    gfx.push(new FishGfx(true, ["red", "orange", "yellow", "orange", "red"], "yellow"));
    gfx.push(new FishGfx(false, ["blue", "blue", "cyan"], "blue"));
    gfx.push(new FishGfx(false, ["DarkOliveGreen", "Lime", "Khaki", "Khaki"], 
			 "DarkGreen"));
    gfx.push(new FishGfx(false, ["black", "black", "white"], "black"));
    gfx.push(new FishGfx(true, ["black", "black", "black", 
				 "green", "white", "green", 
				 "black", "black", "black",
				 "green", "white", "green", 
				 "black", "black", "black",], "black"));

    mono_reacts = {};
    mono_reacts[gfx[0]] = makeMouseMonoReact();
    pair_reacts = {};
    let cluster = makeClusterPairReact();
    let avoid = makeAvoidPairReact();
    let stroll = makeStrollClusterPairReact();

    
    for (let i=0 ; i<gfx.length ; ++i) {
	let o = {}
	for (let j=0 ; j<gfx.length ; ++j) {
	    o[gfx[j]] = (i == j) ? getRnd(cluster, stroll, stroll) : avoid;
	}
	o[(i + 1) % gfx.length] = cluster; 
	pair_reacts[gfx[i]] = o;
    }
    smooth();
    rectMode(CENTER);
    angleMode(DEGREES);

    smooth();
    for (let i=0 ; i<nfishs ; ++i) { 
	fishs.push(new Fish(gfx[floor(random(gfx.length * 0.999))]));
    }
}

function draw() {
    background("#ADD8E6");
    for (let i=0 ; i<fishs.length ; ++i) {
	fishs[i].update();
    }
    for (let i=0 ; i<fishs.length ; ++i) {
	fishs[i].display();
    }
//    gfx[floor(frameCount / 100) % gfx.length].display(1.0, width/2, height/2);
}

