let pixelSize = 20; // Size of each pixel
let cols = 35, rows = 35;
let currentColor = 'lit'; // Initial color
const previewWidth = 200;

var undoSprite;

//html objects
var slider1
var sliderLabel1
var slider2
var sliderLabel2



// Function to parse clipboard data and convert it to an array of numbers
function parseInputData(s) {
    var csv_text = s.match(/{([^}]*)}/);
    if (!csv_text || csv_text.length < 2 || !csv_text[1]) {
	return;
    }

    csv_text = csv_text[1].split(',');
    const v = csv_text.map(parseFloat);
    
    if (v[0] * v[1] + 2 != v.length) {
	console.log("bad input length");
	return;
    }
    return v; 
}

function insideRect(x, y, rc) {	// 
    return (x >= rc[0] && x < rc[0] + rc[2] && 
	    y >= rc[1] && y < rc[1] + rc[3]);
}

function copyTextToClipboard(text) {
    // Create a temporary textarea element to hold the text
    const textarea = document.createElement('textarea');
    textarea.value = text;

    // Set the textarea to be invisible
    textarea.style.position = 'absolute';
    textarea.style.left = '-9999px';

    document.body.appendChild(textarea);

    // Select and copy the text inside the textarea
    textarea.select();
    document.execCommand('copy');

    // Remove the textarea from the DOM
    document.body.removeChild(textarea);
}



let sprite;

function handleTextChange() {
    let inputValue = document.getElementById('textInput').value;
    let save = sprite.clone();    
    let v = parseInputData(inputValue);
    if (v) {
	sprite.fill("transparent");
	sprite.importPixels(v);
    }

    if (!save.isEqual(sprite)) {
	undoSprite = save;
    }
}

function setup() {
    document.getElementById("radio1").checked = true;

    slider1 = document.getElementById("myRange1");
    sliderValue1 = document.getElementById("sliderText1");
    slider1.value = 5;
    sliderValue1.textContent = "5";
    slider1.addEventListener("input", logSliderValue1);

    slider2 = document.getElementById("myRange2");
    sliderValue2 = document.getElementById("sliderText2");
    slider2.value = 5;
    sliderValue2.textContent = "5";
    slider2.addEventListener("input", logSliderValue2);

    createCanvas(cols * pixelSize + previewWidth, rows * pixelSize).parent("canvasContainer");
    sprite = new PixelSprite(cols, rows);

    canvas = document.querySelector('canvas');
}

function draw() {
    background(75);
    sprite.display();

    let w = (previewWidth - sprite.cols);
    let h = (height - sprite.rows);
    for (let i=0 ; i<25 ; ++i) {
	let x = sin(i + frameCount * 0.002) * w / 2.2 + w / 2 + width - previewWidth;
	let y = cos(i * 1.1 + frameCount * 0.003) * h / 2.2 + h / 2;

	sprite.sprite(floor(x), floor(y));
    }
}


function changeSelectedRadioButton(index) {
    // Get all radio buttons with the name "radio"
    const radioButtons = document.getElementsByName("radio");

    // Loop through each radio button
    for (let i = 0; i < radioButtons.length; i++) {
        // If the index matches the desired button, set it as checked
        if (i === index) {
            radioButtons[i].checked = true;
        } else {
            radioButtons[i].checked = false;
        }
    }
}

function mousePressed() {
    const x = floor(mouseX / pixelSize);
    const y = floor(mouseY / pixelSize);
    let save = sprite.clone();
    sprite.setPixel(x, y, currentColor);
    if (!save.isEqual(sprite)) {
	undoSprite = save;
    }
}

function mouseDragged() {
    mousePressed();
}

function keyPressed() {
    const x = floor(mouseX / pixelSize);
    const y = floor(mouseY / pixelSize);

    const slideW = int(slider1.value);
    const slideH = int(slider2.value);

    let save = sprite.clone();

    console.log("keypressed ", key)

    if (key === '1') {
	changeSelectedRadioButton(0);
	currentColor = 'lit';
    } else if (key === '2') {
	changeSelectedRadioButton(1);
	currentColor = 'dark';
    } else if (key === '3') {
	changeSelectedRadioButton(2);
	currentColor = 'transparent';
    } else if (key === "4") {
	copyTextToClipboard(sprite.exportToCArray());
    } else if (key === "f") {
	sprite.paintFill(x, y, currentColor);
    } else if (key === "x") {
	sprite.insertColumn(x);
    } else if (key === "X") {
	sprite.deleteColumn(x);
    } else if (key === "y") {
	sprite.insertRow(y);
    } else if (key === "Y") {
	sprite.deleteRow(y);
    } else if (key === "c") {
	sprite.center();
    } else if (key === "r") {
	sprite.rect(x, y, slideW, slideH, currentColor);
    } else if (key === "e") {
	sprite.ellipse(x, y, slideW, slideH, currentColor);
    } else if (key === "R") {
	sprite.fillRect(x, y, slideW, slideH, currentColor);
    } else if (key === "u") {
	if (undoSprite) {
	    sprite = undoSprite;
	}
    } else if (key === "-") {
	slider1.value -= 1;
	logSliderValue1()
	slider2.value -= 1;
	logSliderValue2()
    } else if (key === "=" || key === "+") {
	slider1.value = int(slider1.value) + 1;
	logSliderValue1()
	slider2.value = int(slider2.value) + 1;
	logSliderValue2()
    }
    if (!save.isEqual(sprite)) {
	undoSprite = save;
    }
}

function buttonClicked(buttonNumber) {
    console.log('Button ' + buttonNumber + ' clicked!');
    // Add your button click handling code here

    let save = sprite.clone();

    switch(buttonNumber) {
    case 1:
	currentColor = 'lit';
	break;
    case 2:
	currentColor = 'dark';
	break;
    case 3:
	currentColor = 'transparent';
	break;
    case 4:
	let txt = sprite.exportToCArray();
	copyTextToClipboard(txt);
	document.getElementById('textInput').value = txt;
	break;
    case 5:
	sprite.fill("transparent")
	break;
    case 6:	
	handleTextChange();
	break;
    }
    if (!save.isEqual(sprite)) {
	undoSprite = save;
    }
}

function radioChanged(x) {
    console.log("radio changed ", x);
}

function logSliderValue1() {
  sliderValue1.textContent = slider1.value;
}
function logSliderValue2() {
  sliderValue2.textContent = slider2.value;
}

