
class Flower {
    static PTS = 200;

    constructor (r, f_amp, period, speed, color) {
	this.f_amp = f_amp;
	this.period = period;
	this.speed = speed;
	this.r = r;
	this.color = color
	
	this.rotation = 0; 
    }


    display() {
	fill(this.color);
	stroke(0);
	beginShape();
	for(let i=0 ; i<=Flower.PTS ; ++i) {
	    let angle = i/Flower.PTS * 360;
	    let f_radius = this.f_amp * cos(angle * this.period);
	    let x = (this.r + f_radius) * cos(angle + this.rotation);
	    let y = (this.r + f_radius) * sin(angle + this.rotation);
	    vertex(x, y);
	}
	endShape();

	this.rotation += this.speed;
    }
}
