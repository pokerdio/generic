const { Engine, Render, Runner, World, Bodies, Mouse, MouseConstraint, Events } = Matter;

const engine = Engine.create();
const { world } = engine;
const render = Render.create({
    element: document.body,
    engine: engine,
    options: {
        width: window.innerWidth - 16,
        height: window.innerHeight - 16,
        wireframes: false,
    },
});

const config = {
    rectThickness: 20,
    ballRadius: 20,
    selectedColor: 'red',
    selectedTool:'rect',
    offScreenThreshold: render.canvas.height + 100,
    friction: 0.01,
    frictionAir: 0.01,
    restitution: 0.4,
    bounce: 0.8,
}


Render.run(render);
Runner.run(Runner.create(), engine);


// Adjust render size on window resize
window.addEventListener('resize', () => {
    render.canvas.width = window.innerWidth - 16;
    render.canvas.height = window.innerHeight - 16;
    render.options.width = window.innerWidth - 16;
    render.options.height = window.innerHeight - 16;
});




// Variables for color and points
let startPoint = null;

// Add color buttons as static bodies
const colors = ['#FF0000', '#00FF00', '#0000FF', '#ffff00', '#00ff66'];
const tools = ['rect', 'ball', 'delete', 'climb', 'bounce'];

colors.forEach((color, index) => {
    var button
    switch(tools[index]) {
    case "ball":
	button = Bodies.circle(50 + index * 70, 30, 25, {
            isStatic: true,
            render: { fillStyle: color },
	});
	break;
    case "delete":
 	button = [Bodies.rectangle(50 + index * 70, 30, 60, 15, {
            isStatic: true,
	    angle: 0.5,
            render: { fillStyle: color },
	}), Bodies.rectangle(50 + index * 70, 30, 60, 15, {
            isStatic: true,
	    angle: -0.5,
            render: { fillStyle: color },
	})];

	break; 
    default: 
	button = Bodies.rectangle(50 + index * 70, 30, 60, 30, {
            isStatic: true,
            render: { fillStyle: color },
	});
    }
    let buttons = [].concat(button)

    for (let b of buttons) {
	b.customColor = color; // Custom property to store color
	b.customTool = tools[index]
    }
    World.add(world, buttons);
});

function addClimb(pointA, pointB, color) {
    const width = Math.abs(pointB.x - pointA.x); // Calculate the distance between points
    const height = Math.abs(pointB.y - pointA.y); // Constant thickness
    const centerX = (pointA.x + pointB.x) / 2;
    const centerY = (pointA.y + pointB.y) / 2;

// Create the sensor body and add it to the world
    const climb = Bodies.rectangle(centerX, centerY, width, height, {
	isStatic: true,
	isSensor: true,
	customRole: "climb",
	render: { fillStyle: color }
    });

    World.add(world, climb);
    world.bodies.sort((a,b) =>(b.customRole == "climb" ? 1 : 0) - (a.customRole == "climb" ? 1 : 0) )
}


// Function to add a new rectangle
function addRectangle(pointA, pointB, color, restitution) {
    const width = Math.hypot(pointB.x - pointA.x, pointB.y - pointA.y); // Calculate the distance between points
    const height = config.rectThickness; // Constant thickness
    const centerX = (pointA.x + pointB.x) / 2;
    const centerY = (pointA.y + pointB.y) / 2;
    const angle = Math.atan2(pointB.y - pointA.y, pointB.x - pointA.x); // Calculate angle between points

    console.log("creating", restitution || config.restitution)
    const rectangle = Bodies.rectangle(centerX, centerY, width, height, {
	angle: angle, // Set the rotation angle
	friction: config.friction,
	frictionAir: config.frictionAir,
	restitution: restitution || config.restitution,
	isStatic: true,
	render: { fillStyle: color },
    });

    console.log(rectangle.restitution)
    World.add(world, rectangle);
}

// Function to add a new rectangle
function addBall(point, color) {
    const height = 20; // Constant thickness
    const ball = Bodies.circle(point.x, point.y, config.ballRadius, {
	friction: config.friction,
	frictionAir: config.frictionAir,
	restitution: config.restitution,
	render: { fillStyle: color },
    });
    console.log("ball resti", ball.restitution)
    World.add(world, ball);
}


// Mouse event handling
const mouse = Mouse.create(render.canvas);
const mouseConstraint = MouseConstraint.create(engine, { mouse });
World.add(world, mouseConstraint);

Events.on(mouseConstraint, 'mousedown', (event) => {
    const { x, y } = event.mouse.position;
    const clickedBodies = Matter.Query.point([ ...world.bodies ], { x, y });

    for (body of clickedBodies) { 
	// Check if a color button was clicked
	if (body.customTool) {
            config.selectedColor = body.customColor;
	    config.selectedTool = body.customTool;
	    startPoint = null
	    return; 
	} 
	if (config.selectedTool == "delete") {
	    World.remove(world, body)
	    return; 
	}
    }
    
    let resti = config.restitution
    switch(config.selectedTool)  {
    case 'bounce':
	resti = config.bounce
    case 'rect':
	if (!startPoint) {
	    startPoint = { x, y };
	} else {
	    addRectangle(startPoint, { x, y }, config.selectedColor, resti);
	    startPoint = null;
	}
	break;
    case 'ball':
	startPoint = null;
	addBall({x, y}, config.selectedColor);
	break;
    case 'climb':
	if (!startPoint) {
	    startPoint = { x, y };
	} else {
	    addClimb(startPoint, { x, y }, config.selectedColor);
	    startPoint = null;
	}
	break; 
    }
});

// Set a threshold for objects that fall off-screen

// Function to remove off-screen bodies
function removeOffScreenBodies() {
    let killList = []
    world.bodies.forEach(body => {
	if (body.position.y > config.offScreenThreshold) {
	    killList.push(body)
	}
    })
    killList.forEach((body => World.remove(world, body)))
//    console.log("bodies", world.bodies.length)
}

// Run the function periodically (e.g., on every engine update)
Events.on(engine, 'afterUpdate', removeOffScreenBodies);

// Function to find and apply an upward force to bodies intersecting with the sensor
function applyUpwardForceToIntersectingBodies() {
    let upSet = new Set()


    for (body of world.bodies) {
	if (body.customRole == "climb") {
	    const sensorBounds = body.bounds;

	    // Query all bodies that intersect with the sensor's bounding box
	    const bodiesInRegion = Matter.Query.region(world.bodies, sensorBounds);

	    // Loop through each intersecting body and apply an upward force
	    bodiesInRegion.forEach(body => {
		if (!body.isStatic) { // Ensure we don't apply force to the sensor itself
		    upSet.add(body)
		}
	    });
	}
    }

    for (body of upSet) {
	Matter.Body.applyForce(body, body.position, { x: 0, y: -0.005 });
    }
}

// Call this function periodically, e.g., in each engine update
Events.on(engine, 'afterUpdate', applyUpwardForceToIntersectingBodies);

