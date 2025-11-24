let canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');


window.addEventListener('resize', resizeCanvas, false);

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    // Redraw everything after resizing the window
    drawStuff(); 
  }

resizeCanvas();

function hovere(elem){
    hovere.style.border = 'LightGray';
  }

function drawStuff(){

let cvw = canvas.width;
thonny =  new Image() ;
thonny.src = "https://user-images.githubusercontent.com/1057839/104211453-61c0f400-5434-11eb-8f52-c61c616578da.png";

notepadpp = new Image();
notepadpp.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Notepad%2B%2B_Logo.svg/277px-Notepad%2B%2B_Logo.svg.png"

capytale = new Image();
capytale.src = "https://capytale2.ac-paris.fr/logo.svg";


thonny.onload = function (){
    ctx.drawImage(thonny, 0, 0, cvw/5, thonny.height/thonny.width*cvw/5);
}
notepadpp.onload = function(){
    ctx.drawImage(notepadpp, cvw/5,0, cvw/5, notepadpp.height/notepadpp.width*cvw/5);

}
capytale.onload = function(){
    ctx.drawImage(capytale, 2*cvw/5,0, cvw/5, capytale.height/capytale.width*cvw/5);

}
thonny.addEventListener('hover', () => hovere(thonny), false);
}

function drawCan(){

}

