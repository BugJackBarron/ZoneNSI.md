
var simon_string = Array();
var possible = ["red", "yellow", "green", "blue"];

var notes = new Map();
notes.set("red", new Audio('piano-G3.wav'));
notes.set("blue", new Audio('piano-F3.wav'));
notes.set("yellow", new Audio('piano-E3.wav'));
notes.set("green", new Audio('piano-D3.wav'));

possible.forEach((col)=>{
    document.getElementById(col).addEventListener('click', ()=>{soundtest(col);});
});

document.getElementById("test").addEventListener('click', addSound);
document.getElementById("reset").addEventListener('click', resetSimon);
document.getElementById("play").addEventListener('click', ()=>{playSimon(0);});

function choose(choices) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
  }


function addSound(){
    simon_string.push(choose(possible));

}

function resetSimon(){
    simon_string = Array();
}

function playSimon(i){
    let note = simon_string[i];
    console.log(note);
    audio = notes.get(note);
    audio.play();
    audio.addEventListener('ended', ()=>{
        if (i<simon_string.length-1){
            console.log("stop "+i);
            playSimon(i+1);
        }
        else{
            resetSimon();
        }

    });
        
    

}


function fade_in(b) {
    var i = 0;
    b.style.opacity = 0.5;
    var k = window.setInterval(function() {
      if (i >= 5) {
        clearInterval(k);
      } else {
        b.style.opacity = 0.5+i / 10;
        i++;
      }
    }, 100);
}
  

function soundtest(c){
    let b = document.getElementById(c);
    let audio = notes.get(c);
    audio.play();
    fade_in(b);
    audio.addEventListener('ended', ()=>{
        b.style.opacity = 0.5;
        audio.currentTime = 0;
    });

}
    

    
    

