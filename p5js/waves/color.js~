const palette_strings = {
    //https://lospec.com/palette-list ones
    mondrian:'000000,FF0000,FFFF00,0000FF,FFFFFF',
    sunset:'FF150c21,FF332232,FF703c67,FF5a2d2a,FFb15b35,FFeaa44a,FFf0ce6e,FFfcf8f4',
    purple: 'FF381a31,FF8e43a1,FFe9edff,FFcaa860', 
    red:'FF6a063a,FFac4859,FFfc948e,FFffe1da',
    
    //chatgpt ones 
    tranquil_lake:'#92A8D1,#034F84,#76C7C0,#D9BF77,#B5AE4E',
    pastel_dream: "#FFD1DC,#FFB7B2,#FFDB58,#C9FFA2,#B2B2B2",
    ocean_breeze: "#83C5BE,#6A0572,#AB83A1,#F7C5D1,#FFE156",
    sunset_serenity: "#FF9068,#FFDCA8,#9AD1D4,#5E4B56,#2F2F2F",
    mystical_forest: "#32533D,#61845F,#B9A48A,#E9B44C,#A23B72",
    electric_vibes: "#00F5A0,#0083A8,#150485,#FF00F5,#FFD800",
    cherry_blossom: "#FF9AA2,#FFB7B2,#FFDAC1,#E2F0CB,#B5EAD7",
    galactic_explorer: "#001F3F,#003366,#C4DEF6,#2ECC40,#FF4136",
    golden_hour: "#FFB86F,#D8A07E,#5E5757,#005D63,#008891",
    purple_haze: "#23022E,#570E37,#840038,#BD1550,#E97F5F"

};

const hex_decode = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5,
		    "6":6, "7":7, "8":8, "9":9, a:10, b:11, 
		    c:12, d:13, e:14, f:15}

function hexDecode(s) {
    s = s.toLowerCase();
    ret = 0;
    mult = 1;
    for (let i=s.length - 1 ; i>=0 ; --i) {
	ret = ret + hex_decode[s[i]] * mult
	mult = mult * 16
    }
    return ret;
}

function makePal(palette_string) {
    let s = palette_string.split("\n");
    if (s.length == 1) {
	s = s[0].split(",");
    }
    let ret = [];
    for (let i=0 ; i<s.length ; ++i) {
	let c = s[i]
	if (c.length == 8) {
	    c = c.substring(2, 8);
	}
	if (c.length == 7) {
	    c = c.substring(1);
	}
	ret[i] = color(hexDecode(c.substring(0, 2)), 
		       hexDecode(c.substring(2, 4)), 
		       hexDecode(c.substring(4, 6)))
    }
    return ret
}


function getPal(palette_name) {
    let ret = makePal(palette_strings[palette_name])
    return ret
}

function getRandomPalette() {
    let col_name = random(Object.keys(palette_strings));
    getRandomPalette.col_name = col_name
    return makePal(palette_strings[col_name]);
}
