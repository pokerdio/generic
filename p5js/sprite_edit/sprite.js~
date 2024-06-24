class PixelSprite {
    static color = {lit:'white', dark:'black', transparent:'gray'}
    constructor(cols, rows) {
	this.cols = cols;
	this.rows = rows;
	this.pixels = new Array(cols * rows).fill('transparent');
    }

    clone() {
	let obj = new PixelSprite(this.cols, this.rows);
	for (let i=0 ; i<this.rows ; ++i) {
	    for (let j=0 ; j<this.cols ; ++j) {
		obj.setPixel(j, i, this.getPixel(j, i))
	    }
	}
	return obj; 
    }

    // ellipse(cx, cy, rx, ry, col) {
    // 	let aa = (rx + 0.5) * (rx + 0.5);
    // 	let bb = (ry + 0.5) * (ry + 0.5);
    // 	let a2b2 = aa * bb; 
    // 	for (let x=-rx ; x<=rx ; ++x) {
    // 	    for (let y=-ry ; y<=ry ; ++y) {
    // 		if (x * x * bb + y * y * aa <= a2b2) {
    // 		    this.setPixel(x + cx, y + cy, col);
    // 		}
    // 	    }
    // 	}
    // }
    ellipse(x0, y0, w, h, col) {
	console.log("ellipse on", x0, y0, w, h, col)
	if (w <= 1 || h <= 1) {
	    return this.fillRect(x0, y0, w, h, col);
	}
	let cx = x0 + (w - 1) / 2.0;
	let cy = y0 + (h - 1) / 2.0;
	let rx = w / 2.0;
	let ry = h / 2.0; 
	let aa = rx * rx; 
	let bb = ry * ry; 
	let a2b2 = aa * bb; 

	for (let x=x0 ; x<x0+w ; ++x) {
	    for (let y=y0 ; y<y0+h ; ++y) {
		let dx = cx - x;
		let dy = cy - y; 

		console.log(x, y, dx, dy, "-", cx, cy, "-", rx, ry)
		if (dx * dx * bb + dy * dy * aa <= a2b2) {
		    this.setPixel(x, y, col);
		}
	    }
	}
    }
    fillEllipse(x0, y0, w, h, col, otherCol) {
	if (w <= 2 || h <= 2) {
	    return this.ellipse(x0, y0, w, h, col);
	}
	this.ellipse(x0, y0, w, h, col);
	this.ellipse(x0 + 1, y0 + 1, w - 2, h - 2, otherCol);
    }

    isEqual(other) {
	if (this.cols != other.cols || this.rows != other.rows) {
	    return false 
	}
	for (let i=0 ; i<this.rows ; ++i) {
	    for (let j=0 ; j<this.cols ; ++j) {
		if (other.getPixel(j, i) != this.getPixel(j, i)) {
		    return false;
		}
	    }
	}
	return true; 
    }

    fill(col) {
	for(let i=0 ; i<this.pixels.length ; ++i) {
	    this.pixels[i] = col || "transparent";
	}
    }

    fillRect(x, y, w, h, col) {
	for (let i=y ; i<y+h ; ++i) {
	    for (let j=x ; j<x+w ; ++j) {
		this.setPixel(j, i, col);
	    }
	}
    }

    fillBox(x, y, w, h, outCol, innerCol) {
	this.fillRect(x, y, w, h, outCol);

	if (w > 2 && h > 2) {
	    this.fillRect(x + 1, y + 1, w - 2, h - 2, innerCol);
	}
    }

    line(x1, y1, x2, y2, col) {
	let dx = abs(x2 - x1);
	let dy = abs(y2 - y1);
	let sx = (x1 < x2) ? 1 : -1;
	let sy = (y1 < y2) ? 1 : -1;

	let err = dx - dy;
	for (let i=0 ; i<100 ; ++i) {
	    this.setPixel(x1, y1, col);
	    if (x1 == x2 && y1 == y2) {
		break;
	    }
	    let e2 = 2 * err;
	    if (e2 > -dy) {
		err -= dy;
		x1 += sx;
	    }
	    if (e2 < dx) {
		err += dx;
		y1 += sy;
	    }
	}
    }

    fatLine(x1, y1, x2, y2, col) {
	let dx = abs(x2 - x1);
	let dy = abs(y2 - y1);
	let sx = (x1 < x2) ? 1 : -1;
	let sy = (y1 < y2) ? 1 : -1;

	let err = dx - dy;
	for (let i=0 ; i<100 ; ++i) {
	    this.setPixel(x1, y1, col);
	    if (x1 == x2 && y1 == y2) {
		break;
	    }
	    let e2 = 2 * err;

	    if (e2 > -dy && e2 < dx) {
		if (e2 + dy > dx - e2)  {
		    err -= dy;
		    x1 += sx;
		} else {
		    err += dx;
		    y1 += sy;
		}
	    } else if (e2 > -dy) {
		err -= dy;
		x1 += sx;
	    } else if (e2 < dx) {
		err += dx;
		y1 += sy;
	    }
	}
    }
    rect(x, y, w, h, col) {
	for (let i=y ; i<y+h ; ++i) {
	    console.log(i, y+h)
	    this.setPixel(x, i, col);
	    this.setPixel(x + w - 1, i, col);
	}
	for (let j=x ; j<x+w ; ++j) {
	    console.log(j, x+w)
	    this.setPixel(j, y, col);
	    this.setPixel(j, y + h - 1, col);
	}
    }

    insertColumn(xPos) {
	if (xPos < 0 || xPos >= this.cols) {
	    return;
	}
	for (let y=0 ; y<this.rows ; ++y) {
	    for (let x=this.cols-1 ; x>xPos ; --x) {
		this.setPixel(x, y, this.getPixel(x - 1, y));
	    }
//	    this.setPixel(xPos, y, "transparent")
	}
    }
    deleteColumn(xPos) {
	if (xPos < 0 || xPos >= this.cols) {
	    return;
	}
	for (let y=0 ; y<this.rows ; ++y) {
	    for (let x=xPos ; x<this.cols-1 ; ++x) {
		this.setPixel(x, y, this.getPixel(x + 1, y));
	    }
	    this.setPixel(this.cols-1, y, "transparent")
	}
    }
    insertRow(yPos) {
	if (yPos < 0 || yPos >= this.rows) {
	    return;
	}
	for (let x=0 ; x<this.cols ; ++x) {
	    for (let y=this.rows-1 ; y>yPos ; --y) {
		this.setPixel(x, y, this.getPixel(x, y - 1));
	    }
//	    this.setPixel(x, yPos, "transparent")
	}
    }
    deleteRow(yPos) {
	if (yPos < 0 || yPos >= this.rows) {
	    return;
	}
	for (let x=0 ; x<this.cols ; ++x) {
	    for (let y=yPos ; y<this.rows-1 ; ++y) {
		this.setPixel(x, y, this.getPixel(x, y + 1));
	    }
	    this.setPixel(x, this.rows-1, "transparent")
	}
    }

    center() {
	let [minX, minY, width, height] = this.getBoundingBox();
	let desired_minX = floor((this.cols - width) / 2);
	let desired_minY = floor((this.rows - height) / 2);
	console.log("center", minX, desired_minX)
	if (minX > desired_minX) {
	    for (let x=minX ; x>desired_minX ; --x) {
		this.deleteColumn(0);
	    }
	} else {
	    for (let x=minX ; x<desired_minX ; ++x) {
		this.insertColumn(0);
	    }
	}
	if (minY > desired_minY) {
	    for (let y=minY ; y>desired_minY ; --y) {
		this.deleteRow(0);
	    }
	} else {
	    for (let y=minY ; y<desired_minY ; ++y) {
		this.insertRow(0);
	    }
	}
    }
    

    paintFill(x, y, newCol) {
	if (x < 0 || x >= this.cols || y < 0 || y >= this.cols) {
	    return;
	}
	const oldCol = this.getPixel(x, y);
	if (!oldCol || (oldCol == newCol)) {
	    return;
	}
	const queue = [{x: x, y: y}];

	while (queue.length > 0) {
            const current = queue.shift();
            const { x, y } = current;
	    if (this.getPixel(x, y) != oldCol) {
		continue; 
	    }
            this.setPixel(x, y, newCol);

            // Check left
            if (x > 0 && this.getPixel(x - 1, y) === oldCol) {
		queue.push({x: x - 1, y: y});
            }

            // Check right
            if (x < this.cols-1 && this.getPixel(x + 1, y) === oldCol) {
		queue.push({x: x + 1, y: y});
            }

            // Check up
            if (y > 0 && this.getPixel(x, y - 1) === oldCol) {
		queue.push({x: x, y: y - 1});
            }

            // Check down
            if (y < this.rows-1 && this.getPixel(x, y + 1) === oldCol) {
		queue.push({x: x, y: y + 1});
            }
	}
    }

    paintFillStrict(x, y, newCol) {
	if (x < 0 || x >= this.cols || y < 0 || y >= this.cols) {
	    return;
	}
	const oldCol = this.getPixel(x, y);
	if (!oldCol || (oldCol == newCol)) {
	    return;
	}
	const queue = [{x: x, y: y}];

	let clone = this.clone();

	while (queue.length > 0) {
            const current = queue.shift();
            const { x, y } = current;
	    if (this.getPixel(x, y) != oldCol) {
		continue; 
	    }
	    let not_ok = false; 
	    for (let dxy of [[-1,0],[1,0],[0,1],[0,-1]]) {
		let [dx, dy] = dxy; 
		let pixel = clone.getPixel(x + dx, y + dy);
		console.log(dxy, dx, dy)
		if (null != pixel && oldCol != pixel) {
		    not_ok = true;
		    break; 
		}
	    }
	    if (not_ok) {
		continue; 
	    }
            this.setPixel(x, y, newCol);

            // Check left
            if (x > 0 && this.getPixel(x - 1, y) === oldCol) {
		queue.push({x: x - 1, y: y});
            }

            // Check right
            if (x < this.cols-1 && this.getPixel(x + 1, y) === oldCol) {
		queue.push({x: x + 1, y: y});
            }

            // Check up
            if (y > 0 && this.getPixel(x, y - 1) === oldCol) {
		queue.push({x: x, y: y - 1});
            }

            // Check down
            if (y < this.rows-1 && this.getPixel(x, y + 1) === oldCol) {
		queue.push({x: x, y: y + 1});
            }
	}
    }
    importPixels(pixArray) {
	let dx = Math.floor((this.cols - pixArray[0]) / 2)
	let dy = Math.floor((this.rows - pixArray[1]) / 2)
	const colorMap = { 2:'transparent', 0:'dark', 1:'lit'};

	let i = 0; 
	for (let y=dy ; y<pixArray[1]+dy ; ++y) {
	    for (let x=dx ; x<pixArray[0]+dx ; ++x) {
		this.pixels[y * this.cols + x] = colorMap[pixArray[2 + i++]];
	    }
	}
    }

    setPixel(x, y, color) {
	const index = x + y * this.cols;
	if (x >= 0 && x < this.cols && y >= 0 && y < this.rows) {
	    this.pixels[index] = color;
	}
    }

    getPixel(x, y) {
	const index = x + y * this.cols;
	if (x >= 0 && x < this.cols && y >= 0 && y < this.rows) {
	    return this.pixels[index];
	}
	return null;
    }

    display(pointX, pointY) {
	noStroke()
	let count = 0; 
	for (let y = 0; y < this.rows; y++) {
	    for (let x = 0; x < this.cols; x++) {
		count ++; 
		const color = PixelSprite.color[this.getPixel(x, y)];
		fill(color);
		rect(x * pixelSize, y * pixelSize, pixelSize-1, pixelSize-1);
	    }
	}
	if (typeof(pointX) == "number" && typeof(pointY) == "number" &&
	    pointX >= 0 && pointX < this.cols && 
	    pointY >= 0 && pointY < this.rows) 
	{
	    strokeWeight(1.0);
	    stroke(0);
	    fill("red");
	    ellipse(pointX * pixelSize + pixelSize / 2.0, 
		    pointY * pixelSize + pixelSize / 2.0, 
		    pixelSize / 2.0, pixelSize / 2.0);	    
	}
    }
    sprite(xpos, ypos) {
	xpos = floor(xpos || 0);
	ypos = floor(ypos || 0);
	push();

	for (let y = 0; y < this.rows; y++) {
	    for (let x=0; x < this.cols; x++) {
		switch(this.getPixel(x, y)) {
		case "lit":
		    noStroke();
		    fill(255);
		    rect(xpos + x * 2, ypos + y * 2, 2, 2);
		    break;
		case "dark":
		    noStroke()
		    fill(0);
		    rect(xpos + x * 2, ypos + y * 2, 2, 2);
		    break;
		}
	    }
	}
	pop();
    }
    getBoundingBox() {
	let minX = Infinity;
	let minY = Infinity;
	let maxX = -Infinity;
	let maxY = -Infinity;

	for (let y = 0; y < this.rows; y++) {
	    for (let x = 0; x < this.cols; x++) {
		const color = this.getPixel(x, y);
		if (color !== 'transparent') {
		    minX = Math.min(minX, x);
		    minY = Math.min(minY, y);
		    maxX = Math.max(maxX, x);
		    maxY = Math.max(maxY, y);
		}
	    }
	}

	if (minX === Infinity) {
	    return [0, 0, 0, 0];
	}
	const width = maxX - minX + 1;
	const height = maxY - minY + 1;

	return [minX, minY, width, height];
    }

    exportToCArray() {
	const bb = this.getBoundingBox();

	if (!bb[2] || !bb[3]) {
	    return "const uint8_t sprite[] = {0, 0};\n";
	}
	let cArray = `const uint8_t sprite[] = {${bb[2]}, ${bb[3]}, \n`;
	const colorMap = { 'transparent': 2, 'dark': 0, 'lit': 1 };


	for (let y = bb[1]; y<bb[1]+bb[3] ; y++) {
	    for (let x = bb[0]; x<bb[0]+bb[2] ; x++) {
		const pixel = this.getPixel(x, y);
		const value = colorMap[pixel];
		cArray += value + ', ';
	    }
	    cArray += '\n';
	}
	cArray = cArray.slice(0, -3) + '\n};';
	console.log(cArray); // Print C language array representation
	return cArray;
    }
}
