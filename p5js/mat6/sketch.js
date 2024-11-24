const { Engine, Render, Runner, World, Bodies, Body, Constraint, Events } = Matter;

// Configuration constants
const CONFIG = {
    width: window.innerWidth,
    height: window.innerHeight,
    zeroHeight: window.innerHeight - 40,
    groundColor:"black",

    wall: {
	x0: 100,
	r: 20,
	row: 10,
	col: 3,
	brickMass:0.1,
    },

    scale:0.9,
    arm: {
	length: 250,
	thickness: 15,
	height:180,
	x:window.innerWidth - 350,
	mass: 1,
	color:"#33ffaa"
    },
    counterweight: {
        radius: 25,
        mass: 60,
        ropeLength: 45,
	color:"red"
    },
    projectile: {
        radius: 15,
        mass: 1,
        ropeLength: 145,
	color:"orange"
    },
    stiffness: 0.99,
    pivotLocation: 0.153,
};

// Global variables
let engine, world, render;
let arm, counterweight, projectile, counterweightConstraint, projectileConstraint, wall;

function densityRect (mass, w, h) {
    return mass / (w * h); 
}

function densityCircle(mass, r) {
    return mass / Math.PI / (r * r); 
}


function localToWorld(body, localPoint) {
    const rotatedPoint = Matter.Vector.rotate(localPoint, body.angle); // Rotate by body angle
    return Matter.Vector.add(rotatedPoint, body.position); // Translate by body position
}

function createRectangleBody(length, width, x, y, drop, mass, color) {
    color = color || "orange"
    const angle = Math.atan2(drop, length); // Angle of the lower segment
    const x2 = x + length * Math.cos(angle); // x-coordinate of the second point
    const y2 = y + length * Math.sin(angle); // y-coordinate of the second point

    // Calculate the perpendicular vector for the top segment
    const dxPerp = width * Math.sin(angle); // x-offset for width (perpendicular to lower segment)
    const dyPerp = -width * Math.cos(angle); // y-offset for width (perpendicular to lower segment)

    // Define the four corners of the rectangle
    const corners = [
        { x: x, y: y }, // Lower-left
        { x: x2, y: y2 }, // Lower-right
        { x: x2 + dxPerp, y: y2 + dyPerp }, // Upper-right
        { x: x + dxPerp, y: y + dyPerp }, // Upper-left
    ];

    // Compute the center of the rectangle
    const centerX = corners.reduce((sum, p) => sum + p.x, 0) / 4;
    const centerY = corners.reduce((sum, p) => sum + p.y, 0) / 4;

    // Create the Matter.js rectangle body
    const rectangle = Matter.Bodies.rectangle(centerX, centerY, length, width, {
        angle: angle, // Rotation angle of the rectangle
	density: densityRect(mass, length, width),
	render: {
	    fillStyle:color
	}
    });

    return [rectangle, 
	    x + dxPerp / 2, y + dyPerp / 2, 
	    x2 + dxPerp / 2, y2 + dyPerp / 2, 
	    centerX, centerY];
}

function interpXY(x1, y1, x2, y2, p) {
    return [x1 * (1 - p) + x2 * p, y1 * (1 - p) + y2 * p]
}

function createWorld() {
    // Create a new engine
    engine = Engine.create();
    world = engine.world;

    // Ground
    const ground1 = Bodies.rectangle(CONFIG.width / 16, CONFIG.zeroHeight + 20 , CONFIG.width / 8, 40, 
				    { isStatic: true,
				      render: {fillStyle: CONFIG.groundColor}});
    World.add(world, ground1);


    const ground2 = Bodies.rectangle(CONFIG.width * 7 / 8, CONFIG.zeroHeight + 20 , CONFIG.width / 4, 40, 
				    { isStatic: true,
				      render: {fillStyle: CONFIG.groundColor}});
    World.add(world, ground2);



    // Trebuchet arm
    const armLength = CONFIG.arm.length * CONFIG.scale;

    const x0 = CONFIG.arm.x; // left of screen
    const y0 = CONFIG.zeroHeight - CONFIG.arm.height * CONFIG.scale;

    const [armObject, x1, y1, x2, y2, cx, cy] = 
	  createRectangleBody(armLength, CONFIG.arm.thickness * CONFIG.scale, x0, y0, 
			      CONFIG.arm.height * CONFIG.scale, 
			      CONFIG.arm.mass, CONFIG.arm.color)
    arm = armObject
    World.add(world, arm);
    console.log("adding arm", x1, y1, x2, y2)

    // Counterweight
    const [cwX, cwY] = interpXY (x1, y1, x2, y2, 0.03);
    const cwRopeY = cwY + CONFIG.counterweight.ropeLength * CONFIG.scale;

    counterweight = Bodies.circle(cwX, cwRopeY, CONFIG.counterweight.radius * CONFIG.scale, {
        density: densityCircle(CONFIG.counterweight.mass, CONFIG.counterweight.radius * CONFIG.scale),
	render: {fillStyle: CONFIG.counterweight.color},
    });
    console.log("adding weight", cwX, cwY)
    World.add(world, counterweight);

    // Counterweight constraint
    counterweightConstraint = Constraint.create({
        bodyA: counterweight,
        bodyB: arm,
        pointB: { x: cwX - cx, y: cwY - cy},
        length: CONFIG.counterweight.ropeLength * CONFIG.scale,
        stiffness: CONFIG.stiffness,
    });
    World.add(world, counterweightConstraint);

    // Projectile
    const projectileX = x2 - CONFIG.projectile.ropeLength * CONFIG.scale;
    const projectileY = CONFIG.zeroHeight - CONFIG.projectile.radius * CONFIG.scale;
    projectile = Bodies.circle(projectileX, projectileY, CONFIG.projectile.radius * CONFIG.scale, {
        density: densityCircle(CONFIG.projectile.mass, CONFIG.projectile.radius * CONFIG.scale),
	frictionAir: 0,
	render: {fillStyle: CONFIG.projectile.color},
    });
    World.add(world, projectile);
    console.log("adding projectile", projectileX, projectileY)


    const [proX, proY] = interpXY (x1, y1, x2, y2, 0.97);
    // Projectile constraint
    projectileConstraint = Constraint.create({
        bodyA: projectile,
        bodyB: arm,
        pointB: { x: proX - cx, y: proY - cy},
        //length: CONFIG.projectile.ropeLength,
        stiffness: CONFIG.stiffness,
    });
    World.add(world, projectileConstraint);

    const dPivot = CONFIG.arm.length * CONFIG.scale / 10

    const [pivotX, pivotY] = interpXY (x1, y1, x2, y2, CONFIG.pivotLocation);
    const pivotConstraint1 = Constraint.create({
        pointA: {x: pivotX - dPivot, y:pivotY - dPivot},
        bodyB: arm,
        pointB: { x: pivotX - cx, y: pivotY - cy},
        //length: CONFIG.projectile.ropeLength,
        stiffness: CONFIG.stiffness,
    });
    World.add(world, pivotConstraint1)

    const pivotConstraint2 = Constraint.create({
        pointA: {x: pivotX + dPivot, y:pivotY - dPivot},
        bodyB: arm,
        pointB: { x: pivotX - cx, y: pivotY - cy},
        //length: CONFIG.projectile.ropeLength,
        stiffness: CONFIG.stiffness,
    });
    World.add(world, pivotConstraint2)
    wall = []
    for (let i=0 ; i<CONFIG.wall.row ; ++i) {
	for (let j=0 ; j<CONFIG.wall.col ; ++j) {
	    let brick = Bodies.rectangle(CONFIG.wall.x0 + CONFIG.wall.r * (j + 0.5), 
					 CONFIG.zeroHeight - CONFIG.wall.r * (i + 0.5), 
					 CONFIG.wall.r, CONFIG.wall.r,
					 {render: {fillStyle: (i + j) % 2 ? "white" : "black"},
					  density: densityRect(CONFIG.wall.brickMass, 
							       CONFIG.wall.r, CONFIG.wall.r)});
	    World.add(world, brick);
	    wall.push(brick);
	}
    }
}

function setupSimulation() {
    // Renderer
    render = Render.create({
        element: document.body,
        engine: engine,
        options: {
            width: CONFIG.width,
            height: CONFIG.height,
            wireframes: false,
            background: '#444444'
        },
    });
    Render.run(render);

    // Runner
    const runner = Runner.create();
    Runner.run(runner, engine);
}

// Initialize and reset world
function initialize() {
    if (render) {
        Render.stop(render);
        World.clear(world);
        Engine.clear(engine);
        render.canvas.remove();
    }
    createWorld();
    setupSimulation();
}

let launched = false;
initialize();

// Mouse interaction
document.addEventListener("mousedown", () => {
    if (!launched) {
        // Release the projectile
        World.remove(world, projectileConstraint);
        launched = true;
    } else {
        // Reset the world
        launched = false;
        initialize();
    }
});
