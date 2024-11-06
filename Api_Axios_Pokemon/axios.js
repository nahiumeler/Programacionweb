 let imagen = '';
 axios.get('https://pokeapi.co/api/v2/pokemon/ditto')
    .then((respuesta)=> {
        console.log(respuesta.data.abilities[0].ability.name);
        console.log(respuesta.data.name);
        console.log(respuesta.data.sprites.front_default);

        imagen = `<img class="poster" src="${respuesta.data.sprites.front_default}"></img>`

        document.getElementById('contenedor').innerHTML = imagen;
    })
    .catch((error)=>{
        console.log(error)
    });

//Forma alternativa
/* const obtenerPeliculas = async () =>{
    try{    
        const respuesta = await axios.get('https://api.themoviedb.org/3/movie/popular', {
            params: {
                api_key: '192e0b9821564f26f52949758ea3c473',
                language: 'es-MX'
            }
        });
        
        console.log(respuesta);
    }catch(error){
        console.log(error);
    }
} */



