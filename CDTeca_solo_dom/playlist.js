/* playlist.js */

window.onload = init;

function init() {
	var button = document.getElementById("addButton");
	button.onclick = handleButtonClick;

}

function handleButtonClick(e) {
	var textInput = document.getElementById("songTextInput");
	var songName = textInput.value;
	//alert("Adding " + songName);

	if (songName == "") {
		alert("Por favor, ingrese una canción");
	}
	else {
		//alert("Adding " + songName);
		var li = document.createElement("li");
		li.innerHTML = songName;
		var ul = document.getElementById("playlist");
		ul.appendChild(li);

		
	}
}


