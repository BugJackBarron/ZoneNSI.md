let canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
thonny =  new Image() ;
thonny.src = "https://user-images.githubusercontent.com/1057839/104211453-61c0f400-5434-11eb-8f52-c61c616578da.png";
thonny.onload = function (){
    ctx.drawImage(thonny, 0,0);
}
function drawCan(){

}

