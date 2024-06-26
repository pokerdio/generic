class Atom {
    static w = 400;
    static h = 400;
    static halfw = 200;
    static halfh = 200;
    static interact_d = 20;

    static colors = ["red", "lime", "deepskyblue", "yellow"];
    constructor(x, y, color) {
	if (x == undefined) {
	    x = random(Atom.w);
	}
	if (y == undefined) {
	    y = random(Atom.h);
	}

	if (color == undefined) {
	    color = Atom.colors[floor(random(Atom.colors.length - 0.0001))];
	}
	this.color = color;
	this.pos = createVector(x, y);
	this.v = createVector(random(-2, 2), random(-2, 2));
	this.f = createVector(0, 0);
    }
    towardsVector(other) {
	let ret = other.pos.copy();
	ret.sub(this.pos);
	if (ret.x > Atom.halfW) {
	    ret.x -= Atom.w;
	} else if (ret.x < -Atom.halfW) {
	    ret.x += Atom.w;
	}
	if (ret.y > Atom.halfH) {
	    ret.y -= Atom.h;
	} else if (ret.y < -Atom.halfH) {
	    ret.y += Atom.h;
	}
	return ret;
    }
    interact(other) {
	let vs = towardsVector(other);
	let d = vs.mag();
	if (d > Atom.interact_d) {
	    return;
	}

	
    }

    update() {
	this.pos.add(this.v);
	this.pos.x = (Atom.w + this.pos.x) % Atom.w;
	this.pos.y = (Atom.h + this.pos.y) % Atom.h;
	this.f.set(0, 0);
    }
    display() {
	noStroke();
	fill(this.color);
	ellipse(this.pos.x, this.pos.y, 8, 8);
    }
}
