// © 2014 Peter Higginson (plh256 at hotmail.com)
// Set of functions for use with JavaScript sessons
// Convert screen size tests to warnings so runs on small windows with scrolling

// note 0,0 is the top left corner, any names must go in quotes e.g. "name"

// Provided functions
// 	rectangle("name", x, y, width, height, "centre_colour", "edge_colour", opt);  // opt=1 for thin border, 2 for thick
// 	text("name", "text", x, y, size, "colour");
// 	text("name", "text", x, y, size, "colour", "attribute", "value", "font"); 	// attribute, value and font are optional
// 	remove("name");
//	randomInt(min, max);						// note returns the result
//	button("name", "text", x, y, "function");
//	image("name", "file", x, y, "description");			// description is required - e.g. used by a braille reader
//	imageOrder("name", z);					// specify which comes on top (higher numbers)
//	move("name", x, y);
//	trapKey("character", "upFunction", "downFn");		// note functions may have one parameter - the character trapped
//	getMilliseconds();
// 	timeout = delay(milliseconds, "function", parameters);  	// note returns a value which can be used with clearTimeout
// System functions
//	clearTimeout(timeout);
//	alert("message");
//	prompt("Question : ", "default answer");
//	location.reload();						// reload the page (to restart the game)

var maxHeight, maxWidth; 	//current window dimensions

function startIt()
{
	getDimensions();
	main();
}

function getDimensions()
{
	if(typeof(window.innerWidth) == 'number' ) {	//Chrome
		maxWidth = window.innerWidth;
		maxHeight = window.innerHeight;
	} else { 							//IE 6+ in 'standards compliant mode'
		maxWidth = document.documentElement.clientWidth;
		maxHeight = document.documentElement.clientHeight;
	}
}

function rectangle(name,x,y,width,height,centre_colour,edge_colour,thin)
{
	x = Math.floor(x +0.49);		// allow for non-exact parameters
	y = Math.floor(y + 0.49);

	// make sure that the rectangle fits on the screen
	if (x < 0 || y < 0 || width <= 0 || height <= 0 || width > (maxWidth - 10) || height > (maxHeight -10)) {
		console.log("rectangle - warning - not on screen");
	}
	//if ((x + width) > maxWidth) x = maxWidth - width;
	//if ((y + height) > maxHeight) x = maxHeight - height;

	// see if it already exists
	var elePosn = document.getElementById(name);
	if (elePosn) {
		if (elePosn.nodeName != "DIV") {
			console.log("rectangle - name already in use for non-rectangle/text");
			return;
		}
	} else {   						// if not create and insert
		elePosn = document.createElement("div");
		elePosn.id = name;
		document.body.appendChild(elePosn);
	}
	elePosn.style.position = "absolute";
	elePosn.style.left = x+"px";
	elePosn.style.top = y+"px";
	elePosn.style.width = width+"px";
	elePosn.style.height = height+"px";
	elePosn.style.background = centre_colour;
	if (edge_colour) {
		if (thin == 1) elePosn.style.border = "thin solid "+edge_colour;
		else if (thin == 2) elePosn.style.border = "thick solid "+edge_colour;
		else elePosn.style.border = "medium solid "+edge_colour;
	}
}

// attribute is optional but must be of form "onclick"
function text(name, contents, x, y, size, colour, attribute, value, font)
{
	x = Math.floor(x +0.49);		// allow for non-exact parameters
	y = Math.floor(y + 0.49);
	
	// make sure that the rectangle fits on the screen
	if (x < 0 || y < 0 || x > (maxWidth - 10) || y > (maxHeight -10)) {
		console.log("text - warning - not on screen");
	}

	// see if it already exists
	var elePosn = document.getElementById(name);
	if (elePosn) {
		if (elePosn.nodeName != "DIV") {
			console.log("text - name already in use for non-rectangle/text");
			return;
		}
	} else {   						// if not create and insert
		elePosn = document.createElement("div");
		elePosn.id = name;
		document.body.appendChild(elePosn);
	}
	elePosn.style.position = "absolute";
	elePosn.style.left = x+"px";
	elePosn.style.top = y+"px";
	elePosn.style.color = colour;
	elePosn.style.fontSize = size+"px";
	if (font) elePosn.style.fontFamily = font;	
	if (attribute) {
		elePosn.setAttribute(attribute, value);
	}
	elePosn.innerHTML = contents;
}

function move(name, x, y)
{
	x = Math.floor(x +0.49);		// allow for non-exact parameters
	y = Math.floor(y + 0.49);

	// make sure that the move is at least partly on the screen
	// the -10 might be a problem with very small objects - may need to improve at some point
	if (x < 0 || y < 0 || x > (maxWidth - 10) || y > (maxHeight -10)) {
		console.log("move - warning - not on screen");
	}
	// make sure it already exists
	var elePosn = document.getElementById(name);
	if (!elePosn) {
		console.log("move- name "+name+" does not exist");
		return;
	}
	elePosn.style.position = "absolute";
	elePosn.style.left = x+"px";
	elePosn.style.top = y+"px";
}

// calling move twice for the blobs caused separation - particularly on Firefox
// so try to make the move more interlaced
function dmove(name, x, y, name2, x2, y2)
{
	x = Math.floor(x +0.49);		// allow for non-exact parameters
	y = Math.floor(y + 0.49);
	x2 = Math.floor(x2 +0.49);		// allow for non-exact parameters
	y2 = Math.floor(y2 + 0.49);

	// make sure that the move is at least partly on the screen
	// the -10 might be a problem with very small objects - may need to improve at some point
	if (x < 0 || y < 0 || x > (maxWidth - 10) || y > (maxHeight -10)) {
		console.log("dmove - warning - not on screen");
	}
	if (x2 < 0 || y2 < 0 || x2 > (maxWidth - 10) || y2 > (maxHeight -10)) {
		console.log("dmove - warning - not on screen");
	}
	// make sure it already exists
	var elePosn = document.getElementById(name);
	if (!elePosn) {
		console.log("dmove - name "+name+" does not exist");
		return;
	}
	var elePosn2 = document.getElementById(name2);
	if (!elePosn2) {
		console.log("dmove - name "+name2+" does not exist");
		return;
	}
	elePosn.style.position = "absolute";
	elePosn2.style.position = "absolute";
	elePosn.style.left = x+"px";
	elePosn2.style.left = x2+"px";
	elePosn.style.top = y+"px";
	elePosn2.style.top = y2+"px";
}

	
	
	
function remove(name)
{
	var elePosn = document.getElementById(name);
	if (elePosn) document.body.removeChild(elePosn);
}

function randomInt(min,max)
{
    return Math.floor(Math.random()*(max-min+1)+min);
}

// attempt to get button better on iPAD
function button(name, txt, x, y, func)
{
	text(name,'<button onclick="'+func+'">'+txt+'</button>',x,y,12, "black");
}

/* button as a form displayed differently (and too big) on iPAD
function button(name, text, x, y, func)
{
	x = Math.floor(x +0.49);		// allow for non-exact parameters
	y = Math.floor(y + 0.49);

	// make sure that the button is at least partly on the screen
	if (x < 0 || y < 0 || x > (maxWidth - 10) || y > (maxHeight -10)) {
		console.log("button - warning - not on screen");
	}

	// see if it already exists
	var elePosn = document.getElementById(name);
	if (elePosn) {
		if (elePosn.nodeName != "FORM") {
			console.log("button - name already in use for non-button");
			return;
		}
	} else {   						// if not create and insert
		elePosn = document.createElement("form");
		elePosn.id = name;
		document.body.appendChild(elePosn);
	}
	elePosn.style.position = "absolute";
	elePosn.style.left = x+"px";
	elePosn.style.top = y+"px";
	elePosn.innerHTML = '<input type="button" value="'+text+'" onClick="'+func+'">';
} */

function image(name, fileName, x, y, desc)
{
	x = Math.floor(x +0.49);		// allow for non-exact parameters
	y = Math.floor(y + 0.49);

	// make sure that the image is at least partly on the screen
	if (x < 0 || y < 0 || x > (maxWidth - 10) || y > (maxHeight -10)) {
		console.log("image - warning - not on screen");
	}

	// see if it already exists
	var elePosn = document.getElementById(name);
	if (elePosn) {
		if (elePosn.nodeName != "IMG") {
			console.log("image- name already in use for non-image");
			return;
		}
	} else {   						// if not create and insert
		elePosn = document.createElement("img");
		elePosn.id = name;
		document.body.appendChild(elePosn);
	}
	elePosn.style.position = "absolute";
	elePosn.style.left = x+"px";
	elePosn.style.top = y+"px";
	elePosn.src = fileName;
	elePosn.alt = desc;
}

function imageOrder(name, z)
{
	// make sure it already exists
	var elePosn = document.getElementById(name);
	if (!elePosn) {
		console.log("imageOrder - name "+name+" does not exist");
		return;
	}
	elePosn.style.zIndex = z;
}

function getMilliseconds()
{
	var d = new Date();
	return d.getTime();
}

function delay(ms, fn)	// has additional parameters as arguments to fn
{
	var tmp = fn+"(";
	for (var i = 2; i < arguments.length; i++) {
		if (i > 2) tmp += ",";
		tmp += arguments[i];
	}
	tmp += ")";
	// console.log("delay "+ms+"ms, call "+tmp);
	return setTimeout(tmp, ms);
}

var chrsToMatch = [];
var dnFnCall = [];
var upFnCall = [];
var chrsDown = [];

function trapKey(chr, fnDn, fnUp)		// note fnDn/fnUp can have one parameter - the character trapped
{
	var indx = chrsToMatch.indexOf(chr);
	if (indx == -1) {				// not seen this character before
		indx = chrsToMatch.push(chr) - 1;
		chrsDown[indx] = 0;
	}
	dnFnCall[indx] = fnDn;
	upFnCall[indx] = fnUp;
}

function keyDown(e)
{
	var x=e.keyCode;
        if (x == 8) {
		var d = e.srcElement || e.target;
		var preventKeyPress;
		switch (d.tagName.toUpperCase()) {
		case 'TEXTAREA':
			preventKeyPress = d.readOnly || d.disabled;
			break;
                case 'INPUT':
			preventKeyPress = d.readOnly || d.disabled ||
				(d.attributes["type"] && $.inArray(d.attributes["type"].value.toLowerCase(), ["radio", "checkbox", "submit", "button"]) >= 0);
			break;
                case 'DIV':
			preventKeyPress = d.readOnly || d.disabled || !(d.attributes["contentEditable"] && d.attributes["contentEditable"].value == "true");
			break;
		default:
			preventKeyPress = true;
			break;
		}
		if (preventKeyPress) e.preventDefault();
        }
	var keychar=String.fromCharCode(x);
	if (x == 27 || x == 9) keychar = x;
	var indx = chrsToMatch.indexOf(keychar);
	if (indx == -1) {
		// waste of space on console log
		// console.log("Key " + keychar + " was pressed down "+x);
	} else {
		// when you hold a key down you do not get ups
		// if (chrsDown[indx] == 0) {
			chrsDown[indx] = 1;
			if (dnFnCall[indx]) window[dnFnCall[indx]](e);
		//}
	}
}

function keyUp(e)
{
	var x=e.keyCode;
	var keychar=String.fromCharCode(x);
	if (x == 27 || x == 9) keychar = x;
	var indx = chrsToMatch.indexOf(keychar);
	if (indx != -1 && chrsDown[indx] == 1) {
		chrsDown[indx] = 0;
		if (upFnCall[indx]) window[upFnCall[indx]](e);		
	}
}
