let cols; let rows;
let size = 15;
let config = {spawn_chance: 5.0, 
	      spawn_chance_extra:25.0,
	      spawn_max_age:15000.0,
	      dy: 3.5, max_size: 30,
	      canvasX: 600, canvasY: 400, mouse_approach: 0.1,
	      small_frac: 0.125, blockv: 0.5,
	      block_col: [[55,0,0], 
			  [0,55,0], 
			  [0,0,55], 
			  [55,0,55], 
			  [55,55,0], ]};

let world = {
    age: 0, 
    blocks: [],
    playerX: 10,
    playerY: config.canvasY - 10,
    playerX_target: 10,
    dead: false
}
let blocks = [];

function setup() {
    createCanvas(config.canvasX, config.canvasY);
    rectMode(CENTER);
    angleMode(DEGREES);
}

function mouseMoved() {
    world.playerX_target = mouseX;
    if ((mouseX < 0) || (mouseX > config.canvasX) || 
	(mouseY < 0) || (mouseY > config.canvasY)) {
	cursor(ARROW);
	if (mouseX < 0) {
	    world.playerX_target = 0;
	}	
	if (mouseX > config.canvasX) {
	    world.playerX_target = config.canvasX;
	}
    } else {
	noCursor();
    }


    world.playerX += (world.playerX_target - world.playerX) * 
	config.mouse_approach;
}

function mouseClicked () {
    world.dead = false;
    world.blocks = [];
    world.age = 0;
}

function fadeOut () {
    fill (0, 0, 0, 15);
    rect (config.canvasX / 2, config.canvasY / 2,
	  config.canvasX, config.canvasY);
}

function advance_blocks () {
    let chance = config.spawn_chance;
    if (world.age > config.spawn_max_age) {
	chance += config.spawn_chance_extra
    } else {
	chance += config.spawn_chance_extra * world.age / 
	    config.spawn_max_age;
    }

    fill("black");
    textSize(22);
    text(Math.floor(chance * 4) * 0.25, 50, 50);

    if (random (100) < chance) {
	world.blocks.push(new Block());
    }
    for (let i=0 ; i<world.blocks.length ; ++i) {
	world.blocks[i].move();
    }
    for (let i=0 ; i<world.blocks.length ; ++i) {
	world.blocks[i].display();
    }
    new_blocks = [];
    for (let i=0 ; i<world.blocks.length ; ++i) {
	if (world.blocks[i].y - world.blocks[i].size < height) {
	    new_blocks.push(world.blocks[i])
	}
    }
    world.blocks = new_blocks;
}

function advance_player() {
    push();
    translate( world.playerX, world.playerY);
    strokeWeight(1.5);
    stroke(0, 0, 0);
    fill(255, 100, 100);
    triangle(0, -10, -10, 0, 10, 0);
    pop();
}

function dist (x1, y1, x2, y2)  {
    let dx = abs(x1 - x2);
    let dy = abs(y1 - y2);
    return sqrt(dx * dx + dy * dy);
}

function collision_detect() {
    triangle();
    for ([dx, dy] of [[0, -10], [-10, 0], [10, 0]]) {
	for (let i=0 ; i<world.blocks.length ; ++i) {
	    let b = world.blocks[i];
	    let d = dist(b.x, b.y, 
			 world.playerX + dx, 
			 world.playerY + dy);
	    if (d < b.size) {
		world.dead = true;
		return;
	    }
	}
    }
}

function draw() {
    if (world.dead) {
	fadeOut();
	return;
    }
    world.age += 1; 
    background(220);

    advance_blocks();
    advance_player();
    collision_detect();
}
