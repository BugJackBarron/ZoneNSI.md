let carroussel = document.getElementById('carroussel');
carroussel.style.display="flex";
carroussel.style.flexWrap = "wrap";

DocumentFragment.getElementByClass

function addImage(source, destination){
    this.image = new Image();
    this.image.src = source;

    this.dest = destination;
    let iw = this.image.width;
    let ih = this.image.height;
    
    let link = carroussel.appendChild(document.createElement('a'));
    let img = link.appendChild(document.createElement('img'));
    img.src=this.image.src;
    img.width = 200;
    img.height = ih*200/iw;
    link.href = this.dest;
    link.target="_blank";
    link.style.display = "block";
    link.style.width = "2OOpx;"
    link.style.margin="auto";
    img.addEventListener('mouseover', ()=>{
        img.style.border="solid 10px ";
        img.style.borderColor ="#546d78"
    }, false);
    img.addEventListener('mouseout', ()=>{
        img.style.border="none"
    }, false);
}
//Python
addImage("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png","https://www.python.org/")
//Thonny
addImage("https://user-images.githubusercontent.com/1057839/104211453-61c0f400-5434-11eb-8f52-c61c616578da.png","https://thonny.org/");
//Capytale
addImage("https://capytale2.ac-paris.fr/logo.svg","");
//Pygame
addImage("https://www.pygame.org/docs/_images/pygame_logo.png","");
//HTML5
addImage("https://www.w3.org/html/logo/img/html5-display.png","");
//CSS3
addImage("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/363px-CSS3_logo_and_wordmark.svg.png","");
//Javascript
addImage("https://w7.pngwing.com/pngs/503/848/png-transparent-javascript-computer-icons-software-developer-cascading-style-sheets-javascript-logo-angle-text-rectangle-thumbnail.png","");
//Notepad++
addImage("https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Notepad%2B%2B_Logo.svg/277px-Notepad%2B%2B_Logo.svg.png","");
