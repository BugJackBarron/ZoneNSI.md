// RISC simulator
// © 2016 Peter Higginson (plh256 at hotmail.com)

// BEWARE you cannot do == NaN (at least not to get the result you expect)
// THIS NEEDS FIXING here !!!!!!

// This is a follow on from my LMC Simulator http://www.peterhigginson.co.uk/LMC

// It is vaguely ARM/Thumb like but has a 16 bit word addressed memory and no byte or
// 32 bit operations. See the help file for a list of instructions.

// At the time I wrote the original LMC emulator, I was also showing a Primary School
// Computer Club some JavaScript programming. To make that less complex, I provided
// the set of functions listed below. So this project was also a test of those functions.

// This is much more complex than the programs the students were expected to do so there
// are places where other system functions are used and places where a more advanced
// knowledge of CSS and HTML is required. One common extension is that "text()" is used as
// a <div> container with some complex HTML in it and is extended with optional parameters
// to set attributes of the <div>.

// Functions in routines.js
// 	rectangle("name", x, y, width, height, "centre_colour", "edge_colour",opt);  // opt=1 for thin border, 2 for thick
// 	text("name", "text", x, y, size, "colour");
// 	text("name", "text", x, y, size, "colour", "attribute", "value", "font"); 	// attribute, value and font are optional
// 	remove("name");
//	randomInt(min, max);					// note returns the result
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

// global variables
var myTimeout = false; 					// to hold return from setTimeOut()
var myTimeout1 = false; 					// for first blob during FETCH cycle
var myTimeout2 = false; 					// for second blob during FETCH cycle
var register = [];						// register file
var registerSP = 0;
var registerLR = 0;
var flags = 0;						// N Z C V
var pCounter = 0;
var programText = "";					// loaded or selected file
var programHTML = "";					// display version of programText
var programEdit = "";					// formatted version to edit
var output = "";
var output1 = "";						// copy as characters
var address = [];					// main memory
var instructionTxt = [];
var speed;
var defaultSpeed = 175;				//175 for moving blobs case, 100 if not
var inst;							// made global for FETCH/EXECUTE use
var addr;							// made global for FETCH/EXECUTE use
var waitingForInput = false;
var registerToInput = 0;
var modifyingProgram = false;
var s2T = 1;
var stopping;
var runRate;						// measured update speed
var valW = 5;						// tick delay for execution display - set dynamically
var oneStep;
var monospace = '"Courier New Bold",courier,monospace';
var running = false;
var submit;						// flag to handle code area cancel
var oldPCMarker = 0;
var oldSPMarker = 400;
var memOpt = 0;					// 0 = 2's comp, 1 = unsigned, 2 = hex, 3 = binary
var execErr = false;
var stepTxt = '';

halted="Programme stopp&eacute. REINIT, CHARGER, SELECT ou modifier la m&eacutemoire";

function main()						// main is called when the page is loaded
{
	window.document.title = "Simulateur RISC par Peter Higginson";
	trapKey(9, "tabKey", null);			// trap TAB in program input mode
	trapKey(27, "escKey", null);			// trap ESC to exit from input mode
	rectangle("background", 0, 0, 1021, 719, "white", "lightBlue");
	image("layout", "layout.png", 2, 2, "RISC System layout");
	rectangle("memory", 535, 48, 470, 630, "white", "#5B81A8");
	rectangle("program", 21, 52, 227, 545, "white", "green");
	rectangle("output", 398, 559, 106, 90, "white", "blue");
	rectangle("input", 269, 560, 90, 16, "white", "blue");
	rectangle("ir", 329, 311, 72, 20, "white", "#BE5050");
	rectangle("flags", 360, 280, 40, 16, "white", "#BE5050");
	rectangle("R0", 330, 232, 46, 16, "white", "");
	rectangle("R1", 330, 216, 46, 16, "white", "");
	rectangle("R2", 330, 200, 46, 16, "white", "");
	rectangle("R3", 330, 184, 46, 16, "white", "");
	rectangle("R4", 330, 168, 46, 16, "white", "");
	rectangle("R5", 330, 152, 46, 16, "white", "");
	rectangle("R6", 330, 136, 46, 16, "white", "");
	rectangle("R7", 330, 120, 46, 16, "white", "");
	rectangle("sp", 335, 104, 41, 16, "white", "");
	rectangle("lr", 335, 88, 41, 16, "white", "");
	rectangle("pc", 335, 72, 41, 16, "white", "");
	rectangle("message", 25, 679, 484, 18, "white", "");
	button("assemble", "ASSEMBLER", 19, 610, "assemble()");	
	button("run", "LANCER", 100, 610, "run()");
	button("step", "PAS", 160, 610, "step3()");
	button("reset", "REINIT", 19, 638, "reset1()");
	if (window.File && window.FileReader) {
		text("load", loadText, 72, 638, 12, "black");		
	} else {
		alert("L'interface fichiers n'est pas support\351e dans ce navigateur.");
	}
	button("help", "AIDE", 142, 638, "window.open('help.html')");
	text("ch", menu, 187, 640, 10, "black");
	text("op", options, 266, 640, 10, "black");
	updateR(0,0);
	updateR(1,0);
	updateR(2,0);
	updateR(3,0);
	updateR(4,0);
	updateR(5,0);
	updateR(6,0);
	updateR(7,0);
	updateFlags(0);
	updateLR(0);
	updateSP(400);	
	updatePC(0);
	text("program", "", 21, 52, 12, "black", "onclick", "openProgram(this)", monospace);	// to get the onclick
	message("SELECT pour choisir un exemple, CHARGER pour charger un fichier, ou entrez un programme, ou &eacutecrivez dans la m&eacutemoire");	
	rectangle("ver1", 560, 690, 190, 18, "white", "");   // needed to stop funny
	rectangle("ver2", 760, 690, 200, 18, "white", "");   // wrapping at large scales
	text("ver1", "<b>Simulateur RISC V1.06</b>", 560, 690, 16, "black");
	text("ver2", "<b>&copy; Peter L Higginson 2016</b>", 760, 690, 16, "black");
	rectangle("mode", 735, 21, 250, 18, "white", "");   // and this one
	text("mode","<b>(mots de 16 bits en sign&eacute)",735,21,16,"black");
	for (var i=0; i<=9;++i) text("memt"+i, "<b>"+i+"</b>", 600+i*43, 58, 14, "black");
	for (var i=0; i<=39; ++i) {
		// if prefer space padding &#8199; is supposed to be the same width as a number
		if (i==0) t = "<b>000</b>";
		else if (i<10) t = "<b>0"+i+"0</b>";
		else t = "<b>"+i+"0</b>";
		text("meml"+i, t, 544, 76+i*15, 14, "black");
	}
	delay(1, "main1");					// pause to draw most of page at this point
}

var holdI;

function main1()					// time drawing one line at a time
{
	holdI = 0;
	runRate = getMilliseconds();
	main2();
}

function main2()					// time drawing one thing at a time
{
	for (var i=0; i<10; ++i) {
		rectangle("a"+holdI, 568+(holdI%10)*43, 74+Math.floor(holdI/10)*15, 40, 14, "white", "white",1);
		setAddress(holdI,0);
		++holdI;
	}
	if (holdI >= 400) {
		updatePCmarker(0);
		delay(1, "main3");
	} else delay(1, "main2");
}
	
function main3()				
{
	runRate = (getMilliseconds() - runRate)/20;
	// typical values for RISC Simulator memory layout is around 10 to 14 on my Dell
	console.log("runRate for updates is "+runRate);
}

function blinkoff()
{
	if (!waitingForInput) return;					// ignore if not doing input
									// should already have been deleted
	text("inpxx", "", 261, 541, 12, "red");
	delay(500, "blinkon");
}
function blinkon()
{
	if (!waitingForInput) return;					// ignore if not doing input
	text("inpxx", " &nbsp; Entrer valeur", 261, 541, 12, "red");
	delay(1000, "blinkoff");
}

// ESCAPE key handler - for all input cases except program requested input
function escKey(e)
{
	if (!waitingForInput) return;					// ignore if not doing input
	if (myTimeout || myTimeout1 || myTimeout2) return;	// ignore if running a program
	e.preventDefault();
	waitingForInput = false;
	if (savOpenAddress) {						// has a memory address open
		var x = parseInt(savOpenAddress.id[1]);
		if (savOpenAddress.id.length >= 3) x = x*10 + parseInt(savOpenAddress.id[2]);
		if (savOpenAddress.id.length == 4) x = x*10 + parseInt(savOpenAddress.id[3]);
		if (x < 400) setAddress(x, address[x]);	// removes input form and resets value
		savOpenAddress = false;
	} else if (modifyingProgram) {					// has the program area open
		modifyingProgram = false;
		textToHtml();
	} else {								// must be the PC which is open
		updatePC(pCounter);
		updatePCmarker(pCounter);
	}
	message("ESC pour stopper la saisie");
}

// TAB key handler - for all input cases except program requested input
function tabKey(e)
{
	e.preventDefault();
	// Warning - do not put an alert before the preventDefault
	if (!waitingForInput) return;						// ignore if not doing input
	if (myTimeout || myTimeout1 || myTimeout2) return;	// ignore if running a program
	if (savOpenAddress) {						// has a memory address open
		var x = parseInt(savOpenAddress.id[1]);
		if (savOpenAddress.id.length >= 3) x = x*10 + parseInt(savOpenAddress.id[2]);
		if (savOpenAddress.id.length == 4) x = x*10 + parseInt(savOpenAddress.id[3]);
		var inp = document.getElementById("aForm");
		var ok = checkInput(inp.value); // so do not overwrite error message
		loseAddress(inp);				// ignore errors because "alert" wrecks things
		if (x < 399) {					// open next location
			++x;
			if (ok) message("Modification du contenu de la m&eacutemoire");
			var elePosn = document.getElementById("a"+x);
			var widthX = (memOpt == 3) ? '114' :'50';
			elePosn.innerHTML = '<form action="javascript:addressSubmit()"><input id="aForm" type="text" style="padding:0; border:0; width:'+widthX+'px;font-size:90%;"></form>';
			document.getElementById("aForm").focus();
			document.getElementById("aForm").setAttribute("onblur","loseAddress(this)");
			waitingForInput = true;
			savOpenAddress = elePosn;
		}
	} else if (modifyingProgram) {			// has the program area open		
		var textarea = document.getElementById('pForm');
		var s = textarea.selectionStart;
		textarea.value = textarea.value.substring(0,textarea.selectionStart) + "\t" + textarea.value.substring(textarea.selectionEnd);
		textarea.selectionEnd = s+1; 					// should reset the cursor
	} else {							// must be the PC
		var inp = document.getElementById("PCForm");
		losePC(inp);				// ignore errors because "alert" wrecks things
	}
}

function openProgram(inp)
{
	if (waitingForInput) return;					// ignore if doing input (ours or the program)
	if (myTimeout || myTimeout1 || myTimeout2) return;		// ignore if something running
	submit = true;						// flag and two save areas to handle code area cancel
	message("Modification du programme");
	inp.style.overflow = "initial";					// reset scroll mode because textarea has own
	inp.innerHTML = '<form action="javascript:programSubmit()"><textarea id="pForm" rows="29" cols="26" style="padding:0; border:0; font-size:14px;" spellcheck="false">'+
			programEdit+'</textarea><input type="submit" value="Valider" style="color:red;font-weight:bold;margin:5px"><input onclick="programCancel()" type="submit" value="Annuler" style="color:red;font-weight:bold;margin:5px"></form>';
	document.getElementById("pForm").focus();
	waitingForInput = true;
	modifyingProgram = true;
}

function programSubmit()
{
	if (!waitingForInput) {
		alert("Mauvaise saisie - entr\351e non attendue");
		return false;
	}
	var elePosn = document.getElementById("pForm");
	waitingForInput = false;
	modifyingProgram = false;
	if (submit) {
		programText = elePosn.value;
		textToHtml();
		assemble();
	} else {				// reset original values
		text("program", programHTML, 21, 52, 12, "black", "onclick", "openProgram(this)", monospace);
		document.getElementById("program").style.overflow = "auto";
	}
	return;					// returning false caused problems with IE
}

function programCancel()
{
	submit = false;
}

function ch2()				// a selection has been made
{
	reset1();
	var ch = document.getElementById("ch1").value;
	if (ch > 0 && ch < 6) {
		programText = program[ch];
		textToHtml();
		assemble();
	} else {
		message("Mauvaise s&eacutelection");
	}
}


function op2()				// an option selection has been made
{
	var op = document.getElementById("op1").value;
	// switch did not work - probably op is a string
	if (op == 1) {					// clear memory
		for (var i = 0; i < 400; ++i) {
			setAddress(i, 0);
		}
		text("op", options, 272, 640, 10, "black");	// rewrite to clear selection
	} else if (op > 1 && op < 6) {			// 2 = 2's comp, 3 = unsigned, 4 = hex, 5 = binary
		memOpt = op-2;
		if (memOpt == 0) text("mode","<b>(mots de 16 bits en sign&eacute)",735,21,16,"black");
		else if (memOpt == 1) text("mode","<b>(mots de 16 bits en non sign&eacute)",735,21,16,"black");
		else if (memOpt == 3) text("mode","<b>(mots de 16 bits en binaire)",735,21,16,"black");
		else text("mode","<b>(mots de 16 bits en hexad&eacutecimal)",735,21,16,"black");
		
		// rewrite the outer ring and memory
		rectangle("background", 0, 0, (memOpt == 3) ? 1935 : 1021, 719, "white", "lightBlue");
		rectangle("memory", 535, 48, (memOpt == 3) ? 1385 : 470, 630, "white", "#5B81A8");
		
		// rewrite the heading (use memX so have scale in one place)
		var baseX = (memOpt == 3) ? 628 : 600;
		for (var i=0; i<=9;++i) text("memt"+i, "<b>"+i+"</b>", baseX+i*memX(1), 58, 14, "black");
		for (var i=0; i<400; ++i) {		// rewrite the contents
			rectangle("a"+i, 568+memX(i), 74+Math.floor(i/10)*15, (memOpt == 3)?133:40, 14, "white", "white",1);
			setAddress(i, address[i]);
		}
		for (var i=0; i<8; ++i) {
			updateR(i , register[i]);
		}
		updatePCmarker(pCounter);		// so move to correct place
		updateSP(registerSP);
		
	} else if (op > 5 && op < 10) {		// set default speed (turn fetch/execute on or off)
		defaultSpeed = 175;
		if (op == 6) defaultSpeed = 1;
		if (op == 7) defaultSpeed = 100;
		if (op == 9) defaultSpeed = 250;
		if (running) {
			speed = defaultSpeed;		// so speeds up instantly
			doSpeed();
		}
	}
}

function read_chg(inp)
{
	reset1();
	var fs = inp['files'];
	if(!fs) { alert("Mauvais retour du s\351lecteur de fichiers"); return; }
	var fr=new FileReader;
	fr.readAsText(fs[0],'utf-8');
	fr.onload = function() {
		programText = fr.result;
		textToHtml();
		assemble();
		text("ch", menu, 184, 640, 10, "black");		// reset SELECT (so does not look as if running one of those)
		text("load", loadText, 79, 638, 12, "black");	// re-write so can load same file again		
	}
}

var program = [];
// Simple ADD of two numbers
program[1] = "\tINP R0,2\n\tINP R1,2\n\tADD R2,R1,R0\n\tOUT R2,4\n\tHLT\n// Affiche la somme de deux nombres\n";
// Output Max of two numbers
program[2] = "\tINP R0,2\n\tINP R1,2\n\tCMP R1,R0\n\tBGE HIGHER\n\tOUT R0,4\n\tBRA DONE\nHIGHER\tOUT R1,4\nDONE\tHLT\n// Lire deux nombres et afficher le plus grand des deux\n\t";
// ASCII
program[3] = "MOV R2,#32\nLOOP: OUT R2,7\nADD R2,#1\nCMP R2,#127\nBLT LOOP\nMOV R2,#10\nOUT R2,7\nHLT\n// Affiche le code ASCII de tous les caract&egraveres\n"

var menu = '<select id="ch1" onchange="ch2()"><option value="0">SELECT</option><option value="1">add</option><option value="2">max</option><option value="3">ascii</option></select>';

var loadText = '<input type="file" id="read-input" onchange="read_chg(this)" autocomplete="off" style="display:none;" ><button onclick="document.getElementById(&#39;read-input&#39;).click()">CHARGER</button>';

var inputForm = '<form action="javascript:inputSubmit()"><input id="iForm" type="text" style="padding:0 0 0 2px; border:0; width:80px; font-size:14px;"></form>';

var options = '<select id="op1" onchange="op2()"><option value="0">OPTIONS</option><option value="1">r&eacuteinit m&eacutemoire</option><option value="2">sign&eacute</option><option value="3">non sign&eacute</option><option value="4">hexad&eacutecimal</option><option value="5">binaire</option><option value="6">def rapide</option><option value="7">def ex&eacutecution</option><option value="8">def normal</option><option value="9">def lent</option></select>';

// format a program - from the input to the display, also produce the version to edit with correct tabbing
function textToHtml()
{
	programHTML = "";
	programEdit = "";
	var lines = 0;
	var count = 0;
	var lineHTML="";
	var comment = false;
	var pLength = programText.length;
	if (programText[pLength-1] != "\n") {		// make sure last line ends correctly
		programText += "\n";
		++pLength;
	}
	for (var n = 0; n < pLength; ++n) {
		var letter = programText[n];
		if (letter == '\t') {
			letter = ' ';
		}
		if (letter == ' ' && n+1 < pLength && programText[n+1] == ' ') continue; // ignore multiple spaces
		if (letter != '\n' && letter < ' ') continue;	// ignore all control characters other than newline
		if (count == 0) { 					// start of a line
			if (letter == '\n') continue;		// ignore blank lines
			if (letter == ' ') continue;		// ignore leading spaces
			if (letter == '/') {
				count = 10;		// stop comments being padded
				comment = true;	// or numbered
			}
			if (n+3 < pLength && instruction((letter+programText[n+1]+programText[n+2]).toUpperCase()) < 200 && programText[n+3] <= ' ') {
				lineHTML += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
				programEdit += "        ";
				count = 7;
			}
		}
		// remember that HTML will ignore multiple spaces anyway
		while (count < 7 && letter == ' ' && programText[n+1] > ' ') {
			programEdit += " ";
			lineHTML += "&nbsp;";
			++count;
		}
		if (letter == '\n') {
			if (comment) {
				programHTML += lineHTML;
			} else {
				if (lines <10) programHTML += '&nbsp;';
				if (lines <100) programHTML += '&nbsp;';
				programHTML += lines + '&nbsp;' + lineHTML;
				++lines;
			}
			lineHTML = "";
			if (n+1 < pLength) programHTML += "<br />";		// dont need br at end
			programEdit += "\n";
			count = 0;
			comment = false;
		} else {
			++count;
			lineHTML += letter;
			programEdit += letter;
		}
	}
	text("program", programHTML, 21, 52,12, "black", "onclick", "openProgram(this)", monospace);
	document.getElementById("program").style.overflow = "auto";
}

function message(y)
{
	text("message", y, 25, 679, 14, "#FF0000");
}

function assemble()
{
	if (waitingForInput) return;
	reset1();
	for (var i = 0; i < 400; ++i) {					// clear the memory
		setAddress(i, 0);
	}
	var pLength = programText.length;
	if (programText[pLength-1] != "\n") {		// make sure last line ends correctly
		programText += "\n";
		++pLength;
	}
	var lineCount = 0;
	var wordCount = 0;
	var tempWordText = "";
	var labelText = [];					// make 3 entries per line: label/0, instruction, address/label/0
	var instText = [];
	var offsetText = [];					// for RISC the offsetText can be quite complex
	var comment = false;
	var comma = false;
	for (var n = 0; n < pLength; ++n) {
		var letterText = programText[n];
		if (comment && letterText != '\n') continue;
		if (letterText == '/') {
			comment = true;
			continue;
		}
		if (letterText == ',') {
			comma = true;
		} else {
			if (comma) {
				if (letterText == ' ') continue;	// remove spaces (ot tabs) after a comma
				comma = false;
			}
		}
		if (letterText == '\t') letterText = ' ';
		if (letterText == ':' && wordCount == 0) letterText = ' ';
		if (letterText == ' ' || letterText == '\n') {	// end of word
			if (tempWordText != "") {				// ignore leading/trailing spaces
				if (wordCount == 0 && instruction(tempWordText.toUpperCase()) < 200) {
					labelText[lineCount] = 0;				// no label
					++wordCount;
				}
				if (wordCount == 0) {
					if (tempWordText.length == 2 &&
					    (tempWordText[0] == 'R' || tempWordText[0] == 'r')
					    && tempWordText[1] >= '0' &&
					    tempWordText[1] <= '9') {
						message("&eacutetiquette ne peut pas &ecirctre un nom de registre  "+tempWordText);
						showError(lineCount);
						return;
					}
					var a;
					for (a = 0; a < lineCount; ++a) {
						if (tempWordText == labelText[a]) break;
					}
					if (a < lineCount) {		// duplicate label
						message("&eacutetiquette dupliqu&eacutee aux lignes  "+a+" and "+lineCount+' &nbsp;'+tempWordText);
						showError(lineCount);
						return;
					}
					labelText[lineCount] = tempWordText;
				} else if (wordCount == 1) instText[lineCount] = tempWordText.toUpperCase();
				else if (wordCount == 2) offsetText[lineCount] = tempWordText;
				else offsetText[lineCount] += tempWordText;
				tempWordText = "";
				++wordCount;
			}
		}
		if (letterText == '\n') {
			if (wordCount > 0) {				// ignore blank lines (or just comments)
				if (wordCount == 1) instText[lineCount] = 0;	// no inst - produce error later
				if (wordCount < 3) offsetText[lineCount] = 0;	// no offset
				wordCount = 0;
				++lineCount;
			}
			comment = false;
		}
		if (letterText > ' ') {
			tempWordText += letterText;
		}
	}
	if (lineCount > 400) {		// max 400 memory locations
		message('Programme trop gros - '+lineCount+' lignes (maximum de 400)');
		showError(400);
		return;
	}
	var r = 0;
	var error = false;
	while (r < lineCount) {
		var inst = instruction(instText[r]);
		if (inst == 200) {
			error = "instruction inconnue &agrave la ligne "+r+' '+instText[r];
			break;
		}
		// for RISC we need to work out the format of the offsetText
		var decode = instKey[inst];	
		// 1 = no parameters 2 = Rd,Rx 4 = Rd,#immed(8) 8= Rd,#immed(4) 16 = Rd,address 32 = Rd,device
		// 64 = Rx 128 = address 256 = Rd,Rs,Rb 512 = Rd,offset(Rn) 1024 = number(16)
		// 2048 = Rd,Rs,#immed(4) 4096 = Rs/Rd can be SP/LR/PC/flags (MOV only)
		// 8192 = Rd can be SP (2 param inst) 16384 = Rn can be SP 

		// get the various types of op codes (for the various layouts - only valid if decode bit set)
		var I1 = inst1[inst];		// note & with 0xFFF0 for R,#im8 and R,off(R) but
			// use as is for 0/1 parameter insts (exc R) and for R,dev, R,cnt(4) and Rd,Rs,#cnt(4)
		var I2 = inst2[inst];		// op code for 2 & 3 reg and BRA Rx type instructions
		var I3 = (inst1[inst] & 0xF) * 4096;		// R,addr type instructions
		var a = 0;
		
		if (!offsetText[r]) {
			if ((decode&1)==0) {
				error = "param&egravetres attendus &agrave la ligne "+r+' '+instText[r];
				break;
			}
			a = I1;						// no parameters
		} else if (offsetText[r][0] == '{') {	// PSH/POP register list only
			if (inst != 41 && inst != 42) {	// PSH is 42, POP is 41
				error = "Mauvais param&egravetres &agrave la ligne "+r+' '+instText[r];
				break;
			}
			a = 0x7C00;
			for (var i = 1; i < offsetText[r].length; ++i) {
				if (offsetText[r][i] == '}') break;
				if (offsetText[r][i] == ' ') continue;
				if (offsetText[r][i] == ',') continue;
				var reg1 = regDecode(offsetText[r].substring(i,i+2));
				// returns 0-7 for R0 to R7, 15=PC 13=SP 14=LR 12=flags, 20 if NaN else 21
				if (i > (offsetText[r].length-2) ||
				    (offsetText[r][i+2] =='-' && reg1 > 7) ||
				    (offsetText[r][i+2] !='-' &&
					offsetText[r][i+2] !=',' &&
					offsetText[r][i+2] !=' ' &&
					offsetText[r][i+2] !='}') ||
				    (inst == 41 && reg1 > 7 && reg1 != 15) ||
				    (inst == 42 && reg1 > 7 && reg1 != 14)) {
					error = "Mauvais param&egravetres &agrave la ligne "+r+' '+instText[r];
					break;
				}
				if (offsetText[r][i+2] !='-') { // simple case
					++i;
					if (reg1 < 8) a |= (1<<reg1);
					else a |= 0x100;
				} else {				// reg1-reg2 case
					i+=3;
					var reg2 = regDecode(offsetText[r].substring(i,i+2));
					if (i > (offsetText[r].length-2) || reg2 > 7 ||
					    (offsetText[r][i+2] !=',' &&
						offsetText[r][i+2] !=' ' &&
						offsetText[r][i+2] !='}') ||
					    reg1 > reg2) {
						error = "Mauvais param&egravetres &agrave la ligne "+r+' '+instText[r];
						break;
					}
					++i;
					while (reg1 <= reg2) {
						a |= (1<<reg1);
						++reg1;
					}
				}
			}
			if (error) break;
			if (inst == 41) a += 0x200;
		} else {
			var pos1 = offsetText[r].indexOf(',',0);
			if (pos1 == -1) {				// no commas - so one parameter only
				var reg = regDecode(offsetText[r]);
				// returns 0-7 for R0 to R7, 15=PC 13=SP 14=LR 12=flags, 20 if NaN else 21
				if (reg == 21) {		// it is numeric
					if ((decode&(128+1024))==0 ||
					    (a=parseInt(offsetText[r])) == NaN ||
					    a > 65535 || a < -32768 ||
					    ((a>399||a<0) && (decode&1024)==0)) {
						error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
						break;
					}
					a += I1;
				} else if (reg == 20) {	// it is a label
					for (a = 0; a < lineCount; ++a) {
						if (offsetText[r] == labelText[a]) break;
					}
					if (a >= lineCount) {
						error = "&eacutetiquette inconnue &agrave la ligne "+r;
						break;
					}
					if ((decode&128)==0) {
						error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
						break;
					}
					a += I1;
				} else if (reg>8) {		// SP etc. - now not allowed with PSH/POP
					error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
					break;
				} else {				// R0 to R7
					if ((decode&64)==0){
						error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
						break;
					}
					a = reg + I2;
				}
			} else {
				var pos2 = offsetText[r].indexOf(',',pos1+1);
				if (pos2 == -1) {			// 1 comma - so two parameters
					var reg1 = regDecode(offsetText[r].substring(0,pos1));
					// returns 0-7 for R0 to R7, 15=PC 13=SP 14=LR 12=flags, 20 if NaN else 21
					var reg2 = regDecode(offsetText[r].substring(pos1+1));
					if (reg1!=13 || (decode&8192)==0 || reg2!=20) { // not ADD/SUB SP,#imm case
						if (reg1 > 15 || ((decode&4096)==0 && (reg1>7 || (reg2>7 && reg2<20)) ||
						    (reg1>7 && reg2>7 && reg2<20) ||
						    (reg1<8 && (decode&(2+4+8+16+32+256+512)) == 0)) ||
						    (reg2<8 && (decode&(2+256))==0)) {
							error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
							break;
						}
					}
					if (reg1>7 && (decode&4096)!=0) { // MOV specisl,Rs
						a = 0x7220 + (reg1&3)*8 + reg2;
					} else if (reg2 == 21) {		// a number (not immediate)
						a=parseInt(offsetText[r].substring(pos1+1));
						if ((decode&32)!=0 && a!=NaN && a<16 && a >= 0) { // Rd,device
							a += I1 + reg1*16;
						} else if ((decode&16)!=0 && a!=NaN && a<400 && a >= 0) { 
							a+= I3 + reg1*512;				// Rd,address
						} else {
							error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
							break;
						}
					} else if (reg2 == 20) {	// a label or a #imm or #cnt or off(R)
						var nxt = offsetText[r].substring(pos1+1,pos1+2);
						if ( nxt == '#') {		// #immediate or #count
							a=parseInt(offsetText[r].substring(pos1+2));
							if (a==NaN || a>255 || a < 0 || (decode&(12+2048))==0 ||
							    ((decode&(8+2048))!=0 && a>15)) {
								error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
								break;
							}
							if (reg1==13) {
								if (inst==1) a+= 0x6E00;
								else a+= 0x6F00;
							} else {
								if ((decode&2048)!=0) reg1 += reg1*8;	// change to 2 reg inst
								else if ((decode&8)==0) reg1 *= 16;
								a += (I1 & 0xFFF0) + reg1*16;  // so *256 for imm(8)
							}
						} else if(nxt=='(' || nxt=='[' || (nxt>='0' && nxt<='9')) {
							// I1 & 0xFFF0 for  R,off(R) type
							pos2 = offsetText[r].indexOf('(',pos1+1);
							if (pos2 == -1) pos2 = offsetText[r].indexOf('[',pos1+1);
							if (pos2 == -1 || (decode & 512) == 0) {
								error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
								break;
							}
							if (pos2 == (pos1+1)) a = 0;
							else a=parseInt(offsetText[r].substring(pos1+1,pos2));
							reg2 = regDecode(offsetText[r].substring(pos2+1,pos2+3));
							if (a == NaN || a < 0 || a > 63 || (reg2 >8 && reg2 !=13 &&
								(decode&16384)!=0)) {
								error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
								break;
							}
							if (reg2==13) {		// LDR/STR offset(SP) case
								if (inst==39) a+= (reg1<<6) +0x7800;
								else a+= (reg1<<6) +0x7A00;
							} else {
								a += (I1 & 0xF000) + (reg1<<9) + (reg2<<6);
							}
						} else {		// try for R,label
							var label = offsetText[r].substring(pos1+1);
							for (a = 0; a < lineCount; ++a) {
								if (label == labelText[a]) break;
							}
							if (a >= lineCount) {
								error = "&eacutetiquette inconnue &agrave la ligne "+r;
								break;
							}
							if ((decode&16)==0) {
								error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
								break;
							}
							a += I3 + reg1*512;
						}
					} else if (reg2 > 7) {		// MOV Rd,specisl
						a = 0x7200 + (reg2&3)*8 + reg1;
					} else {			// a two register instruction
						if (decode&256) {		// a three register encoding exists
							a = I2 + reg1*64 + reg1*8 + reg2;
						} else if (decode&2) {
							a = I2 + reg1*8 + reg2;
						} else {
							error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
							break;
						}
					}
				} else {			// two commas - can only be three register or R,R,cnt4
					//alert("decoding line "+r+" inst "+instText[r]+" three parameters");
					var reg1 = regDecode(offsetText[r].substring(0,pos1));
					// returns 0-7 for R0 to R7, 15=PC 13=SP 14=LR 12=flags, 20 if NaN else 21
					var reg2 = regDecode(offsetText[r].substring(pos1+1,pos2));
					var reg3 = regDecode(offsetText[r].substring(pos2+1));

					//alert("line "+r+" inst "+instText[r]+" decode "+decode+" reg1 "+reg1+" reg2 "+reg2+" reg3 "+reg3);
					if (reg3 == 20) {		// R,R,#cnt4 case
						a = 20;			// more than 16 to trap as error below
						var nxt = offsetText[r].substring(pos2+1,pos2+2);
						if ( nxt == '#') {		// #count
							a=parseInt(offsetText[r].substring(pos2+2));
						}
						if ((decode&2048)==0 || reg1>7 || reg2>7 ||
						    offsetText[r].indexOf(',',pos2+1) != -1 || // 3 commas
						    a==NaN || a>15 || a < 0) {
							error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
							break;
						}
						a += I1 + reg1*128 + reg2*16;
					} else {				// note 3 commas bad
						if ((decode&256)==0 || reg1>7 || reg2>7 ||
						reg3 > 7 || offsetText[r].indexOf(',',pos2+1) != -1) {
							error = "Mauvais param&egravetre &agrave la ligne "+r+' '+instText[r];
							break;
						}
						a = I2 + reg1*64 + reg2*8 + reg3;
					}
				}
			}
		}
		//if (inst) setAddressHex(r, a); else
		setAddress(r, a);		// save DAT in denary - now all same but in current mode
		++r;
	}
	if (error) {
		for (var i = 0; i <= r; ++i) {					// clear the memory
			setAddress(i, 0);
		}
		message(error);
		showError(r);
	} else message("LANCER/PAS pour ex&eacutecuter le programme, SELECT, CHARGER ou &eacutediter un programme");
}

// Indicate where the error is
function showError(r)
{
	var r_pad = '';
	if (r < 100) rpad = '&nbsp;';
	if (r < 10) rpad = '&nbsp;&nbsp;';		
	var pos1 = programHTML.indexOf('<br />'+rpad+r+'&nbsp;',0);
	var pos3;
	if (r == 0) {pos1 = 0; pos3 = 0; }
	else pos3 = pos1+6;
	var pos2 = programHTML.indexOf('<br />',pos3);
	if (pos1 < 0 || pos2 < 0) alert("Impossible d'indiquer la localisation de l'erreur");
	else {
		programHTML = programHTML.substring(0,pos3) + '<span style="background-color:pink;">' + programHTML.substring(pos3,pos2) + '</span>' + programHTML.substring(pos2);
		text("program", programHTML, 21, 52,12, "black", "onclick", "openProgram(this)", monospace);
	}
}

// decode potential Register specifier returns 0-7 for R0 to R7, 15=PC 13=SP 14=LR 12=flags, 20 if NaN else 21
function regDecode(text)
{
	if (text == 'PC'||text == 'pc') return 15;
	if (text == 'SP'||text == 'sp') return 13;
	if (text == 'LR'||text == 'lr') return 14;
	if (text == 'flags'||text == 'FLAGS') return 12;
	if (text.length == 2 && (text[0] == 'R' || text[0]=='r')) {
		var x = text[1]-'0';
		if (x >= 0 && x < 8) return x;
	}
	if (isNaN(text)) return 20;
	return 21;
}

// update PC
function updatePC(y)
{
	while (y < 0) y += 65536;
	while (y > 399) y -= 400;
	pCounter = y;
	// &#8199; is supposed to be the same width as a number
	if (y < 10) y = '&#8199;&#8199;&#8199;&#8199;'+y;
	else if (y < 100) y = '&#8199;&#8199;&#8199;'+y;
	else if (y < 1000) y = '&#8199;&#8199;'+y;
	else if (y < 10000) y = '&#8199;'+y;
	text("pc", y, 335, 72, 16, "black", "onclick", "openPC(this)");
}

function openPC(inp)
{
	if (waitingForInput) return;					// ignore if doing input (ours or the program)
	if (myTimeout || myTimeout1 || myTimeout2) return;		// ignore if something running
	message("Modification du registre PC");
	//var tmp = inp.innerHTML;
	inp.innerHTML = '<form action="javascript:PCSubmit()"><input id="PCForm" type="text" style="padding:0; border:0; width:40px; font-size:14px;"></form>';
	document.getElementById("PCForm").focus();
	document.getElementById("PCForm").setAttribute("onblur","losePC(this)");
	waitingForInput = true;
}

function PCSubmit()
{
	if (!waitingForInput) {
		alert("Mauvaise saisie - entr\351e non attendue");
		return;
	}
	var elePosn = document.getElementById("PCForm");
	elePosn.removeAttribute("onblur");
	if (isNaN(elePosn.value) || elePosn.value=="") {
		alert("Mauvaise saisie - doit \352tre un nombre");
		return;
	}
	// isNaN lets through 0b and 0o that we don't support
	if (elePosn.value[0] == '0' && elePosn.value.length > 1) {
		if (elePosn.value[1] > '9' && (elePosn.value[1] != 'x' &&
			elePosn.value[1] != 'X')) {
			alert("Mauvaise saisie - decimal ou hexad\351cimal seulement");
			return;
		}
	}
	var value = parseInt(elePosn.value);
	if (isNaN(value) || value > 399 || value < 0) {
		alert("Mauvaise saisie - valeur invalide pour le PC");
		return;
	}
	updatePC(value);			// removes input form as well
	updatePCmarker(value);
	waitingForInput = false;
	if (programText == "") message("SELECT pour choisir un exemple, CHARGER pour charger un fichier, ou entrez un programme, ou &eacutecrivez dans la m&eacutemoire");
	else message("ASSEMBLER, LANCER/PAS ou modifier la m&eacutemoire ou le programme");
}

function losePC(inp)
{
	if (!waitingForInput) return;		// happens after PCSubmit as well
	if (isNaN(inp.value) || inp.value=="") {	// bad value
		document.getElementById("PCForm").removeAttribute("onblur");
		updatePC(pCounter);			// removes input form as well
		waitingForInput = false;
		if (programText == "") message("SELECT pour choisir un exemple, CHARGER pour charger un fichier, ou entrez un programme, ou &eacutecrivez dans la m&eacutemoire");
		else message("ASSEMBLER, LANCER/PAS ou modifier la m&eacutemoire ou le programme");
	} else PCSubmit();
}

function memX(x)
{
	if (memOpt == 3) return (x%10)*135;
	return (x%10)*43;
}

// update PC and put the red marker square over the current PC location in memory
function updatePCmarker(x)
{
	if (x != oldPCMarker) {
		if (oldPCMarker >= registerSP)
			document.getElementById("a"+oldPCMarker).style.background = "lightGreen";
		else document.getElementById("a"+oldPCMarker).style.background = "white";
	}
	document.getElementById("a"+x).style.background = "pink";
	oldPCMarker = x;
}

// update a register
function updateR(r,y)
{
	if (r >= 0 && r < 8) {
		while (y < 0) y += 65536;
		while (y > 65535) y -= 65536;

		register[r] = y;
		if (memOpt != 2 && y > 32767) {			// 0/3 = 2's comp, 1 = unsigned, 2 = hex
			y = 65536 - y;
			if (y < 10) y = '&#8199;&#8199;&#8199;&#8199;-'+y;
			else if (y < 100) y = '&#8199;&#8199;&#8199;-'+y;
			else if (y < 1000) y = '&#8199;&#8199;-'+y;
			else if (y < 10000) y = '&#8199;-'+y;
			else y = '-'+y;
		} else if (memOpt != 2) {					// treat +ve 2's comp as unsigned
			if (y < 10) y = '&#8199;&#8199;&#8199;&#8199;'+y;
			else if (y < 100) y = '&#8199;&#8199;&#8199;'+y;
			else if (y < 1000) y = '&#8199;&#8199;'+y;
			else if (y < 10000) y = '&#8199;'+y;
			y = '&nbsp;'+y;
		} else if (y == 65535) {
			y = '&nbsp;<span style="letter-spacing:0.15em;">xffff</span>';
		} else {
			var hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
			var z = Math.floor(y/256);
			y = y%256;
			y = 'x'+hex[Math.floor(z/16)]+hex[z%16]+hex[Math.floor(y/16)]+hex[y%16];
			y = '&nbsp;'+y;
		}		
		text("R"+r, y, 330, 232-16*r, 16, "black");
	}
}

function updateLR(y)
{
	while (y < 0) y += 65536;
	while (y > 65535) y -= 65536;

	registerLR = y;
	// &#8199; is supposed to be the same width as a number
	if (y < 10) y = '&#8199;&#8199;&#8199;&#8199;'+y;
	else if (y < 100) y = '&#8199;&#8199;&#8199;'+y;
	else if (y < 1000) y = '&#8199;&#8199;'+y;
	else if (y < 10000) y = '&#8199;'+y;
	text("lr", y, 335, 88, 16, "black");
}

function updateSP(y)
{
	while (y < 0) y += 65536;
	while (y > 400) y -= 400;

	registerSP = y;
	// &#8199; is supposed to be the same width as a number
	if (y < 10) y = '&#8199;&#8199;&#8199;&#8199;'+y;
	else if (y < 100) y = '&#8199;&#8199;&#8199;'+y;
	else if (y < 1000) y = '&#8199;&#8199;'+y;
	else if (y < 10000) y = '&#8199;'+y;
	text("sp", y, 335, 104, 16, "black");
	
	// mark where the SP is in memory
	var spy = 74+Math.floor((registerSP-1)/10)*15;
	var spx = ((memOpt == 3) ? 700 : 611)+memX(registerSP-1);
	rectangle("SPPOS", spx, spy, 2, 14, "green", "green",1);
	imageOrder("SPPOS", 100);

	// show extent of stack
	if (registerSP > oldSPMarker) {
		for (var x = oldSPMarker; x < registerSP; ++x) {
			if (x != oldPCMarker)
				document.getElementById("a"+x).style.background = "white";
		}
	} else if (registerSP < oldSPMarker) {
		for (var x = registerSP; x < oldSPMarker; ++x) {
			if (x != oldPCMarker)
				document.getElementById("a"+x).style.background = "lightGreen";
		}
	}
	oldSPMarker = registerSP;
}

function updateFlags(y)
{
	flags = y&15;
	var txt = (y&8)!=0?'1':'0';
	txt += '&thinsp;'+((y&4)!=0?'1':'0');
	txt += '&thinsp;'+((y&2)!=0?'1':'0');
	txt += '&thinsp;'+((y&1)!=0?'1':'0');
	text("flags", txt, 361, 280, 14, "black");
	document.getElementById("flags").style.paddingLeft = "1px";
	/* text("flags",'&#8199;'+((y&8)==0?'1':'0'+'&#8199;')+
		((y&4)==0?'1':'0')+'&#8199;'+((y&2)==0?'1':'0')+
		'&#8199;'+(y&1)==0?'1':'0', 361, 280, 16, "black"); */
}


// latest - change MVH to NOP and remove #imm from TST, add MVN
var instructions = ["DAT", "ADD", "SUB", "CMP", "MOV", "AND", "ORR", "XOR", "NOP", "MUL", "UDV", "MOD", "MLX", "ADC", "SBC", "LSR", "LSL", "ASR", "ROR", "TST", "INP", "OUT", "BRA", "BEQ", "BNE", "BCS", "BCC", "BMI", "BPL", "BVS", "BVC", "BHI", "BLS", "BGE", "BLT", "BGT", "BLE", "JMS", "RET", "STR", "LDR", "POP", "PSH", "DIV", "BIC", "NEG", "HLT", "MVN", "BHS", "BLO",  "BIS", "EOR"];

// to assist indexing, put 10 per line
// note the last 4 instructions are fake - any new instruction goes before them
// 00 "DAT", "ADD", "SUB", "CMP", "MOV", "AND", "ORR", "XOR", "NOP", "MUL",
// 10 "UDV", "MOD", "MLX", "ADC", "SBC", "LSR", "LSL", "ASR", "ROR", "TST",
// 20 "INP", "OUT", "BRA", "BEQ", "BNE", "BCS", "BCC", "BMI", "BPL", "BVS",
// 30 "BVC", "BHI", "BLS", "BGE", "BLT", "BGT", "BLE", "JMS", "RET", "STR",
// 40 "LDR", "POP", "PSH",  "DIV", "BIC", "NEG", "HLT", "MVN", "BHS", "BLO", 
// 50 "BIS", "EOR"
// PSH/POP as 42/41 used in code - do not change

// ADD, SUB, AND, OR, XOR, LSR, LSR are the only three register operations
// LSL and LSR two registers and a count (since I only need 4 bits for a count)
// ADD Rd, <direct> and LDR, STR are the only direct memory instructions (plus branches)

// A key to assist decoding instruction operands - bit significant
// 1 = no parameters 2 = Rd,Rx 4 = Rd,#immed(8) 8= Rd,#immed(4) 16 = Rd,address 32 = Rd,device
// 64 = Rx 128 = address 256 = Rd,Rs,Rb 512 = Rd,offset(Rn) 1024 = number(16)
// 2048 = Rd,Rs,#immed(4) 4096 = Rs/Rd can be SP/LR/PC/flags (MOV only)
// 8192 = Rd can be SP (2 param inst) 16384 = Rn can be SP 
var instKey = [1+128+1024,4+16+256+8192,4+16+256+8192,6,6+4096+8192,260,260,260,1,6,/*10*/6,6,2,2,2,256+2048,256+2048,10,10,2,/*20*/34,34,64+128,128,128,128,128,128,128,128,/*30*/128,128,128,128,128,128,128,64+128,1,16+512+16384,/*40*/16+512+16384,64,64,2,2,2,1,2];

// Instruction tables to generate the op codes inst1 has lowest Hex digit as the op code for
// R,addr type instructions and top 12 bits as the code for R,#im8 and R,off(R) types
// the whole word is used for 0/1 parameter insts and for R,dev, R,#cnt(4) and Rd,Rs,#cnt(4)
var inst1 = [0,0x100C,0x180D,0x2000,0x2800,0x3000,0x3800,0x4000,0x7700,0x5000,/*10*/0x4800,0x0800,0,0,0,0x5800,0x5C00,0x7000,0x7080, 0x0000,/*20*/0x7100,0x7180,0x8000,0x8200,0x8400,0x8600,0x8800,0x8A00,0x8C00,0x8E00,/*30*/0x9000,0x9200,0x9400,0x9600,0x9800,0x9A00,0x9C00,0x9E00,0x7260,0xA00E,/*40*/0xB00F,0,0,0,0,0,0,0];

// inst2 has the whole word as the op code for 2 and 3 register instructions
// and for BRA Rx type instructions (no overlap between the 3 cases)
var inst2 = [0,0x6000,0x6200,0x7680,0x7700,0x6400,0x6600,0x6800,0,0x77C0,/*10*/0x7400,0x7440,0x7480,0x7740,0x7780,0x6A00,0x6C00,0x74C0,0x7500,0x76C0,/*20*/0x7600,0x7640,0x7250,0,0,0,0,0,0,0,/*30*/0,0,0,0,0,0,0,0x7258,0,0x7800,/*40*/0x7A00,0x7240,0x7248,0x7540,0x7580,0x75C0,0,0x7280];

/* Special register instructions (not encoded in the above tables)
0x6E00	1101 1110		ADD SP, #immediate	- in code	if (inst==1) a+= 0x6E00;
0x6F00	1101 1111		SUB SP, #immediate   - in code	else a+= 0x6F00;
0x7200	0111 0010 000	MOV Rd, SP/LR/PC/flags 		in code
0x7220	0111 0010 001	MOV SP/LR/PC/flags, Rs		in code
0x7800	0111 100		STR Rs, offset(SP) - could be inst2 but curr in code 	if (inst==39) a+= (reg1<<6) +0x7800;
0x7A00	0111 101		LDR Rd, offset(SP) - could be inst2 but curr in code	else a+= (reg1<<6) +0x7A00;
0x7C00	0111 11x		POP and PSH multiple registers	in code		a = 0x7C00;
*/

// note map 48=>25, 49=>26, BIS(50)=>ORR(6), EOR(51)=>XOR(7)
// match the text to a known instruction, return 1-47 for instructions, 0 for DAT
// and 200 for no match (use 200 so if increase basic instructions do not change it)
function instruction(text)
{
	for (var k = 0; k < 52; ++k) {
		if (text == instructions[k]) break;
	}
	if (k < 48) return k;		// first because most common case
	if (k == 49) return 26;
	if (k == 48) return 25;
	if (k == 50) return 6;
	if (k == 51) return 7;
	return 200;
}

var savOpenAddress = false;

function openAddress(inp)
{
	if (waitingForInput) return;					// ignore if doing input (ours or the program)
	if (myTimeout || myTimeout1 || myTimeout2) return;	// ignore if something running
	message("Modification du contenu de la m&eacutemoire");
	//var tmp = inp.innerHTML;					// if need current value
	var widthX = (memOpt == 3) ? '133' :'50';
	inp.innerHTML = '<form action="javascript:addressSubmit()"><input id="aForm" type="text" style="padding:0; border:0; width:'+widthX+'px;font-size:90%;"></form>';
	document.getElementById("aForm").focus();
	document.getElementById("aForm").setAttribute("onblur","loseAddress(this)");
	waitingForInput = true;
	savOpenAddress = inp;
}

// used by tab and focus changes to filter out the error cases, return true if OK
// reason is to avoid addressSubmit() doing an alert (which changes focus)
// it means that in some cases (like TAB) we do these tests 3 times
function checkInput(iValue)
{
	if (!waitingForInput) return false;	// should not happen
	if (memOpt == 3) iValue = iValue.replace(' ','');
	if (isNaN(iValue) || iValue=="") return false;
	if (memOpt == 3) {
		var x = 0;
		while (x < iValue.length) {
			if (iValue[x] < '0' || iValue[x] > '1') {
				return false;
			}
			++x;
		}
	} else if (iValue[0] == '0' && iValue.length > 1) {
		// isNaN lets through 0b and 0o that we don't support
		if (iValue[1] > '9' && (iValue[1] != 'x' &&
			iValue[1] != 'X')) {
			return false;
		}
	}
	var value = (memOpt == 3) ? parseInt(iValue,2) : parseInt(iValue);
	if (isNaN(value) || value > 65535 || value < -32768) {
		return false;
	}
	return true;
}

function addressSubmit()
{
	if (!waitingForInput) {
		alert("Mauvaise saisie - entr\351e non attendue");
		return;
	}
	var elePosn = document.getElementById("aForm");
	var epvalue = elePosn.value;  // so can remove space in binary
	if (memOpt == 3) epvalue = epvalue.replace(' ','');
	
	if (isNaN(epvalue) || epvalue=="") {
		alert("Mauvaise saisie - doit \352tre un nombre");
		return;
	}
	if (memOpt == 3) {
		var x = 0;
		while (x < epvalue.length) {
			if (epvalue[x] < '0' || epvalue[x] > '1') {
				alert("Mauvaise saisie - nombre binaire invalide");
				return;
			}
			++x;
		}
	} else if (epvalue[0] == '0' && epvalue.length > 1) {
		// isNaN lets through 0b and 0o that we don't support
		if (epvalue[1] > '9' && (epvalue[1] != 'x' &&
			epvalue[1] != 'X')) {
			alert("Mauvaise saisie - decimal ou hexad\351cimal seulement");
			return;
		}
	}

	var value = (memOpt == 3) ? parseInt(epvalue,2) : parseInt(epvalue);
	if (isNaN(value) || value > 65535 || value < -32768) {
		alert("Mauvaise saisie - nombre trop petit ou trop grand");
		return;
	}
	document.getElementById("aForm").removeAttribute("onblur");	
	// need to decode savOpenAddress.id
	var x = parseInt(savOpenAddress.id[1]);
	if (savOpenAddress.id.length >= 3) x = x*10 + parseInt(savOpenAddress.id[2]);
	if (savOpenAddress.id.length == 4) x = x*10 + parseInt(savOpenAddress.id[3]);
	setAddress(x, value);		// removes input form as well
	waitingForInput = false;
	savOpenAddress = false;
	if (programText == "") message("SELECT pour choisir un exemple, CHARGER pour charger un fichier, ou entrez un programme, ou &eacutecrivez dans la m&eacutemoire");
	else message("ASSEMBLER, LANCER/PAS ou modifier la m&eacutemoire ou le programme");
}

function loseAddress(inp)
{
	if (!waitingForInput) return;		// happens after addressSubmit as well
	if (checkInput(inp.value)) addressSubmit();
	else {		// bad value 
		document.getElementById("aForm").removeAttribute("onblur");	
		var x = parseInt(savOpenAddress.id[1]);
		if (savOpenAddress.id.length >= 3) x = x*10 + parseInt(savOpenAddress.id[2]);
		if (savOpenAddress.id.length == 4) x = x*10 + parseInt(savOpenAddress.id[3]);
		setAddress(x, address[x]);		// removes input form as well
		waitingForInput = false;
		savOpenAddress = false;
		message("Mauvaise entr&eacutee ignor&eacute");
	}
}

// change the contents of the address x in the memory to y
function setAddress(x, y)
{
	if (isNaN(y)) {alert("Tentative d'&eacutecriture de la valeur NaN "+y); return;}
	if (x<0 || x>=400) {alert("Ecriture &agrave une adresse erron&eacute  "+x); return;}

	while (y < 0) y += 65536;
	while (y > 65535) y -= 65536;	
	address[x] = y;
	// &#8199; is supposed to be the same width as a number
	if (memOpt == 0 && y > 32767) {				// 0 = 2's comp, 1 = unsigned, 2 = hex
		y = 65536 - y;
		if (y < 10) y = '&#8199;&#8199;&#8199;&#8199;-'+y;
		else if (y < 100) y = '&#8199;&#8199;&#8199;-'+y;
		else if (y < 1000) y = '&#8199;&#8199;-'+y;
		else if (y < 10000) y = '&#8199;-'+y;
		else y = '-'+y;
	} else if (memOpt < 2) {					// treat +ve 2's comp as unsigned
		if (y < 10) y = '&#8199;&#8199;&#8199;&#8199;'+y;
		else if (y < 100) y = '&#8199;&#8199;&#8199;'+y;
		else if (y < 1000) y = '&#8199;&#8199;'+y;
		else if (y < 10000) y = '&#8199;'+y;
		y = '&nbsp;'+y;
	} else if (memOpt == 3) {				// binary
		var s = '<span style="font-family:\'Courier New\'; font-size:12px;">';
		for (var i = 0; i<16; ++i) {
			s += ((y<<i) & 0x8000)?"1":"0";
			if (i == 7) s+= '</span> <span style="font-family:\'Courier New\'; font-size:12px;">';
		}
		y = s+'</span>';
	} else if (y == 65535) {
		y = '&nbsp;x<span style="letter-spacing:0.18em;">ffff</span>';
		//y = '&nbsp;<span style="font-kerning:none;">xffff</span>';
	} else {
		var hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
		var z = Math.floor(y/256);
		y = y%256;
		y = 'x'+hex[Math.floor(z/16)]+hex[z%16]+hex[Math.floor(y/16)]+hex[y%16];
		y = '&nbsp;'+y;
	}
	text("a"+x,  y, 568+memX(x), 74+Math.floor(x/10)*15, 14, "black", "onclick", "openAddress(this)");
}

// converts x to a string in the current mode
function getMode(x)		// memOpt is 0 = 2's comp, 1 = unsigned, 2 = hex, 3 = binary (but treat as 2'comp for these strings)
{
	if (memOpt == 2) {
		var hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
		var z = Math.floor(x/256);
		x = x%256;
		return hex[Math.floor(z/16)]+hex[z%16]+hex[Math.floor(x/16)]+hex[x%16];
	}  // else
	if (x > 32767) x -= 65536;
	return String(x);
}


/* // change the contents of the address x in the memory to y and display in hex
function setAddressHex(x, y)
{
	if (isNaN(y)) {alert("attempt to store NaN "+y); return;}
	if (x<0 || x>=400) {alert("store at bad address "+x); return;}

	while (y < 0) y += 65536;
	while (y > 65535) y -= 65536;	
	address[x] = y;
	//var hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	var hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
	var z = Math.floor(y/256);
	y = y%256;
	y = 'x<span style="font-family:Courier New Bold,Courier New,monospace;">'+hex[Math.floor(z/16)]+hex[z%16]+hex[Math.floor(y/16)]+hex[y%16]+'</span>';
	text("a"+x, y, 568+(x%10)*37, 73+Math.floor(x/10)*15, 14, "black", "onclick", "openAddress(this)");
} */

// step button pressed 
function step3()		// run step2 to get execution indication of one instruction
{
	oneStep = true;
	run2();
}

// run button pressed
function run()
{
	oneStep = false;
	run2();
}

function run2()				// make step same as run 
{
	if (waitingForInput) return;
	//reset1();
	button("run", "STOPPER", 100, 610, "stop()");
	button("step", "<<", 164, 610, "slower()");
	button("gt", ">>", 192, 610, "faster()");
	stopping = false;
	speed = defaultSpeed;
	doSpeed();						// set default (show execution) speed
	runContinue();
}

function slower()
{
	if (speed > 225) return;				// max value 250
	if (speed >= 50) speed += 25;
	else if (speed >= 5) speed +=5;
	else ++speed;
	doSpeed();
}

function doSpeed()
{
	running = true;
	var indx = (250-speed)/25;			// get 0 to 9.96
	s2T = 3;						// set default values for transition case (as the fastest speed 5)
	valW = 1;
	if (speed <= 100) {
		text("speed", "VITESSE "+indx, 224, 616, 12, "blue");
		return;					// not showing execution so valW and s2T dont apply but leave defaults for transition case
	}
	// not enough space for the LMC version of this
	//text("speed", "SHOW FETCH/EXECUTE &nbsp; VITESSE "+indx, 60, 616, 12, "blue");
	text("speed", "VITESSE "+indx, 224, 616, 12, "blue");
	if (indx < 5) {
		if (runRate < 4.5) valW = 5;
		else valW = 4;					// slow implementations do even worse if you ask for > 4
	}
	if (indx == 4) s2T = 2;
	if (indx <= 3) s2T = 1;
	if (indx == 2) valW *= 2;
	if (indx == 1) valW *= 4;
	if (indx == 0) valW *= 8;
}

function faster()
{
	if (speed <= 100 && step2Busy) return;		// because cannot speed up till current instruction finished
	if (speed >= 75) speed -= 25;
	else if (speed >= 10) speed -=5;
	else if (speed > 1) --speed;
	doSpeed();
}

function runContinuex()					// to get extra delay between instructions when doing FETCH/EXECUTE
{
	if (step2Busy) {					// always wait for a FETCH/EXECUTE to finish
		myTimeout = delay(speed, "runContinuex");
		return;
	}
	if (speed < 125 || stopping) runContinue();	// user has pressed the faster key or stop key
	else myTimeout = delay((speed+400)/(s2T+1), "runContinue");
}

function runContinuey()					// wait for a halt to finish
{
	if (step2Busy) {					// always wait for the instruction to finish
		myTimeout = delay(25, "runContinuey");
		return;
	}
	button("run", "LANCER", 100, 610, "run()");
	button("step", "PAS", 160, 610, "step3()");
	remove("gt");
	remove("speed");
	running = false;
	message(halted);		// try adding this
	myTimeout = false;
}

function runContinuez()				// wait for input in fast execution - needed for one step case
{
	if (waitingForInput) {
		myTimeout = delay(speed, "runContinuez");
	} else {
		message(stepTxt);
		myTimeout = delay(speed, "runContinue");
	}
}

function runContinue()
{
	myTimeout = false;
	if (stopping) {
		button("run", "LANCER", 100, 610, "run()");
		button("step", "PAS", 160, 610, "step3()");
		remove("gt");
		remove("speed");
		running = false;
		if (!oneStep) message("Program stopp&eacute. LANCER ou PAS pour continuer le programme, REINIT pour stopper.");
		else message(stepTxt);
		return;
	}
	if (oneStep) stopping = true;
	if (speed > 100) {					// show FETCH/EXECUTE
		var inst = address[pCounter];
		execErr = false;
		step2();
		if (inst < 0x800 || execErr) {	// do not continue running for HLT or bad instructions
			myTimeout = delay(25, "runContinuey");	// but need to reset the butttons after the instruction finishes		
			return;
		}
		myTimeout = delay(speed, "runContinuex");
		return;
	}
	// here for the run without FETCH/EXECUTE display case
	if (address[pCounter] >= 0x800) {	// not a halt
		if (step1()) {
			button("run", "LANCER", 105, 610, "run()");
			button("step", "PAS", 160, 610, "step3()");
			remove("gt");
			remove("speed");
			running = false;
			return;
		}
		if (waitingForInput) {
			myTimeout = delay(speed, "runContinuez");
		} else {
			message(stepTxt);
			myTimeout = delay(speed*4, "runContinue");
		}
	} else {
		step1();			// show the halt instruction
		button("run", "LANCER", 100, 610, "run()");
		button("step", "PAS", 160, 610, "step3()");
		remove("gt");
		remove("speed");
		running = false;
		message(halted);
	}
}

// stop button pressed (note that stop is only available when running)
function stop()
{
	stopping = true;					// always stop
	if (!step2Busy) return;				// if not showing fetch/execute we are done
	if (s2T) {
		s2T = 0;
		text("speed", "Appuyer &agrave nouveau sur STOPPER pour terminer l'instructionn", 80, 695, 12, "red");
	} else {
		doSpeed();
	}
}

function stop2()
{
	if (myTimeout) clearTimeout(myTimeout);
	myTimeout = false;
	if (myTimeout1) clearTimeout(myTimeout1);
	myTimeout1 = false;
	if (myTimeout2) clearTimeout(myTimeout2);
	myTimeout2 = false;
	if (maskCnt) {		// if were doing a multi register move
		for (var i=0; i<maskCnt; ++i) {
			remove("blueM"+i);
			remove("blueN"+i);
		}
		maskCnt = 0;
	}
	button("run", "LANCER", 100, 610, "run()");
	button("step", "PAS", 160, 610, "step3()");
	remove("gt");
	remove("speed");
	running = false;
	remove("au");
	remove("red1");
	remove("red2");
	remove("blue1");
	remove("blue2");
	step2Busy = false;
}

// reset button pressed
function reset1()								// note reset did not work but is not listed as a reserved word
{
	stop2();
	updateR(0,0);
	updateR(1,0);
	updateR(2,0);
	updateR(3,0);
	updateR(4,0);
	updateR(5,0);
	updateR(6,0);
	updateR(7,0);
	updateLR(0);
	updateSP(400);	
	updatePC(0);							// if open for editing this replaces the input
	updatePCmarker(0);
	updateFlags(0);
	output = "";
	output1 = "";
	text("output", "", 398, 559, 12, "black");			// clear the output window
	text("ir", "", 329, 311, 18, "black");				// clear the IR display
	remove("cu");
	if (savOpenAddress) {			// has a memory address open
		// these two lines look like a bug!!! (found during AQA development)
		// setAddress(x, address[x]);		// removes input form and resets value
		// savOpenAddress = false;

		var x = parseInt(savOpenAddress.id[1]);
		if (savOpenAddress.id.length >= 3) x = x*10 + parseInt(savOpenAddress.id[2]);
		if (savOpenAddress.id.length == 4) x = x*10 + parseInt(savOpenAddress.id[3]);
		if (x > 399) x = 0;
		setAddress(x, address[x]);	// removes input form and resets value
		waitingForInput = false;
		savOpenAddress = false;
	}
	if (modifyingProgram) {
		modifyingProgram = false;
		textToHtml();
		waitingForInput = false;
	}
	if (waitingForInput) {
		waitingForInput = false;
	}
	remove("inpxx");
	text("input", "", 269, 560, 16, "black");
	message("R&eacuteinitialisation effectu&eacutee, &eacutediter et ASSEMBLER, LANCER/PAS ou modifier la m&eacutemoire ou le programme");
}

// test in increasing direction only (so can put exceptions first)
var IMask = [0xF800,0xF800,0xE000,0xE000,0xE000,0xFE00,0xF000,0xE000,0xFE00,0xFF80,0xFC00,0xFC00,0xFC00,0xFFC0,0x8000];
var IValue = [0x0000,0x5800,0x8000,0xA000,0xC000,0x6E00,0x6000,0xE000,0x7000,0x7200,0x7800,0x7400,0x7C00,0x7280,0x0000];
// indexes 0 = HLT, 1 = R,R,cnt4 2 = B,addr9 3 = R,offset(R) 4 = ADD/SUB Rd,addr9 5 = SP,imm8 6 = R,R,R
// 7 = R,addr9 8 = R,cnt4/R,dev4 9 = special/spare 10 = R,off6(SP) 11 = R,R 12 = reg mask 14 = R,imm8
// 13 = MVN (switch as 11 for R,R)


// called from runContinue to do one instruction (no indication), returns !=0 if an error which should cause run to stop
function step1()			// note step did not work but is not listed as a reserved word
{
	if (waitingForInput) return 0;
	inst = address[pCounter];
	var hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
	var z = Math.floor(inst/256);
	var y = inst%256;
	y = '&nbsp;<span style="letter-spacing:0.15em;">x'+hex[Math.floor(z/16)]+hex[z%16]+hex[Math.floor(y/16)]+hex[y%16]+'</span>';
	text("ir", y, 329, 311, 18, "black");			// update the IR display
	document.getElementById("ir").style.paddingTop = "0";

	// do not re-use y below so can update IR with instruction name (although I changed that)

	updatePC(pCounter+1);			// increment the PC
	updatePCmarker(pCounter);		// same value because updatePC changes pCounter

	var iy = "";	// to hold instruction name
	var iz = "";	// to hold parameter format
	var format;
	for (format = 0; format < 15; ++format) {
		if ((inst&IMask[format])==IValue[format]) break;
	}
	switch(format) {
	case 0:			// HLT is a good instruction - caller detects
		iy = 'HLT';
		break;
	case 1:			// 2 regs and a cnt4
		var cnt4 = inst&15;
		var rs = (inst>>4)&7;
		var rd = (inst>>7)&7;
		var result;
		flags = 0;		// N Z C V
		iz = 'Rd,Rs,#cnt';
		if ((inst&0x400)==0) {			// LSR
			iy = 'LSR';
			result = register[rs]>>cnt4;
			if (cnt4 > 0 && ((register[rs]>>(cnt4-1))&1) != 0) flags |= 2;
		} else {						// LSL
			iy = 'LSL';
			result = register[rs]<<cnt4;
			if ((result&0x10000)!=0) flags |= 2;
		}
		result &= 0xFFFF;
		if (result == 0) flags |= 4;
		if ((result&0x8000)!=0) flags |= 8;
		updateR(rd, result);
		updateFlags(flags);		
		break;
	case 2:			// Branches and JMS with address in 9 bits
		var add = inst&511;
		if (add > 399) add -= 400;
		iz = 'address';
		switch ((inst>>9)&15) {
		case 0:		// BRA
			iy = 'BRA';
			updatePC(add);
			updatePCmarker(add);
			break;
		case 1:		// BEQ
			iy = 'BEQ';
			if ((flags&4)!=0) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 2:		// BNE
			iy = 'BNE';
			if ((flags&4)==0) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 3:		// BCS
			iy = 'BCS';
			if ((flags&2)!=0) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 4:		// BCC
			iy = 'BCC';
			if ((flags&2)==0) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 5:		// BMI
			iy = 'BMI';
			if ((flags&8)!=0) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 6:		// BPL
			iy = 'BPL';
			if ((flags&8)==0) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 7:		// BVS
			iy = 'BVS';
			if ((flags&1)!=0) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 8:		// BVC
			iy = 'BVC';
			if ((flags&1)==0) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 9:		// BHI	C set and Z clear (N Z C V)
			iy = 'BHI';
			if ((flags&6)==2) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 10:		// BLS	C clear or Z set
			iy = 'BLS';
			if ((flags&0x6)!=2) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 11:		// BGE	N and V both set or both clear (N Z C V)
			iy = 'BGE';
			if ((flags&9)==9 || (flags&9)==0) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 12:		// BLT	N set and V clear OR N clear and V set
			iy = 'BLT';
			if ((flags&9)==8 || (flags&9)==1) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 13:		// BGT	Z clear AND (N and V both set or both clear)
			iy = 'BGT';
			if ((flags&4)==0 && ((flags&9)==9 || (flags&9)==0)) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 14:		// BLE	Z set OR N set and V clear OR N clear and V set  (N Z C V)
			iy = 'BLE';
			if ((flags&4)!=0 || (flags&9)==8 || (flags&9)==1) {
				updatePC(add);
				updatePCmarker(add);
			}
			break;
		case 15:		// JMS
			iy = 'JMS';
			updateLR(pCounter);		// ??? do we wantto stack the previous LR or not???
			updatePC(add);
			updatePCmarker(add);
			break;
		}
		break;
	case 3:			// STR and LDR R,offset(R) - flags not affected
		// assume format is Rsd Rb offset6
		var off6 = inst&63
		var rb = (inst>>6)&7;
		var rsd = (inst>>9)&7;
		var iz = 'Rsd,offset(Ra)';
		off6 = (register[rb]+off6)%400;
		if ((inst&0x1000)==0) {			// STR
			iy = 'STR';
			setAddress(off6, register[rsd]);
		} else {						// LDR
			iy = 'LDR';
			updateR(rsd,address[off6]);
		}
		break;
	case 4:			// ADD/SUB Rd,addr9 - flags set
		iz = 'Rd,direct';
		var add = inst&511;
		if (add > 399) add -= 400;
		var rd = (inst>>9)&7;
		var result;
		flags = 0;	// for ADD V is set if the operands have the same sign and the result is a different sign
		if ((inst&0x1000)==0) { // ADD
			iy = 'ADD';
			result = register[rd] + address[add];
			if (((register[rd]^address[add])&0x8000)==0 &&
				((result^register[rd])&0x8000)!=0) flags = 1;
			if ((result&0x10000)!=0) flags |= 2;
		} else {				// SUB
			iy = 'SUB';
			result = register[rd] - address[add];
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if (((register[rd]^address[add])&0x8000)!=0 &&
				((result^register[rd])&0x8000)!=0) flags = 1;
			if ((result&0x10000)==0) flags |= 2;
		}
		result &= 0xFFFF;
		if (result == 0) flags |= 4;
		if ((result&0x8000)!=0) flags |= 8;
		updateR(rd, result);
		updateFlags(flags);		
		break;
	case 5:			// ADD/SUB SP,imm8 - no flags set
		var imm = inst&255;
		var result;
		if (imm == 0) {	// nothing to do, treat as NOP
			iz = '';
			iy = 'NOP';
			
			break;
		}
		iz = 'SP,#imm';
		if ((inst&0x100)==0) {
			iy = 'ADD';
			result = registerSP + imm;
		} else {
			iy = 'SUB';
			result = registerSP - imm;
		}
		if (result < 0 || result > 400) {
			//y += '<span style="font-size:8pt"> '+iy+'</span>';
			text("cu", iy, 352, 337, 12, "white");
			//text("ir", y, 329, 311, 18, "black");			// update the IR display
			message("SP invalide au PC = "+pCounter);
			return 1;
		}
		updateSP(result);
		break;
	case 6:			// three register instructions - all set flags
		var ra = inst&7;
		var rs = (inst>>3)&7;
		var rd = (inst>>6)&7;
		var result;
		flags = 0;		// N Z C V
		iz = 'Rd,Rs,Rb';
		switch((inst>>9)&7) {
		case 0:		// ADD
			iy = 'ADD';
			result = register[rs] + register[ra];
			// V is set if the operands have the same sign and the result is a different sign
			if (((register[rs]^register[ra])&0x8000)==0 &&
				((result^register[rs])&0x8000)!=0) flags = 1;
			if ((result&0x10000)!=0) flags |= 2;
			break;
		case 1:		// SUB
			iy = 'SUB';
			result = register[rs] - register[ra];
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if (((register[rs]^register[ra])&0x8000)!=0 &&
				((result^register[rs])&0x8000)!=0) flags = 1;
			if ((result&0x10000)==0) flags |= 2;
			break;
		case 2:		// AND
			iy = 'AND';
			result = register[rs] & register[ra];
			break;
		case 3:		// ORR
			iy = 'ORR';
			result = register[rs] | register[ra];
			break;
		case 4:		// XOR
			iy = 'XOR';
			result = register[rs] ^ register[ra];
			break;
		case 5:		// LSR
			iy = 'LSR';
			result = register[rs] >> register[ra];
			if (register[ra] > 0 &&
				((register[rs]>>(register[ra]-1))&1) != 0) flags |= 2;
			break;
		case 6:		//  LSL
			iy = 'LSL';
			result = register[rs] << register[ra];
			if ((result&0x10000)!=0) flags |= 2;
			break;
		case 7:		// should not happen
			message("Instruction invalide au PC = "+pCounter);
			return 1;
		}
		result &= 0xFFFF;
		if (result == 0) flags |= 4;
		if ((result&0x8000)!=0) flags |= 8;
		updateR(rd, result);
		updateFlags(flags);		
		break;
	case 7:			// STR and LDR R,addr9 - flags not affected
		var add = inst&511;
		if (add > 399) add -= 400;
		var rsd = (inst>>9)&7;
		iz = 'Rsd,direct';
		if ((inst&0x1000)==0) {			// STR
			iy = 'STR';
			setAddress(add, register[rsd]);
		} else {						// LDR
			iy = 'LDR';
			updateR(rsd,address[add]);
		}
		break;
	case 8:			// R,cnt4/R,dev4
		var cnt4 = inst&15;
		var rsd = (inst>>4)&7;
		var result;
		iz = 'Rsd,#cnt';
		switch((inst>>7)&3) {
		case 0:				// ASR
			iy = 'ASR';
			flags = 0;
			result = register[rsd];
			if ((result&0x8000)!=0) result |= 0xFFFF0000
			result = result>>cnt4;
			if (cnt4 > 0 && ((register[rsd]>>(cnt4-1))&1) != 0) flags |= 2;
			result &= 0xFFFF;
			if (result == 0) flags |= 4;
			if ((result&0x8000)!=0) flags |= 8;
			updateR(rsd, result);
			updateFlags(flags);		
			break;
		case 1:				// ROR
			iy = 'ROR';
			flags = 0;
			result = register[rsd] + (register[rsd] << 16);
			result >>= cnt4;
			if ((result&0x10000)!=0) flags |= 2;
			result &= 0xFFFF;
			if (result == 0) flags |= 4;
			if ((result&0x8000)!=0) flags |= 8;
			updateR(rsd, result);
			updateFlags(flags);				
			break;
		case 2:				// INP - flags not set
			iy = 'INP';
			iz = 'Rd,device';
			// currently only one device so ignore parameter
			message("Entrer une valeur");
			registerToInput = rsd;
			waitingForInput = true;
			inst = 0;	// to distinguish step1() case from FETCH/EXECUTE case
			remove("input");
			rectangle("inpxx", 261, 541, 100, 37, "white", "red", 2);
			text("inpxx", ' &nbsp; Entrer valeur', 261, 541, 12, "red");
			rectangle("input", 269, 560, 90, 16, "white", "blue");
			text("input", inputForm, 269, 560, 12, "black");
			var elePosn = document.getElementById("iForm");
			elePosn.focus();
			delay(1000, "blinkoff");					// start blink	
			break;
		case 3:				// OUT
			iy = 'OUT';
			iz = 'Rs,device';
			// currently only one device bt parameter gives mode
			outputNum(register[rsd],inst&7);
			break;
		}
		break;
	case 9:			// special/spare - 0111 0010 0 - next bits 00 mov Rd,special; 01 mov special,Rd
		// 1000 pop Rd; 1001 push Rs; 1010 BRA Rs; 1011 JMS Rs; 11000 pop special; 11001 psh special; 1101000 ret
		// do not alter the flags
		var result;
		if ((inst &0xFFC0)==0x7200) {   // MOV cases
			iy = 'MOV';
			var rsd = inst & 7;
			switch((inst>>3)&7) {	// 3=PC 1=SP 2=LR 0=flags +4 if specials are dest
			case 0:			// MOV Rd,flags
				iz = 'Rd,flags';
				result = flags;
				updateR(rsd, result);
				break;
			case 1:			// MOV Rd,SP
				iz = 'Rd,SP';
				result = registerSP;
				updateR(rsd, result);
				break;
			case 2:			// MOV Rd,LR
				iz = 'Rd,LR';
				result = registerLR;
				updateR(rsd, result);
				break;
			case 3:			// MOV Rd,PC
				iz = 'Rd,PC';
				result = pCounter;
				updateR(rsd, result);
				break;
			case 4:			// MOV flags,Rs
				iz = 'flags,Rs';
				updateFlags(register[rsd]);
				break;
			case 5:			// MOV SP,Rs
				iz = 'SP,Rs';
				result = register[rsd];
				updateSP(result);
				break;
			case 6:			// MOV LR,Rs
				iz = 'LR,Rs';
				result = register[rsd];
				updateLR(result);
				break;
			case 7:			// MOV PC,Rs
				iz = 'PC,Rs';
				result = register[rsd];
				updatePC(result);
				updatePCmarker(pCounter);
				break;
			}
		} else if ((inst &0xFFF0)==0x7240) {   // POP/PSH Rsd cases
			var rsd = inst & 7;
			iz = 'Rsd';
			if ((inst&0x8)==0) {
				iy = 'POP';
				if (registerSP > 399) {
					message("SP invalide au PC = "+pCounter);
					return 1;
				}
				result = address[registerSP];
				updateR(rsd, result);
				updateSP(registerSP+1);
			} else {
				iy = 'PSH';
				if (registerSP == 0) {
					message("SP invalide au PC = "+pCounter);
					return 1;
				}
				updateSP(registerSP-1);
				result = register[rsd];
				setAddress(registerSP, result);
			}
		} else if ((inst &0xFFF0)==0x7250) {   // BRA/JMS Rs cases
			iz = 'Rs';
			if ((inst&0x8)!=0) {		// JMS case rather than BRA
				iy = 'JMS';
				updateLR(pCounter);
			} else iy = 'BRA';
			updatePC(register[inst&7]);
			updatePCmarker(pCounter);
		} /* else if ((inst &0xFFFC)==0x7260) {   // POP special regs
			iy = 'POP';
			iz = 'special';
			if (registerSP > 399) {
				message("Bad SP value at PC = "+pCounter);
				return 1;
			}
			result = address[registerSP];
			updateSP(registerSP+1);
			switch (inst&3) {
			case 0:			// POP flags
				updateFlags(result);
				flagsWanted=false;
				break;
			case 1:			// POP SP
				updateSP(result);
				break;
			case 2:			// POP LR
				updateLR(result);
				break;
			case 3:			// POP PC
				updatePC(result);
				updatePCmarker(pCounter);
				break;
			}
		} else if ((inst &0xFFFC)==0x7264) {   // PSH special regs
			iy = 'PSH';
			iz = 'special';
			if (registerSP == 0) {
				message("Bad SP value at PC = "+pCounter);
				return 1;
			}
			updateSP(registerSP-1);
			switch (inst&3) {
			case 0:			// PSH flags
				result = flags;
				break;
			case 1:			// PSH SP - the logic is that PSH SP, POP SP should leave
				result = registerSP+1;	// the SP unchanged, not an ARM instruction!
				break;
			case 2:			// PSH LR
				result = registerLR;
				break;
			case 3:			// PSH PC
				result = pCounter;
				break;				
			}
			flagsWanted = false;
			setAddress(registerSP, result);
		} */ else if (inst==0x7260) {			// RET
			iy = 'RET';
			updatePC(registerLR);
			updatePCmarker(pCounter);
		} else {		
			message("Instruction inexistante au PC = "+pCounter);
			return 1;
		}
		break;
	case 10:					// STR/LDR R,off6(SP) - no flags changes
		var off6 = inst&63;
		var rsd = (inst>>6)&7;
		iz = 'Rsd,offset(SP)';
		off6 = (registerSP+off6)%400;
		if ((inst&0x200)==0) {			// STR
			iy = 'STR';
			setAddress(off6, register[rsd]);
		} else {						// LDR
			iy = 'LDR';
			updateR(rsd,address[off6]);
		}
		break;
	case 11:					// two register instructions - most set flags
	case 13:					// MVN
		var ra = inst&7;
		var rsd = (inst>>3)&7;
		if ((inst&0xFFC0)==0x7640) {		// OUT is very different from the rest
			iz = 'Rs,Ra';
			iy = 'OUT';
			// currently only one device but parameter gives mode
			outputNum(register[rsd],register[ra]);
			break;
		}		
		var result=0;
		var a = register[ra];
		var b = register[rsd];
		var setFlags = true;
		var flgs = 0;
		iz = 'Rsd,Rb';
		if (format == 13) {		// MVN case
			iy = 'MVN';
			result = a ^ 0xFFFF;
			updateR(rsd, result);			
		} else switch((inst>>6)&15) {
		case 0:		// unsigned DIV
			iy = 'UDV';
			if (a == 0) flgs = 1;
			else result = Math.floor(b/a);
			updateR(rsd, result);
			break;
		case 1:		// MOD
			iy = 'MOD';
			if (a == 0) flgs = 1;
			else result = b%a;
			updateR(rsd, result);
			break;
		case 2:		// MLX - do 32 bit result (unsigned multiply)
			iy = 'MLX';
			result = b*a;
			updateR(rsd, result&0xFFFF);
			if (result == 0) flgs |= 4;
			result >>= 16;
			if (rsd<7) updateR(rsd+1, result);
			if ((result&0x8000)!=0) flgs |= 8;
			updateFlags(flgs);
			setFlags = false;
			break;
		case 3:		// ASR
			iy = 'ASR';
			result = b;
			if (a > 15) {
				if ((b&0x8000)!=0) {
					result = 0xFFFF;
					flgs |= 2;
				} else result = 0;
			} else {
				if ((b&0x8000)!=0) result |= 0xFFFF0000
				result >>= a;
				if (a > 0 && ((b>>(a-1))&1) != 0) flgs |= 2;
			}
			updateR(rsd, result);
			break;
		case 4:		// ROR
			iy = 'ROR';
			result = b + (b << 16);
			result >>= (a&15);
			if ((result&0x10000)!=0) flgs |= 2;
			updateR(rsd, result);
			break;
		case 5:		// signed DIV
			iy = 'DIV';
			if (a == 0) flgs = 1;
			else {
				var s = 0;
				if ((a&0x8000)!=0) {a = 65536-a; s=1;}
				if ((b&0x8000)!=0) {b = 65536-b; s^=1;}
				result = Math.floor(b/a);
				if (result>32767) flgs=1;
				if (s) result = 65536-result;
			}
			updateR(rsd, result);
			break;
		default:		// not sure there is anything left - but just in case
			message("Instruction invalide au PC = "+pCounter);
			return 1;
			break;
		case 6:		// BIC
			iy = 'BIC';
			result = b & (~a);
			updateR(rsd, result);
			break;
		case 7:		// NEG
			iy = 'NEG';
			result = -a;
			updateR(rsd, result);
			break;
		case 8:		// INP
			iy = 'INP';
			// currently only one device so ignore parameter
			message("Entrer une valeur");
			registerToInput = rsd;
			waitingForInput = true;
			inst = 0;	// to distinguish step1() case from FETCH/EXECUTE case
			remove("input");
			rectangle("inpxx", 261, 541, 100, 37, "white", "red", 2);
			text("inpxx", ' &nbsp; Entrer valeur', 261, 541, 12, "red");
			rectangle("input", 269, 560, 90, 16, "white", "blue");
			text("input", inputForm, 269, 560, 12, "black");
			var elePosn = document.getElementById("iForm");
			elePosn.focus();
			delay(1000, "blinkoff");					// start blink
			setFlags = false;
			break;
		case 10:		// CMP
			iy = 'CMP';
			result = b - a;
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if (((b^a)&0x8000)!=0 && ((result^b)&0x8000)!=0) flgs = 1;
			if ((result&0x10000)==0) flgs |= 2;
			break;
		case 11:		// TST
			iy = 'TST';
			result = b & a;
			break;
		case 12:		// MOV
			setFlags = false;
			if ((inst&31) == 0) {	// MOV R0,R0 - nothing to do, treat as NOP
				iz = '';
				iy = 'NOP';
				break;
			}
			iy = 'MOV';
			result = a;
			updateR(rsd, result);
			break;
		case 13:		// ADC
			iy = 'ADC';
			result = b + a + ((flags&2)>>1);
			if (((b^a)&0x8000)==0 && ((result^b)&0x8000)!=0) flgs = 1;
			if ((result&0x10000)!=0) flgs |= 2;
			updateR(rsd, result);
			break;
		case 14:		// SBC
			iy = 'SBC';
			result = b - a - 1 + ((flags&2)>>1);
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if (((b^a)&0x8000)!=0 && ((result^b)&0x8000)!=0) flgs = 1;
			if ((result&0x10000)==0) flgs |= 2;
			updateR(rsd, result);
			break;
		case 15:		// MUL
			iy = 'MUL';
			result = b*a;
			if (result>65535) flgs=2;		// unsigned overflow
			if ((result&0xFFFF)>32767) {
				var tmp = result/65536;
				if ((tmp&(tmp+1))!=0)flgs|=1;
			} else {
				if ((result&0xFFFF0000)!=0)flgs|=1;
			}
			updateR(rsd, result);
			break;
		}
		if (setFlags) {
			result &= 0xFFFF;	// some instructions only set flags so dont save reg here
			if (result == 0) flgs |= 4;
			if ((result&0x8000)!=0) flgs |= 8;
			updateFlags(flgs);
		}
		break;
	case 12:					// register mask
		iz = 'Reg mask';		// do not allow the SP to "wrap" - the blobs code would fail
		if ((inst & 0x200) == 0) {	// PSH
			iy = 'PSH';
			for (var i = 0; i < 8; ++i) {
				if ((inst&(1<<i)) != 0) {
					if (registerSP == 0) {
						message("SP invalide au PC = "+pCounter);
						return 1;
					}
					updateSP(registerSP-1);
					setAddress(registerSP, register[i]);
				}
			}
			if ((inst & 0x100) != 0) {	// LR
				if (registerSP == 0) {
					message("SP invalide au PC = "+pCounter);
					return 1;
				}
				updateSP(registerSP-1);
				setAddress(registerSP, registerLR);
			}
		} else {					// POP
			iy = 'POP';
			if ((inst & 0x100) != 0) {	// PC
				if (registerSP == 400) {
					message("SP invalide au PC = "+pCounter);
					return 1;
				}
				updatePC(address[registerSP]);
				updatePCmarker(pCounter);
				updateSP(registerSP+1);
			}
			for (var i = 7; i >= 0; --i) {
				if ((inst&(1<<i)) != 0) {
					if (registerSP == 400) {
						message("SP invalide au PC = "+pCounter);
						return 1;
					}
					updateR(i, address[registerSP]);
					updateSP(registerSP+1);
				}
			}
		}
		break;
	case 14:					// R,imm8
		var imm = inst&255;
		var rsd = (inst>>8)&7;
		var result=0;
		var b = register[rsd];
		var sw = (inst>>11)&31;
		if (sw != 5) flags = 0;		// N Z C V - MOV does not set flags (no ALU)
		iz = 'Rsd,#imm';
		switch(sw) {
		case 2:		// ADD
			iy = 'ADD';
			result = b + imm;
			if ((b&0x8000)==0 && ((result^b)&0x8000)!=0) flags = 1;
			if ((result&0x10000)!=0) flags |= 2;
			updateR(rsd, result);
			break;
		case 3:		// SUB
			iy = 'SUB';
			result = b - imm;
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if ((b&0x8000)!=0 && ((result^b)&0x8000)!=0) flags = 1;
			if ((result&0x10000)==0) flags |= 2;
			updateR(rsd, result);
			break;
		case 4:		// CMP
			iy = 'CMP';
			result = b - imm;
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if ((b&0x8000)!=0 &&
				((result^b)&0x8000)!=0) flags = 1;
			if ((result&0x10000)==0) flags |= 2;
			break;
		case 5:		// MOV
			iy = 'MOV';
			result = imm;
			updateR(rsd, result);
			break;
		case 6:		// AND
			iy = 'AND';
			result = b & imm;
			updateR(rsd, result);
			break;
		case 7:		// ORR
			iy = 'ORR';
			result = b | imm;
			updateR(rsd, result);
			break;
		case 8:		// XOR
			iy = 'XOR';
			result = b ^ imm;
			updateR(rsd, result);
			break;
		case 10:		// MUL
			iy = 'MUL';
			result = b*imm;
			if (result>65535) flags=2;		// unsigned overflow
				if ((result&0xFFFF)>32767) {
				var tmp = result/65536;
				if ((tmp&(tmp+1))!=0)flags|=1;
			} else {
				if ((result&0xFFFF0000)!=0)flags|=1;
			}
			updateR(rsd, result);
			break;
		case 9:		// unsigned DIV
			iy = 'UDV';
			if (imm == 0) flags = 1;
			else result = Math.floor(b/imm);
			updateR(rsd, result);
			break;
		case 1:		// MOD
			iy = 'MOD';
			if (imm == 0) flags = 1;
			else result = b%imm;
			updateR(rsd, result);
			break;
		default:		// this should not happen
			message("Instruction invalide au PC = "+pCounter);
			return 1;
			break;
		}
		if (sw != 5) {		// MOV does not set flags
			result &= 0xFFFF;	// some instructions only set flags so dont save reg here
			if (result == 0) flags |= 4;
			if ((result&0x8000)!=0) flags |= 8;
			updateFlags(flags);
		}
		break;
	default:
		message("Instruction invalide au PC = "+pCounter);
		return 1;
		break;
	}
	//y += '<span style="font-size:8pt"> '+iy+'</span>';
	//text("ir", y, 329, 311, 18, "black");			// update the IR display
	text("cu", iy, 352, 337, 12, "white");
	stepTxt = "Done instruction "+iy+' '+iz;
	//if (inst) message("Done instruction "+iy+' '+iz);	// not in input case
	return 0;
}

//  mode is 4 for signed, 5 for unsigned, 6 for hex and 7 for character
function outputNum(y,mode)
{
	// Note output is the HTML output, output1 is a copy with space instead of new line

	// if the user is switching modes force a space after any mode 7 output
	if (mode != 7 && output1.length > 0 && output1[output1.length-1] != ' ') {
		output1 += ' ';
		output += ' ';
	}
	
	switch (mode) {
	case 4:
		if (y > 32767) {  // negative
			y = 65536 - y
			output1 += '-'+y+' ';
			output += '-'+y+' ';
		} else {
			output1 += y+' ';
			output += y+' ';
		}
		break;
	case 5:
		output1 += y+' ';
		output += y+' ';
		break;
	case 6:
		var hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
		output1 += '0x';
		output += '0x';
		var z = Math.floor(y/4096);
		if (z) {output1 += hex[z]; output += hex[z];}
		z = Math.floor(y/256);
		if (z) {output1 += hex[z%16]; output += hex[z%16];}
		z = Math.floor(y/16);
		if (z) {output1 += hex[z%16]; output += hex[z%16];}
		output1 += hex[y%16] + ' ';
		output += hex[y%16] + ' ';
		break;
	case 7:
		var z = String.fromCharCode(y);
		if (y == 10) {
			output1 += '\n';
			output += '<br /> ';
		} else if (z == '<') {
			output1 += z;
			output += '&lt;';
		} else if (z == '>') {
			output1 += z;
			output += '&gt;';
		}else if (z == '&') {
			output1 += z;
			output += '&amp;';
		} else if (y > 31) {
			output1 += z;
			output += z;
		}			
		// need to get a wrap every 11 chars
		var i = output1.length;
		while (--i >= 0) if (output1[i] == ' ' || output1[i] == '\n') break;
		if ((output1.length - i) > 11) {
			output1 += '\n';
			output += '<br />';
		}
		break;
	} 
	// need to count lines, can get 5 lines of up to 11 chars but wraps if number does not fit
	var cnt = 0;
	var pos = 0;
	var nxt = 0;
	var lines = 0;
	var first = 0;
	while (pos < output1.length) {
		while ((nxt+cnt) < 13 && pos < output1.length) {
			cnt += nxt;
			nxt = 0;
			while (pos < output1.length && output1[pos] != ' ' && output1[pos] != '\n') {++nxt; ++pos;}
			if (output1[pos] == '\n') {
				++pos;
				cnt = pos;
				nxt = 0;
				break;
			}
			++pos;
			++nxt;
		}
		if (lines == 0) first = cnt;
		if (pos >= output1.length &&  (nxt+cnt)> 12) ++lines;
		cnt = 0;
		++ lines;
	}
	//alert("pos="+pos+" nxt="+nxt+" cnt="+cnt+" lines="+lines+" first="+first);
	if (lines > 5) {
		output1 = output1.substring(first);
		pos = 0;
		for (cnt = 0; cnt < first; ++cnt) {
			if (output[pos] == '&') {
				while (output[pos] != ';') ++pos;
			} else if (output[pos] == '<') {
				while (output[pos] != '>') ++pos;
			}
			++pos;
		}
		output = output.substring(pos);
		// dont understand why this was needed
		if (output[0] == '<') output = output.substring(6);
	}
	text("output", output, 398, 559, 14, "black", "", "", monospace);
}


var redX;			// Note that "red" is the FETCH moving blob and may be red as an address or blue as data
var redY;
var redVal;
var blueX;			// Blue is used for memory accesses and starts as red as well - used by FETCH and EXECUTE
var blueY;
var blueVal;		// note that red.gif and blue.gif are round,blue3.gif and red3.gif 
				// are oval to allow for 3 digits (and 4 for 4 digits)
var step2Busy = false;

// called from runContinue if running with execution indication (step now uses runContinue)
// set execErr true if get an error executing the instruction;
function step2()		// one instruction with execution indication
{
	if (waitingForInput) return;
	if (step2Busy) return;
	step2Busy = true;
	remove("cu");
	message("Etape de LECTURE - chargement de l'instruction courante et ajout de 1 au registre PC");
	redX = 350;
	redY = 68;
	image("red1", (pCounter<100)?"red.gif":"red3.gif", redX, redY, "PC");
	text("red2", pCounter, redX+4, redY+4, 14, "black");
	myTimeout1 = delay(valW, "step2a1");
}

function moveRed(x, y, dfn)	// return true if arrived else false (and set delay)
{
	if (redX == x && redY == y) return true;
	if (x > redX) {
		if ((x-redX)>s2T) redX+=s2T;
		else redX=x;
	} else if (x < redX) {
		if ((redX-x)>s2T) redX-=s2T;
		else redX=x;
	}
	if (y > redY) {
		if ((y-redY)>s2T) redY+=s2T;
		else redY=y;
	} else if (y < redY) {
		if ((redY-y)>s2T) redY-=s2T;
		else redY=y;
	}
	dmove("red1", redX, redY,"red2", redX+4, redY+4);
	myTimeout1 = delay(valW, dfn);
	return false;
}

function moveBlue(x, y, dfn)	// return true if arrived else false (and set delay)
{
	if (blueX == x && blueY == y) return true;
	if (x > blueX) {
		if ((x-blueX)>s2T) blueX+=s2T;
		else blueX=x;
	} else if (x < blueX) {
		if ((blueX-x)>s2T) blueX-=s2T;
		else blueX=x;
	}
	if (y > blueY) {
		if ((y-blueY)>s2T) blueY+=s2T;
		else blueY=y;
	} else if (y < blueY) {
		if ((blueY-y)>s2T) blueY-=s2T;
		else blueY=y;
	}
	dmove("blue1", blueX, blueY, "blue2", blueX+4, blueY+4);
	myTimeout2 = delay(valW, dfn);
	return false;
}

// similar to above for multiple regs POP except does not delay
function maskMove(i, x, y)
{
	if (maskX[i] == x && maskY[i] == y) return true;
	if (x > maskX[i]) {
		if ((x-maskX[i])>s2T) maskX[i]+=s2T;
		else maskX[i]=x;
	} else if (x < maskX[i]) {
		if ((maskX[i]-x)>s2T) maskX[i]-=s2T;
		else maskX[i]=x;
	}
	if (y > maskY[i]) {
		if ((y-maskY[i])>s2T) maskY[i]+=s2T;
		else maskY[i]=y;
	} else if (y < maskY[i]) {
		if ((maskY[i]-y)>s2T) maskY[i]-=s2T;
		else maskY[i]=y;
	}
	dmove("blueM"+i, maskX[i], maskY[i], "blueN"+i, maskX[i]+4, maskY[i]+4);
	return false;
}

function step2a1()			// fetch cycle - PC update - down to bus
{
	if (moveRed(350,154,"step2a1")) step2a2();
}
function step2a2()			// fetch cycle - PC update - right to main bus
{
	if (moveRed(469,154,"step2a2")) {	// need to split blobs
		blueVal = pCounter;						// because pCounter may change
		blueX = redX;
		blueY = redY+5;
		image("blue1", (blueVal<100)?"red.gif":"red3.gif", blueX, blueY, "PC");	// red on way there, blue on way back
		text("blue2", blueVal, blueX+4, blueY+4, 14, "black");
		inst = 0;			// marker that step2e is doing FETCH (step2e used in several cases)
		myTimeout2 = delay(valW, "step2e");
		step2b();
	}
}
function step2b()			// fetch cycle - PC update - up main bus to incrementor
{
	if (moveRed(469,68,"step2b")) {	// arrived so add 1
		button("au", "+1", 430, 68, "");
		text("red2", "+1", redX+4, redY+4, 14, "black");
		myTimeout1 = delay(400/(s2T+1), "step2c");
	}
}
function step2c()			// fetch cycle - PC update - had pause to add 1
{
	image("red1", (pCounter<99)?"blue.gif":"blue3.gif", redX, redY, "PC");	
	text("red2", pCounter+1, redX+4, redY+4, 14, "black");
	step2d()
}
function step2d()			// fetch cycle - move blob back to PC
{
	if (redX < 440) remove("au");			// delay so is more visible
	if (moveRed(350,68,"step2d")) {		// finished - update PC
		myTimeout1 = false;
		updatePC(pCounter+1);		// delay updating the marker until the fetch is done
		remove("red1");
		remove("red2");
	}
}

function step2e()			// fetch or execute cycle - PC address  or data address to memory
{						// up or down to memory (address) bus	
	if (moveBlue(469,190,"step2e")) step2e1();
}
function step2e1()			// right to memory tens column
{
	if (moveBlue(541,190,"step2e1")) step2e2();
}
function step2e2()			// up or down memory tens column
{						// setAddress uses x=568+memX(x), y=74+Math.floor(x/10)*15,
	var y = 72+Math.floor(blueVal/10)*15;
	if (moveBlue(541,y,"step2e2")) step2f();
}
function step2f()			// right to memory location
{
	var x = 588+memX(blueVal);
	var y = 72+Math.floor(blueVal/10)*15;
	if (moveBlue(x,y,"step2f")) {
		if (inst && bFlg == 301) {
			if (maskCnt > 1) {
				stepMR();
				return;
			}
			bFlg = 14;		// one reg - may as well just use normal logic
			ALUdst = maskRegs[0];
			ALUres = address[blueVal];
			ALUflg = -1;
		}
		var str = getMode(address[blueVal]);
		x -= str.length*3-3;
		blueX = x;
		image("blue1", getBlueS(str.length), x, y, "PC");
		text("blue2", str, x+4, y+4, 14, "black");
		myTimeout2 = delay(valW*2, "step2g");
	}
}	
function step2g()			// left to memory tens column
{
	var y = 72+Math.floor(blueVal/10)*15;
	if (moveBlue(541,y,"step2g")) step2g1();
}
function step2g1()			// up or down to memory bus
{
	if (moveBlue(541,264,"step2g1")) step2g2();
}
function step2g2()			// left to main bus
{
	if (moveBlue(469,264,"step2g2")) {
		if (inst) {
			if (bFlg == 13) stepALUb3();	// memory read for ALU operation
			else if (bFlg == 14) {
				stepALUb8();	// write to register (from POP as well)
				/* if (ALUflg >= 0) {		// set flags on value reading from memory
					var flg = (value==0)?4:0;
					if ((value&0x8000)!=0) flg+= 8;
					updateFlags(flg);	// if dest is flags will be overwritten
				} */
			}				
			//else step2j();				// some other part of EXECUTE
		} else {
			updatePCmarker(pCounter);	// slight race condition here - assume PC has been updated by now
			step2h();				// doing FETCH
		}
	}
}

function step2h()			// fetch cycle  - move instruction down the bus
{
	if (moveBlue(469,312,"step2h")) step2h1();
}
function step2h1()			// fetch cycle  - move instruction left to IR
{
	if (moveBlue(360,312,"step2h1")) {
		message("LECTURE de l'instruction termin&eacute, d&eacutecodage de l'instruction");
		inst = address[blueVal];
		remove("blue1");
		remove("blue2");
		var hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
		var z = Math.floor(inst/256);
		var y = inst%256;
		y = '&nbsp;<span style="letter-spacing:0.15em;">x'+hex[Math.floor(z/16)]+hex[z%16]+hex[Math.floor(y/16)]+hex[y%16]+'</span>';
		text("ir", y, 329, 311, 18, "black");			// update the IR display
		document.getElementById("ir").style.paddingTop = "0";
		myTimeout2 = delay(600/(s2T+1), "step2i");
	}
}

var busABusy = 0;		// 0 idle, 1 active moving, 2 waiting for B bus
var getBlue = ["blue.gif","blue.gif","blue.gif","blue3.gif","blue4.gif","blue5.gif","blue6.gif","blue6.gif"];
// make a function because out of range does really strange things
function getBlueS(len)
{
	if (len < 0) len =0;
	if (len > 7) len = 7;
	return getBlue[len];
}
var ALUop;
var ALUres;
var ALUflg;
var ALUdst;
var TRaddr;
var Bflg;

// function to start the execution blobs for ALU operations, the parameters are
// as = source register for the left (A) bus operation to ALU, uses the RED channel, -1 if nothing to do
// bs = same for main (B) bus, uses blue channel, 0-7 are regs, 8=SP, 9=LR, 10=PC, 11=flags, 12=imm, 13 = mem
// bVal = immediate value or memory address
// iy = the ALU code for the operation (text string)
// result = the ALU output
// rd = the register to put the result in - 0-7,8-11, >=12 using ALU for address calcualtion, -1 for CMP/TST
//		200 used for switch to write reg to memory logic (after address calcalation)
//		100+reg used for switch to fetch logic to read memory into a register
//		300 used for PSH multiple registers (after writing back the SP)
// new_flags = the new flags (or -1 if no change)
function startALU(as, bs, bVal, iy, result, rd, new_flags)
{
	ALUop = iy;
	ALUres = result;
	ALUflg = new_flags;
	ALUdst = rd;
	if (as >= 0) {
		redX = 350;
		var val;
		if (as>10) {	// assume flags
			redY = 278;
			val = String(flags);
		} else {
			redY = 230-16*as;
			if (as < 8) val = getMode(register[as]);
			else if (as == 8) val = String(registerSP);
			else if (as == 9) val = String(registerLR);
			else val = String(pCounter);
		}
		image("red1", getBlueS(val.length), redX, redY, "PC");
		text("red2", val, redX+4, redY+4, 14, "black");
		busABusy = 1;
		myTimeout1 = delay(valW, "stepALUa1");
	}
	if (bs > 11) {			// 12=imm, 13=memory (add/sub direct) 
		blueX = 370;		// need to get a field from the IR
		blueY = 312;
		bFlg = bs;		// marker for which case we are doing
		blueVal = bVal;		// for case 13, read from memory
		var val = bVal;
		if (bs == 12) {		// immediate case
			val = getMode(bVal);
			image("blue1", getBlueS(val.length), blueX, blueY, "IMM");
		} else {
			// move address as unsigned and in red blob
			image("blue1", (bVal<100)?"red.gif":"red3.gif", blueX, blueY, "ADDR");
		}
		text("blue2", val, blueX+4, blueY+4, 14, "black");
		myTimeout2 = delay(valW, "stepALUb0");
	} else if (bs >= 0) {		// register destination cases
		blueX = 360;
		var val;
		if (bs>10) {	// assume flags
			blueY = 278;
			val = String(flags);
		} else {
			blueY = 230-16*bs;
			if (bs < 8) val = getMode(register[bs]);
			else if (bs == 8) val = String(registerSP);
			else if (bs == 9) val = String(registerLR);
			else val = String(pCounter);
		}
		image("blue1", getBlueS(val.length), blueX, blueY, "PC");
		text("blue2", val, blueX+4, blueY+4, 14, "black");
		myTimeout2 = delay(valW, "stepALUb1");
	}
}

// function to move a register contents to the B bus using the blue channel for use by a
// subsequent read or write to/from memory (and possibly other cases but not fetch)
// bs is source register (not flags), bVal is the contents to use (normally also the address)
// rd is the code on what to do at the B bus - 200 and 100+reg as startALU, <12 to pass the SP
// through the incrementer back to the SP and the read memory into register rd
// 301 when get to memory do a multiple regs read, also do a multiple increment on the SP
// 400+device to output
function startReg(bs, bVal, rd)
{
	ALUop = 0;
	ALUdst = rd;
	ALUres = bVal;		// memory address (output value for 400 case)
	ALUflg = -1;		// in case we use the ALU at some point - possibly redundant
	blueX = 360;
	blueY = 230-16*bs;
	if (rd < 400) bVal = bVal % 400;
	var val;
	if (bs < 8) val = getMode(bVal);
	else val = String(bVal);
	if (rd >= 400) image("blue1", getBlueS(val.length), blueX, blueY, "DATA");
	else image("blue1", (bVal<100)?"red.gif":"red3.gif", blueX, blueY, "ADDR");
	text("blue2", val, blueX+4, blueY+4, 14, "black");
	myTimeout2 = delay(valW, "stepRega");
}

// function to do the JMS with blobs, involves a transfer from PC to LR (RED) and IMM to PC (BLUE)
// although both are blue blobs, don't see why we cannot do them in parallel
// mode is -1 for immediate or a register as the address source
function startJMS(add,mode)
{
	// first setup the internal PC to LR transfer (blink and you will miss it)
	redX = 350;
	redY = 68;
	var val = String(pCounter);
	image("red1", (pCounter<100)?"blue.gif":"blue3.gif", redX, redY, "PC");
	text("red2", val, redX+4, redY+4, 14, "black");
	myTimeout1 = delay(valW*5, "stepJMS1");
	updateLR(pCounter); // do now to avoid saving and hope the blob obscures or it is quick
	if (mode == -1) startB(add);		// use standard direct address to PC move
	else startTR(mode, 10, add);
}
function startB(add)		// move direct address to PC
{					// just a special case of the general transfer
	startIMM(10, add);
}

// control unit to register rountine - merge with end of ALU ops - use BLUE channel
// rd = destination, 0-7 are regs, 8=SP, 9=LR, 10=PC, 11=flags (100+R for read memory to register)
// result = the value to put in the data blob and the register on arrival, unsigned in blob
function startIMM(rd, result)
{
	ALUop = 0;
	ALUres = result;	// needed to update dest when we get there
	ALUflg = -1;		// possibly redundant
	ALUdst = rd;
	blueX = 370;		// need to get a field from the IR
	blueY = 312;
	var val;
	if (rd<8) val = getMode(result);
	else val = String(result);
	if (rd > 99) {		// need a red blob to go to memory
		image("blue1", (result<100)?"red.gif":"red3.gif", blueX, blueY, "ADD");
		bFlg = rd;
		blueVal = result;	// memory address to read from
		ALUdst -= 100;	// and write to this register
		ALUres = address[result];	// with this value
	} else {
		image("blue1", getBlueS(val.length), blueX, blueY, "IMM");
		bFlg = 222;		// marker for which case we are doing
	}
	text("blue2", val, blueX+4, blueY+4, 14, "black");
	myTimeout2 = delay(valW, "stepALUb0");
}

// function to move a blue blob up or down the internal register bus
// if rs or rd is a special register it is done unsigned, else in current mode
function startTR(rs, rd, result)
{
	ALUop = 0;
	ALUres = result;	// needed to update dest when we get there
	ALUflg = -1;		// possibly redundant
	ALUdst = rd;
	blueX = 350;		// does not change
	if (rs>10) blueY = 278;	// assume flags
	else blueY = 230-16*rs;
	var val;
	if (rs < 8 && rd < 8) val = getMode(result);
	else val = String(result);
	if (val.length > 3) blueX = 334;
	image("blue1", getBlueS(val.length), blueX, blueY, "IMM");
	text("blue2", val, blueX+4, blueY+4, 14, "black");
	myTimeout2 = delay(valW*5, "stepALUb10");
}
/* function stepTRa()
{
	if (ALUflg >= 0) updateFlags(ALUflg);	// might be overwriting these later
	stepALUb10();						// standard finish - might need slowing down
} */

// ERROR in below POP is a READ function - so a bit like FETCH with +1 and read data
// For POP we need to add 1 and write back to the SP (use the PC's incrementor)
// Solution - ARM does not have POP SP al an allowed instruction so we do not have it either

// Plan for write to memory - feeder routine gets the address to the B bus in a red blob on the
// blue channel. The data source is a register. For PSH we need to write the address back to the SP
var writeAdd;		// address we are going to
var writeDat;		// data we are going to put there
var writeReg;		// the register the data comes from
var writeMode;		// 0 just write the data to memory, 1 write SP as well, 2 multiple regs push
var writeDataOnB;	// to control when address moves off
// what the caller has to do is call setWrite with the data and then start a feeder function to get the
// red address blob to the B bus using the blue channel. The feeder then traps into step2n().
function setWrite(addr, data, reg, mode)
{
	writeAdd = addr;
	writeDat = data;
	writeReg = reg;
	writeMode = mode;
	writeDataOnB = false;
}

function stepRega()			// register to B bus for memory op/OUT - down to bus
{
	if (moveBlue(350,154,"stepRega")) stepRegb();
}
function stepRegb()			// register to B bus for memory op/OUT - right to main bus
{
	if (moveBlue(469,154,"stepRegb")) {
		if (ALUdst == 200) step2n();		// write reg to memory
		else if (ALUdst >= 400) step2t();		// OUT instruction		
		else if (ALUdst > 99 && ALUdst < 110) {
			blueVal = ALUres;
			bFlg = 14;		// come back to stepALUb8() after memory get
			ALUdst -= 100;	// and write to this register
			ALUres = address[ALUres];	// with this value
			step2e();		// need to read from memory first
		} else if (ALUdst < 12 || ALUdst == 301) {
			// need to split the red blob and move it up
			redX = blueX;
			redY = blueY;
			image("red1", (ALUres<100)?"red.gif":"red3.gif", redX, redY, "SP");
			text("red2", ALUres, blueX+4, blueY+4, 14, "black");
			myTimeout1 = delay(valW, "stepRegc");
			if (ALUdst == 301) {
				bFlg = 301;		// multiple read when get to memory
				blueVal = registerSP;
			} else {
				blueVal = ALUres;
				bFlg = 14;		// come back to stepALUb8() after memory get
				ALUres = address[ALUres];	// with this value
			}
			step2e();		// need to read from memory in parallel
		}
	}
}
function stepRegc()			// move an SP copy up to the incrementor (red channel)
{
	if (moveRed(469,68,"stepRegc")) {		// arrived at incrementor
		if (ALUdst == 301) button("au", "+"+maskCnt, 430, 68, "");
		else button("au", "+1", 430, 68, "");
		text("red2", "+", redX+4, redY+4, 14, "black");
			myTimeout1 = delay(400/(s2T+1), "stepRegd");
	}
}
function stepRegd()			// passing SP through incrementor
{
	if (ALUdst == 301) {	// care blueVal is also the memory address the other blob is going to
		image("red1", ((blueVal+maskCnt)<100)?"blue.gif":"blue3.gif", redX, redY, "SP");	
		text("red2", blueVal+maskCnt, redX+4, redY+4, 14, "black");
	}else {
		image("red1", (blueVal<99)?"blue.gif":"blue3.gif", redX, redY, "SP");	
		text("red2", blueVal+1, redX+4, redY+4, 14, "black");
	}
	stepRege()
}
function stepRege()			// moving left towards internal bus to SP
{
	if (redX < 440) remove("au");			// delay so is more visible
	if (moveRed(350,68,"stepRege")) stepRegf();
}
function stepRegf()			// moving down to SP
{
	if (moveRed(350,102,"stepRegf")) {		// finished - update SP
		if (ALUdst == 301) updateSP(blueVal+maskCnt);
		else updateSP(blueVal+1);
		remove("red1");
		remove("red2");
		myTimeout1 = false;
	}
}

function step2n()			// write to memory address to split point (if required)
{
	if (writeMode) {	// need to split the blob - but if below the link move up first
		if (blueY > 220) {		// delay the split while move up
			if (!moveBlue(469,220,"step2n")) return;
		}
		// use the red channel for a copy
		redX = blueX;
		redY = blueY;
		image("red1", (writeAdd<100)?"red.gif":"red3.gif", redX, redY, "ADDR");
		text("red2", writeAdd, redX+4, redY+4, 14, "black");
		myTimeout1 = delay(valW, "step2n1");
	} else step2p();	// start red channel moving data from register
	step2o();
}
function step2n1()
{
		if (moveRed(469,220,"step2n1")) step2n2();	// arrived at link to registers
}

function step2n2()			// moving left towards internal bus to SP
{
	if (moveRed(350,220,"step2n2")) step2n3();
}
function step2n3()			// moving up to SP
{
	if (moveRed(350,102,"step2n3")) {		// finished - update SP
		updateSP(writeAdd);
		if (writeMode == 2 && maskCnt > 1) {
			remove("red1");
			remove("red2");	// note wait channel 1 reused but not red
			stepMW();			// will need to fake writeDataOnB and redY
		} else step2p();			// re-uses red channel
	}
}

function step2o()			// write to memory - address to bus exit
{
	if (moveBlue(469,190,"step2o")) step2o1();
}
function step2o1()			// write to memory - move along bus towards memory
{						// but wait to be caught up by the data blob
	var targetX = 500;
	if (writeDataOnB && redY < 220 && redY > 160) targetX = 541;
	if (moveBlue(targetX,190,"step2o1")) {
		if (targetX == 500) myTimeout2 = delay(valW, "step2o1");
		else step2o2();
	}
}
function step2o2()			// write to memory - move address up or down tens column
{
	var y = 72+Math.floor(writeAdd/10)*15;
	if (moveBlue(541,y,"step2o2")) step2o3();
}
function step2o3()			// move address blob right to memory location
{
	var x = 588+memX(writeAdd);
	var y = 72+Math.floor(writeAdd/10)*15;
	if (moveBlue(x,y,"step2o3")) myTimeout2 = false;
	// just exit when get there because waiting for blue blob (i.e. leave red blob just sitting there)
}

function step2p()			// use the red channel to start a blue blob at the source register
{						// used for all registers in PSH case
	redX = 360;
	if (writeReg == 11) redY = 278;
	else redY = 230-16*writeReg;
	var val;
	if (writeReg > 7) val = String(writeDat);
	else val = getMode(writeDat);
	image("red1", getBlueS(val.length), redX, redY, "DATA");
	text("red2", val, redX+4, redY+4, 14, "black");
	myTimeout1 = delay(valW, "step2p1");
}
function step2p1()		// move from register to the link to bus B
{
	if (moveRed(360,154,"step2p1")) step2p2();
}
function step2p2()		// move to bus B, for non PSH writes we need to pause
{					// if the address blob has not got to the memory link yet
	if (redX > 400 && blueY != 190) myTimeout1 = delay(valW, "step2p2");
	else if (moveRed(469,154,"step2p2")) step2p3();
}
function step2p3()		// move down bus B to memory link
{					// might join other cases here if data can come from ALU for example
	writeDataOnB = true;
	if (moveRed(469,190,"step2p3")) step2p4();
}
function step2p4()		// move along bus towards memory
{
	if (moveRed(541,190,"step2p4")) step2p5();
}
function step2p5()			// move up or down tens column
{
	var y = 72+Math.floor(writeAdd/10)*15;
	if (moveRed(541,y,"step2p5")) step2p6();
}
function step2p6()			// move blob right to memory location
{
	var x = 588+memX(writeAdd);
	var y = 72+Math.floor(writeAdd/10)*15;
	if (moveRed(x,y,"step2p6")) {
		// when done update the memory, remove the blobs and end the instruction
		setAddress(writeAdd, writeDat);
		remove("red1");
		remove("red2");
		remove("blue1");
		remove("blue2");
		myTimeout1 = false;
		step2Busy = false;
	}	
}

// Redesign. a) Have a control unit to register rountine - merge with end of ALU ops
//	b) have a register to register routine - startTR possibly
//	c) have a read memory routine (source address control unit)
//	d) have a write memory routine (source address control unit)
// need variants of c and d for (SP) and off(reg) cases

function stepALUa1()		// move to bus A and down to the kink
{
	if (moveRed(325,253,"stepALUa1")) stepALUa2();
}
function stepALUa2()		// move left on bus A
{
	if (moveRed(286,253,"stepALUa2")) stepALUa3();
}
function stepALUa3()		// move down on bus A
{
	if (moveRed(286,430,"stepALUa3")) { // stop inside the ALU
		busABusy = 2;
	}
}

function stepALUb0()		// move value from IR to B bus - down to link
{
	if (moveBlue(370,341,"stepALUb0")) stepALUb0a();
}
function stepALUb0a()		// move value from IR to B bus - right along link
{
	if (moveBlue(469,341,"stepALUb0a")) {
		if (bFlg == 12) stepALUb3();		// ADD etc. immediate case - join the regs path
		else if (bFlg == 13) step2e();		// read from memory next
		else if (bFlg == 222) stepALUb8();	// write to reg
		else if (bFlg == 200) step2n();		// write reg to memory
		else if (bFlg > 99 && bFlg < 110) {
			bFlg = 14;					// write to register after memory read
			step2e();					// need to read from memory first
		}
	}
}

function stepALUb1()		// move from register to the link to bus B
{
	if (moveBlue(360,154,"stepALUb1")) stepALUb2();
}
function stepALUb2()		// move to bus B
{
	if (moveBlue(469,154,"stepALUb2")) stepALUb3();
}
function stepALUb3()		// move down bus B
{
	if (moveBlue(469,433,"stepALUb3")) stepALUb4();
}
function stepALUb4()		// move left to the ALU
{
	if (moveBlue(388,433,"stepALUb4")) {
		if (busABusy == 1) myTimeout2 = delay(valW, "stepALUb4");
		else stepALUb5();		// start to converge the blobs
	}
}
function stepALUb5()		// converge the blobs
{
	button("au", ALUop, 290, 495, "");
	// red is no longer running so do it manually - moves in tandem with blue
	if (busABusy == 2) {	// providing it is not negate or similar
		redX+=s2T;
		redY+=s2T;	
		dmove("red1", redX, redY, "red2", redX+4, redY+4);
	}
	if (moveBlue(338,482,"stepALUb5")) {
		if (busABusy) {
			remove("red1");
			remove("red2");
			busABusy = 0;
		}
		var val;			// put result in single blob;
		if (ALUdst < 8) val = getMode(ALUres&0xFFFF);
		else val = String(ALUres);
		if (ALUdst > 99) {	// we have been making an address
			image("blue1", (ALUres<100)?"red.gif":"red3.gif", blueX, blueY, "AD");
		} else {
			image("blue1", getBlueS(val.length), blueX, blueY, "DT");
		}
		text("blue2", val, blueX+4, blueY+4, 14, "black");
		if (ALUflg >= 0) updateFlags(ALUflg);
		if (ALUdst == -1) myTimeout2 = delay(valW*5, "stepALUb5a"); // CMP
		else myTimeout2 = delay(valW, "stepALUb6");
		if (ALUop == 'MLX' && ALUdst < 7) {   // need to start high reg write
			val = getMode((ALUres>>16)&0xFFFF);	// beware >> is signed
			image("red1", getBlueS(val.length), redX, redY, "MXH");	
			text("red2", val, redX+4, redY+4, 14, "black");
			step2l();
		}
	}
}
function stepALUb5a()		// CMP or TST instruction, after a pause tidy up
{
	remove("blue1");		// end of instruction for now
	remove("blue2");
	myTimeout2 = false;
	step2Busy = false;
}

function stepALUb6()		// move to the exit point
{
	if (moveBlue(388,489,"stepALUb6")) {
		remove("au");
		stepALUb7();
	}
}
function stepALUb7()		// move to B bus
{
	if (moveBlue(469,489,"stepALUb7")) {
		// work out where the result is going - apart from special cases it is a register
		if (ALUdst < 12) stepALUb8();
		else if (ALUdst >= 200) {		// LDR/STR R,offset(R) and POP use this 
			// 200 means calculate address as red blob (for STR) and switch to write reg to memory
			// 300 means take the blob to the memory port and write to the SP
			step2n();
		} else if (ALUdst > 99) {
			// 100+R means send address to memory as red blob and put contents in rsd (LDR)
			blueVal = ALUres;
			bFlg = 14;		// come back to stepALUb8() after memory get
			ALUdst -= 100;	// and write to this register
			ALUres = address[ALUres];	// with this value
			step2e();		// use fetch code to get memory
		}
	}
}
function stepALUb8()		// move up B bus to register port
{
	if (moveBlue(469,220,"stepALUb8")) stepALUb9();
}
function stepALUb9()		// move to registers
{
	if (moveBlue(350,220,"stepALUb9")) stepALUb10();
}
function stepALUb10()		// move to register itself (some joining cases have flags as dest)
{						// the startTR case uses a variable X that we need to preserve
	var y = 230-16*ALUdst;
	if (ALUdst == 11) y = 278;
	if (moveBlue(blueX,y,"stepALUb10")) {
		if (ALUdst<8) updateR(ALUdst,ALUres&0xFFFF);
		else if (ALUdst == 8) updateSP(ALUres);
		else if (ALUdst == 9) updateLR(ALUres);
		else if (ALUdst == 10) {
			updatePC(ALUres);
			updatePCmarker(ALUres);
		} else updateFlags(ALUres);
		remove("blue1");		// finished with the blob
		remove("blue2");
		myTimeout2 = false;
		if (ALUop != 'MLX' || ALUdst == 7) {   // no high reg write in process
			step2Busy = false;	// end of instruction
		}
	}
}

function step2l()		// special case - blue blob on red channel with high part of MLX
{					// simplified version of the above with delays so follows the blue
	if (blueX < 388) myTimeout1 = delay(valW, "step2l");
	else if (moveRed(388,489,"step2l")) step2l1();
}
function step2l1()		// move to B bus
{
	if (blueX < 469) myTimeout1 = delay(valW, "step2l1");
	else if (moveRed(469,489,"step2l1")) step2l2();
}
function step2l2()		// move up B bus to register port
{
	if (moveRed(469,220,"step2l2")) step2l3();
}
function step2l3()		// move to registers
{
	if (moveRed(350,220,"step2l3")) step2l4();
}
function step2l4()
{
	var y = 230-16*(ALUdst+1);
	if (moveRed(350,y,"step2l4")) {
		updateR(ALUdst+1,(ALUres>>16)&0xFFFF);
		remove("red1");		// finished with the blob
		remove("red2");
		myTimeout1 = false;
		step2Busy = false;	// end of instruction
	}
}

function stepJMS1()		// red channel move PC to LR
{
	if (moveRed(350,86,"stepJMS1")) {
		// we updated the LR already
		remove("red1");		// assume done long before rest of JMS
		remove("red2");
		myTimeout1 = false;
	}
}


function step2i()					// end of fetch cycle  - decode the instruction
{
	if (s2T == 0) {				// just had a big delay - trap STOP hit and wait
		myTimeout2 = delay(200, "step2i");
		return;
	}
	myTimeout2 = false;			// some instructions do not move blobs
	// need to decode the instruction (copy step1())
	var iy = "";	// to hold instruction name
	var iz = "";	// to hold parameter format
	var format;
	for (format = 0; format < 15; ++format) {
		if ((inst&IMask[format])==IValue[format]) break;
	}	
	switch(format) {
	case 0:			// HLT is a good instruction - caller detects
		iy = 'HLT';
		++inst;		// so still outputs message
		step2Busy = false;
		break;
	case 1:			// 2 regs and a cnt4
		var cnt4 = inst&15;
		var rs = (inst>>4)&7;
		var rd = (inst>>7)&7;
		var result;
		var flgs = 0;		// N Z C V
		iz = 'Rd,Rs,#cnt';
		if ((inst&0x400)==0) {			// LSR
			iy = 'LSR';
			result = register[rs]>>cnt4;
			if (cnt4 > 0 && ((register[rs]>>(cnt4-1))&1) != 0) flgs |= 2;
		} else {						// LSL
			iy = 'LSL';
			result = register[rs]<<cnt4;
			if ((result&0x10000)!=0) flgs |= 2;
		}
		result &= 0xFFFF;
		if (result == 0) flgs |= 4;
		if ((result&0x8000)!=0) flgs |= 8;
		startALU(rs, 12, cnt4, iy, result, rd, flgs);
		break;
	case 2:			// Branches and JMS with address in 9 bits
		var add = inst&511;
		if (add > 399) add -= 400;
		iz = 'address';
		switch ((inst>>9)&15) {
		case 0:		// BRA
			iy = 'BRA';
			startB(add);
			break;
		case 1:		// BEQ
			iy = 'BEQ';
			if ((flags&4)!=0) startB(add);
			else step2Busy = false;
			break;
		case 2:		// BNE
			iy = 'BNE';
			if ((flags&4)==0) startB(add);
			else step2Busy = false;
			break;
		case 3:		// BCS
			iy = 'BCS';
			if ((flags&2)!=0) startB(add);
			else step2Busy = false;
			break;
		case 4:		// BCC
			iy = 'BCC';
			if ((flags&2)==0) startB(add);
			else step2Busy = false;
			break;
		case 5:		// BMI
			iy = 'BMI';
			if ((flags&8)!=0) startB(add);
			else step2Busy = false;
			break;
		case 6:		// BPL
			iy = 'BPL';
			if ((flags&8)==0) startB(add);
			else step2Busy = false;
			break;
		case 7:		// BVS
			iy = 'BVS';
			if ((flags&1)!=0) startB(add);
			else step2Busy = false;
			break;
		case 8:		// BVC
			iy = 'BVC';
			if ((flags&1)==0) startB(add);
			else step2Busy = false;
			break;
		case 9:		// BHI	C set and Z clear (N Z C V)
			iy = 'BHI';
			if ((flags&6)==2) startB(add);
			else step2Busy = false;
			break;
		case 10:		// BLS	C clear or Z set
			iy = 'BLS';
			if ((flags&0x6)!=2) startB(add);
			else step2Busy = false;
			break;
		case 11:		// BGE	N and V both set or both clear (N Z C V)
			iy = 'BGE';
			if ((flags&9)==9 || (flags&9)==0) startB(add);
			else step2Busy = false;
			break;
		case 12:		// BLT	N set and V clear OR N clear and V set
			iy = 'BLT';
			if ((flags&9)==8 || (flags&9)==1) startB(add);
			else step2Busy = false;
			break;
		case 13:		// BGT	Z clear AND (N and V both set or both clear)
			iy = 'BGT';
			if ((flags&4)==0 && ((flags&9)==9 || (flags&9)==0)) startB(add);
			else step2Busy = false;
			break;
		case 14:		// BLE	Z set OR N set and V clear OR N clear and V set  (N Z C V)
			iy = 'BLE';
			if ((flags&4)!=0 || (flags&9)==8 || (flags&9)==1) startB(add);
			else step2Busy = false;
			break;
		case 15:		// JMS
			iy = 'JMS';
			startJMS(add,-1);
			break;
		}
		break;
	case 3:			// STR and LDR R,offset(R) - flags not affected
		// assume format is Rsd Rb offset6
		var off6 = inst&63
		var rb = (inst>>6)&7;
		var rsd = (inst>>9)&7;
		var iz = 'Rsd,offset(Ra)';
		if ((inst&0x1000)==0) {			// STR
			iy = 'STR';
			// setWrite sets up phase 2 of the write to move the address to memory
			// and the data from a register to memory (mode - the last parameter is 1 for PSH)
			setWrite((off6+register[rb])%400, register[rsd], rsd, 0)
			// we then use a feeder function to generate the address in a red blob on
			// the blue channel - the feeder then calls step2n() (flagged by the 200)
			if (off6) {
				startALU(rb, 12, off6, '&nbsp;+&nbsp;', (off6+register[rb])%400, 200, -1);
			} else {	// no need to use ALU if nothing to add
				startReg(rb, register[rb], 200);
			}
		} else {						// LDR
			iy = 'LDR';
			if (off6) {
				startALU(rb, 12, off6, '&nbsp;+&nbsp;', (off6+register[rb])%400, 100+rsd, -1);
				// 100+R means send address to memory as red blob and put contents in rsd
				// will merge with step2e
			} else {	// no need to use ALU if nothing to add
				startReg(rb, register[rb], 100+rsd);
			}				
		}
		break;
	case 4:			// ADD/SUB Rd,addr9 - flags set
		iz = 'Rd,direct';
		var add = inst&511;
		if (add > 399) add -= 400;
		var rd = (inst>>9)&7;
		var result;
		var flgs = 0;	// for ADD V is set if the operands have the same sign and the result is a different sign
		if ((inst&0x1000)==0) { // ADD
			iy = 'ADD';
			result = register[rd] + address[add];
			if (((register[rd]^address[add])&0x8000)==0 &&
				((result^register[rd])&0x8000)!=0) flgs = 1;
			if ((result&0x10000)!=0) flgs |= 2;
		} else {				// SUB
			iy = 'SUB';
			result = register[rd] - address[add];
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if (((register[rd]^address[add])&0x8000)!=0 &&
				((result^register[rd])&0x8000)!=0) flgs = 1;
			if ((result&0x10000)==0) flgs |= 2;
		}
		result &= 0xFFFF;
		if (result == 0) flgs |= 4;
		if ((result&0x8000)!=0) flgs |= 8;
		startALU(rd, 13, add, iy, result, rd, flgs);
		break;
	case 5:			// ADD/SUB SP,imm8 - no flags set
		var imm = inst&255;
		var result;
		if (imm == 0) {	// nothing to do, treat as NOP
			iz = '';
			iy = 'NOP';	// delay so NOP can be seen
			myTimeout1 = delay(400/(s2T+1), "step2z");
			break;
		}
		iz = 'SP,#imm';
		if ((inst&0x100)==0) {
			iy = 'ADD';
			result = registerSP + imm;
		} else {
			iy = 'SUB';
			result = registerSP - imm;
		}
		if (result < 0 || result > 400) {
			//y += '<span style="font-size:8pt"> '+iy+'</span>';
			text("cu", iy, 352, 337, 12, "white");
			//text("ir", y, 329, 311, 18, "black");			// update the IR display
			message("SP invalide au PC = "+(pCounter-1));
			return;		// user must use RESET
		}
		startALU(8, 12, imm, iy, result, 8, -1);
		break;
	case 6:			// three register instructions - all set flags
		var ra = inst&7;
		var rs = (inst>>3)&7;
		var rd = (inst>>6)&7;
		var result;
		var flgs = 0;		// N Z C V
		iz = 'Rd,Rs,Rb';
		switch((inst>>9)&7) {
		case 0:		// ADD
			iy = 'ADD';
			result = register[rs] + register[ra];
			// V is set if the operands have the same sign and the result is a different sign
			if (((register[rs]^register[ra])&0x8000)==0 &&
				((result^register[rs])&0x8000)!=0) flgs = 1;
			if ((result&0x10000)!=0) flgs |= 2;
			break;
		case 1:		// SUB
			iy = 'SUB';
			result = register[rs] - register[ra];
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if (((register[rs]^register[ra])&0x8000)!=0 &&
				((result^register[rs])&0x8000)!=0) flgs = 1;
			if ((result&0x10000)==0) flgs |= 2;
			break;
		case 2:		// AND
			iy = 'AND';
			result = register[rs] & register[ra];
			break;
		case 3:		// ORR
			iy = 'ORR';
			result = register[rs] | register[ra];
			break;
		case 4:		// XOR
			iy = 'XOR';
			result = register[rs] ^ register[ra];
			break;
		case 5:		// LSR
			iy = 'LSR';
			result = register[rs] >> register[ra];
			if (register[ra] > 0 &&
				((register[rs]>>(register[ra]-1))&1) != 0) flgs |= 2;
			break;
		case 6:		//  LSL
			iy = 'LSL';
			result = register[rs] << register[ra];
			if ((result&0x10000)!=0) flgs |= 2;
			break;
		case 7:		// should not happen
			message("Instruction invalide au PC = "+(pCounter-1));
			return 1;
		}
		result &= 0xFFFF;
		if (result == 0) flgs |= 4;
		if ((result&0x8000)!=0) flgs |= 8;
		startALU(rs, ra, 0, iy, result, rd, flgs);
		break;
	case 7:			// STR and LDR R,addr9 - flags not affected
		var add = inst&511;
		if (add > 399) add -= 400;
		var rsd = (inst>>9)&7;
		iz = 'Rsd,direct';
		if ((inst&0x1000)==0) {			// STR
			iy = 'STR';
			setWrite(add, register[rsd], rsd, 0);
			startIMM(200,add);	// use to get the imm out to the bus in red
		} else {						// LDR
			iy = 'LDR';
			startIMM(100+rsd,add);	// use to get the imm out to the bus in red
		}
		break;
	case 8:			// R,cnt4/R,dev4
		var cnt4 = inst&15;
		var rsd = (inst>>4)&7;
		var result;
		var flgs = 0;
		iz = 'Rsd,#cnt';
		switch((inst>>7)&3) {
		case 0:				// ASR
			iy = 'ASR';
			result = register[rsd];
			if ((result&0x8000)!=0) result |= 0xFFFF0000
			result = result>>cnt4;
			if (cnt4 > 0 && ((register[rsd]>>(cnt4-1))&1) != 0) flags |= 2;
			result &= 0xFFFF;
			if (result == 0) flgs |= 4;
			if ((result&0x8000)!=0) flgs |= 8;
			startALU(rsd, 12, cnt4, iy, result, rsd, flgs);
			break;
		case 1:				// ROR
			iy = 'ROR';
			result = register[rsd] + (register[rsd] << 16);
			result >>= cnt4;
			if ((result&0x10000)!=0) flgs |= 2;
			result &= 0xFFFF;
			if (result == 0) flgs |= 4;
			if ((result&0x8000)!=0) flgs |= 8;
			startALU(rsd, 12, cnt4, iy, result, rsd, flgs);
			break;
		case 2:				// INP
			iy = 'INP';
			iz = 'Rd,device';
			// currently only one device so ignore parameter
			message("Entrer une valeur");
			registerToInput = rsd;
			waitingForInput = true;
			remove("input");
			rectangle("inpxx", 261, 541, 100, 37, "white", "red", 2);
			text("inpxx", ' &nbsp; Entrer valeur', 261, 541, 12, "red");
			rectangle("input", 269, 560, 90, 16, "white", "blue");
			text("input", inputForm, 269, 560, 12, "black");
			var elePosn = document.getElementById("iForm");
			elePosn.focus();
			delay(1000, "blinkoff");					// start blink	
			break;
		case 3:				// OUT
			iy = 'OUT';
			iz = 'Rs,device';
			// currently only one device but parameter gives mode
			startReg(rsd, register[rsd], 400+(inst&7));
			break;
		}
		break;
	case 9:			// special/spare - 0111 0010 0 - next bits 00 mov Rd,special; 01 mov special,Rd
		// 1000 pop Rd; 1001 push Rs; 1010 BRA Rs; 1011 JMS Rs; 11000 pop special; 11001 psh special; 1101000 ret
		if ((inst &0xFFC0)==0x7200) {   // MOV cases
			iy = 'MOV';
			var rs = inst & 7;
			var rd = rs;		// set to -1 if not to update
			switch((inst>>3)&7) {	// 3=PC 1=SP 2=LR 0=flags +4 if specials are dest
			case 0:			// MOV Rd,flags
				iz = 'Rd,flags';
				result = flags;
				rs = 11;
				break;
			case 1:			// MOV Rd,SP
				iz = 'Rd,SP';
				result = registerSP;
				rs = 8;
				break;
			case 2:			// MOV Rd,LR
				iz = 'Rd,LR';
				result = registerLR;
				rs = 9;
				break;
			case 3:			// MOV Rd,PC
				iz = 'Rd,PC';
				result = pCounter;
				rs = 10;
				break;
			case 4:			// MOV flags,Rs
				iz = 'flags,Rs';
				result=register[rs];
				rd = 11;
				flagsWanted = false;
				break;
			case 5:			// MOV SP,Rs
				iz = 'SP,Rs';
				result = register[rs];
				rd = 8;
				break;
			case 6:			// MOV LR,Rs
				iz = 'LR,Rs';
				result = register[rs];
				rd = 9;
				break;
			case 7:			// MOV PC,Rs
				iz = 'PC,Rs';
				result = register[rs];
				rd = 10;
				break;
			}
			// these are just direct transfers (no flags set)
			startTR(rs, rd, result);
			break;
		} else if ((inst &0xFFF0)==0x7240) {   // POP/PSH Rsd cases
			var rsd = inst & 7;
			iz = 'Rsd';
			if ((inst&0x8)==0) {
				iy = 'POP';
				startReg(8, registerSP, rsd);
			} else {
				iy = 'PSH';
				// setWrite sets up phase 2 of the write to move the address to memory
				// and the data from a register to memory (mode - the last parameter is 1 for PSH)
				setWrite(registerSP-1, register[rsd], rsd, 1)
				// we then use a feeder function to generate the address in a red blob on
				// the blue channel - the feeder then calls step2n() (flagged by the 200)
				// push no longer sets the flags
				startALU(-1, 8, registerSP, '&nbsp;-1&nbsp;', registerSP-1, 200,-1);
			}
		} else if ((inst &0xFFF0)==0x7250) {   // BRA/JMS Rs cases
			iz = 'Rs';
			if ((inst&0x8)!=0) {		// JMS case rather than BRA
				iy = 'JMS';
				startJMS(register[inst&7],inst&7);
			} else {
				iy = 'BRA';
				startTR(inst&7, 10, register[inst&7]);
			}
		} /* else if ((inst &0xFFFC)==0x7260) {   // POP special regs
			iy = 'POP';
			iz = 'special';
			var x = 7+(inst&3);
			if (x==7) x=11;	// flags case
			startReg(8, registerSP, x);
		} else if ((inst &0xFFFC)==0x7264) {   // PSH special regs
			iy = 'PSH';
			iz = 'special';
			var rs = 7 + (inst&3);
			switch (inst&3) {
			case 0:			// PSH flags
				result = flags;
				rs = 11;
				break;
			case 1:			// PSH SP - the logic is that PSH SP, POP SP should leave
				result = registerSP;	// the SP unchanged, not an ARM instruction!
				break;
			case 2:			// PSH LR
				result = registerLR;
				break;
			case 3:			// PSH PC
				result = pCounter;
				break;				
			}
			// setWrite sets up phase 2 of the write to move the address to memory
			// and the data from a register to memory (mode - the last parameter is 1 for PSH)
			setWrite(registerSP-1, result, rs, 1)
			// we then use a feeder function to generate the address in a red blob on
			// the blue channel - the feeder then calls step2n() (flagged by the 200)
			// PSH special does not set the flags
			startALU(-1, 8, registerSP, '&nbsp;-1&nbsp;', registerSP-1, 200, -1);
		} */ else if (inst==0x7260) {			// RET
			iy = 'RET';
			startTR(9, 10, registerLR);
		} else {		
			message("Instruction invalide au PC = "+(pCounter-1));
			return 1;
		}
		break;
	case 10:					// STR/LDR R,off6(SP) - no flags changes
		var off6 = inst&63;
		var rsd = (inst>>6)&7;
		iz = 'Rsd,offset(SP)';
		if ((inst&0x200)==0) {			// STR
			iy = 'STR';
			setWrite((off6+registerSP)%400, register[rsd], rsd, 0)
			if (off6) {
				startALU(8, 12, off6, '&nbsp;+&nbsp;',(off6+registerSP)%400, 200, -1);
			} else {	// no need to use ALU if nothing to add
				startReg(8, registerSP, 200);
			}
		} else {						// LDR
			iy = 'LDR';
			if (off6) {
				startALU(8, 12, off6, '&nbsp;+&nbsp;', (off6+registerSP)%400, 100+rsd, -1);
			} else {	// no need to use ALU if nothing to add
				startReg(8, registerSP, 100+rsd);
			}
		}
		break;
	case 11:					// two register instructions - most set flags
	case 13:					// MVN
		var ra = inst&7;
		var rsd = (inst>>3)&7;
		if ((inst&0xFFC0)==0x7640) {		// OUT is very different from the rest
			iz = 'Rs,Ra';
			iy = 'OUT';
			// currently only one device but parameter gives mode
			startReg(rsd, register[rsd], 400+(register[ra]&7));
			break;
		}		
		var result=0;
		var a = register[ra];
		var b = register[rsd];
		var carry = (flags&2)>>1;
		var setReg = rsd;	// set -1 if just a compare instruction
		var flgs = 0;		// N Z C V
		iz = 'Rsd,Rb';
		var sw = (inst>>6)&15;
		if (format == 13) {		// MVN case
			iy = 'MVN';
			result = a ^ 0xFFFF;
			rsd = ra;	// it would look better to move the single register down the A bus
			ra = -1;	// but it is too much hard work for one or two instructions
			sw = 16;
		} else switch(sw) {
		case 0:		// unsigned DIV
			iy = 'UDV';
			if (a == 0) flgs = 1;
			else result = Math.floor(b/a);
			break;
		case 1:		// MOD
			iy = 'MOD';
			if (a == 0) flgs = 1;
			else result = b%a;
			break;
		case 2:		// MLX - do 32 bit result (unsigned multiply)
			iy = 'MLX';
			result = b*a;
			// MLX will need a special case ending
			break;
		case 3:		// ASR
			iy = 'ASR';
			result = b;
			if (a > 15) {
				if ((b&0x8000)!=0) {
					result = 0xFFFF;
					flgs |= 2;
				} else result = 0;
			} else {
				if ((b&0x8000)!=0) result |= 0xFFFF0000
				result >>= a;
				if (a > 0 && ((b>>(a-1))&1) != 0) flgs |= 2;
			}
			break;
		case 4:		// ROR
			iy = 'ROR';
			result = b + (b << 16);
			result >>= (a&15);
			if ((result&0x10000)!=0) flgs |= 2;
			break;
		case 5:		// signed DIV
			iy = 'DIV';
			if (a == 0) flgs = 1;
			else {
				var s = 0;
				if ((a&0x8000)!=0) {a = 65536-a; s=1;}
				if ((b&0x8000)!=0) {b = 65536-b; s^=1;}
				result = Math.floor(b/a);
				if (result>32767) flgs=1;
				if (s) result = 65536-result;
			}
			break;
		default:		// dont think can happen
			message("Instruction invalide au PC = "+(pCounter-1));
			return;		// require the user to hit RESET
			break;
		case 6:		// BIC
			iy = 'BIC';
			result = b & (~a);
			break;
		case 7:		// NEG
			iy = 'NEG';
			result = -a;
			rsd = ra;	// it would look better to move the single register down the A bus
			ra = -1;	// but it is too much hard work for one instruction
			break;
		case 8:		// INP
			iy = 'INP';
			// currently only one device so ignore parameter
			message("Entrer une valeur");
			registerToInput = rsd;
			waitingForInput = true;
			remove("input");
			rectangle("inpxx", 261, 541, 100, 37, "white", "red", 2);
			text("inpxx", ' &nbsp; Entrer valeur', 261, 541, 12, "red");
			rectangle("input", 269, 560, 90, 16, "white", "blue");
			text("input", inputForm, 269, 560, 12, "black");
			var elePosn = document.getElementById("iForm");
			elePosn.focus();
			delay(1000, "blinkoff");					// start blink
			break;
		case 10:		// CMP
			iy = 'CMP';
			result = b - a;
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if (((b^a)&0x8000)!=0 && ((result^b)&0x8000)!=0) flgs = 1;
			if ((result&0x10000)==0) flgs |= 2;
			setReg = -1;
			break;
		case 11:		// TST
			iy = 'TST';
			result = b & a;
			setReg = -1;
			break;
		case 12:		// MOV
			if ((inst&31) == 0) {	// MOV R0,R0 - nothing to do, treat as NOP
				iz = '';
				iy = 'NOP';	// delay so NOP can be seen
				myTimeout1 = delay(400/(s2T+1), "step2z");
				break;
			}
			iy = 'MOV';
			result = a;
			break;
		case 13:		// ADC
			iy = 'ADC';
			result = b + a + carry;
			if (((b^a)&0x8000)==0 && ((result^b)&0x8000)!=0) flgs = 1;
			if ((result&0x10000)!=0) flgs |= 2;
			break;
		case 14:		// SBC
			iy = 'SBC';
			result = b - a - 1 + carry;
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if (((b^a)&0x8000)!=0 && ((result^b)&0x8000)!=0) flgs = 1;
			if ((result&0x10000)==0) flgs |= 2;			
			break;
		case 15:		// MUL
			iy = 'MUL';
			result = b*a;
			if (result>65535) flgs=2;		// unsigned overflow
			if ((result&0xFFFF)>32767) {
				var tmp = result/65536;
				if ((tmp&(tmp+1))!=0)flgs|=1;
			} else {
				if ((result&0xFFFF0000)!=0)flgs|=1;
			}
			break;
		}
		if (sw == 2) {	// MLX result is 32 bits
			if (result == 0) flgs |= 4;
			if ((result&0x80000000)!=0) flgs |= 8;
		} else if (sw != 8) {
			result &= 0xFFFF;	// all these instructions set flags except INP and MOV
			if (result == 0) flgs |= 4;
			if ((result&0x8000)!=0) flgs |= 8;
		}
		if (sw == 12) {		// MOV does not go through the ALU
			startTR(ra,rsd,result);
		} else if (sw != 8) {		// nothing here for INP
			startALU(ra,rsd,0,iy,result,setReg,flgs);
		}
		break;
	case 12:					// register mask
		iz = 'Reg mask';		// do not allow the SP to wrap (the blobs could not cope)
		maskCnt = 0;
		maskRegs = [];
		maskStage = [];
		if ((inst&0x1ff) == 0) {	// either error it or treat it as NOP (the blobs could not cope)
			message("Instruction invalide au PC = "+(pCounter-1));
			return;
		}
		if ((inst & 0x200) == 0) {	// PSH
			iy = 'PSH';		// note unlike the non-blobs implementation which just 
			// repeats PSH, we start at the low address so the list is in same order as POP
			if ((inst & 0x100) != 0) {	// LR
				maskRegs[maskCnt] = 9;
				maskStage[maskCnt] = 0;
				++maskCnt;
			}
			for (var i = 7; i >= 0; --i) {
			// for (var i = 0; i < 8; ++i) {
				if ((inst&(1<<i)) != 0) {
					maskRegs[maskCnt] = i;
					maskStage[maskCnt] = 0;
					++maskCnt;
				}
			}
			if ((registerSP - maskCnt) < 0) {
				message("SP invalide au PC = "+(pCounter-1));
				return;
			}
			maskBaseSP = registerSP-maskCnt;
			// need to do a setup for step2n(). Note that the middle two paraments are used only
			// when maskCnt is 1 because uses normal PSH case if only one register
			var val;
			if (maskRegs[0]==9) val = registerLR;
			else val = register[maskRegs[0]];
			setWrite(maskBaseSP,val,maskRegs[0],2);
			// we use a feeder function to generate the address in a red blob on
			// the blue channel - the feeder then calls stepMW() (flagged by the 300 and 2 above)
			// PSH mask does not set the flags (note &#8211; is a wide minus)
			startALU(8, 12, maskCnt, '&nbsp;&#8211;&nbsp;', maskBaseSP, 300, -1);
		} else {					// POP
			iy = 'POP';
			if ((inst & 0x100) != 0) {	// PC
				maskRegs[maskCnt] = 10;
				maskStage[maskCnt] = 0;
				++maskCnt;
			}
			for (var i = 7; i >= 0; --i) {
				if ((inst&(1<<i)) != 0) {
					maskRegs[maskCnt] = i;
					maskStage[maskCnt] = 0;
					++maskCnt;
				}
			}
			if ((registerSP + maskCnt) > 400) {
				message("SP invalide au PC = "+(pCounter-1));
				return;
			}
			maskBaseSP = registerSP;
			// similar to POP but the incrementor adds a variable amount, 301 to switch to multi-read
			startReg(8, registerSP, 301);
		}
		break;
	case 14:					// R,imm8
		var imm = inst&255;
		var rsd = (inst>>8)&7;
		var setReg = rsd;	// set -1 if just a compare instruction
		var result=0;
		var b = register[rsd];
		var flgs = 0;		// N Z C V
		iz = 'Rsd,#imm';
		var sw = (inst>>11)&31;
		switch(sw) {
		case 2:		// ADD
			iy = 'ADD';
			result = b + imm;
			if ((b&0x8000)==0 && ((result^b)&0x8000)!=0) flgs = 1;
			if ((result&0x10000)!=0) flgs |= 2;
			break;
		case 3:		// SUB
			iy = 'SUB';
			result = b - imm;
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if ((b&0x8000)!=0 && ((result^b)&0x8000)!=0) flgs = 1;
			if ((result&0x10000)==0) flgs |= 2;
			break;
		case 4:		// CMP
			iy = 'CMP';
			result = b - imm;
			// V is set if the operands have the different signs and the result is a different sign from rs
			// C is set if NO borrow
			if ((b&0x8000)!=0 &&
				((result^b)&0x8000)!=0) flgs = 1;
			if ((result&0x10000)==0) flgs |= 2;
			setReg = -1;			// no save of result
			break;
		case 5:		// MOV
			iy = 'MOV';
			result = imm;
			break;
		case 6:		// AND
			iy = 'AND';
			result = b & imm;
			break;
		case 7:		// ORR
			iy = 'ORR';
			result = b | imm;
			break;
		case 8:		// XOR
			iy = 'XOR';
			result = b ^ imm;
			break;
		case 10:		// MUL
			iy = 'MUL';
			result = b*imm;
			if (result>65535) flgs=2;		// unsigned overflow
			if ((result&0xFFFF)>32767) {
				var tmp = result/65536;
				if ((tmp&(tmp+1))!=0)flgs|=1;
			} else {
				if ((result&0xFFFF0000)!=0)flgs|=1;
			}
			break;
		case 9:		// DIV
			iy = 'DIV';
			if (imm == 0) flgs = 1;
			else {
				var s = 0;
				if ((b&0x8000)!=0) {b = 65536-b; s^=1;}
				result = Math.floor(b/imm);
				if (result>32767) flgs=1;
				if (s) result = 65536-result;
			}
			break;
		case 1:		// MOD
			iy = 'MOD';
			if (imm == 0) flgs = 1;
			else result = b%imm;
			break;
		default:		// this should not happen
			message("Instruction invalide au PC = "+(pCounter-1));
			return;		// require the user to hit RESET
			break;
		}
		result &= 0xFFFF;		// some instructions only set flags so dont save reg here
		if (sw == 5) {		// MOV does not use the ALU (so flgs not used)
			startIMM(rsd,result);
		} else {
			if (result == 0) flgs |= 4;
			if ((result&0x8000)!=0) flgs |= 8;
			startALU(rsd,12,imm,iy,result,setReg,flgs);
		}
		break;
	default:
		message("Instruction invalide au PC = "+(pCounter-1));
		return;
		break;
	}
	text("cu", iy, 352, 337, 12, "white");
	if (inst) message("Ex&eacutecution de l'instruction "+iy+' '+iz);	// not in input case
	stepTxt = "On a fini l'ex&eacutecution de l'instruction "+iy+' '+iz;
}

// The logic for the multipe registers PSH/POP - PSH starts using the ALU to decrement the PC (by n)
var maskBaseSP;	// the original SP value for POP and final for PSH
var maskCnt = 0;	// the number of registers we are writing (set to zero when finished for reset)
var maskRegs;		// array of register numbers we are reading or writing
var maskStage;		// where each register is in the process
var maskX = [];
var maskY = [];
// need to send the low address to memory and read or write a string of blobs 

// read logic (POP) - come initially after the red blob on the blue channel has reached the base SP address
// also return here as we step through the process
function stepMR()
{
	var done = 0;
	for (var i = 0; i < maskCnt; ++i) {
		switch (maskStage[i]) {
		case 0:			// first time for this address
			var x = 588+memX(maskBaseSP+i);
			var y = 72+Math.floor((maskBaseSP+i)/10)*15;
			if (i > 0) { // need to wait for the previous blob to move off
				if (y == maskY[i-1]) {	// same row
					if ((x-maskX[i-1]) < 80) {	// for i-1 first wait till moves y
						myTimeout1 = delay(valW, "stepMR");
						return;
					}
				} else {			// different rows
					if (maskX[i-1] > 588) {
						myTimeout1 = delay(valW, "stepMR");
						return;
					}
					if (y > 320) {		// moving up
						if ((y-maskY[i-1])<45) {
							myTimeout1 = delay(valW, "stepMR");
							return;
						}
					} else if (y < 210) {	// moving down
						if ((maskY[i-1]-y)<45) {
							myTimeout1 = delay(valW, "stepMR");
							return;
						}
					} else if (maskX[i-1] > 469) {	// close - wait till on B bus
						myTimeout1 = delay(valW, "stepMR");
						return;
					}
				}
			}
			// create a new blob for this memory contents
			var str = getMode(address[maskBaseSP+i]);
			x -= str.length*3-3;		// looks better if wide ones are a bit left
			image("blueM"+i, getBlueS(str.length), x, y, "DATA");
			text("blueN"+i, str, x+4, y+4, 14, "black");
			maskX[i] = x;
			maskY[i] = y;
			++maskStage[i];		// start its journey
			// move the red blob (blue channel) to the next address or cancel it
			if (i == (maskCnt-1)) {	// last one cancel
				remove("blue1");
				remove("blue2");
			} else {
				x = 588+memX(maskBaseSP+i+1);
				y = 72+Math.floor((maskBaseSP+i+1)/10)*15;
				move("blue1", x, y);
				text("blue2", maskBaseSP+i+1, x+4, y+4, 14, "black");
			}
			myTimeout1 = delay(valW, "stepMR");
			return; // every time we find one in state 0 we dont process more till it moves
		case 1:		// left to memory tens column
			var y = 72+Math.floor((maskBaseSP+i)/10)*15;
			if (maskMove(i,541,y)) ++maskStage[i];
			break;
		case 2:		// up or down to memory bus
			if (maskMove(i,541,264)) ++maskStage[i];
			break;
		case 3:		// left to main bus
			if (maskMove(i,469,264)) ++maskStage[i];
			break;
		case 4:		// move up B bus to register port
			if (maskMove(i,469,220)) ++maskStage[i];
			break;
		case 5:		// move to registers
			if (maskMove(i,350,220)) ++maskStage[i];
			break;
		case 6:		// move to the destination register
			var y = 230-16*maskRegs[i];
			if (maskMove(i,350,y)) {		// arrived
				if (maskRegs[i]<8)
					updateR(maskRegs[i],address[maskBaseSP+i]);
				else if (maskRegs[i] == 10) {
					updatePC(address[maskBaseSP+i]%400);
					updatePCmarker(address[maskBaseSP+i]%400);
				}
				remove("blueM"+i);
				remove("blueN"+i);
				++maskStage[i]
			}
			break;
		case 7:			// they may start in order but they dont finish in order
			++done;		// so we have to count how many have finished
			break;
		}
	}
	if (done == maskCnt) {
		myTimeout1 = false;  // terminate
		maskCnt = 0;		// so reset knows
		step2Busy = false;	// end of instruction
	} else myTimeout1 = delay(valW, "stepMR");
}


// read logic (PSH) - come here after the SP has been written back and we can read the registers
// also return here as we step through the process
// note the red blob on the blue channel containing the address is waiting on the memory link
// and we need to fake up writeDataOnB and redY in order to release it
function stepMW()
{
	var done = 0;
	for (var i = 0; i < maskCnt; ++i) {
		switch (maskStage[i]) {
		case 0:			// first time for this address
			if (i > 0) { // need to wait for the previous blob to move off
				if (maskX[i-1] < 469) {	// still in the regs area
					myTimeout1 = delay(valW, "stepMW");
					return;	// other regs must wait their turn
				}
			}
			// create a new blob for this register
			maskX[i] = 360;
			maskY[i] = 230-16*maskRegs[i];
			var val;			
			if (maskRegs[i]==9) val = String(registerLR);
			else if (maskRegs[i]<8) val = getMode(register[maskRegs[i]]);
			else alert("Ligne 4026 erreur de registre "+maskRegs[i]);			
			image("blueM"+i, getBlueS(val.length), x, y, "DATA");
			text("blueN"+i, val, x+4, y+4, 14, "black");
			++maskStage[i];		// start its journey
			myTimeout1 = delay(valW, "stepMW");
			return;	// other regs must wait their turn
			break;
		case 1:		// move from register to the link to bus B
			if (maskMove(i,360,154)) ++maskStage[i];
			break;
		case 2:		// move to bus B
			if (maskMove(i,469,154)) ++maskStage[i];
			break;
		case 3:		// move down bus B to memory link
			if (maskMove(i,469,190)) ++maskStage[i];			
			if (i == 0) {		// first reg done
				writeDataOnB = true;
				redY = maskY[0];	// releases the red address blob when get near
			}
			break;
		case 4:		// move along bus towards memory
			if (maskMove(i,541,190)) ++maskStage[i];
			break;
		case 5:		// move up or down tens column
			var y = 72+Math.floor((maskBaseSP+i)/10)*15;
			if (maskMove(i,541,y)) ++maskStage[i];
			break;
		case 6:		// move blob right to memory location
			var x = 588+memX(maskBaseSP+i);
			var y = 72+Math.floor((maskBaseSP+i)/10)*15;
			if (maskMove(i,x,y)) {		// we have arrived
				var addr = registerLR;
				if (maskRegs[i]<8) addr = register[maskRegs[i]];
				setAddress(maskBaseSP+i, addr);
				remove("blueM"+i);
				remove("blueN"+i);
				++maskStage[i];
				// move the red blob (blue channel) to the next address or cancel it
				if (i == (maskCnt-1) || (maskBaseSP+i)%10 == 9) {
					// last one or last one in row so cancel - if last in row will have
					remove("blue1");	// already done the start of the next row
					remove("blue2");
				} else if ((maskBaseSP+i)%10 >= maskBaseSP%10) {
					// same row so can move blob to right (same y)
					x = 588+memX(maskBaseSP+i+1);
					move("blue1", x, y);
					text("blue2", maskBaseSP+i+1, x+4, y+4, 14, "black");
				}
			}
			break;
		case 7:			// they may start in order but they dont always finish in order
			++done;		// so we have to count how many have finished
			break;
		}
	}
	if (done == maskCnt) {
		myTimeout1 = false;  // terminate
		maskCnt = 0;		// so reset knows
		step2Busy = false;	// end of instruction
	} else myTimeout1 = delay(valW, "stepMW");
}

function step2r()		// INPUT - move up
{
	if (moveBlue(306,520,"step2r")) step2s();
}
function step2s()		// INPUT - move right to B bus
{
	if (moveBlue(469,520,"step2s")) stepALUb8();	
}

function step2t()		// OUT instruction - blue blob has reached to B bus - move down to Output
{
	if (moveBlue(469,540,"step2t")) {
		// ALUdst is 400+device (to give mode), ALUres is the value to write
		outputNum(ALUres,ALUdst-400);
		remove("blue1");
		remove("blue2");
		myTimeout2 = false;
		step2Busy = false;
	}
}

function step2z()		// after delay just end instruction
{
	myTimeout1 = false;
	step2Busy = false;
}

function inputSubmit()
{
	var elePosn = document.getElementById("iForm");
	if (!elePosn) {
		alert("Mauvaise saisieSubmit call");
		return;
	}
	if (!waitingForInput) {
		alert("Mauvaise saisie - entr\351e non attendue");
		return;
	}	
	if (isNaN(elePosn.value) || elePosn.value=="") {
		alert("Mauvaise saisie - doit \352tre un nombre");
		return;
	}
	// isNaN lets through 0b and 0o that we don't support
	if (elePosn.value[0] == '0' && elePosn.value.length > 1) {
		if (elePosn.value[1] > '9' && (elePosn.value[1] != 'x' &&
			elePosn.value[1] != 'X')) {
			alert("Mauvaise saisie - decimal ou hexad\351cimal seulement");
			return;
		}
	}
	var value = parseInt(elePosn.value);
	if (value > 65635 || value < -32768) {
		alert("Mauvaise saisie - nombre trop petit ou trop grand");
		return;
	}
	remove("inpxx");
	text("input", '<div style="padding:0 0 0 2px;">'+value+'</div>', 269, 560, 14, "black");
	message("Valeur d'entr&eacutee charg&eacutee dans le registre "+registerToInput);
	if (inst) {							// fetch/execute case
		ALUdst = registerToInput;
		ALUres = value;			// setup for eventual use of stepALUb8()
		ALUop = '';
		blueX = 306;			// create a blue data blob for input value
		blueY = 560;
		var str = getMode(value);
		image("blue1",  getBlueS(str.length), blueX, blueY, "Entr&eacute");
		text("blue2", str, blueX+4, blueY+4, 14, "black");
		myTimeout2 = delay(valW, "step2r");
	} else {
		// INP no longer sets flags
		updateR(registerToInput, value);
	}
	waitingForInput = false;
}
