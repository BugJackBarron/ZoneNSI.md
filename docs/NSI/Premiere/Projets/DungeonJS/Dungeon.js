function draw(cx, cy){


const canvas = document.getElementById("dungeon");
const ctx = canvas.getContext("2d");
ctx.fillStyle = "black";
ctx.fillRect(0,0, 480, 480);
let img_bg = new Image();
img_bg.src ="Dungeon.png";
let mage = new Image() ;
mage.src = "npc_mage.png";
Promise.all(
[ctx.drawImage(img_bg,0,0, 480, 480)]).then(
[ctx.drawImage(mage,48*cx,48*cy, 48, 48)]);



}


window.addEventListener('load', ()=>{draw(5,9);});
