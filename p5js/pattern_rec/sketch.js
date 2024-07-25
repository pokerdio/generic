let img;
let pat = []

let try_poly = 0;
let try_maker = 0; 

let nomZero = new Nom(0)
let nomOne = new Nom(1)
let lineZero = [[nomZero, nomZero], [nomOne, nomZero]]
    
let box = [-2, -2, 2, 2]

let lastProcessedCommand = "";

function resetPats() {
    pat = [];
    tiling1_Octo(...lineZero, 5, tryPoly)
}

function setup() {
    let canvas = createCanvas(800, 600);
    canvas.parent('canvasContainer');

    strokeWeight(0.02)
    noSmooth()
    resetPats()
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


    // let processedValue = repeatLetters(value);
    // if (processedValue.startsWith(lastProcessedCommand)) {
    // 	let len = lastProcessedCommand.length
    // 	lastProcessedCommand = processedValue;
    // 	processedValue = processedValue.slice(len)
    // } else {
    // 	lastProcessedCommand = processedValue;
    // 	resetPats()
    // }
}

function segmentId(a, b) {
    return a.toString() + "%" + b.toString()
}

function tryPoly(poly) {
    console.log("try poly" + poly)
    try_poly++; 
    for (let p of pat) {
	if (poly.intersect(p)) {
	    console.log("fail")
	    return false; 
	}
    }
    pat.push(poly)
    console.log("success", pat.length)
    return true;
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

function lineEqual(l1, l2) {
    for (let i=0 ; i<2 ; ++i) {
	for (let j=0 ; j<2 ; ++j) {
	    if (!l1[i][j].eql(l2[i][j])) {
		return false;
	    }
	}
    }
    return true;
}

