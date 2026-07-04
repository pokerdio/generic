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
	let f = random();
	f = f * f;
	this.size = config.max_size * config.small_frac +
	    f * (1 - config.small_frac) * config.max_size;

	this.vx = (random() * 2.0 - 1.0) * config.blockv;
	this.vy = (random() * 2.0 - 1.0) * config.blockv;
	
	this.color = config.block_col
	[Math.floor(random() * config.block_col.length)];
    }

    display() {
	this.x += this.vx;
	this.y += this.vy;

	push();
	translate(this.x, this.y);
	strokeWeight(1.5);
	stroke(0, 0, 0);
	fill(this.color);
	circle(0, 0, this.size * 2);
	strokeWeight(0);
	fill("black");
	circle(-this.size*0.4, -this.size*0.4, 
	       this.size * 0.5);
	fill("white");
	circle(-this.size*0.5, -this.size*0.5, 
	       this.size * 0.3);

	fill("black");
	circle(this.size*0.6, -this.size*0.4, 
	       this.size * 0.5);
	fill("white");
	circle(this.size*0.5, -this.size*0.5, 
	       this.size * 0.3);

	pop();
    }

    move() {
	this.y += config.dy;
    }
}
