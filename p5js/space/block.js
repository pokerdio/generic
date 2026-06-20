class Generator {


    constructor(type, entry_time, parameter_array) {
	this.type = type;
	this.entry_time = entry_time;
	this.parameter_array = parameter_array;
    }
}

class Block {
    constructor() {
	this.x = random(width);
	this.y = 0;
	this.size = random(config.max_size / 4.0, 
			   config.max_size)
    }

    display() {
	push();
	translate(this.x, this.y);
	strokeWeight(2.5);
	stroke(255, 0, 100);
	fill(0, 50, 75);
	circle(0, 0, this.size);
	pop();
    }

    move() {
	this.y += config.dy;
    }
}
