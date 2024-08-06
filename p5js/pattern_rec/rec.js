var Rec = class {
    constructor (defs) {
	if (typeof defs === "string") {
	    defs = Rec.proc(defs)
	}
	this.defs = defs || []
	this.f = []
    }

    static proc(s) {
	s = s.toLowerCase();
	s = s.split(/[\s,;]+/)
	let ret = {}
	for (let word of s) {
	    let match = word.match(/^[a-z]:([a-z](-*|[0-9]+)[.^>]*)*$/)
	    if (!match) {
		continue; 
	    }
	    word = match[0]

	    let ret_entry = []
	    let ret_key = word[0]
	    let val = 0;
	    let parm = [];
	    let letter = null
	    for (let i=2 ; i<word.length ; ++i) {
		let char = word[i]
		if (char === "-") {
		    val--;
		} else if (/^\d$/.test(char)) {
		    if (val <= 0) {
			val = parseInt(char)
		    } else {
			val = val * 10 + parseInt(char)
		    }
		} else if (".^>".includes(char)) {
		    parm.push(char)
		} else {
		    if (letter) {
			ret_entry.push([letter, val, parm])
		    }
		    letter = char;
		    val = -1;
		    parm = [];
		}
	    }
	    if (letter) {
		ret_entry.push([letter, val, parm])
	    }
	    if (ret_entry.length >= 1) { 
		ret[ret_key] = ret_entry
	    }
	}
	return ret
    }

    setDefs(defs) {
	this.defs = defs
    }
    addF (c, f) {
	this.f[c] = f
    }
    static isChar(c) {
	return typeof c === "string" && c.length === 1
    }
    static assert(ok, error) {
	if (!ok) {
	    throw new Error(error || "error")
	}
    }
    push(data) {
	this.stack[this.stack.length - 1].push(data)
    }
    pop() {
	for (let i=this.stack.length-1 ; i>=0 ; --i) {
	    let val = this.stack[i].pop()
	    if (val) {
		return val
	    }
	}
    }
    execf (f, depth) {
	return this.f[f](() => this.pop(), depth)
    }
    rec(command, depth) {
	console.log("rec", command, depth)
	if (depth <= 0) {
	    return
	}

	if (!command in this.defs) {
	    console.log("unknown command ", command)
	    return
	} 
	let local_stack = []
	let ret = []
	this.stack.push(local_stack)

	for (let c of this.defs[command]) {
	    console.log("doing sub commands", c)
	    let [c2, d2, parms] = c
	    parms = parms || []
	    let val
	    if (d2 < 0) {
		d2 = Math.max(depth + d2, 0)
	    }
	    if (c2 in this.defs) {
		if (d2 > 0) {
		    val = this.rec(c2, d2)
		}
	    } else if (c2 in this.f) {
		val = this.execf(c2, d2)
	    }

	    if (!val || val.length <= 0) {
		continue;
	    }

	    var parm = ">" 
	    if (parms.length > 0) {
		parm = parms[parms.length - 1]
	    }
	    for (let i=0 ; i<val.length ; i++) {
		if (i < parms.length) {
		    parm = parms[i]
		}
		if (parm === "^") {
		    ret.push(val[i])
		} else if (parm === ">") {
		    local_stack.push(val[i])
		}
	    }
	}
	this.stack.pop()
	return ret
    }
    setErrorMessageFunction (f) {
	this.errorMessageFunction = f
    }
    go (initial_data) {
	initial_data = initial_data || "patient zero"
	this.stack = [[initial_data]]
	try {
	    this.rec("x", 2)
	} catch (e) {
	    if (this.errorMessageFunction) {
		this.errorMessageFunction(e.message)
	    } else {
		console.log("thrown error", e.message)
	    }
	}

    }
}


 
function foo(fconsume) {
    console.log("executing foo")
    console.log("consuming: ", fconsume())
    return ["message 1", "message 2", "message 3"]
}

rec = new Rec("x:q4;q:f.>.q")

rec.addF("f", foo)
