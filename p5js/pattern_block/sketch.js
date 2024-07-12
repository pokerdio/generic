let img;
let pat = []

let try_poly = 0;
let try_maker = 0; 

let nomZero = new Nom(0)
let nomOne = new Nom(1)
let lineZero = [[nomZero, nomZero], [nomOne, nomZero]]
    
let open = [lineZero]

let box = [-2, -2, 2, 2]

let lastProcessedCommand = "";

function setup() {
    let canvas = createCanvas(800, 600);
    canvas.parent('canvasContainer');

    strokeWeight(0.02)
    noSmooth()
    // Add an event listener for pasting images
}

function fitBoxToCanvas(box) {
    let [x0, y0, x1, y1] = box;
    let cx = (x0 + x1) / 2;
    let cy = (y0 + y1) / 2;
    let boxWidth = x1 - x0;
    let boxHeight = y1 - y0;
    
    let scaleX = width / boxWidth;
    let scaleY = height / boxHeight;
    let scaleXY = min(scaleX, scaleY) * 0.95;

    let newWidth = width / scaleXY; 
    let newHeight = height / scaleXY; 

    x0 = cx - newWidth / 2;
    y0 = cy - newHeight / 2;
    x1 = cx + newWidth / 2;
    y1 = cy + newHeight / 2;

    scale(scaleXY)
    translate(-x0, -y0)

    return scaleXY
}

function myLine(a, b) {
    let v = [a[0], a[1], b[0], b[1]]
    for (let i=0 ; i<4 ; ++i) {
	if (v[i] instanceof Nom) {
	    v[i] = v[i].toFloat()
	}
    }
    line(...v)
}


let draw_old = [0,0,0,0]
function draw() {
    box = approachBox(box, getBox(pat))
    background(120);
    push();
    let sc = fitBoxToCanvas(box)

    let thin = 1.0
    let thicc = 10.0
    let w = max(min(map(sqrt(sc), 25, 5, thicc, thin), thicc), thin);

    let wActual = w / (sc + 0.002);

    for (let p of pat) {
	p.draw(wActual);
    }

    // testing pointInside
    // stroke(0)
    // strokeWeight(0.025)
    // for (let i=0 ; i<1.0 ; i+=0.025) {
    // 	for (let j=0 ; j<1.0 ; j+=0.025) {
    // 	    let x = box[0] + i * (box[2] - box[0])
    // 	    let y = box[1] + j * (box[3] - box[1])
    // 	    let pint = [new Nom(x), new Nom(y)]
    // 	    for (let p of pat) {
    // 		if (p.pointInside(pint)) {
    // 		    point(x, y);
    // 		    break;
    // 		}
    // 	    }
    // 	}
    // }
    // for (let i=1 ; i<open.length ; ++i) {
    // 	stroke(0)
    // 	strokeWeight(0.08);
    // 	myLine(...open[i])
    // 	stroke(0, map(i, 0, open.length, 255, 50), 0)
    // 	strokeWeight(0.05);
    // 	myLine(...open[i])
    // }

    if (open.length > 0) {
	stroke(255, 150, 150)
	strokeWeight(0.1);
	myLine(...open[0])
	stroke(255)
	strokeWeight(0.05);
	myLine(...open[0])
    }
    pop();


    //if (Pat.box_intersect_count - draw_old[0] > 0) {
    // console.log("box", Pat.box_intersect_count, "(", Pat.box_intersect_count - draw_old[0],
    // 		") int", Pat.intersect_count, "(", Pat.intersect_count - draw_old[1],
    // 		") try_poly", try_poly, "(", try_poly - draw_old[2],
    // 		") try_maker", try_maker, "(", try_maker - draw_old[3],
    // 		")");
    // }

    draw_old = [Pat.box_intersect_count, Pat.intersect_count, try_poly, try_maker]
}

function mousePressed() {
}

function mouseReleased() {
    let endX = mouseX;
    let endY = mouseY;
}

function handleTextChange(event) {
    const textarea = event.target;
    const value = textarea.value;
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;


    let processedValue = repeatLetters(value);
    if (processedValue.startsWith(lastProcessedCommand)) {
	let len = lastProcessedCommand.length
	lastProcessedCommand = processedValue;
	processedValue = processedValue.slice(len)
    } else {
	lastProcessedCommand = processedValue;
	pat = [];
	open = [lineZero];
    }
    for (let i=0 ; i<processedValue.length ; ++i) {
	doLetter(processedValue[i]);
    }
}

function segmentId(a, b) {
    return a.toString() + "%" + b.toString()
}

function vetLine(line) {
    for (let f of [Pat.makeTri, Pat.makeNeedle, Pat.makeNeedleRev]) {
	let poly = f(...line)
	let ok = true
	for (let p of pat) {
	    if (poly.intersect(p)) {
		ok = false;
		break;
	    }
	}
	if (ok) {
	    return true;
	}
    }
    return false; 
}

function vetOpen() {
    while (open.length > 0 && !vetLine(open[0])) {
	open.shift();
    }
}

function vetPoly(poly) {
    for (let p of pat) {
	if (poly.intersect(p)) {
	    return false; 
	}
    }
    return true;
}

function tryPoly(poly, i) {
    try_poly ++; 
    if (vetPoly(poly)) {
	if (i == 0) {
	    open.shift()
	} else {
	    open = open.slice(i + 1).concat(open.slice(0, i))
	}
	pat.push(poly)
	return true; 
    } 
    return false;
}

function tryMaker(maker, alt_maker) {
    if (open.length <= 0) {
	return false
    }
    try_maker++;
    for (let i=0 ; i<open.length ; ++i) {
	let poly = maker(...open[i])
	if (tryPoly(poly, i)) {
	    return true;
	}
	if (alt_maker) {
	    poly = alt_maker(...open[i])
	    if (tryPoly(poly, i)) {
		return true;
	    }
	}
    }
    return false;
}

function takeNumber(str, idx) {
    let numberStr = '';
    while (idx < str.length && /\d/.test(str[idx])) {
	numberStr += str[idx];
	idx++;
    }
    return [idx, parseInt(numberStr)]
}

function parenEnd(str, idx) {
    let parenCount = 1; 
    while (idx < str.length) {
	if (str[idx] == "(") {
	    parenCount += 1;
	} else if (str[idx] == ")") {
	    parenCount -= 1;
	}
	if (parenCount === 0) {
	    return idx + 1;
	}
	++idx; 
    }
    return false;
}

function repeatLetters(input) {
    // Remove all whitespace from the input string
    input = input.replace(/\s+/g, '');
    
    let result = '';
    let i = 0;
    
    while (i < input.length) {
	const currentChar = input[i];

	if (currentChar == "(") {
	    let end = parenEnd(input, i + 1)
	    let [after, num] = takeNumber(input, end);
	    if (num) {
		input = input.slice(0, i) + 
		    input.slice(i + 1, end - 1).repeat(num) +
		    input.slice(after);
	    } else {
		i++;
	    }
	    continue;
	}

	let [newidx, num] = takeNumber(input, i + 1);


	result += currentChar.repeat(min(num || 1, 2500));
	i = max(newidx, i+1);
    }
    
    return result;
}

function lineAntiEqual(l1, l2) {
    for (let i=0 ; i<2 ; ++i) {
	for (let j=0 ; j<2 ; ++j) {
	    if (!l1[i][j].eql(l2[1-i][j])) {
		return false;
	    }
	}
    }
    return true;
}

function delAntiLine(l) {
    for (let i=0 ; i<open.length ; ++i) {
	if (lineAntiEqual(l, open[i])) {
	    open.splice(i, 1)
	    return true;
	} 
    }
    return false; 
}

function doLetter(key) {
    let pat_len = pat.length; 
    if (open.length == 0) {
	return; 
    }
    key = key.toLowerCase()

    if (key === "w") {
	tryMaker(Pat.makeHex())
    } else if (key === "a") {
	tryMaker(Pat.makeSquare())
    } else if (key === "s") {
	tryMaker(Pat.makeOcto())
    } else if (key === "d") {
	tryMaker(Pat.makeRho(), Pat.makeRhoRev())
    } else if (key === "f") {
	tryMaker(Pat.makeRhoRev(), Pat.makeRho())
    } else if (key === "e") {
	tryMaker(Pat.makeNeedle(), Pat.makeNeedleRev())
    } else if (key === "r") {
	tryMaker(Pat.makeNeedleRev(), Pat.makeNeedle())
    } else if (key === "q") {
	tryMaker(Pat.makeTri())
    } else if (key === "c") {
	tryMaker(Pat.makeTrap(), Pat.makeTrapRev())
    } else if (key === "v") {
	tryMaker(Pat.makeTrapRev(), Pat.makeTrap())
    } else if (key === "b") {
	tryMaker(Pat.makeTrapRev2())
    } else if (key == "z") { 
	open.push(open.shift());
    } else if (key == "x") { 
	open.unshift(open.pop());
    } else if (key === "y") { // WHITE TEAM
	tryMaker(Pat.makeHex(255))
    } else if (key === "g") {
	tryMaker(Pat.makeSquare(255))
    } else if (key === "h") {
	tryMaker(Pat.makeOcto(255))
    } else if (key === "j") {
	tryMaker(Pat.makeRho(255), Pat.makeRhoRev(255))
    } else if (key === "k") {
	tryMaker(Pat.makeRhoRev(255), Pat.makeRho(255))
    } else if (key === "u") {
	tryMaker(Pat.makeNeedle(255), Pat.makeNeedleRev(255))
    } else if (key === "i") {
	tryMaker(Pat.makeNeedleRev(255), Pat.makeNeedle(255))
    } else if (key === "t") {
	tryMaker(Pat.makeTri(255))
    } else if (key === "n") {
	tryMaker(Pat.makeTrap(255), Pat.makeTrapRev(255))
    } else if (key === "m") {
	tryMaker(Pat.makeTrapRev(255), Pat.makeTrap(255))
    } else if (key === "l") {
	tryMaker(Pat.makeTrapRev2(255))
    } else if (key == "o") { 
	open.push(open.shift());
    } else if (key == "p") { 
	open.unshift(open.pop());
    }

    if (pat.length > pat_len) {
	let pts = pat[pat.length - 1].points
	let n = pts.length
	if (pat_len == 0) {
	    for (let i=0 ; i<n ; ++i) {
		open.push([pts[(i + 1) % n], pts[i]])
	    }
	} else {
	    for (let i=1 ; i<n ; ++i) {
		let l = [pts[(i + 1) % n], pts[i]]
		if (!delAntiLine(l)) {
		    open.push(l)
		}
	    }	    
	}
    }
}
