let carroussel = document.getElementById('carroussel');
carroussel.style.display="flex";
carroussel.style.flexWrap = "wrap";
carroussel.style.marginBottom ="20px";

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
    if (iw>=ih){
        img.width = 200;
        img.height = ih*200/iw;
    }else{
        img.height = 200;
        img.width = iw*200/ih;
    } 
    link.href = this.dest;
    link.target="_blank";
    link.style.display = "block";
    link.style.width = "2OOpx;"
    link.style.margin="auto";
    img.addEventListener('mouseover', ()=>{
        img.style.border="solid 10px ";
        img.style.borderRadius = "20px";
        img.style.borderColor ="#546d78";
        img.style.transition = "border-width 0.3s ease-in-out 0s"
    }, false);
    img.addEventListener('mouseout', ()=>{
        img.style.border="solid 0px";
    }, false);
}
//Python
addImage("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png","https://www.python.org/")
//Thonny
addImage("https://user-images.githubusercontent.com/1057839/104211453-61c0f400-5434-11eb-8f52-c61c616578da.png","https://thonny.org/");
//Capytale
addImage("https://capytale2.ac-paris.fr/logo.svg","https://capytale2.ac-paris.fr/web/c-auth/list");
//Pygame
addImage("https://www.pygame.org/docs/_images/pygame_logo.png","https://www.pygame.org/news");
//HTML5
addImage("https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/512px-HTML5_logo_and_wordmark.svg.png?20170517184425","https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/HTML_basics");
//CSS3
addImage("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/363px-CSS3_logo_and_wordmark.svg.png","https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/CSS_basics");
//Javascript
addImage("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/600px-JavaScript-logo.png?20120221235433","https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/JavaScript_basics");
//Notepad++
addImage("https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Notepad%2B%2B_Logo.svg/277px-Notepad%2B%2B_Logo.svg.png","https://notepad-plus-plus.org/");
//SQL
addImage("https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Sql_data_base_with_logo.png/800px-Sql_data_base_with_logo.png?20210130181641","https://sql.sh/");
//DBBrowwerLite
addImage("https://linuxiac.b-cdn.net/wp-content/uploads/2021/08/sqlite-db-browser.png","https://sqlitebrowser.org/");
//Flask
addImage("https://flask.palletsprojects.com/en/2.3.x/_images/flask-horizontal.png","https://flask.palletsprojects.com/en/2.3.x/");
//Filius
addImage("https://www.lernsoftware-filius.de/.cm4all/uproc.php/0/.filius128.png/picture-1200?_=17db3de0a08","https://www.lernsoftware-filius.de/Herunterladen");


