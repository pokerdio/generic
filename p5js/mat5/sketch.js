const { Engine, Render, World, Bodies, Mouse, MouseConstraint, Constraint, Events } = Matter;

const config = {
    clength: 150,
    scale:2.5,
    stiffness:0.03,
    radius: 10,
    dy:25,
    dx:50,
    restitution:0.1,
    friction: 0.02,
    frictionAir: 0.05,
    timeScale: 0.7,
    damping:0.05,
}

// Create an engine and a renderer
const engine = Engine.create();
engine.world.gravity.y = -engine.world.gravity.y

engine.timing.timeScale = config.timeScale
const render = Render.create({
    element: document.body,
    engine: engine,
    options: {
        width: window.innerWidth - 16,
        height: window.innerHeight - 16,
        wireframes: false,
        background: '#444444'
    }
});

// Run the renderer
Render.run(render);

// Run the engine
Engine.run(engine);


window.addEventListener('resize', () => {
    render.canvas.width = window.innerWidth - 16;
    render.canvas.height = window.innerHeight - 16;
    render.options.width = window.innerWidth - 16;
    render.options.height = window.innerHeight - 16;
});


// Enable mouse control
const mouse = Mouse.create(render.canvas);
const mouseObject = Bodies.circle(100, 100, config.radius * config.scale * 0.01, {
    isStatic:false,
    restitution: config.restitution,
    mass: 5.0,
    render: { fillStyle: randomColor() }
});

World.add(engine.world, mouseObject);

function randomColor() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
}

// Function to recursively create circles
function createRecursiveCircles(body, depth, digitString, bodies, constraints) {

    if (depth >= digitString.length) return;

    // Get the number of circles to create at this depth
    const numCircles = parseInt(digitString[depth]) + 1;
    const radius = config.radius * config.scale;  // Radius of each circle

    const parentCircles = []; // Array to keep track of this level's circles

    for (let i = 0; i < numCircles; i++) {
        // Random position around the parent position
        const offsetX = (Math.random() - 0.5) * config.dx * (depth ? config.scale : 1.5 * config.scale);
        const offsetY = config.dy * (depth ? config.scale : 1.5 * config.scale);
        const circlePosition = {
            x: body.position.x + offsetX,
            y: body.position.y + offsetY
        };

        // Create the circle
        const circle = Bodies.circle(circlePosition.x, circlePosition.y, radius, {
            friction: config.friction,
	    frictionAir: config.frictionAir,
            restitution: config.restitution,
	    
            render: { fillStyle: randomColor(), strokeStyle:'#000000', lineWidth: 2 }
        });
	bodies.push(circle)

        // Create a constraint connecting it to the parent position
        const constraint = Constraint.create({
            bodyA: body,
            bodyB: circle,
            stiffness: config.stiffness,
	    damping:config.damping,
            render: { type: 'line', strokeStyle: '#3498db', lineWidth: 1, anchors: false }
        });
	constraints.push(constraint)


        // Add this circle to the array of parent circles
        parentCircles.push(circle);
    }

    // Recursively create children circles for each of this level's circles
    parentCircles.forEach(circle => {
        createRecursiveCircles(circle, depth + 1, digitString, bodies, constraints);
    });
}

// Main function to generate the structure based on the input string
function createStructureFromDigits(digitString) {
    // Clear the world before creating a new structure
    World.clear(engine.world, false);
    World.add(engine.world, mouseObject);  // Re-add mouse constraint

    let bodies = []
    let constraints = []
    createRecursiveCircles(mouseObject, 0, digitString, bodies, constraints);

    World.add(engine.world, bodies);
    World.add(engine.world, constraints);
}

// Detect mouse movement to update initial circle positions
Events.on(engine, "beforeUpdate", () => {
    mouseObject.position.x = mouse.position.x;
    mouseObject.position.y = mouse.position.y;
});

// Test with an example stringc
createStructureFromDigits("1100");

// // For testing: Change structure when clicking anywhere
document.addEventListener("click", () => {
    const randomDigits = Math.floor(Math.random() * 12 + 6).toString(3); // Random 3-digit number
    createStructureFromDigits(randomDigits);
});
