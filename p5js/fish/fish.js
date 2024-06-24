class Fish {
    static w = 800;
    static h = 400;
    static halfw = 400;
    static halfh = 200;
    static interact_d = 20;

    static colors = ["red", "lime", "deepskyblue", "yellow"];
    constructor(x, y, color, speed, size) {
	if (speed == undefined) {
	    speed = random(0.5,3);
	}
	this.speed = speed;
	this.size = size || random(0.75, 1.25);
	if (x == undefined) {
	    x = random(Fish.w);
	}
	if (y == undefined) {
	    y = random(Fish.h);
	}

	if (color == undefined) {
	    color = Fish.colors[floor(random(Fish.colors.length - 0.0001))];
	}
	this.color = color;
	this.pos = createVector(x, y);
	this.v = createVector(random(-2, 2), random(-2, 2));
	this.v.setMag(this.speed);
	this.f = createVector(0, 0);
    }

    setFollow(other_fish) {
	if (this != other_fish) {
	    this.follow = other_fish;
	} else {
	    this.follow = undefined;
	}
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
//	let rel_pos = this.follow.pos.copy().sub(this.pos);
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
	let color = this.color;
	fill(this.color);

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
		translate(x0, y0);
		scale(this.size);
		rotate(-atan2(this.v.x, this.v.y));

		ellipse(0, 0, 35, 90);

		strokeWeight(0.5);
		fill("white");
		ellipse(-6, 30, 8, 8);
		ellipse(6, 30, 8, 8);

		fill("black");
		ellipse(-6, 31, 4, 4)
		ellipse(6, 31, 4, 4)

		translate(0, -45);
		rotate(30 * sin(frameCount * 6 * this.speed));
		strokeWeight(2.0);
		fill(this.color);
		triangle(0, 0, 10,-20,-10,-20);

		pop();
	    }
	}
    }
}
