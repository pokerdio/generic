const HIGH_DX = 0.1;
const LOW_DX = 0.0001;

function gen1(ds, f) {
    let ret = [];
    let last_fval = f(0.0);
    ret.push({f:last_fval, x:0.0});

    let dx = HIGH_DX;
    let x = 0;
    
    let fval;
    while (true) {
	fval = f(x + dx);
	let no_down_move = true;
	while (abs(fval - last_fval) > ds && dx > LOW_DX) {
	    dx = dx * 0.8;
	    fval = f(x + dx);
	    no_down_move = false;
	}
	while (no_down_move && abs(fval - last_fval) < ds && dx < HIGH_DX) {
	    let attempt_dx = dx * 1.2;
	    let attempt_fval = f(x + attempt_dx);
	    if (abs(last_fval - attempt_fval) > ds) {
		break;
	    }
	    fval = attempt_fval;
	    dx = attempt_dx;
	}
	x += dx; 
	if (x > 1.0) {
	    ret.push({x:1.0, f:f(1.0)});
	    return ret;
	}
	ret.push({x:x, f:fval});
	last_fval = fval;
    }
}
