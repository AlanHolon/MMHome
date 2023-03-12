var n = 0;
const df = new Date(2022, 10, 27, 13, 0, 0, 0);
const dfm = df.getTime();
function pass(){
	const d = new Date();
	let DT = new Date(dfm - d.getTime());
	document.getElementById("ora").innerHTML = "&#9200 &#9203 " + DT.getHours() + ":" + DT.getMinutes() + ":" + DT.getSeconds();
	n++;
	if (n == 60) {window.location.reload()};
};
pass();
setInterval('pass()', 1000);
