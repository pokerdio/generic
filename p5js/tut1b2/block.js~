class Block {
    constructor(x, y, size, img, img_rect) {
	this.x = x;
	this.y = y;
	this.size = size;

	this.size_target = 0

	this.img = img
	this.img_rect = img_rect
    }

    display() {
	push();
	translate(this.x, this.y);
	let sz = this.target_size
	if (this.img) {
	    image(this.img, -sz/2, -sz/2, sz, sz, ...this.img_rect)
	}
	noFill();
	rect(-sz/2, -sz/2, sz, sz);

	pop();
    }
    initiate_move() {
	let distance = dist(mouseX, mouseY, this.x + this.size/2, this.y + this.size/2)
	let max_dist = this.size * 8.5;
	if (distance < max_dist) {
	    this.target_size = map(distance, 0, max_dist, this.size * 2, this.size);
	    if (this.target_size > this.size * 1.6) {
		this.target_size = this.size * 1.6;
	    }
	} else {
	    this.target_size = this.size;
	}
    }
    move() {
    }

}
