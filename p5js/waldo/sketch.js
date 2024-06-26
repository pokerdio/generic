let zoom_size = 355;
let zoom_src = 150;

let img, img0, imgs; 
let img_idx = 0;

let img_zoom, img_mask; 
let lastMouseX = -1, lastMouseY = -1;
let mouse_moved;


function preload() {
    imgs = [
    loadImage('https://r4.wallpaperflare.com/wallpaper/1012/261/292/waldo-puzzles-where-s-wally-wallpaper-f9e088adc1da3ddbb6a7782f30a1765d.jpg')]
}

function mousePressed () {
    img_idx = (1 + img_idx) % imgs.length
    clear();
    setup();
}

function fillImageColor(imageObject, fillColor) {
    // ignores alpha
    imageObject.loadPixels();
    let [r, g, b] = [red(fillColor), green(fillColor), blue(fillColor)];

    // Loop through each pixel and set the color to the specified fill color
    for (let i = 0; i < imageObject.pixels.length; i += 4) {
	imageObject.pixels[i] = r; 
	imageObject.pixels[i + 1] = g;
	imageObject.pixels[i + 2] = b;
    }
    imageObject.updatePixels();
}

function mouseMoved() {
    fillImageColor(img_zoom, 255)
    img_zoom.copy(img0, 
		  mouseX * img0.width / img.width - zoom_src / 2, 
		  mouseY * img0.width / img.width - zoom_src / 2, 
		  zoom_src, zoom_src, 
		  0, 0, zoom_size, zoom_size);    
    img_zoom.mask(img_mask);
    mouse_moved = true; 
}

function windowResized() {
    clear();
    setup();
}

function fitImageToWindow(img) {
    // Calculate the aspect ratios
    let imgAspectRatio = img.width / img.height;
    let windowAspectRatio = windowWidth / windowHeight;

    // Resize the image based on the aspect ratios
    if (imgAspectRatio > windowAspectRatio) {
	img.resize(windowWidth, 0);
    } else {
	img.resize(0, windowHeight);
    }
}

function setup() {
    img0 = imgs[(++img_idx) % imgs.length]
    img = img0.get()

    img_zoom = createImage(zoom_size, zoom_size);
    img_zoom.copy(img, 500, 500, zoom_size, zoom_size, 0, 0, zoom_size, zoom_size);

    fitImageToWindow(img);
//    img.resize(1400, 1400 * img.height / img.width);
    createCanvas(img.width, img.height);

    img_mask = createGraphics(zoom_size, zoom_size);
    img_mask.fill(255);
    img_mask.ellipse(zoom_size / 2, zoom_size / 2, zoom_size, zoom_size);
    img_zoom.mask(img_mask);

    image(img, 0, 0);
    mouse_moved = false; 
}

function draw() {
    if (mouse_moved) {
	if (lastMouseX >= 0) {
	    image(img, 0, 0);
	    image(img, lastMouseX  - zoom_size / 2, lastMouseY  - zoom_size / 2, zoom_size, zoom_size,
		 lastMouseX  - zoom_size / 2, lastMouseY  - zoom_size / 2, zoom_size, zoom_size);
	}
	image(img_zoom, mouseX - zoom_size / 2, mouseY - zoom_size / 2);

	noFill();
	stroke(0);
	strokeWeight(5);
	ellipse(mouseX, mouseY, zoom_size - 5, zoom_size - 5);
	strokeWeight(1);
	// line(mouseX - zoom_size * 0.48, mouseY, mouseX - zoom_size * 0.1, mouseY)
	// line(mouseX + zoom_size * 0.48, mouseY, mouseX + zoom_size * 0.1, mouseY)
	// line(mouseX, mouseY - zoom_size * 0.48, mouseX, mouseY - zoom_size * 0.1)
	// line(mouseX, mouseY + zoom_size * 0.48, mouseX, mouseY + zoom_size * 0.1)

	lastMouseX = mouseX;
	lastMouseY = mouseY;
	mouse_moved = false;

	// Retrieve the current frame rate
	let currentFrameRate = frameRate();

	// Display the frame rate on the canvas
	fill(255);
	textSize(15);
	stroke(0);
	strokeWeight(2.5);
	let [x, y] = [mouseX - zoom_size * 0.3, mouseY - zoom_size * 0.3];
	text("FPS:" + currentFrameRate.toFixed(1), x, y);
    }
}
