class Block {
    constructor(x, y, size, img, img_rect) {
	this.x = x;
	this.y = y;
	this.size = size;

	this.size_target = 0

	this.img = img
	this.img_rect = img_rect
    }

    display(percent) {
	if (percent > 1) {
	    percent = 1;
	}
	push();
	translate(this.x, this.y);
	let sz = this.size * percent;
	if (this.img) {
	    image(this.img, -sz/2, -sz/2, sz, sz, ...this.img_rect)
	}
	if (percent > 0.9) {
	    strokeWeight(map(percent, 0.9, 1.0, 1, 0));
	} else {
	    strokeWeight(1);
	}
	noFill();
	rect(-sz/2, -sz/2, sz, sz);
	pop();
    }
}
