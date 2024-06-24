update_stroll() {
    let delta = 0.02 * this.speed;

    if (this.gfx == mouse_gfx) {
	if (mouseX > 0 && mouseX < Fish.w && mouseY > 0 && mouseY < Fish.h) {
	    let v = createVector(mouseX, mouseY);
	    v.sub(this.pos);
	    let d = v.mag();		
	    let sign = 1;
	    if (d < 80) {
		sign = 0; 
	    } else if (d > 30) {
		sign = map(d, 30, 80, 0, 1);
	    } else {
		sign = 0; 
	    }
	    this.v.x += v.x * delta * 4 * sign;
	    this.v.y += v.y * delta * 4 * sign;
	}
    }

    for (let i=0 ; i<fishs.length ; ++i) {
	let f = fishs[i];
	//	    let v = this.towardsVector(f.pos);
	let v = f.pos.copy();
	v.sub(this.pos);
	let d = v.mag();
	let sign = 1;
	v.normalize();
	if (fishs[i].gfx === this.gfx) {
	    if (d < 50) {
		sign = -1; 
	    } else if (d > 150) {
		sign = 1;
	    } else {
		sign = 0.5;
	    }
	} else {
	    if (this.gfx === mouse_gfx) {
		sign = 0; 
	    } else {
		if (d < 150) {
		    sign = -1; 
		} else {
		    sign = 0;
		}
	    }
	}
	this.v.x += v.x * delta * sign;
	this.v.y += v.y * delta * sign;
    }
}
