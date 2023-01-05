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

function request_to_nasa(parameters){
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

// VOTRE CODE DOIT ETRE SITUE EN DESSOUS


