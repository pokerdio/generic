const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
gradient.addColorStop(0.0, "red");
gradient.addColorStop(0.2, "magenta");
gradient.addColorStop(0.6, "yellow");
gradient.addColorStop(0.8, "green");
gradient.addColorStop(1.0, "blue");

class Symbol {
    constructor (x, y, fontSize, canvasHeight) {
	this.characters = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンヴヵヶヽヾー0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	this.x = x;
	this.y = y;
	this.fontSize = fontSize;
	this.text = '';
	this.canvasHeight = canvasHeight;
    }

    draw (context) {
	this.text = this.characters.charAt(
	    Math.floor(Math.random() * this.characters.length))
	context.fillText(this.text, this.x * this.fontSize, this.y * this.fontSize);
	if (this.y * this.fontSize > this.canvasHeight && Math.random() > 0.98) {
	    this.y = 0;
	} else {
	    this.y += 1;
	}
    }
}


class Effect {
    constructor(canvasWidth, canvasHeight, fontSize) {
	this.fontSize = fontSize || 25;
	this.resize(canvasWidth, canvasHeight);
    }

    #initialize() {
	for (let i=0 ; i<this.columns ; ++i) {
	    this.symbols[i] = new Symbol(i, 0, this.fontSize, this.canvasHeight);
	}
    }
    draw () {
	this.symbols.forEach((s) => s.draw(ctx));
    }

    resize(width, height) {
	this.canvasWidth = width;
	this.canvasHeight = height; 
	this.columns = this.canvasWidth / this.fontSize;
	this.symbols = [];
	this.#initialize();
    }
}

const effect = new Effect(canvas.width, canvas.height, 25);
const effect2 = new Effect(canvas.width, canvas.height, 8);

function animate() {
    ctx.fillStyle = 'rgba(0,0,0,0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "#0aff0a";
    ctx.textAlign = 'center';
    ctx.font = effect.fontSize + 'px monospace';
    effect.draw();
    ctx.fillStyle = gradient;
    ctx.font = effect2.fontSize + 'px monospace';
    effect2.draw();
    setTimeout(()=>requestAnimationFrame(animate), 20);
//    requestAnimationFrame(animate);
}

animate();
window.addEventListener('resize', function() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    effect.resize(canvas.width, canvas.height);
    effect2.resize(canvas.width, canvas.height);
})
