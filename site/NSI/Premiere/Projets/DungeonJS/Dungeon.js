/* Base de travail pour le projet Dungeon.js */
window.addEventListener('load',()=>{
const Carac = document.getElementById("Carac");

document.getElementById("force_output").textContent = 'Force : '+(10-Carac.value);
document.getElementById("pv_output").textContent = 'PV : '+(10+parseInt(Carac.value));

Carac.addEventListener("input", function () {
    document.getElementById("force_output").textContent = 'Force : '+(10-Carac.value);
    document.getElementById("pv_output").textContent = 'PV : '+(10+parseInt(Carac.value));
});

});






/* L'image de base a été crée avec Tiled, sur une base de 16 pixels
de côté par tuile, et sur une carte de 10x10 tuiles*/





const BASE_TILE = 16;
const XTILE = 10;
const YTILE = 10;

/* Calculs des constantes nécessaires pour l'utilisation du contexte */
const canvas = document.getElementById("dungeon");
const ctx = canvas.getContext("2d");
const CTX_WIDTH = canvas.width;
const CTX_HEIGHT = canvas.height;
const SCALEX = CTX_WIDTH/XTILE;
const SCALEY = CTX_HEIGHT/YTILE;
ctx.fillStyle = "black";
ctx.fillRect(0,0, CTX_WIDTH, CTX_HEIGHT);

/* Fonction de chargement d'une image, basée sur une promesse */
const loadImage = (url) => new Promise((resolve, reject) => {
    const img = new Image();
    img.addEventListener('load', () => resolve(img));
    img.addEventListener('error', (err) => reject(err));
    img.src = url;
  });

/* fonction traçant la carte et le personnage dans le canvas, avec le brouillard */
function draw(cx, cy){
ctx.reset();    
ctx.fillStyle = "black";
ctx.fillRect(0,0, CTX_WIDTH, CTX_HEIGHT);
loadImage("Dungeon.png").then(
img1 => {
    loadImage("npc_mage.png").then(
        img2 => {
            ctx.beginPath();
            ctx.arc(SCALEX*(cx+0.5), SCALEY*(cy+0.5), SCALEX*2, 0, 6.28, false); //draw the circle
            ctx.clip(); //call the clip method so the next render is clipped in last path
            ctx.stroke();
            ctx.closePath();
            
            
            ctx.drawImage(img1,0,0, CTX_WIDTH, CTX_HEIGHT);
            ctx.drawImage(img2,SCALEX*cx,SCALEY*cy, SCALEX, SCALEY);
            ctx.beginPath();
            ctx.strokeStyle = "orange";
            ctx.lineWidth = 4;
            ctx.arc(SCALEX*(cx+0.5), SCALEY*(cy+0.5), SCALEX*2-2, 0, 6.28, false); 
            ctx.stroke();
            ctx.closePath();

        }
    )
}
);
};

/* Création d'une variable contenant les caractéristiques du personnage */

var perso = {
    nom: "Rincevent",
    age: 32,
    sexe: "masculin",
    force : 10,
    pv : 10
};

/* récupération des données de bases du personnage */
function get_carac(){
    perso.nom = document.getElementById("perso_nom").value;
    perso.force = 10-parseInt(document.getElementById("Carac").value);
    perso.pv = 10+parseInt(document.getElementById("Carac").value);
    
    document.getElementById("choix_perso").style.display = 'none';
    document.getElementById("main").style.display = 'flex';
    levels = generate_levels();
    set_level(0);
    
}

/* le son quand le perso meurt */
var audio = new Audio('VOXScrm_Cri wilhelm (ID 0477)_LS.wav');

/* Création dune variable contenant les différents éléments du jeu */

let levels = new Map();

/* Niveau pour la mort */
function generate_levels(){
    levels.set(666,{
        x : -10,
        y : -10,
        action : [['sound',0],['reset',10]],
        monster : null,
        text : ['Tu es MORT !','Ben oui, tu t\'attendais à quoi ?'],
        choices : [["Recommencer", 0]]

        });

    levels.set(0,{
        x : 5,
        y : 9,
        action : null,
        monster : null,
        text : ['Bienvenue dans le donjon de la mort '+perso.nom+'. Tu as une force de '+perso.force+' et '+perso.pv+' points de vie.',
        " Devant toi se trouve un couloir sombre, dont tu ne vois pas la fin.",
        " Que veux-tu faire ?"],
        choices : [["Avancer", 1],
                ["Reculer", 666]]
        });

    levels.set(1,{
        x : 5,
        y : 6,
        action : null,
        monster : null,
        text : ['Après quelques mètres de progression, devant toi se trouve une porte, dont proviennent des bruits effrayants.',
        " A gauche, le couloir est sombre mais tu sembles percevoir une lumière venant du fond du couloir.",
        " A droite, le couloir est sombre, mais tu entends le bruit d'un écoulement, comme si tu entendais une fontaine.",
        " Que veux tu faire ?"],
        choices : [["Aller à gauche", 2],
                    ["Aller à droite", 3],
                ["Ouvrir la porte", 4],
            ["Reculer", 0]]
        });

    levels.set(2,{
        x : 3,
        y : 6,
        action : null,
        monster : null,
        text : ['Une torche est allumée, mais tu ne vois pas le fond du couloir.',
        " Il y a devant toi un trou, dont tu ne vois pas le fond.",
        " Que veux tu faire ?"],
        choices : [["Sauter dans le trou", 666],
                    ["Sauter au dessus du trou", 9],
                    ["Reculer", 1]]
        });

    levels.set(3,{
        x : 7,
        y : 6,
        action : null,
        monster : null,
        text : ['Le couloir se termine par un cul de sac, mais devant toi coule une substance verdâtre provenant d\'une fontaine.',
        " Que veux tu faire ?"],
        choices : [["Boire le liquide", 5],
                    ["Reculer", 1]]
        });

    levels.set(4,{
        x : 5,
        y : 4,
        action : null,
        monster : null,
        text : ['Tu rentres dans la pièce dont la puanteur te fais suffoquer. Un grognement bestial vient de la zone non éclairée'],
        choices : [["Combattre", 8],
                    ["Fuir", 1]]
    });


    levels.set(5,{
        x : 7,
        y : 6,
        action : [['gain_force', 20]],
        monster : null,
        text : ['Tu te sens plus fort ! ',
        " Que veux tu faire ?"],
        choices : [["Boire à nouveau", 6],
                    ["Reculer", 1]]


    });

    levels.set(6,{
        x : 7,
        y : 6,
        action : [['gain_force', 20],
                    ['perte_pv', 5]],
        monster : null,
        text : ['Tu te sens plus vraiment plus fort, mais tu saigne du nez !',
        " Que veux tu faire ?"],
        choices : [["Boire à nouveau", 666],
                    ["Reculer", 1]]
    });
    levels.set(8,{
        x : 5,
        y : 3,
        action : null,
        monster : null,
        text : final_boss(),
        choices : [["Frapper Cthulhu", 666],
                    ["Esquiver Cthlhu", 666],
                ['Fuir Cthlhu', 666]]
    });
    levels.set(9,{
        x : 1,
        y : 6,
        action : [['perte_pv',2]],
        monster : null,
        text : ['Après un saut impeccable, ta réception laisse toutefois à désirer et tu te blesse légèrement au genou.',
    'Malheureusement, c\'est un cul-de-sac !',
    'Que veux-tu faire ?'],
        choices : [["Sauter au-dessus du trou", 10],
                    ["Sauter dans le trou", 666],
                ['Essayer de creuser le mur', 11]]
    });
    levels.set(11,{
        x : 1,
        y : 6,
        action : [['perte_pv',2], ['perte_force', 5]],
        monster : null,
        text : ['Tu t\'épuises contre un mur en pierre. Tes mains sont en sang, et tu n\'as pas avancé.',
           'Que veux-tu faire ?'],
        choices : [["Sauter au-dessus du trou", 10],
                    ["Sauter dans le trou", 666],
                ['Continuer à creuser le mur', 11]]
    });
    levels.set(10,{
        x : 3,
        y : 6,
        action : [['perte_pv',3]],
        monster : null,
        text : ['Après un saut moins impeccable dû à ta blessure au genou, tu te ramasses à l\'aterrissage.',
       'Que veux-tu faire ?'],
        choices : [["Re-Sauter au-dessus du trou", 9],
                    ["Sauter dans le trou", 666],
                ['Retourner devant la porte', 11]]
    });

    return levels;
}


/* Utilisation des niveaux */

function set_level(n){
    if (n==8){
        levels = generate_levels();
    }    
    
    if (levels.has(n)){
        
        level = levels.get(n);
        if (level.action != null){
            do_things(level.action);
        }
        if ((n!=666) && ((perso.pv<=0)||(perso.force<=0))){
            set_level(666);
        }
        draw(level.x,level.y);
        fill_text(level.text);
        fill_choices(level.choices);
        document.getElementById("nom").innerText = perso.nom;
        document.getElementById("force").innerText = perso.force;
        document.getElementById("pv").innerText = perso.pv;
    }
    else{
        document.getElementById("text").innerHTML = "<p>Unknown level</p>";
        document.getElementById("choices").replaceChildren();
        
    }
    
}


function fill_text(texts){

    let n = texts.length;
    let txt_zone = document.getElementById("text");
    txt_zone.replaceChildren();

    for(var i=0; i<n; i=i+1){
        let new_p = txt_zone.appendChild(document.createElement("p"));
        new_p.innerText = texts[i];
    }
};

function fill_choices(choices){
    let n = choices.length;
    let choices_zone = document.getElementById("choices");
    choices_zone.replaceChildren();
    for(var i=0; i<n; i=i+1){
        let new_p = choices_zone.appendChild(document.createElement("p"));
        let new_b = new_p.appendChild(document.createElement("button"));
        new_b.innerText = choices[i][0];
        new_b.id="tolevel_"+choices[i][1];
        let target=choices[i][1];
        
        new_b.onclick = () => {

            set_level(target);};
    }

};

function do_things(todo){

    for (var i =0; i<todo.length; i=i+1){
        switch (todo[i][0]){
            case "perte_pv":
                perso.pv -= todo[i][1];
                break;
            case "gain_pv" :
                perso.pv += todo[i][1];
                break;
            case "perte_force" :
                perso.force -= todo[i][1];
                break;
            case "gain_force" :
                perso.force += todo[i][1];
                break;
            case 'sound' :
                audio.play()
                break;
            case 'reset' :
                
                reset();
                break;
        }
        
        
    }

}


function final_boss(){
    if (perso.force<50){
        return ['Tu approches terrifié, la bête devant toi bouge ses tentacules multi-millénaires !',
    'Tu la sens s\'insinuer dans ton esprit : «Qui ose déranger le grand Cthulhu !»',
    'Que fais-tu ?']   
    }else{
        return ['Tu approches, confiant. La bête devant toi bouge ses tentacules multi-millénaires !',
    'Tu la sens s\'insinuer dans ton esprit : «Qui ose déranger le grand Cthlhu !»',
    'Tu te sens si fort que tu réponds «Moi, '+perso.nom+' !',
    'Que fais-tu ?']
    }
}

function reset(){
    document.getElementById("choix_perso").style.display = 'block';
    document.getElementById("main").style.display = 'none';

}