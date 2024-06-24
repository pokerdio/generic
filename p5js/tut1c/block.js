class Block {
    constructor(x, y, size, img, img_rect) {
	this.x = x;
	this.y = y;
	this.size = size;

	this.angle_target = 0

	this.angle = 0;
	this.img = img
	this.img_rect = img_rect
    }

    display() {
	push();
	translate(this.x, this.y);
	rotate(this.angle);
	if (this.img) {
	    image(this.img, -this.size/2, -this.size/2, this.size, this.size, ...this.img_rect)
	}

	noFill();
	rect(-this.size/2, -this.size/2, this.size, this.size);

	pop();
    }
    initiate_move() {
	let distance = dist(mouseX, mouseY, this.x + this.size/2, this.y + this.size/2)
	let max_dist = this.size * 2.5;
	if (distance < max_dist) {
//	    this.angle_target = map(distance, 0, max_dist, 180, 0);
	    this.angle_target = 360;
	} else {
	    this.angle_target = 0;
	}
    }
    move() {
	if (this.angle > this.angle_target) {
	    this.angle -= 2.5;
	    if (this.angle < this.angle_target) {
		this.angle = this.angle_target;
	    }
	}
	if (this.angle < this.angle_target) {
	    this.angle += 2.5;
	    if (this.angle > this.angle_target) {
		this.angle = this.angle_target;
	    }
	}
	if (this.angle == 360) {
	    this.angle = 0;
	    this.angle_target = 0;
	}
    }
}
