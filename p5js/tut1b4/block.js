class Block {
    constructor(img, img_rect) {
	this.img = img
	this.img_rect = img_rect
    }

    display(x0, y0, x1, y1) {
	if (this.img) {
	    image(this.img, x0, y0, x1 - x0, y1 - y0, ...this.img_rect)
	}
	strokeWeight(0.3);
	noFill();
//	rect(x0, y0, x1 - x0, y1 - y0);
    }
}
