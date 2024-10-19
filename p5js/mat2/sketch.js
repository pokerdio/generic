// Matter.js module aliases
const {Engine, World, Bodies, Body, Constraint, Vector} = Matter;

// Engine and world
let engine;
let world;

// Arrays for storing bodies
let boxes = [];
let box_colors = []; 
let ground, lwall, rwall;

function bump(o, force = 1.0) {
    Body.setVelocity(o, {
	x: o.velocity.x + (Math.random() - 0.5) * 2 * force,
	y: o.velocity.y + (Math.random() - 0.5) * 2 * force
    });    
}

function setup() {
    createCanvas(800, 600);

    // Create engine and world
    engine = Engine.create();
    world = engine.world;

    // Create ground
    let options = {
        isStatic: true
    };

    ground = Bodies.rectangle(400, height - 50, 810, 60, options);
    World.add(world, ground);
    lwall = Bodies.rectangle(10, 270, 20, 540, options);
    World.add(world, lwall);
    rwall = Bodies.rectangle(790, 270, 20, 540, options);
    World.add(world, rwall);

}

function mousePressed() {
    // Add a new box when the mouse is pressed
    let randomShape = Math.floor(random(4));  // Random number between 0 and 3
    let body, b1, b2, b;

    let col = [random(255), random(255), random(255)];

    switch (randomShape) {
    case 0:  // Rectangle
        b1 = Bodies.rectangle(mouseX, mouseY, random(20, 80), random(20, 80));
        b2 = Bodies.rectangle(mouseX, mouseY - 100, random(20, 80), random(20, 80));

	let distance = Vector.magnitude(Vector.sub(b1.position, b2.position));

	let c = Constraint.create({
	    bodyA: b1,
	    bodyB: b2,
	    length: distance,  // Set the length to the current distance
	    stiffness: 0.01    // You can adjust stiffness as needed
	});


	boxes.push(b1);	
	box_colors.push(col)
	World.add(world, b1);

	boxes.push(b2);	
	box_colors.push(col)
	World.add(world, b2);

	World.add(world, c);
        break;
    case 1:  // Circle
        b = Bodies.circle(mouseX, mouseY, random(20, 40));
	boxes.push(b);
	box_colors.push(col)

	World.add(world, b);
        break;
    case 2:  // Polygon (triangle to hexagon)
        b = Bodies.polygon(mouseX, mouseY, Math.floor(random(3, 7)), random(20, 40));
	boxes.push(b);
	box_colors.push(col)
	World.add(world, b);
        break;
    case 3:  // Trapezoid
        b = Bodies.trapezoid(mouseX, mouseY, random(40, 80), random(20, 40), random(0.3, 0.7));
	boxes.push(b);      
	box_colors.push(col)
	World.add(world, b);  
	break;
    }

}

function draw() {
    background(51);

    // Update the physics engine
    Engine.update(engine);
    
    if (boxes.length > 0) {
	bump(boxes[floor(random(0, boxes.length))], 4)
    }
    // Draw ground
    noStroke();
    fill(170);
    rectMode(CENTER);
    rect(ground.position.x, ground.position.y, 810, 60);

    fill("red");
    rect(lwall.position.x, lwall.position.y, 20, 540);
    rect(rwall.position.x, rwall.position.y, 20, 540);

    // Draw all boxes
    for (let i = 0; i < boxes.length; i++) {
	fill(box_colors[i]);
        beginShape();
        for (let j = 0; j <boxes[i].vertices.length ; j++) {
            vertex(boxes[i].vertices[j].x, boxes[i].vertices[j].y);
        }
        endShape(CLOSE);
    }
}

function keyPressed() {
    boxes = [];
    box_colors = []; 
    World.clear(world, true);
    World.add(world, ground);
}
