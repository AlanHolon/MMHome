const dfm = df.getTime();
const d = new Date();
let DT = new Date(dfm - d.getTime() - 7200000);
let orafin = document.getElementById("orafin");
let orafinp = document.getElementById("orafinp");
let ora = document.getElementById("ora");
let orap = document.getElementById("orap");
function twochars(x) {
	if (x.toString().length == 1) {return "0"+x;} else {return x;};
}
function nochars(x) {
	if (x == 0) {return "";} else {return x+":";};
}
function pass(){
	const d = new Date();
	let DT = new Date(dfm - d.getTime() - 7200000);
	document.getElementById("orafin").innerHTML = nochars(DT.getMinutes()) + twochars(DT.getSeconds());
	document.getElementById("ora").innerHTML = "&#9203 " + nochars(DT.getMinutes()) + twochars(DT.getSeconds());
	if (DT < 60000) {orafin.style.fontSize = (70 - (DT.getMilliseconds())*0.7/10) + "vh";}
	if (DT < 0) {orafin.style.fontSize = 60+"vh"; document.getElementById("orafin").innerHTML = "&#127937VIA!";}
    if (DT < - 60000) {clearInterval(id); window.location.reload();}
    if (DT < 60000 && DT > 59000) {orap.style.opacity = DT.getMilliseconds()/10 + "%"; ora.style.opacity = DT.getMilliseconds()/10 + "%"; orafin.style.opacity = (100 - DT.getMilliseconds()/10)+"%"; orafinp.style.opacity = (100 - DT.getMilliseconds()/10) + "%";}
}
if (DT < 60000) {orap.style.opacity = 0; ora.style.opacity = 0; orafin.style.opacity = 100+"%"; orafinp.style.opacity = 100+"%";}
pass();
let id = setInterval('pass()', 10);
