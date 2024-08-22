let img;

let imgtiles = []; 
let tilex = [];
let tiley = [];
let tiles = [];

let gridSize = 4;
let tileSize;
let emptySpace = { x: 0, y: 0 };
let moves = [];

function preload() {
  // Load the image
  img = loadImage('https://upload.wikimedia.org/wikipedia/commons/c/ce/2012-09-15_Tierpark_Berlin_26_%28cropped%29.jpg'); // Replace with your image path
}


function initGame() {
    let k = 0; 
    // Divide the image into tiles
    for (let i = 0; i < gridSize; i++) {
	tiles[i] = [];
	for (let j = 0; j < gridSize; j++) {
	    let x = j * tileSize;
	    let y = i * tileSize;
	    [tilex[k], tiley[k]] = [x, y];
	    imgtiles[k] = img.get(x, y, tileSize, tileSize);
	    tiles[i][j] = k++;
	}
    }

    // Remove one tile for the empty space
    tiles[gridSize - 1][gridSize - 1] = -1;
    emptySpace.x = gridSize - 1;
    emptySpace.y = gridSize - 1;
    
    // Shuffle the tiles
    shuffleTiles();
}

function setup() {
    createCanvas(800, 800);

    tileSize = width / gridSize;
    img.resize(width, height);
    initGame();
}

function approach(actual, desired) {
    delta = desired - actual; 
    if (abs(delta) < 2.5) {
	return actual
    } else {
	return 0.9 * desired + 0.1 * actual;
    }
}


function draw() {
    background(220);

    // Draw the tiles
    for (let i = 0; i < gridSize; i++) {
	for (let j = 0; j < gridSize; j++) {
	    if (tiles[i][j] >= 0) {
		let k = tiles[i][j];
		tilex[k] = approach(tileSize * j, tilex[k])
		tiley[k] = approach(tileSize * i, tiley[k])
		image(imgtiles[k], tilex[k], tiley[k]);
	    }
	}
    }

    // Check if the puzzle is solved
    if (isSolved()) {
	noLoop();
	alert('You solved the puzzle!');
	console.log("after alert")
    }
}

function mousePressed() {
    let i = floor(mouseY / tileSize);
    let j = floor(mouseX / tileSize);
    
    if (isValidMove(i, j)) {
	// Swap the clicked tile with the empty space
	tiles[emptySpace.y][emptySpace.x] = tiles[i][j];
	tiles[i][j] = -1;
	emptySpace.x = j;
	emptySpace.y = i;
    }
}

function isValidMove(i, j) {
  return (abs(j - emptySpace.x) + abs(i - emptySpace.y)) === 1;
}

function shuffleTiles() {
    for (let n = 0; n < 1000; n++) {
	let validMoves = [];
	if (emptySpace.x > 0) validMoves.push({ x: emptySpace.x - 1, y: emptySpace.y });
	if (emptySpace.x < gridSize - 1) validMoves.push({ x: emptySpace.x + 1, y: emptySpace.y });
	if (emptySpace.y > 0) validMoves.push({ x: emptySpace.x, y: emptySpace.y - 1 });
	if (emptySpace.y < gridSize - 1) validMoves.push({ x: emptySpace.x, y: emptySpace.y + 1 });

	let move = random(validMoves);
	tiles[emptySpace.y][emptySpace.x] = tiles[move.y][move.x];
	tiles[move.y][move.x] = -1;
	emptySpace.x = move.x;
	emptySpace.y = move.y;
    }
}

function isSolved() {
    let k = 0; 
    for (let i=0; i<gridSize; i++) {
	for (let j=0; j<gridSize; j++) {
	    if (i === gridSize - 1 && j === gridSize - 1) {
		return true;
	    }
	    if (tiles[i][j] != k++) {
		return false;
	    }
	}
    }
}
