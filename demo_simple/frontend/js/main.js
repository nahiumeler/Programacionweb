const SUPER_HEROES_URL = "http://localhost:5000/listar";
// Se define una constante SUPER_HEROES_URL que contiene la URL de la API local donde se listarán los superhéroes.

function fetchSuperHeroesAPI() {
// Se declara la función fetchSuperHeroesAPI, encargada de obtener datos de la API.

	axios.get(SUPER_HEROES_URL)
// Se hace una petición GET a la URL de SUPER_HEROES_URL usando axios, una biblioteca para realizar solicitudes HTTP.
	.then(response => {
		console.log(response.data);
		renderSuperHeroes(response.data);
	})
// then ejecuta el código si la petición GET es exitosa.
// console.log(response.data); muestra los datos obtenidos en la consola.
// renderSuperHeroes(response.data); llama a la función renderSuperHeroes para procesar y mostrar los datos.
	.catch(error => {
		console.log(error);
	})
}
// catch maneja cualquier error en la solicitud y lo muestra en la consola.


fetchSuperHeroesAPI();
// Llama a la función fetchSuperHeroesAPI para iniciar la solicitud de datos.


function renderSuperHeroes(superheroes) {
// Se declara la función renderSuperHeroes, que recibe como parámetro superHeroes, una lista de objetos de superhéroes.
	for (let i=0 ; i<superheroes.length ; i++) {
		addElementDOM(superheroes[i]);
	}

}
// Itera sobre cada superhéroe en superHeroes y llama a addElementDOM para añadir cada uno al DOM.


function addElementDOM(superheroes) {
// Se define la función addElementDOM, que recibe un objeto superHero y lo agrega visualmente al DOM.

	superheroesDiv = document.createElement("div");
	superheroesDiv.id = "my-element"
// Crea un div para contener la información del superhéroe y le asigna el ID "my-element".

	superheroesName = document.createElement("h3");
	superheroesName.innerHTML = superheroes["name"];
// Crea un elemento <h2>, y establece su contenido (innerHTML) con el nombre del superhéroe (superHero["name"]).

	superheroesSkill = document.createElement("p");
	superheroesSkill.innerHTML = superheroes["skill"];
// Crea un <p> para mostrar la habilidad del superhéroe y asigna el texto (innerHTML) de superHero["skill"].

	
	superheroesImage = document.createElement("img");
	superheroesImage.src = "img/" + superheroes["image"];
	superheroesImage.width = "300";
// Crea una imagen (<img>) y establece su fuente (src) en función del nombre de archivo en superHero["image"], además de un ancho de 300 píxeles.

	superheroesDiv.appendChild(superheroesName);
	superheroesDiv.appendChild(superheroesSkill);
	superheroesDiv.appendChild(superheroesImage);
// Añade el nombre, habilidad e imagen del superhéroe al contenedor superHeroDiv.


	superheroesContainer = document.getElementById("main-container");
	superheroesContainer.appendChild(superheroesDiv);

}
// Selecciona el elemento con ID main-container y añade el contenedor superHeroDiv con todos los datos del superhéroe.