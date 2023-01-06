const MY_NASA_KEY = "RBGXm5wakyukgagSwBM7Vgb69SiYQMQwVxzlFpYK"

// La variable suivante contiendra la liste de tous les objets récupérés par la requête.
// c'est un objet de type Array, regardez sur le net pour en connaître les propriétés.

var imgArray = [];

// La variable suivante est un objet de type Map, c'est-à-dire comme un dictionnaire.
// Il doit contenir les paramètres de la requête comme, le nom du rover, le nom de la caméra,
// et la date terreinne ou le nombre de jours solaires.
// Pour ajouter une paire clé/valeur, il faut utiliser la méthode set, comme par exemple :
// request_parameters.set('rover', 'curiosity');
// request_parameters.set('sol', 50);
// request_parameters.set('earth_date', '2019-5-7')
// request_parameters.set('camera','NAVCAM');

request_parameters =  new Map()

// La fonction suivante est largmenet hors programme dans sa conception, mais
// son utilisation est simple. Après l'exécution des 4 lignes suivantes :

// request_parameters.set('rover','curiosity');
// request_parameters.set('sol',50);
// request_parameters.set('camera','NAVCAM');
// request_to_nasa(request_parameters);

// alors la variable imgArray contiendra le résultat de la requếté pour les photos de la NAVCAM 
// de curiosity au sol 50.

async function request_to_nasa(parameters){
    let url = "https://api.nasa.gov/mars-photos/api/v1/rovers/";
    if ((parameters.has('rover'))&&(['curiosity', 'opportunity', 'spirit'].includes(parameters.get('rover')))){
        url += parameters.get('rover')+"/photos";        
        if (parameters.size>1){
            url += "?";
            let parameters_accepted = ['camera', 'earth_date', 'sol'];
            parameters_accepted.forEach(item => {
                if (parameters.has(item)){
                    url += item+"="+parameters.get(item)+"&";
                }

            }
            );
        }
        url +="api_key="+MY_NASA_KEY;
        return fetch(url).then( (reponse) => {
                if(reponse.ok) {
                    return  reponse.json();                    
                } else {
                    throw new Error('Server response wasn\'t OK');
                }
            }).then(jsonobj => imgArray=jsonobj.photos.map(p => p));
    }
    else {
        throw new Error('Unable to find rover');
    }
}


async function main(request_parameters){
    let attente_div = document.getElementById("en_attendant");
    let contenu_div = document.getElementById("Contenu");
    
    attente_div.style.display = 'block';
    contenu_div.style.display = 'none';
    
    await request_to_nasa(request_parameters);
    
    attente_div.style.display = 'none';
    contenu_div.style.display = 'block';
    
    
    }

// VOTRE CODE DOIT ETRE SITUE EN DESSOUS

var actualImage = 0

let previous_button = document.getElementById('previous');
previous_button.addEventListener('click', previous_img);
let next_button = document.getElementById('next');
next_button.addEventListener('click', next_img);

let photo_date=document.getElementById('date');
photo_date.addEventListener('change', get_parameters)

function get_parameters(){

}

function previous_img(){
    if (actualImage > 0){ actualImage = actualImage -1;} 
    document.getElementById("photo").src =  imgArray[actualImage]['img_src'];
	document.getElementById("photo_info").innerText =  (parseInt(imgArray[actualImage]['id'])- parseInt(imgArray[0]['id']))+ " / " + (parseInt(imgArray[imgArray.length-1]['id'])-parseInt(imgArray[0]['id']));
}

function next_img(){
    if (actualImage <imgArray.length-1){ actualImage = actualImage +1;} 
    document.getElementById("curiosity").src =  imgArray[actualImage]['img_src'];
	document.getElementById("photo_info").innerText =  (parseInt(imgArray[actualImage]['id'])- parseInt(imgArray[0]['id']))+ " / " + (parseInt(imgArray[imgArray.length-1]['id'])-parseInt(imgArray[0]['id']));
}


request_parameters.set('rover','curiosity');
request_parameters.set('earth_date','2021-12-01');
request_parameters.set('camera','NAVCAM');
main(request_parameters);

let image = imgArray[actualImage];
document.getElementById("curiosity").src =  image;
document.getElementById("photo_info").innerText =  (parseInt(imgArray[actualImage]['id'])- parseInt(imgArray[0]['id']))+ " / " + (parseInt(imgArray[imgArray.length-1]['id'])-parseInt(imgArray[0]['id']));