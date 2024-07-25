function verify2pow(x) {
    if (x < 1 || (x & (x - 1) != 0)) {
	throw new Error(x + " not a power of two ")
    }
}

class Nom {
    constructor(whole, div, two, three, six) {
	if (whole instanceof Nom) {
	    let other = whole;
	    verify2pow(other.div)
	    this.whole = other.whole
	    this.div = other.whole
	    this.two = other.two
	    this.three = other.three
	    this.six = other.six
	    this.simp();
	    return;
	}
        this.whole = whole || 0;
	this.div = div || 1;
        this.two = two || 0;
        this.three = three || 0;
        this.six = six || 0;
	verify2pow(this.div);
	this.simp()
	this.float = (this.whole + 1.4142135623730951 * this.two +
		      1.7320508075688772 * this.three + 
		      2.449489742783178 * this.six) / this.div
    }

    static makeRational(num, denom) {
	verify2pow(denom)
	let ret = new Nom(num)
	ret.div = denom
	ret.simp()
	return ret
    }

    div(power_of_two) {
	verify2pow(power_of_two)
	return new Nom(this.whole, this.div * power_of_two, this.two, this.three, this.six)
    }

    clone() {
	return new Nom(this.whole, this.div, this.two, this.three, this.six);
    }
    isZero() {
	return this.whole === 0 && this.two === 0 && this.three === 0 && this.six === 0;
    }
    isOne() {
	return this.whole === 1 && this.div == 1 && this.two === 0 && 
	    this.three === 0 && this.six === 0;
    }


    simp () {
	while(this.div > 1 && (this.whole % 2 == 0) && (this.two % 2 == 0)&& 
	      (this.three % 2 == 0) && (this.six % 2 == 0)) {
	    this.div /= 2;
	    this.whole /= 2;
	    this.two /= 2;
	    this.three /= 2;
	    this.six /= 2;
	}
    }

    toString() {
        let parts = [];
        if (this.whole !== 0) parts.push(this.whole);
        if (this.two !== 0) parts.push(`${this.two}*sqrt(2)`);
        if (this.three !== 0) parts.push(`${this.three}*sqrt(3)`);
        if (this.six !== 0) parts.push(`${this.six}*sqrt(6)`);
	let s = parts.length > 0 ? parts.join('+') : '0'
	if (this.div > 1) {
	    if (parts.length > 1) {
		s = "(" + s + ")"
	    }
	    s = s + "/" + this.div; 
	}
	return s
    }

    toFloat() {
	return this.float; 
    }

    eql(other) {
        if (other instanceof Nom) {
	    return (this.whole == other.whole) &&(this.two == other.two) &&
		(this.three == other.three) &&(this.six == other.six) &&(this.div == other.div)
        } else if (typeof other === 'number') {
	    return (this.toFloat() - other) < 0.000000001
        } else {
            throw new TypeError('Argument must be a number or an instance of Nom or a number');
        }
    }
    neg() {
	return new Nom(-this.whole, this.div, -this.two, -this.three, -this.six)
    }
    add(other) {
        if (other instanceof Nom) {
	    let this_multi = 1
	    let other_multi = 1
	    if (this.div > other.div) {
		other_multi = this.div / other.div
	    } else {
		this_multi = other.div / this.div
	    }
            return new Nom(
                this.whole * this_multi + other.whole * other_multi,
		Math.max(this.div, other.div),
                this.two * this_multi + other.two * other_multi,
                this.three * this_multi + other.three * other_multi,
                this.six * this_multi + other.six * other_multi
            );
        } else if (typeof other === 'number') {
            return new Nom(
                this.whole + other * this.div,
		this.div,
                this.two,
                this.three,
                this.six,
            );
        } else {
            throw new TypeError('Argument must be a number or an instance of Nom or a number');
        }
    }
    sub(other) {
        if (other instanceof Nom) {
	    let this_multi = 1
	    let other_multi = 1
	    if (this.div > other.div) {
		other_multi = this.div / other.div
	    } else {
		this_multi = other.div / this.div
	    }
            return new Nom(
                this.whole * this_multi - other.whole * other_multi,
		Math.max(this.div, other.div),
                this.two * this_multi - other.two * other_multi,
                this.three * this_multi - other.three * other_multi,
                this.six * this_multi - other.six * other_multi
            );
        } else if (typeof other === 'number') {
            return new Nom(
                this.whole - other * this.div,
		this.div,
                this.two,
                this.three,
                this.six,
            );
        } else {
            throw new TypeError('Argument must be a number or an instance of Nom or a number');
        }
    }


    multiply(other) {
        if (other instanceof Nom) {
            return new Nom(
                this.whole * other.whole + 2 * this.two * other.two + 3 * this.three * other.three + 6 * this.six * other.six,
		this.div * other.div,
                this.whole * other.two + this.two * other.whole + 3 * this.three * other.six + 3 * this.six * other.three,
                this.whole * other.three + this.three * other.whole + 2 * this.two * other.six + 2 * this.six * other.two,
                this.whole * other.six + this.six * other.whole + this.two * other.three + this.three * other.two
            );
        } else if (typeof other === 'number') {
	    return new Nom(
                this.whole * other,
		this.div,
                this.two * other,
                this.three * other,
                this.six * other
	    );
        } else {
            throw new TypeError('Argument must be a number or an instance of Nom');
        }
    }
}


class Matrix2x2 {
    constructor(a, b, c, d) {
	if (typeof a == "number") {
	    a = new Nom(a);
	}
	if (typeof b == "number") {
	    b = new Nom(b);
	}
	if (typeof c == "number") {
	    c = new Nom(c);
	}
	if (typeof d == "number") {
	    d = new Nom(d);
	}

        this.a = a; // First row, first column
        this.b = b; // First row, second column
        this.c = c; // Second row, first column
        this.d = d; // Second row, second column
    }

    isIdentity() {
	return this.a.isOne() && this.b.isZero() && this.c.isZero() && this.d.isOne();
    }
    isZero() {
	return this.a.isZero() && this.b.isZero() && this.c.isZero() && this.d.isZero();
    }

    // Method to multiply this matrix by another 2x2 matrix
    multiply(other) {
        return new Matrix2x2(
            this.a.multiply(other.a).add(this.b.multiply(other.c)), // New a
            this.a.multiply(other.b).add(this.b.multiply(other.d)), // New b
            this.c.multiply(other.a).add(this.d.multiply(other.c)), // New c
            this.c.multiply(other.b).add(this.d.multiply(other.d))  // New d
        );
    }

    // Method to transform a vector [x, y] by this matrix
    transformVector(vector) {
        const [x, y] = vector;
        return [
            this.a.multiply(x).add(this.b.multiply(y)), // New x
            this.c.multiply(x).add(this.d.multiply(y))  // New y
        ];
    }

    // Static method to get the identity matrix
    static identity() {
        return new Matrix2x2(1, 0, 0, 1);
    }

    // Static method to get the zero matrix
    static zero() {
        return new Matrix2x2(0, 0, 0, 0);
    }
}



let sin15 = new Nom(0, 4, -1, 0, 1)
let cos15 = new Nom(0, 4, 1, 0, 1)

let neg_sin15 = new Nom(0, 4, 1, 0, -1)
let neg_cos15 = cos15;

let left15 = new Matrix2x2(cos15, neg_sin15, sin15, cos15)
let right15 = new Matrix2x2(cos15, sin15, neg_sin15, cos15)

let rot = {}
rot[0] = new Matrix2x2(1, 0, 0, 1)

for (angle=15 ; angle<540 ; angle+=15) {
    rot[angle] = rot[angle - 15].multiply(left15)
    rot[-angle] = rot[-angle + 15].multiply(right15)
}

function vectorSub(a, b) {
    return [a[0].sub(b[0]), a[1].sub(b[1])]
}

function vectorSum(a, b) {
    return [b[0].add(a[0]), b[1].add(a[1])]
}

// Function to compute the cross product of vectors AB and AC
function crossProduct(A, B, C) {
    return (B[0].sub(A[0])).multiply(C[1].sub(A[1])).sub((B[1].sub(A[1])).multiply(C[0].sub(A[0])));
}

class Pat {
    static intersect_count = 0; 
    static box_intersect_count = 0; 
    //pseudo intersection test that simply tests if any of the vertices is inside the other poly
    boxIntersect (other) {
	Pat.box_intersect_count++; 
	if (this.maxx <= other.minx || this.maxy <= other.miny ||
	    this.minx >= other.maxx || this.miny >= other.maxy) {
	    return false; 
	}
	return true; 
    }
    intersect(other) {
	if (!this.boxIntersect(other)) {
	    return false; 
	}
	Pat.intersect_count++; 
	if (this.ownLineExclude(other) || other.ownLineExclude(this)) {
	    return false;
	}
	return true;
    }
    ownLineExclude(other) {
	// returns true if
	// this has a line that cuts off all of the points of other
	// from the rest of the points of this
	let n = this.points.length
	let n2 = other.points.length
	for (let i=0 ; i<n ; ++i) {
	    let a = this.points[i];
	    let b = this.points[(i + 1) % n];

	    let ok = true;
	    for (let j=0 ; j<n2 ; ++j) {
		let c = crossProduct(a, b, other.points[j]);
		if (c.toFloat() > 0) {
		    ok = false;
		    break;
		}
	    }
	    if (ok) return true;
	}
	return false;
    }


    toString() {
	let cx = (this.maxx + this.minx) / 2
	let cy = (this.maxy + this.miny) / 2

	return this.name + " at " + cx + " , " + cy
    }

    // Function to check if a point is strictly inside a convex polygon
    pointInside(point) {
	let prevSign = null;
	let polygon = this.points
	let n = polygon.length;

	for (let i = 0; i < n; i++) {
            let A = polygon[i];
            let B = polygon[(i + 1) % n];
            let crossProd = crossProduct(A, B, point);

            // If point is exactly on the edge, return false (not strictly inside)
            if (crossProd.isZero()) {
		return false;
            }

            let currentSign = Math.sign(crossProd.toFloat());

            if (prevSign === null) {
		prevSign = currentSign;
            } else if (prevSign !== currentSign) {
		return false;
            }
	}

	return true;
    }

    constructor(a, b, shape, color) {
	if (typeof a[0] == "number") {
	    a[0] = new Nom(a[0])
	}
	if (typeof a[1] == "number") {
	    a[1] = new Nom(a[1])
	}
	if (typeof b[0] == "number") {
	    b[0] = new Nom(b[0])
	}
	if (typeof b[1] == "number") {
	    b[1] = new Nom(b[1])
	}

	this.points = [a, b]
	let v = vectorSub(b, a)
	

	let minx = min(a[0].toFloat(), b[0].toFloat())
	let miny = min(a[1].toFloat(), b[1].toFloat())	

	let maxx = max(a[0].toFloat(), b[0].toFloat())
	let maxy = max(a[1].toFloat(), b[1].toFloat())	

	let rescue_push

	for (let i=0 ; i<shape.length ; ++i) {
	    let m = shape[i]
	    a = b
	    v = m.transformVector(v)
	    b = vectorSum(b, v)

//	    if ((i == shape.length - 1) || !(shape[i + 1].isIdentity())) {
		this.points.push(b)
//	    } 

	    let bx = b[0].toFloat(), by = b[1].toFloat()
	    minx = min(bx, minx)
	    miny = min(by, miny)

	    maxx = max(bx, maxx)
	    maxy = max(by, maxy)

	}
	this.color = color; 
	this.name = "polygon" + this.points.length

	this.minx = minx
	this.miny = miny
	this.maxx = maxx
	this.maxy = maxy
    }

    static makeSquare(color) {
	return ((a, b) => new Pat(a, b, [rot[90], rot[90]], color || "purple"))
    }
    static makeOcto(color) {
	return (a, b) => new Pat(a, b, [rot[45], rot[45], rot[45], 
					       rot[45], rot[45], rot[45]], 
					color || "cyan")
    }
    static makeTri(color) {
	return (a, b) => new Pat(a, b, [rot[120]], color || "orange")
    }
    static makeHex(color) {
	return (a, b) => new Pat(a, b, [rot[60], rot[60], rot[60], rot[60]], color || "red")
    }
    static makeRho(color) {
	return (a, b) => new Pat(a, b, [rot[60], rot[120]], color || "green")
    }
    static makeRhoRev(color) {
	return (a, b) => new Pat(a, b, [rot[120], rot[60]], color || "green")
    }
    static makeNeedle(color) {
	return (a, b) => new Pat(a, b, [rot[30], rot[150]], color || [100, 100, 255])
    }
    static makeNeedleRev(color) {
	return (a, b) => new Pat(a, b, [rot[150], rot[30]], color || [100, 100, 255])
    }
    static makeTrap(color) {
	return (a, b) => new Pat(a, b, [rot[60], rot[120], rot[0]], color || [255, 255, 125])
    }
    static makeTrapRev(color) {
	return (a, b) => new Pat(a, b, [rot[120], rot[0], rot[120]], 
					color || [255, 255, 125])
    }
    static makeTrapRev2(color) {
	return (a, b) => new Pat(a, b, [rot[60], rot[60], rot[120]], 
					color || [255, 255, 125])
    }

    draw(w) {
	fill(this.color)
	strokeWeight(w);
	stroke("black");

	beginShape();
	for (let v of this.points) {
	    vertex(v[0].toFloat(), v[1].toFloat())
	}
	endShape(CLOSE);
    }
}


function getBox(vpat) {
    let minx=0,miny=0,maxx=1, maxy=0;
    for (let pattern of vpat) {
	for (let p of pattern.points) {
	    minx = min(minx, p[0].toFloat())
	    maxx = max(maxx, p[0].toFloat())
	    miny = min(miny, p[1].toFloat())
	    maxy = max(maxy, p[1].toFloat())
	}
    }
    let w = maxx - minx;
    let h = maxy - miny;
    return [minx - w/7, miny - h/7, maxx + w/7, maxy + h/7];
}


function approachBox(current, desired, step) {
    step = step || 0.05

    let [x0, y0, x1, y1] = current;
    let [dx0, dy0, dx1, dy1] = desired;
    
    x0 += (dx0 - x0) * step;
    y0 += (dy0 - y0) * step;
    x1 += (dx1 - x1) * step;
    y1 += (dy1 - y1) * step;
    
    return [x0, y0, x1, y1];
}


function tiling1_Octo(a, b, depth, createPatCallback, delta) {
    console.log("octo call", a, b, depth)
    let octo = Pat.makeOcto("red")
    let pat = octo(a, b)
    createPatCallback(pat);
    let n = pat.points.length

    if (depth > 0) {
	for (let i=(delta || 0) ; i<n+(delta || 0) ; ++i) {
	    tiling1_Octo(pat.points[(i + 1) % n], pat.points[i % n], depth - 1, createPatCallback)
	    i++;
	    tiling1_Sq(pat.points[(i + 1) % n], pat.points[i % n], depth - 1, createPatCallback)
	}
    }
}


function tiling1_Sq(a, b, depth, createPatCallback) {
    console.log("sq call", a, b, depth)

    let sq = Pat.makeSquare("yellow")
    
    let pat = sq(a, b)

    if (!createPatCallback(pat)) {
	return
    }
    let n = pat.points.length
    if (depth > 0) {
	for (let i=0 ; i<n ; ++i) {
	    tiling1_Octo(pat.points[(i + 1) % n], pat.points[i], depth - 1, createPatCallback, 1)
	}
    }
}
