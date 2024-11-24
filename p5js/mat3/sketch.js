// Matter.js module aliases
const {Engine, World, Bodies, Body, Constraint, Vector, Events} = Matter;

// Engine and world
let engine;
let world;
let bike, ground, ground_color;

let conf = {
    bike_x: 400,
    bike_y: 450,

    bike_driver_mass:50,
    bike_vehicle_mass:10,
    bike_wheel_mass:10,
    
    bike_driver_dx: 50,
    bike_driver_dy: 20,
    bike_driver_radius: 10,
    


    bike_wheel_dx: 50,
    bike_wheel_dy: 50,
    bike_constraint_dx: 30,
    stiff:0.5,
    driver_stiff:0.05,
    timeTouch:5,
    wheelRadius:20,

    terrainWidth:3000,
    terrainCount:128,

    forceMagnitude: 1.5,
    update_steps:2,
    gravity_scale: 5,

    dt: 10, // milliseconds per frame update
    frameRate:30,
}

function bump(o, force = 1.0) {
    Body.setVelocity(o, {
	x: o.velocity.x + (Math.random() - 0.5) * 2 * force,
	y: o.velocity.y + (Math.random() - 0.5) * 2 * force
    });   
}

function bodyTouchesGround(body) {
    const segmentWidth = conf.terrainWidth / conf.terrainCount
    const x = body.position.x; 
    const idx = floor(x / segmentWidth - 0.5); 

    if (idx >= 0 && idx < ground.length) {
	ground_color[idx] = "white";
	if (Matter.SAT.collides(body, ground[idx]).collided) {
	    return true; 
	}
    }
    if (idx + 1 >= 0 && idx + 1 < ground.length) {
	ground_color[idx + 1] = "yellow";
	if (Matter.SAT.collides(body, ground[idx + 1]).collided) {
	    return true; 
	}
    }
    return false; 
}

function createTerrain(width, groundY, segmentCount, minHeight, maxHeight) {
    // Close the polygon by connecting the last point to the bottom of the screen
    let heights = [];
    const segmentWidth = width / segmentCount;


    for (let i=0; i<=segmentCount; i++) {
        heights.push(minHeight + random() * (maxHeight - minHeight));
    }

    for (let smooth=0 ; smooth<2 ; ++smooth) {
	for (let i=1 ; i<segmentCount ; ++i) {
	    heights[i] = (heights[i - 1] + 2 * heights[i] + heights[i + 1]) / 4.0; 
	}
    }

    ground = []
    ground_color = []
    for (let i=0 ; i<segmentCount ; ++i) { 
        const x0 = i * segmentWidth;
	let b = Bodies.fromVertices(0, 0, [{x:0, y:0}, {x:0, y:-heights[i]}, 
					   {x:segmentWidth, y:-heights[i+1]},
					   {x:segmentWidth, y:0}], 
				    {isStatic: true,
				     label:"ground"})

	if (i == 0)  {
	    console.log("heyooo!")
	    console.log(b.position)
	    console.log(b.vertices[0])
	    console.log(b.vertices[1])
	    console.log(b.vertices[2])
	    console.log(b.vertices[3])
	}

	Body.setPosition(b, {x : i * segmentWidth - b.bounds.min.x, 
			     y : height - b.bounds.max.y})
	World.add(world, b)
	ground.push(b)
	ground_color.push("green")
    }
}

function bodyDistance(b1, dx1, dy1, b2) {
    return Vector.magnitude(Vector.sub({x: b1.position.x + dx1, y: b1.position.y + dy1}, b2.position));
}

function createBike() {
    // Bike body
    const vehicleBody = Bodies.rectangle(conf.bike_x, conf.bike_y, 80, 20, { 
	label: 'vehicleBody', 
	density: 0.02 
    });

    const driver = Bodies.circle(conf.bike_x, conf.bike_y - conf.bike_driver_dy, 
				 conf.bike_driver_radius, { 
				     label: 'frontWheel', 
				     friction: 0.9 
				 });


    const driverC0 = Constraint.create({
	bodyA: vehicleBody,
	pointA: {x:-conf.bike_driver_dx, y:0}, 
	bodyB: driver,
	length: bodyDistance(vehicleBody, conf.bike_driver_dx, 0, driver),
	stiffness: conf.driver_stiff,
    });


    const driverC1 = Constraint.create({
	bodyA: vehicleBody,
	pointA: {x:0, y:0}, 
	bodyB: driver,
	length: bodyDistance(vehicleBody, conf.bike_driver_dx, 0, driver),
	stiffness: conf.driver_stiff,
    });

    const driverC2 = Constraint.create({
	bodyA: vehicleBody,
	pointA: {x:conf.bike_driver_dx, y:0}, 
	bodyB: driver,
	length: bodyDistance(vehicleBody, conf.bike_driver_dx, 0, driver),
	stiffness: conf.driver_stiff,
    });


    // Wheels
    const frontWheel = Bodies.circle(conf.bike_x - conf.bike_wheel_dx, 
				     conf.bike_y + conf.bike_wheel_dy, 
				     conf.wheelRadius, { 
					 label: 'frontWheel', 
					 friction: 0.9 
				     });

    const rearWheel = Bodies.circle(conf.bike_x + conf.bike_wheel_dx, 
				    conf.bike_y + conf.bike_wheel_dy, 
				    conf.wheelRadius, { 
					label: 'rearWheel', 
					friction: 0.9 
				    });

    Body.setMass(driver, conf.bike_driver_mass);
    Body.setMass(frontWheel, conf.bike_wheel_mass);
    Body.setMass(rearWheel, conf.bike_wheel_mass);
    Body.setMass(vehicleBody, conf.bike_vehicle_mass);

    // Constraints (axles)
    const crossAxle0 = Constraint.create({
	bodyA: vehicleBody,
	pointA: {x:conf.bike_constraint_dx, y:0}, 
	bodyB: frontWheel,
	length: bodyDistance(vehicleBody, conf.bike_constraint_dx, 0, frontWheel),
	stiffness: conf.stiff,
    });

    const crossAxle1 = Constraint.create({
	bodyA: vehicleBody,
	pointA: {x:-conf.bike_constraint_dx, y:0}, 
	bodyB: rearWheel,
	length: bodyDistance(vehicleBody, -conf.bike_constraint_dx, 0, rearWheel),
	stiffness: conf.stiff,
    });


    const frontAxle = Constraint.create({
	bodyA: vehicleBody,
	pointA: {x:-conf.bike_constraint_dx, y:0}, 
	bodyB: frontWheel,
	length: bodyDistance(vehicleBody, -conf.bike_constraint_dx, 0, frontWheel),
	stiffness: conf.stiff,
    });

    const rearAxle = Constraint.create({
	bodyA: vehicleBody,
	pointA: {x:conf.bike_constraint_dx, y:0}, 
	bodyB: rearWheel,
	length: bodyDistance(vehicleBody, conf.bike_constraint_dx, 0, rearWheel),
	stiffness: conf.stiff,
    });


    const wheelAxle = Constraint.create({
	bodyA: frontWheel,
	bodyB: rearWheel,
	length: bodyDistance(rearWheel, 0, 0, frontWheel),
	stiffness: conf.stiff,
    });


    bike = {vehicleBody: vehicleBody,
	    frontWheel: frontWheel,
	    rearWheel: rearWheel,
	    frontAxle: frontAxle,
	    rearAxle: rearAxle,
	    wheelAxle: wheelAxle,
	    crossAxle0: crossAxle0,
	    crossAxle1: crossAxle1,
	    frontTouchGround:false,
	    rearTouchGround:false,
	    driver: driver,
	    driverC0 : driverC0, 
	    driverC1 : driverC1, 
	    driverC2 : driverC2, 
	    driverPosition: 1}

    World.add(world, [vehicleBody, frontWheel, rearWheel,
		      driver, driverC0, driverC1, driverC2, 
		      frontAxle, rearAxle, wheelAxle, crossAxle0, crossAxle1]);
    fixBikeDriverConstraints();
}




function setup() {
    createCanvas(1200, 600);

    // Create engine and world
    engine = Engine.create();
    engine.constraintIteration = 15; 

    engine.gravity.scale *= conf.gravity_scale
    engine.gravity.scale *= conf.update_steps

    world = engine.world;

    createTerrain(conf.terrainWidth, height, conf.terrainCount, 0, 100)
    createBike();
    frameRate(conf.frameRate)
}

function drawBody(body, delta) {
    strokeWeight(1.5)
    stroke(0);
    beginShape(); 
    for (let i=0 ; i<body.vertices.length ; i++) {
	let b = body.vertices[i]
	vertex(b.x + delta, b.y)
    }
    endShape(CLOSE);
}

function drawBike(delta) {
    push();
    fill("red")
    drawBody(bike.vehicleBody, delta);

    if (bike.frontTouchGround) {
	fill("white");
    } else {
	fill("red");
    }
    drawBody(bike.frontWheel, delta);

    drawBody(bike.frontWheel, delta);
    if (bike.rearTouchGround) {
	fill("white");
    } else {
	fill("red");
    }
    drawBody(bike.rearWheel, delta);

    drawConstraint(bike.rearAxle, delta);
    drawConstraint(bike.frontAxle, delta);
    drawConstraint(bike.wheelAxle, delta);
    drawConstraint(bike.crossAxle0, delta);
    drawConstraint(bike.crossAxle1, delta);


    drawBody(bike.driver, delta);
    // drawConstraint(bike.driverC0, delta);
    // drawConstraint(bike.driverC1, delta);
    // drawConstraint(bike.driverC2, delta);

    pop(); 
}

let delta = 0; 

function updateTouch() {
    bike.rearTouchGround = bodyTouchesGround(bike.rearWheel);
    bike.frontTouchGround = bodyTouchesGround(bike.frontWheel);
}

function draw() {
    ground_color = new Array(ground.length).fill("green");
    background(55,77, 99);
    // Update the physics engine

    fixBikeDriverConstraints(); 


    for (let i=0 ; i<conf.update_steps ; ++i) {
	keyUpdate(); 
	Engine.update(engine, conf.dt / conf.update_steps);
	updateTouch();
    }


    if (delta + bike.vehicleBody.position.x > width - 100) {
	delta = width - 100 - bike.vehicleBody.position.x
    } else if (delta + bike.vehicleBody.position.x < 100) {
	delta = 100 - bike.vehicleBody.position.x	
    }


    fill("green")
    for (let i=0 ; i<ground.length ; ++i)  {
	fill(ground_color[i]);
	drawBody(ground[i], delta);
    }
    drawBike(delta);

    stroke(0)
    fill("red")
    textSize(24);
    text("FPS:" + frameRate().toFixed(1), 20, 30);
}


function drawConstraint(constraint) {
    const posA = constraint.bodyA.position;
    const posB = constraint.bodyB.position;
    
    // Calculate the actual positions where the constraint attaches
    const attachmentA = {
        x: posA.x + constraint.pointA.x,
        y: posA.y + constraint.pointA.y
    };
    
    const attachmentB = {
        x: posB.x + constraint.pointB.x,
        y: posB.y + constraint.pointB.y
    };
    
    stroke(255);  // Set line color to white
    strokeWeight(2);  // Set line thickness
    line(attachmentA.x + delta, attachmentA.y, attachmentB.x + delta, attachmentB.y);  // Draw the constraint as a line
}


function keyUpdate() {
    var forceMagnitude = conf.forceMagnitude / conf.update_steps;  
    if (bike.frontTouchGround && bike.rearTouchGround) {
	forceMagnitude /= 2;
    }


    if (keyIsDown(LEFT_ARROW)) {
        // Apply a leftward force
	if (bike.frontTouchGround) {
            Body.applyForce(bike.frontWheel, bike.frontWheel.position, {
		x: -forceMagnitude,  // Negative force to the left
		y: 0
            });
	}

	if (bike.rearTouchGround) {
            Body.applyForce(bike.rearWheel, bike.rearWheel.position, {
		x: -forceMagnitude,  // Negative force to the left
		y: 0
            });
	}


    } else if (keyIsDown (RIGHT_ARROW)) {
        // Apply a rightward force
	if (bike.frontTouchGround) {
            Body.applyForce(bike.frontWheel, bike.frontWheel.position, {
		x: forceMagnitude,  // Negative force to the left
		y: 0
            });
	}

	if (bike.rearTouchGround) {
            Body.applyForce(bike.rearWheel, bike.rearWheel.position, {
		x: forceMagnitude,  // Negative force to the left
		y: 0
            });
	}
    }
}

function resetBike(x) {
    x = x || bike.vehicleBody.position.x

    if (x < 100) {
	x = 100
    }
    if (x > conf.terrainWidth - 100){
	x = conf.terrainWidth - 100;
    }

    let y = 200
    Body.setPosition(bike.vehicleBody, {x:x , y:y});
    
    Body.setPosition(bike.driver, {x:x , y:y - conf.bike_driver_dy});
    bike.driverPosition = 1;

    Body.setPosition(bike.rearWheel, {x:x  + conf.bike_wheel_dx, y:y + conf.bike_wheel_dy});
    Body.setPosition(bike.frontWheel, {x:x  - conf.bike_wheel_dx, y:y + conf.bike_wheel_dy});
    Body.setVelocity(bike.vehicleBody, {x:0, y:0})
    Body.setVelocity(bike.rearWheel, {x:0, y:0})
    Body.setVelocity(bike.frontWheel, {x:0, y:0})

    // Reset position
    Body.setPosition(bike.vehicleBody, {x: x , y: y});
    Body.setPosition(bike.rearWheel, {x: x  + conf.bike_wheel_dx, y: y + conf.bike_wheel_dy});
    Body.setPosition(bike.frontWheel, {x: x  - conf.bike_wheel_dx, y: y + conf.bike_wheel_dy});

    // Reset linear velocity
    Body.setVelocity(bike.vehicleBody, {x: 0, y: 0});
    Body.setVelocity(bike.rearWheel, {x: 0, y: 0});
    Body.setVelocity(bike.frontWheel, {x: 0, y: 0});

    // Reset rotation
    Body.setAngle(bike.vehicleBody, 0);
    Body.setAngle(bike.rearWheel, 0);
    Body.setAngle(bike.frontWheel, 0);

    // Reset angular velocity
    Body.setAngularVelocity(bike.vehicleBody, 0);
    Body.setAngularVelocity(bike.rearWheel, 0);
    Body.setAngularVelocity(bike.frontWheel, 0);

    fixBikeDriverConstraints();
}

function fixBikeDriverConstraints() {
    let dx = conf.bike_driver_dx
    let dy = conf.bike_driver_dy
    if(keyIsDown(32)) { //space
	dy *= 2;
    }
    switch(bike.driverPosition) {
    case 0:
	bike.driverC0.length = Math.hypot(dx*0.5, dy);
	bike.driverC1.length = Math.hypot(dx*0.5, dy);
	bike.driverC2.length = Math.hypot(dx*1.5, dy);
	break;
    case 1:
	bike.driverC0.length = Math.hypot(dx, dy);
	bike.driverC1.length = Math.hypot(0, dy);
	bike.driverC2.length = Math.hypot(dx, dy);
	break;
    case 2:
	bike.driverC0.length = Math.hypot(dx*1.5, dy);
	bike.driverC1.length = Math.hypot(dx*0.5, dy);
	bike.driverC2.length = Math.hypot(dx*0.5, dy);
	break;
    }

} 

function keyPressed() {
    if (keyCode == DOWN_ARROW && bike.driverPosition > 0) {
	bike.driverPosition--;
    }
    if (keyCode == UP_ARROW && bike.driverPosition < 2) {
	bike.driverPosition++;
    }
    if (key == "r") {
	resetBike();
    }
}

function mousePressed() {
    resetBike(mouseX - delta);
}
