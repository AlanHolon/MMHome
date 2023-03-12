function getcookie(x) {
	let cookiearray = document.cookie.split(";");
	for (let i = 0; i < cookiearray.length; i++) {
		if (x == cookiearray[i].split("=")[0].trim()) {
		    return cookiearray[i].split("=")[1].trim();}
	}
}

/* Anima lista */

/*function setpos() {
    let da = new Date();
    let pos = (da.getTime() % 15000) / 20;
}*/
const mid = document.getElementById("mid").style;
/* let posvib = 0;
/* let pos = 0;
if (getcookie("pos") > 0) {pos = getcookie("pos");}*/
/* function vib(x) {
	if (x > 50) {return 0;} else {return Math.sin(x)*10/x;}
}*/
function frame() {
/*    if (pos == 750) {pos = 0;}
    pos++;*/
    const da = new Date();
    let pos = (da.getTime() % 30000) / 1000;
    mid.top = - pos*sq + 'vh';
};
/*function framevib() {
	if (posvib == 50) {clearInterval(idvib);}
	posvib++;
	mid.left = vib(posvib) + 3 + "vw";
}*/
const id = setInterval('frame()', 5);
/*const idvib = setInterval('framevib()', 20);*/

/* Anima podio */

const podlist = document.getElementById("pn1").innerHTML + document.getElementById("pn2").innerHTML + document.getElementById("pn3").innerHTML;
const cont = document.getElementById("cont").style;
const podio = document.getElementById("podio").style;
const p1 = document.getElementById("p1").style;
const p2 = document.getElementById("p2").style;
const p3 = document.getElementById("p3").style;
const pt1 = document.getElementById("pt1").style;
const pt2 = document.getElementById("pt2").style;
const pt3 = document.getElementById("pt3").style;
const pe1 = document.getElementById("pe1").style;
const pe2 = document.getElementById("pe2").style;
const pe3 = document.getElementById("pe3").style;
const pn1 = document.getElementById("pn1").style;
const pn2 = document.getElementById("pn2").style;
const pn3 = document.getElementById("pn3").style;
const pp1 = document.getElementById("pp1").style;
const pp2 = document.getElementById("pp2").style;
const pp3 = document.getElementById("pp3").style;
let ind = 0;
function framepod() {
    if (ind < 20) {
    ind++;
    podio.opacity = 5*ind + '%';
    pt1.opacity = 5*ind + '%';
    pt2.opacity = 5*ind + '%';
    pt3.opacity = 5*ind + '%';
    pe1.opacity = 5*ind + '%';
    pe2.opacity = 5*ind + '%';
    pe3.opacity = 5*ind + '%';
    pp1.opacity = 5*ind + '%';
    pp2.opacity = 5*ind + '%';
    pp3.opacity = 5*ind + '%';
    p1.opacity = 70 + 1.5*ind + '%';
    p2.opacity = 70 + 1.5*ind + '%';
    p3.opacity = 70 + 1.5*ind + '%';
    p1.width = 10 + ind + "%";
    p1.left = 70 - 1.75*ind + "%";
    p1.height = 7 + 1.65*ind + "vh";
    p1.bottom = 93 - 3.95*ind + "vh";
    p2.width = 10 + ind + "%";
    p2.left = 80 - 3.75*ind + "%";
    p2.height = 7 + 1.15*ind + "vh";
    p2.bottom = 93 - 3.95*ind + "vh";
    p3.width = 10 + ind + "%";
    p3.left = 90 - 1.25*ind + "%";
    p3.height = 7 + 0.65*ind + "vh";
    p3.bottom = 93 - 3.95*ind + "vh";
    pn1.width = 10 + ind + "%";
    pn1.left = 70 - 1.75*ind + "%";
    pn1.bottom = 93 - 0.55*ind + "vh";
    pn1.fontSize = 5 + 0.25*ind + "vh";
    pn2.width = 10 + ind + "%";
    pn2.left = 80 - 3.75*ind + "%";
    pn2.bottom = 93 - 1.05*ind + "vh";
    pn2.fontSize = 5 + 0.25*ind + "vh";
    pn3.width = 10 + ind + "%";
    pn3.left = 90 - 1.25*ind + "%";
    pn3.bottom = 93 - 1.55*ind + "vh";
    pn3.fontSize = 5 + 0.25*ind + "vh";}
    else if (ind < 400) {ind++; }
    else if (ind < 420){
    ind++;
    const din = ind - 400;
    podio.opacity = 100 - 5*din + '%';
    pt1.opacity = 100 - 5*din + '%';
    pt2.opacity = 100 - 5*din + '%';
    pt3.opacity = 100 - 5*din + '%';
    pe1.opacity = 100 - 5*din + '%';
    pe2.opacity = 100 - 5*din + '%';
    pe3.opacity = 100 - 5*din + '%';
    pp1.opacity = 100 - 5*din + '%';
    pp2.opacity = 100 - 5*din + '%';
    pp3.opacity = 100 - 5*din + '%';
    p1.opacity = 100 - 1.5*din + '%';
    p2.opacity = 100 - 1.5*din + '%';
    p3.opacity = 100 - 1.5*din + '%';
    p1.width = 30 - din + "%";
    p1.left = 35 + 1.75*din + "%";
    p1.height = 7 + 1.65*ind + "vh";
    p1.bottom = 14 + 3.95*din + "vh";
    p2.width = 30 - din + "%";
    p2.left = 5 + 3.75*din + "%";
    p2.height = 7 + 1.15*ind + "vh";
    p2.bottom = 14 + 3.95*din + "vh";
    p3.width = 30 - din + "%";
    p3.left = 65 + 1.25*din + "%";
    p3.height = 7 + 0.65*ind + "vh";
    p3.bottom = 14 + 3.95*din + "vh";
    pn1.width = 30 - din + "%";
    pn1.left = 35 + 1.75*din + "%";
    pn1.bottom = 83 + 0.55*din + "vh";
    pn1.fontSize = 10 - 0.3*din + "vh";
    pn2.width = 30 - din + "%";
    pn2.left = 5 + 3.75*din + "%";
    pn2.bottom = 73 + 1.05*din + "vh";
    pn2.fontSize = 10 - 0.3*din + "vh";
    pn3.width = 30 - din + "%";
    pn3.left = 65 + 1.25*din + "%";
    pn3.bottom = 63 + 1.55*din + "vh";
    pn3.fontSize = 10 - 0.3*din + "vh";}
    else {clearInterval(idpod);}
};
if ((podlist.trim() != getcookie("pod")) || (getcookie("tpod") > 1111)) {
    const idpod = setInterval('framepod()', 20); document.cookie = "pod=" + podlist; document.cookie = "tpod=1";}
    else { if (getcookie("tpod") > 0) {document.cookie = "tpod=" + getcookie("tpod") + 1; }
           else {document.cookie = "tpod=1";}	
    };

/* Anima tempo */

var n = 0;
const dfm = df.getTime();
const d = new Date();
let DT = new Date(dfm - d.getTime());
if (DT < 1200000 && DT > -1200000) {
    document.getElementById("mid").style.opacity = (DT - 600000)/6000 + "%";}
document.getElementById("oraf").style.width = 100 - ((DT.getHours()-1)*60 + DT.getMinutes())/1.2 + "%";
function twochars(x) {
	if (x.toString().length == 1) {return "0"+x;} else {return x;};
}
function pass(){
	const d = new Date();
	let DT = new Date(dfm - d.getTime());
	document.getElementById("ora").innerHTML = /*&#9200*/ "&#9203 " + (DT.getHours()-1) + ":" + twochars(DT.getMinutes()) + ":" + twochars(DT.getSeconds());
	n++;
	if (n == 20) {document.cookie = "pos=" + pos; window.location.reload()};
};
pass();
setInterval('pass()', 1000);
