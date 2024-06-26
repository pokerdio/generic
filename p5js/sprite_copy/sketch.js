let img;

let white = [255,255,255]
let black = [0,0,0]

let area = {x1:0.0, y1:0.0, x2:1.0, y2:1.0};
let oldArea = {x1:0.0, y1:0.0, x2:1.0, y2:1.0};

let grid = {x1:0.0, y1:0.0, x2:1.0, y2:1.0};

let gridX = 10, gridY = 10; 
let startX, startY;
let isDragging = false;
let command = "grid"; 

function setup() {
    let canvas = createCanvas(800, 600);
    canvas.parent('canvasContainer');

    noSmooth()
    // Add an event listener for pasting images
    document.addEventListener('paste', handlePaste);
}

function toZoom(x, y) {
    return [map(x, area.x1, area.x2, 0, 1), map(y, area.y1, area.y2, 0, 1)]
}

function draw() {
    background(220);

    if (!img) {
	return;
    }
    // Draw the selected region scaled up to fit the canvas
    console.log (width, height, "-----", 
		 width * area.x1, height * area.y1, 
		 width * (area.x2 - area.x1), height * (area.y2 - area.y1));
    image(img, 0, 0, width, height, width * area.x1, height * area.y1, 
	  width * (area.x2 - area.x1), height * (area.y2 - area.y1));
    if (isDragging) {
	// Draw the selection rectangle
	noFill();
	if (command == "grid") {
	    stroke(255, 0, 0);
	} else {
	    stroke(0, 255, 0);	    
	}
	rect(startX, startY, mouseX - startX, mouseY - startY);
    }
    
    strokeWeight(1.0);
    stroke("red");


    let [x1, y1] = toZoom(grid.x1, grid.y1);
    let [x2, y2] = toZoom(grid.x2, grid.y2);
    for (i=0 ; i<=gridY ; ++i) {
	let y = map(i, 0, gridY, y1, y2) * height;
	line(x1 * width, y, x2 * width, y);
    }
    for (i=0 ; i<=gridX ; ++i) {
	let x = map(i, 0, gridX, x1, x2) * width;
	line(x, y1 * height, x, y2 * height);
    }
}

function mousePressed() {
    if (img) {
	// Start dragging
	startX = mouseX;
	startY = mouseY;
	isDragging = true;
    }
}

function mouseReleased() {
    if (img) {
	// End dragging and set the cut region
	isDragging = false;

	let endX = mouseX;
	let endY = mouseY;

	// Ensure the rectangle is within the bounds of the image
	let x1 = constrain(min(startX, endX), 0, width) / width;
	let y1 = constrain(min(startY, endY), 0, height) / height;
	let x2 = constrain(max(startX, endX), 0, width) / width;
	let y2 = constrain(max(startY, endY), 0, height) / height;

	console.log("mouse rel ", x1, y1, x2, y2);

	x1 = area.x1 + x1 * (area.x2 - area.x1); 
	x2 = area.x1 + x2 * (area.x2 - area.x1); 
	y1 = area.y1 + y1 * (area.y2 - area.y1); 
	y2 = area.y1 + y2 * (area.y2 - area.y1); 

	console.log("mouse rel phase 2 - ", x1, y1, x2, y2);
	let target; 
	if (command == "grid") {
	    target = grid;
	} else {
	    target = area;
	}
	target.x1 = x1;
	target.x2 = x2;
	target.y1 = y1;
	target.y2 = y2; 

	command = "grid";

	// // Map the rectangle coordinates to the image coordinates
	// let imgX = map(x, 0, width, 0, img.width);
	// let imgY = map(y, 0, height, 0, img.height);
	// let imgW = map(w, 0, width, 0, img.width);
	// let imgH = map(h, 0, height, 0, img.height);

	// cutRegion = { x: imgX, y: imgY, w: imgW, h: imgH };
    }
}

function handlePaste(event) {
    const items = (event.clipboardData || event.originalEvent.clipboardData).items;
    for (let i = 0; i < items.length; i++) {
	if (items[i].type.indexOf('image') !== -1) {
	    const blob = items[i].getAsFile();
	    const url = URL.createObjectURL(blob);
	    img = loadImage(url, (loadedImg) => {
		area = {x1:0.0, y1:0.0, x2:1.0, y2:1.0};
		grid = {x1:0.0, y1:0.0, x2:1.0, y2:1.0};
		resizeCanvas(loadedImg.width, loadedImg.height);
	    });
	}
    }
}

function getPixel(img, x, y) {
    // Ensure the coordinates are within the image bounds
    x = constrain(x, 0, img.width - 1);
    y = constrain(y, 0, img.height - 1);

    // Get the color of the pixel at (x, y)
    let c = img.get(x, y);

    // Extract the RGB components
    let r = red(c);
    let g = green(c);
    let b = blue(c);

    return [r, g, b];
}

function colDist(col1, col2) {
    return abs(col1[0] - col2[0]) + abs(col1[1] - col2[1]) + abs(col1[2] - col2[2]);
}

function exportPix(reverse) {
    let s = "{" + (gridX + 1) + "," + (gridY + 1) 

    for (i=0 ; i<= gridY ; ++i) {
	for (j=0 ; j<= gridX ; ++j) {
	    let x = map(j, 0, gridX, grid.x1, grid.x2) * img.width;
	    let y = map(i, 0, gridY, grid.y1, grid.y2) * img.height;

	    let c = getPixel(img, x, y); 
	    s = s + "," + int(reverse ^ (colDist(white, c) > colDist(black, c)));
	}
    }
    s = s + "}"
    console.log(s);
    copyTextToClipboard(s);
}


function keyPressed() {
    console.log("keypressed ", key)
    if (key === "a") {
	white = getPixel(img, mouseX, mouseY);
    } else if (key === "b" || key === "A") {
	black = getPixel(img, mouseX, mouseY);	
    } else if (key === 'w') {
	gridX += 1; 
    } else if (key === 'W') {
	gridX = max(1, gridX - 1); 
    } else if (key === 'h') {
	gridY += 1; 
    } else if (key === 'H') {
	gridY = max(1, gridY - 1); 
    } if (key === 'g') {
	command = "grid";
    } if (key === 'Z') {
	if (area.x1 > 0 || area.x2 < 1.0) {
	    oldArea = area; 	    
	    area = {x1:0.0, y1:0.0, x2:1.0, y2:1.0};
	} else {
	    area = oldArea; 
	}
    } else if (key === 'z') {
	command = "zoom"
    } if (key === "x") {
	exportPix(false);
    } else if (key === "X") {
	exportPix(true);
    }
}




function copyTextToClipboard(text) {
    // Create a temporary textarea element to hold the text
    const textarea = document.createElement('textarea');
    textarea.value = text;

    // Set the textarea to be invisible
    textarea.style.position = 'absolute';
    textarea.style.left = '-9999px';

    document.body.appendChild(textarea);

    // Select and copy the text inside the textarea
    textarea.select();
    document.execCommand('copy');

    // Remove the textarea from the DOM
    document.body.removeChild(textarea);
}
