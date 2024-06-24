const N = 30; 
const NL = 17; 
var pal; 
var linezA, linezB; 
var weight = 0; 
var dw = 0.02; 
var wave = 0, dwave = 0.05; 
var wave_size = 0.1;


function interpLine(v1, v2, weight) {
    let ret = new Array();
    let anti_weight = 1 - weight; 
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

function shakeLine(v) {
    let v2 = makeLine(v.length);
    return interpLine(v, v2, 0.2);
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

function newLinez() {
    linezA = makeLinez();
    linezB = Array.from(linezA, shakeLine);
}

function mousePressed() {
    pal = getRandomPalette();
    newLinez();
}

function makeLinez() {
    let ret = [];
    for (let j=0 ; j<NL ; ++j) {    
	ret.push(makeLine(N));
    }
    return ret; 
}

function setup() {
    createCanvas(800, 400);
    mousePressed();
//    frameRate(4);
    weight = 0;
    newLinez();
}

function draw() {
    wave += dwave; 
    
    weight += dw; 
    if (weight >= 1) {
	linezA = linezB;
	linezB = Array.from(linezA, shakeLine);
	weight = 0; 
    }
    

    let dx = width / (N-1);
    let dy = height / (NL + 2);
    background(0);
    for (let j=0 ; j<NL ; ++j) {
	strokeWeight(2 * j / NL + 1);
	fill(lerpPal(pal, j / NL));
	let y = (j + 1) * dy + dy * sin(wave + j) * j * wave_size;
	let v = interpLine(linezB[j], linezA[j], weight % 1);
	drawLine(v, dx, y);
    }
}
