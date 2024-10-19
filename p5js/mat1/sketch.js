// Matter.js module aliases
let Engine = Matter.Engine,
    World = Matter.World,
    Bodies = Matter.Bodies;

// Engine and world
let engine;
let world;

// Arrays for storing bodies
let boxes = [];
let box_colors = []; 
let ground;

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
}

function mousePressed() {
    // Add a new box when the mouse is pressed
    let b;
    let randomShape = Math.floor(random(4));  // Random number between 0 and 3
    let body;

    switch (randomShape) {
    case 0:  // Rectangle
        b = Bodies.rectangle(mouseX, mouseY, random(20, 80), random(20, 80));
        break;
    case 1:  // Circle
        b = Bodies.circle(mouseX, mouseY, random(20, 40));
        break;
    case 2:  // Polygon (triangle to hexagon)
        b = Bodies.polygon(mouseX, mouseY, Math.floor(random(3, 7)), random(20, 40));
        break;
    case 3:  // Trapezoid
        b = Bodies.trapezoid(mouseX, mouseY, random(40, 80), random(20, 40), random(0.3, 0.7));
        break;
    }

    let c = [random(255), random(255), random(255)];
    boxes.push(b);
    box_colors.push(c)
    World.add(world, b);
}

function draw() {
    background(51);

    // Update the physics engine
    Engine.update(engine);

    // Draw ground
    noStroke();
    fill(170);
    rectMode(CENTER);
    rect(ground.position.x, ground.position.y, 810, 60);

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
