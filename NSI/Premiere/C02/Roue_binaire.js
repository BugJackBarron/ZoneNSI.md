var nb=0;
var timeout;
var speed=100;  
function majDec(){
$('#dec_unites').html(nb%10);
$('#dec_dizaines').html(((nb-nb%10)/10)%10);
$('#dec_centaines').html((nb-nb%100)/100);}
function majBin(){
var nbin=nb.toString(2).padStart(8, '0');
for (var i=0;i<8;i++){
$('#bin_'+i).html(nbin[7-i]);}}
function majHexa(){var nhexa=nb.toString(16).padStart(2, '0').toUpperCase();
for (var i=0;i<2;i++){$('#hexa_'+i).html(nhexa[1-i]);}}
$('.roll').mouseup(function () { clearInterval(timeout);});
$('.roll').mouseout(function () { clearInterval(timeout);});
$('#rollup').mousedown(function(){
timeout = setInterval(function () {
if (nb <255) {
nb+=1;}else {nb=0;}
majDec();
majBin();
majHexa();},speed);});
$('#rolldown').mousedown(function(){
timeout = setInterval(function () {
if (nb >0) {
nb-=1;}else {nb=255;}
majDec();
majBin();
majHexa();},speed);});$('#setSpeed').change(function(){
speed = 300-document.getElementById("setSpeed").value;});
$("#reset").click(function(){
speed = 100 ;
nb=0;
majDec();
majBin();
majHexa();
document.getElementById("setSpeed").value=speed;});
$('#bintxt').click(function(){
if ($('#roue_bin').css('display')=='flex'){
$('#roue_bin').css('display','none');}else{
$('#roue_bin').css('display','flex');}});
$('#hexatxt').click(function(){
if ($('#roue_hexa').css('display')=='flex'){
$('#roue_hexa').css('display','none');}else{
$('#roue_hexa').css('display','flex');}});