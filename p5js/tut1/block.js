class Block {
    constructor(x, y, size) {
	this.x = x;
	this.y = y;
	this.size = size;

	this.angle = 0;
    }

    display() {
	push();
	translate(this.x, this.y);
	rotate(this.angle);
	if (this.angle > 0) {
	    let c = map(this.angle, 0, 90, 0, 255);
	    fill(255, c, c)
	} else {
	    fill(255);
	}
	rect(0, 0, this.size, this.size);
	pop();
    }
    initiate_move() {
	let distance = dist(mouseX, mouseY, this.x, this.y);
	if (distance < this.size * 1.5 && this.angle == 0) {
	    this.angle += 2.5;
	}	
    }
    move() {
	if (this.angle > 0 && this.angle < 90) {
	    this.angle += 2.5;
	} else {
	    this.angle = 0;
	}
    }
}
