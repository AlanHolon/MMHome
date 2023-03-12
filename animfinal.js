const dfm = df.getTime();
const d = new Date();
let DT = new Date(dfm - d.getTime());
let ora = document.getElementById("oraf").style;
let orafin = document.getElementById("orafin");
ora.width = 100 - (DT.getMinutes()*60 + DT.getSeconds())/6 + "%";
function twochars(x) {
	if (x.toString().length == 1) {return "0"+x;} else {return x;};
}
function nochars(x) {
	if (x == 0) {return "";} else {return x+":";};
}
function pass(){
	const d = new Date();
	let DT = new Date(dfm - d.getTime());
	document.getElementById("orafin").innerHTML =  nochars(DT.getMinutes()) + twochars(DT.getSeconds());
    ora.width = 100 - (DT.getMinutes()*60 + DT.getSeconds())/6 + "%";
	if (DT < 60000) {orafin.style.fontSize = (70 - (DT.getMilliseconds())*0.7/10) + "vh";}
	if (DT < 0) {orafin.style.fontSize = 60+"vh"; document.getElementById("orafin").innerHTML = "FINE"; clearInterval(id);}
};
pass();
let id = setInterval('pass()', 10);
