const N = 30; 
const NL = 17; 
var pal; 

function interpLine(v1, v2, weight) {
    let ret = new Array();
    let anti_weight; 
    for (let i=0 ; i<max(v1.length, v2.length) ; ++i) {
	let a = v1[i] || v2[i] || 0;
	let b = v2[i] || v1[i] || 0;
	ret.push(a * weight + b * anti_weight);
    }
    return ret; 
}

function smoothLine(v) {
    let ret = new Array();
    for (let i=0 ; i<v.length ; ++i) {
	ret.push((v[i]+v[i+1]) / 2)
    }
    return ret;
}

function makeLine(n) {
    let v = new Array();
    let dy = 0;
    let y = 0;
    for (let i=0 ; i<=n+1 ; ++i) {
	dy = dy * 0.9 - y / 10;
	if (i < n - 10) {
	    dy = dy + random(-5, 5);      
	}
	y = y + dy;
	v.push(y);
    }
    return smoothLine(smoothLine(v));
}

function drawLine(v, dx, y) {
    beginShape();
    vertex(0, height-1);
    for (let i=0 ; i<N ; ++i) {
	vertex(i * dx, y + v[i])
    }
    vertex((N-1) * dx, height-1);
    endShape();
}

function mousePressed() {
    pal = getRandomPalette();
    
    let dx = width / (N-1);
    let dy = height / (NL + 2);
    background(0);
    for (let j=0 ; j<NL ; ++j) {
	strokeWeight(2 * j / NL + 1);
	fill(lerpPal(pal, j / NL));
	let y = (j + 1) * dy;
	let v = makeLine(N);
	drawLine(v, dx, y);
    }
}
function setup() {
    createCanvas(400, 400);
    mousePressed();
}

function draw() {
}
