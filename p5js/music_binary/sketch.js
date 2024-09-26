let started = false;
let start_note = 48;

let scaleDict = {
    pentatonicMajor: [2, 2, 3, 2],
    pentatonicMinor: [3, 2, 2, 3],
    pentatonicHirajoshi: [2,1,4,1],
    pentatonicEgyptian: [2,3,2,3],
    heptatonicNaturalMinor : [2, 1, 2, 2, 1, 2,],
    heptatonicMelodicMinor : [2, 1, 2, 2, 2, 1,],
    heptatonicMajor: [2, 2, 1, 2, 2, 2, 1],
}

let scale = [1, 3, 3, 3]

let n_osc = 6
let bin = new Array(n_osc).fill(0);
let gray = new Array(n_osc).fill(0);
let old_bin, old_gray

let osc = [];
let env = [];
let bin_str = ""
let gray_str = ""
let beats_per_second = 3
let flip_ticking = false
let dif_play = false
let sust_play = false
let use_gray = false


function binarytoGray()
{
    // MSB of gray code is same as binary code
    gray[bin.length - 1] = bin[bin.length - 1];
 
    // Compute remaining bits, next bit is computed by
    // doing XOR of previous and current in Binary
    for (let i=0; i<bin.length-1 ; i++) {
        gray[i] = bin[i + 1] ^ bin[i];
    }
}

function complete_scale(scale) {
    let s = 12
    for (let i=0 ; i<scale.length ; ++i) {
	s -= scale[i]
    }
    if (s > 0) {
	scale.push(s)
    }
}

complete_scale(scale)

function updateScale() {
    setupSound(); 
}

function updateOsc() {
    setupSound();
}

function setupSound() {
    let note = start_note;
    let t =  1.0 / beats_per_second

    val = document.getElementById('scaleSelect').value;
    if (val in scaleDict) {
	scale = scaleDict[val]
	complete_scale(scale)
    }

    bin = new Array(n_osc).fill(0);
    gray = new Array(n_osc).fill(0);
    osc = new Array(n_osc)
    env = new Array(n_osc)
    for (let i=0 ; i<osc.length ; ++i) {
	osc[i] = new p5.Oscillator(document.getElementById('oscShape').value);
	osc[i].freq(midiToFreq(note));

	note += scale[i % scale.length]
	env[i] = new p5.Envelope();
	// Set attack, decay, sustain, release times
	if (sust_play) {
	    env[i].setADSR(t * 0.2, t * 0.3, 0.2, t * 25);
	} else {
	    env[i].setADSR(t * 0.2, t * 0.3, 0.2, t * 1.2);
	}
	// Set max amplitude (0.8) and sustain level (0)
	env[i].setRange(0.8, 0.0); 


	osc[i].amp(env[i]); // Connect the envelope to the oscillator amplitude
    }
    frameRate(beats_per_second);
    started = false; 
}


function setup() {
    createCanvas(400, 400);
    textAlign(CENTER, CENTER);
    textSize(24);
    
    document.getElementById('checkboxGray').checked = use_gray;
    document.getElementById('checkboxReverse').checked = flip_ticking;
    document.getElementById('checkboxDif').checked = dif_play;
    document.getElementById('checkboxSust').checked = sust_play;

    document.getElementById('numberBitCount').value = n_osc
    document.getElementById('numberNote').value = start_note;
    document.getElementById('numberBps').value = beats_per_second;
    started = false; 
}


function tickBits() {
    old_bin = [...bin]
    old_gray = [...gray]
    if (flip_ticking) {
	bin = bin.reverse(); 
    }

    bin[0]++;
    let i=0; 
    while (bin[i] == 2) {
	bin[i] = 0; 
	if (i < bin.length - 1) {
	    bin[i + 1]++;
	    i++;
	} else {
	    break;
	}
    }


    binarytoGray()

    if (flip_ticking) {
	bin = bin.reverse();
	gray = gray.reverse();
    }


    bin_str = "";
    for (i=0 ; i<bin.length ; ++i) {
	bin_str += bin[i]
    }

    gray_str = "";
    for (i=0 ; i<gray.length ; ++i) {
	gray_str += gray[i]
    }

}

function silenceAll() {
    for (let i=0 ; i<env.length ; ++i) {
	env[i].ramp(osc[i], 0, 0);
    }
}

function playSound() {
    let v = use_gray ? gray : bin; 
    let oldv = use_gray ? old_gray : old_bin; 
    
    for (i=0 ; i<v.length ; ++i) {
	if (dif_play) {
	    if (v[i] && !oldv[i]) {
		env[i].play();
	    }
	    if (!v[i] && sust_play) {
		env[i].ramp(osc[i], 0, 0);
	    }
	} else {
	    if (v[i]) {
		env[i].play();
	    }
	    if (!v[i] && sust_play) {
		env[i].ramp(osc[i], 0, 0);
	    }
	}
    }
}

function draw() {
    background(220);

    if (!started) {
	text('Start Music', width / 2, height / 2);
	return;
    } 
    tickBits(); 
    text(use_gray ? gray_str : bin_str, width / 2, height / 2);
    playSound();
}

function mousePressed() {
    if (started) {
	started = false;
	silenceAll();
	return;
    }

    if (mouseX > 0 && mouseY > 0 && mouseX < width - 1 && mouseY < height - 1 && !started) {
	// Start the AudioContext after user gesture (click)
	userStartAudio().then(() => {
	    setupSound(); 
	    for (let i=0 ; i<osc.length ; ++i) {
		osc[i].start();
	    }
	    started = true;
	});
    } 
}


// Function to update checkbox values
function updateCheckboxes() {
    let checkboxGrayValue = document.getElementById('checkboxGray').checked;
    let checkboxReverseValue = document.getElementById('checkboxReverse').checked;
    let checkboxDifValue = document.getElementById('checkboxDif').checked;
    let checkboxSustValue = document.getElementById('checkboxSust').checked;

    console.log('Checkbox 1:', checkboxGrayValue, 
		'Checkbox 2:', checkboxReverseValue,
	       	'Checkbox 3:', checkboxDif,
		'Checkbox 4:', checkboxSustValue);

    if (checkboxGrayValue != use_gray || 
	checkboxReverseValue != flip_ticking ||
       	checkboxDifValue != dif_play ||
        checkboxSustValue != sust_play) {

	use_gray = checkboxGrayValue
	flip_ticking = checkboxReverseValue
	dif_play = checkboxDifValue
	sust_play = checkboxSustValue

	started = false; 
	silenceAll();
    }
}

// Function to update number values
function updateNumbers() {
    let numberBitCountValue = parseInt(document.getElementById('numberBitCount').value);
    let numberNoteValue = parseInt(document.getElementById('numberNote').value);
    let numberBpsValue = parseInt(document.getElementById('numberBps').value);
    console.log('Number 1:', numberBitCountValue, 
		'Number 2:', numberNoteValue,
		'Number 3:', numberBpsValue);

    if (numberBitCountValue != n_osc || numberNoteValue != start_note || 
	numberBpsValue != beats_per_second) {
	n_osc = numberBitCountValue;
	start_note = numberNoteValue;
	beats_per_second = numberBpsValue;
	started = false; 
	silenceAll();
    }
}
