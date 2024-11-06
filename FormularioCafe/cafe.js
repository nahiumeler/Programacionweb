window.onload = init; //permite que se cree la pagina y el formulario sin ningun dato  y despues llama a las funciones.

function init() {
	var button = document.getElementById("addButton"); //pido addbutton y lo guardo en button.onclick
	button.onclick = handleButtonClick; // y hace la funcion 

}

function handleButtonClick(e) { 
	var textInput1 = document.getElementById("cafeTextInput");
    var textInput2 = document.getElementById("snackTextInput"); //traeme la cancion 
	var BebidaElegida = textInput1.value;
    var SnackElegido = textInput2.value; // y agrego el contenido(string) para ponerlo dentro de la lista
	//alert("Adding " + songName);

	if (BebidaElegida == "" && SnackElegido == " ") { //si el nonmbre de la cancion esta vacio
		alert("Por favor, ingrese su orden"); //sale el alert y te pide que agregues una cancion
	}
	else { //si el nombre esta completo
		//alert("Adding " + songName);
		var li = document.createElement("li"); 
		li.innerHTML = BebidaElegida + " " + SnackElegido; // cambia el contenido 
		var ul = document.getElementById("order"); 
		ul.appendChild(li); // agrego el elemento a la lista ul de la playlist 
		// appendChild inserta un nuevo nodo dentro de la estructura DOM de un documento
		
	}
}

