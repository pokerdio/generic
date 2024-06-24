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


// Function to save alpha values of a graphics object
function saveAlphaValues(graphicsObj) {
    ret = [];
    graphicsObj.loadPixels();
    for (let i = 0; i < graphicsObj.pixels.length; i += 4) {
	// Save alpha value (index + 3 in the pixels array)
	ret.push(graphicsObj.pixels[i + 3]);
    }
    return ret; 
}

// Function to restore alpha values of a graphics object
function restoreAlphaValues(graphicsObj, vals) {
    graphicsObj.loadPixels();
    let k = 0;
    for (let i = 0; i < graphicsObj.pixels.length; i += 4) {
	// Restore alpha value (index + 3 in the pixels array)
	graphicsObj.pixels[i + 3] = vals[k++];
    }
    graphicsObj.updatePixels();
}

class FishGfx {
    constructor (vert, cols, tail) {
	if (!cols.length) {
	    cols.push("black");
	}
	this.tail_color = tail;
	this.colors = cols;
	let w = 50;
	let h = 120;
	this.gfx = createGraphics (w, h);

	let gfx = this.gfx;
	gfx.fill(255);
	gfx.smooth();
	gfx.translate(gfx.width / 2, gfx.height / 2)
	gfx.strokeWeight(3.5);
	gfx.ellipse(0, 0, w - 2, h - 2);

	gfx.noStroke();
	let alpha_val = saveAlphaValues(gfx);
	gfx.blendMode(MULTIPLY);

	for (let i=0 ; i<cols.length ; ++i) {
	    gfx.fill(cols[i]);
	    if (vert) {
		gfx.rect(i * w / cols.length - w/2, -h/2, w / cols.length, h);
	    } else {
		gfx.rect(-w/2, i * h / cols.length - h/2, w, h / cols.length);
	    }
	}
	restoreAlphaValues(gfx, alpha_val);

	gfx.blendMode(BLEND);
	gfx.strokeWeight(1.5);
	gfx.stroke(0);
	gfx.fill("white");
	let d = 18
	let dx = 12
	gfx.ellipse(-dx, 30, d, d);
	gfx.ellipse(dx, 30, d, d);

	gfx.fill("black");
	d = 9
	let dy = 3
	gfx.ellipse(-dx, 30 + dy, d, d)
	gfx.ellipse(dx, 30 + dy, d, d)
    }
    display (size, x, y) {
	push();
	noStroke();
	let w = size * this.gfx.width;
	let h = size * this.gfx.height;
	image(this.gfx, x - w/2, y - h/2, w, h);
	pop();
    }
}

class Fish {
    static w = 800;
    static h = 400;
    static halfw = 400;
    static halfh = 200;
    static interact_d = 20;

    constructor(gfx, x, y, speed, size) {
	this.gfx = gfx;
	if (speed == undefined) {
	    speed = random(0.5,3);
	}
	this.speed = speed;
	this.size = size || random(0.25, 0.35);
	if (x == undefined) {
	    x = random(Fish.w);
	}
	if (y == undefined) {
	    y = random(Fish.h);
	}

	this.pos = createVector(x, y);
	this.v = createVector(random(-2, 2), random(-2, 2));
	this.v.setMag(this.speed);
	this.f = createVector(0, 0);
    }

    towardsVector(other) {
	let ret = other.pos.copy();
	ret.sub(this.pos);
	if (ret.x > Fish.halfw) {
	    ret.x -= Fish.w;
	} else if (ret.x < -Fish.halfw) {
	    ret.x += Fish.w;
	}
	if (ret.y > Fish.halfh) {
	    ret.y -= Fish.h;
	} else if (ret.y < -Fish.halfh) {
	    ret.y += Fish.h;
	}
	return ret;
    }

    update_follow() {
	let rel_pos = this.towardsVector(this.follow);
	if (rel_pos.mag () < 5) {
	    this.follow = undefined;
	    return;
	}

	let a = this.v.angleBetween(rel_pos);

	let max_rot = 2 * this.speed;
	if (a > max_rot) {
	    a = max_rot;
	}
	if (a < -max_rot) {
	    a = -max_rot;
	}
	this.v.rotate(a);
    }
    
    update_stroll() {
	let delta = 0.02 * this.speed;
	this.v.x += random(-delta, +delta);
	this.v.y += random(-delta, delta);
    }
    update() {
	if (this.follow) {
	    this.update_follow();
	} else {
	    this.update_stroll();
	}

	this.v.setMag(this.speed);

	this.pos.add(this.v);
	this.pos.x = (Fish.w + this.pos.x) % Fish.w;
	this.pos.y = (Fish.h + this.pos.y) % Fish.h;
	this.f.set(0, 0);
    }
    display() {
	strokeWeight(2);
	stroke("black")
	let i=0;
	let j=0;
	for (i=-1 ; i<=1 ; ++i) {
	    for (j=-1 ; j<=1 ; ++j) {
		let x0 = i * Fish.w + this.pos.x;
		let y0 = j * Fish.h + this.pos.y;
		if (x0 < -100 || x0 > Fish.w + 100) {
		    continue;
		}
		if (y0 < -100 || y0 > Fish.h + 100) {
		    continue;
		}
		push();
//		translate(x0 - Fish.w / 2, y0 - Fish.h / 2);
		translate(x0, y0);
		scale(this.size);
		rotate(-atan2(this.v.x, this.v.y));
		this.gfx.display(1, 0, 0);

		translate(0, -60);
		rotate(30 * sin(frameCount * 6 * this.speed));
		strokeWeight(2.0);
		fill(this.gfx.tail_color);
		triangle(8,-24,-8,-24, 0, 0);
		pop();
	    }
	}
    }
}
