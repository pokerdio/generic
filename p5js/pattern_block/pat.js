function verify2pow(x) {
    if (x < 1 || (x & (x - 1) != 0)) {
	throw new Error(x + " not a power of two ")
    }
}

class Nom {
    constructor(whole, div, two, three, six) {
        this.whole = whole || 0;
	this.div = div || 1;
        this.two = two || 0;
        this.three = three || 0;
        this.six = six || 0;
	verify2pow(this.div);
	this.simp()
    }

    static makeRational(num, denom) {
	verify2pow(denom)
	let ret = new Nom(num)
	ret.div = denom
	ret.simp()
	return ret
    }

    clone() {
	return new Nom(this.whole, this.div, this.two, this.three, this.six);
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
	let s = parts.length > 0 ? parts.join(' + ') : '0'
	if (this.div > 1) {
	    if (parts.length > 1) {
		s = "(" + s + ")"
	    }
	    s = s + " / " + this.div; 
	}
	return s
    }

    toFloat() {
	return (this.whole + 1.4142135623730951 * this.two +
		1.7320508075688772 * this.three + 2.449489742783178 * this.six) / this.div
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

class Pat {
    static color = {lit:'white', dark:'black', transparent:'gray'}
    constructor(point1, point2) {
	this.cols = cols;
	this.rows = rows;
    }
    isEqual(other) {
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
let left30 = left15.multiply(left15)
let left45 = left15.multiply(left30)
let left60 = left30.multiply(left30)
let left120 = left60.multiply(left60)

let right15 = new Matrix2x2(cos15, sin15, neg_sin15, cos15)
let right30 = right15.multiply(right15)
let right45 = right15.multiply(right30)
let right60 = right30.multiply(right30)
let right120 = right60.multiply(right60)



