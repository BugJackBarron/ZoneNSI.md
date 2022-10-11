const MY_NASA_KEY = "RBGXm5wakyukgagSwBM7Vgb69SiYQMQwVxzlFpYK"
var imgArray = []
var actualImage = 0
let titre = document.getElementById('titre');

let previous_button = document.getElementById('previous');
previous_button.addEventListener('click', previous_img);
let next_button = document.getElementById('next');
next_button.addEventListener('click', next_img);
document.addEventListener("DOMContentLoaded", function (){my_rover_curiosity_request("2020-01-01");});
let photo_date=document.getElementById('date');
photo_date.addEventListener('change', newrequest)



function previous_img(){
    if (actualImage > 0){ actualImage = actualImage -1;} 
    document.getElementById("curiosity").src =  imgArray[actualImage]['img_src'];
	document.getElementById("photo_info").innerText =  (parseInt(imgArray[actualImage]['id'])- parseInt(imgArray[0]['id']))+ " / " + (parseInt(imgArray[imgArray.length-1]['id'])-parseInt(imgArray[0]['id']));
}

function next_img(){
    if (actualImage <imgArray.length-1){ actualImage = actualImage +1;} 
    document.getElementById("curiosity").src =  imgArray[actualImage]['img_src'];
	document.getElementById("photo_info").innerText =  (parseInt(imgArray[actualImage]['id'])- parseInt(imgArray[0]['id']))+ " / " + (parseInt(imgArray[imgArray.length-1]['id'])-parseInt(imgArray[0]['id']));
}


function my_rover_curiosity_request(date) {
    fetch("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date="+date+"&camera=NAVCAM&api_key="+MY_NASA_KEY)
        .then(res => res.json())
        .then(
            function testrover(jsonobj){
                 
                var image = jsonobj['photos'][0]['img_src'];
                imgArray = jsonobj.photos.map(p => p);

                console.log(imgArray);
                document.getElementById("curiosity").src =  image;
				document.getElementById("photo_info").innerText =  (parseInt(imgArray[actualImage]['id'])- parseInt(imgArray[0]['id']))+ " / " + (parseInt(imgArray[imgArray.length-1]['id'])-parseInt(imgArray[0]['id']));
                
            }
        )
}

function newrequest(){
    date = photo_date.value;
	actualImage = 0 ;
    my_rover_curiosity_request(date);

}