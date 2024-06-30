let img;

function setup() {
    let canvas = createCanvas(800, 600);
    canvas.parent('canvasContainer');

    noSmooth()
    // Add an event listener for pasting images
    document.addEventListener('paste', handlePaste);
}

function draw() {
    background(220);

    if (!img) {
	return;
    }
    strokeWeight(1.0);
    stroke("red");
    
}

function mousePressed() {
}

function mouseReleased() {
    let endX = mouseX;
    let endY = mouseY;
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
