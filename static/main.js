var ws = new WebSocket("ws://localhost:8888/websocket");

ws.onopen = function() {
	console.log("Hello! Websocket Opened");
}

ws.onmessage = function(e) {
	console.log(e.data);
	document.getElementById("result").innerHTML = e.data
}

function handleSubmit(e) {
	ws.send(JSON.stringify(e));
}

function speak() {
	const type = 3;
	const data = document.getElementById("result").innerHTML;
	console.log(data);
	ws.send(JSON.stringify({type, data}));
}
