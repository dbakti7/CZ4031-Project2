const OPERATORS = {
	"<=": "is less than or equal to",
	">=": "is larger than or equal to",
	">": "is larger than",
	"<": "is less than",
	"=": "is equal to",
	"-": "minus",
	"\\+": "plus"
};

var ws = new WebSocket("ws://localhost:8888/websocket");

ws.onopen = function() {
	// speak("Hello");
}

ws.onmessage = function(e) {
	console.log(e.data)
	var result = formatResult(e.data);
	speak(result);
	result = formatWhitespace(result);

	document.getElementById("result").innerHTML = result
}

function handleSubmit(e) {
	ws.send(JSON.stringify(e));
}

function speak(text) {
	speech = window.speechSynthesis;

	if (!text) {
			text = document.getElementById("result").innerHTML
	}

	const msg = new SpeechSynthesisUtterance(text);
	window.speechSynthesis.speak(msg);
}

function formatResult(text) {
	Object.keys(OPERATORS).forEach(key => {
		text = text.replace(new RegExp(key, 'g'), OPERATORS[key]);
	})

	return text;
}

function formatWhitespace(text) {
	return text.replace(new RegExp('\\n', 'g'), '<br>');
}
