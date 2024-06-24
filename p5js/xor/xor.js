function tobyte(x) {
    if (x > 255) {
	x = 255
    }
    if (x < 0) {
	x = 0;
    }
    return x;
}
function setup() {
//    createCanvas(512, 512); // Create a canvas with dimensions 1024x1024
    createCanvas(1024, 1024); // Create a canvas with dimensions 1024x1024
    pixelDensity(1); // Set pixel density to 1 for consistency across different displays
    loadPixels(); // Load the pixel array for manipulation

    let diag_r = sqrt(width * width / 4.0 + height * height / 4.0);
    for (let x = 0; x < width; x++) {
	for (let y = 0; y < height; y++) {
	    let index = (x + y * width) * 4; // Calculate the index position in the pixel array
	    let xy = (x ^ y) / 4;

	    dx = x - width / 2;
	    dy = y - width / 2;

	    d = sqrt(dx * dx + dy * dy) / diag_r; // 0..1

	    hugh = sin(atan2(dy, dx) * 2) * 0.7;

	    let r = (xy / 2) * (1.2 + hugh); 
	    let b = (xy / 2) * (1.2 - hugh); 
	    let g = (r + b) / 2.0;

	    let a = 255; 
	    // Set the color values to the pixel array
	    pixels[index] = tobyte(r);
	    pixels[index + 1] = tobyte(g);
	    pixels[index + 2] = tobyte(b);
	    pixels[index + 3] = tobyte(a);
	}
    }
    updatePixels(); // Update the canvas with the modified pixel array
}
