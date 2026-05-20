const MY_NASA_KEY = "..."

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
        console.log(url);
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

// LES FONCTIONS CI-DESSUS NE DOIVENT PAS ETRE MODIFIEES !!!

// Les élements ci-dessous peuvent être modifiés.



// La fonction main ci-dessous permet plusieurs choses :
// 1) elle fait apparaître/disparaître deux divisions d'id "en_attendant" et "Contenu", selon l'état
// de la requête.
// 2) Elle peuple l'attribut "src" d'une balise image d'ID "photo" avec l'image de numéro "actualImage"
//, ainsi que le contenu d'une balise d'ID  "photo_info" avec une numérotation de type "3/5"


async function main(request_parameters){
    let attente_div = document.getElementById("en_attendant");
    let contenu_div = document.getElementById("Contenu");
    attente_div.style.display = 'block';
    contenu_div.style.display = 'none';
    
    await request_to_nasa(request_parameters).then(()=>{
        if (imgArray.length !=0){
            let image = imgArray[actualImage];
            
            document.getElementById("photo").src =  image['img_src'];
            document.getElementById("photo_info").innerText =  (parseInt(image['id'])- parseInt(imgArray[0]['id']))+ " / " + (parseInt(imgArray[imgArray.length-1]['id'])-parseInt(imgArray[imgArray.length-1]['id']));
        } else {
            document.getElementById("photo").src =  '';
            document.getElementById("photo_info").innerText =  'No data found !'
        }
        });
    attente_div.style.display = 'none';
    contenu_div.style.display = 'block';
        
    }



var actualImage = 0

let previous_button = document.getElementById('previous');
previous_button.addEventListener('click', previous_img);
let next_button = document.getElementById('next');
next_button.addEventListener('click', next_img);

let photo_date=document.getElementById('date');
photo_date.addEventListener('change', get_parameters);
let rover = document.getElementById('rover');
rover.addEventListener('click', get_parameters);
let camera = document.getElementById('camera');
camera.addEventListener('click', get_parameters);

function get_parameters(){
    request_parameters.set('rover',rover.value);
    request_parameters.set('earth_date',photo_date.value);
    request_parameters.set('camera',camera.value);
    main(request_parameters);

}

function previous_img(){
    if (actualImage > 0){ actualImage = actualImage -1;} 
    document.getElementById("photo").src =  imgArray[actualImage]['img_src'];
	document.getElementById("photo_info").innerText =  (parseInt(imgArray[actualImage]['id'])- parseInt(imgArray[0]['id']))+ " / " + (parseInt(imgArray[imgArray.length-1]['id'])-parseInt(imgArray[0]['id']));
}

function next_img(){
    if (actualImage <imgArray.length-1){ actualImage = actualImage +1;} 
    document.getElementById("photo").src =  imgArray[actualImage]['img_src'];
	document.getElementById("photo_info").innerText =  (parseInt(imgArray[actualImage]['id'])- parseInt(imgArray[0]['id']))+ " / " + (parseInt(imgArray[imgArray.length-1]['id'])-parseInt(imgArray[0]['id']));
}


get_parameters();