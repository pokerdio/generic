let img;
let pat = []

let open = [[[0.0, 0.0], [1.0, 0.0]]]

let box = [-2, -2, 2, 2]

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

function draw() {
    box = approachBox(box, getBox(pat))
    background(120);
    push();
    fitBoxToCanvas(box);
    for (let p of pat) {
	p.draw();
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
    // 	strokeWeight(0.04);
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

    pat = [];
    open = [[[0.0, 0.0], [1.0, 0.0]]];

    let processedValue = repeatLetters(value);

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

function tryPoly(maker) {
    if (open.length <= 0) {
	return false
    }

    for (let i=0 ; i<open.length ; ++i) {
	let poly = maker(...open[i])
	if (vetPoly(poly)) {
	    if (i == 0) {
		open.shift()
	    } else {
		let cut = open.slice(0, i)
		open.shift()
		open = open.concat(cut);
	    }
	    pat.push(poly)
	    return true; 
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


	result += currentChar.repeat(min(num || 1, 99));
	i = max(newidx, i+1);
    }
    
    return result;
}

function doLetter(key) {
    let pat_len = pat.length; 
    vetOpen(); 
    if (open.length == 0) {
	return; 
    }

    if (key === "h") {
	tryPoly(Pat.makeHex)
    } else if (key === "s") {
	tryPoly(Pat.makeSquare)
    } else if (key === "r") {
	tryPoly(Pat.makeRho)
    } else if (key === "R") {
	tryPoly(Pat.makeRhoRev)
    } else if (key === "n") {
	tryPoly(Pat.makeNeedle)
    } else if (key === "N") {
	tryPoly(Pat.makeNeedleRev)
    } else if (key === "t") {
	tryPoly(Pat.makeTri)
    } else if (key === "a") {
	tryPoly(Pat.makeTrap)
    } else if (key === "b") {
	tryPoly(Pat.makeTrapRev)
    } else if (key === "B") {
	tryPoly(Pat.makeTrapRev2)
    } else if (key == "k") { //"sKip"
	open.push(open.shift());
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
		if (vetLine(l)) {
		    open.push(l)
		}
	    }	    
	}
    }
    vetOpen();
}
