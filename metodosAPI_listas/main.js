document.addEventListener("DOMContentLoaded", function() {   //Al meter todo en DOMcontentLoaded, podemos evitar errores como querer acceder a un elemento pero el script se carga antes de que esos elementos existan en el HTML
    const INGREDIENTES = "http://localhost:5000/listar";
    const AGREGAR_INGREDIENTE = "http://localhost:5000/agregar";
    const ELIMINAR_INGREDIENTE= "http://localhost:5000/eliminar";
    const EDITAR_INGREDIENTE= "http://localhost:5000/editar";


    // OBTENER LOS ELEMENTOS DE LA API Y PONERLOS EN EL HTML
    function fetchingredientesAPI() {
        axios.get(INGREDIENTES)
        .then(response => {
            console.log(response.data);
            recorrer_ingredientes(response.data);
        })
        .catch(error => {
            console.log("Error al obtener ingredientes:", error);
        });
    }

    fetchingredientesAPI();

    function recorrer_ingredientes(ingredientes) {
        const container = document.getElementById("main-container");
        container.innerHTML = "";  //esto habria que hacerlo para que se agregue solo el ingrediente que escribiste. Si no lo pongo se agrega la lista duplicada
        for (let i=0 ; i<ingredientes.length ; i++) {
            addElementDOM(ingredientes[i]);
        }
    }
    

    function addElementDOM(ingrediente) {
        let div_ing=document.createElement("div");
        div_ing.classList.add("contenedor");


        ing = document.createElement("h2");
        ing.innerHTML = ingrediente.ingrediente;

        cantidad=document.createElement("p");
        cantidad.innerHTML = ingrediente.cantidad;

        marca=document.createElement("p");
        marca.innerHTML = ingrediente.marca;
    
        div_ing.append(ing,cantidad,marca);
    
        container = document.getElementById("main-container");
        container.appendChild(div_ing);
    
    }

    //AGREGAR UN ELEMENTO A LA LISTA Y MOSTRARLO EN EL HTML
    function agregarIngrediente() {
        const ingredienteInput = document.getElementById("agregar_nombre");
        const ingrediente = ingredienteInput.value;
        const cantidad_input=document.getElementById("agregar_cantidad");
        const cantidad=cantidad_input.value
        const marca_input=document.getElementById("agregar_marca")
        const marca=marca_input.value

        if (ingrediente.trim() !== "" && cantidad.trim() !== "" && marca.trim() !== "" ) {
            axios.post(AGREGAR_INGREDIENTE, { ingrediente: ingrediente, cantidad:cantidad,marca:marca})
            .then(response => {
                console.log(response.data.mensaje);
                ingredienteInput.value = ""; // Limpiar el campo de entrada
                cantidad_input.value="";
                marca_input.value="";

                fetchingredientesAPI(); // Actualizar lista de ingredientes
            })
            .catch(error => {
                console.log("Error al agregar ingrediente:", error);
            });
        } else {
            alert("Por favor, ingresa un ingrediente.");
        }
    }

    // Añadir evento de clic al botón para agregar ingrediente
    document.getElementById("boton_agregar").addEventListener("click", agregarIngrediente);


    //ELIMINAR UN ELEMENTO
    function eliminar_Ingrediente() {
        const ingrediente_eliminado_Input = document.getElementById("borrar");
        const ingrediente_eliminado = ingrediente_eliminado_Input.value;

        if (ingrediente_eliminado.trim() !== "") {
            axios.delete(ELIMINAR_INGREDIENTE, {data: { ingrediente_a_eliminar: ingrediente_eliminado }})
            .then(response => {
                console.log(response.data.mensaje);
                ingrediente_eliminado_Input.value = ""; // Limpiar el campo de entrada
                fetchingredientesAPI(); // Actualizar lista de ingredientes
            })
            .catch(error => {
                console.log("Error al agregar ingrediente:", error);
            });
        } else {
            alert("Por favor, ingresa un ingrediente.");
        }
    }

    // Añadir evento de clic al botón para agregar ingrediente
    document.getElementById("boton_borrar").addEventListener("click", eliminar_Ingrediente);



    //EDITAR UN ELEMENTO
    function editar_ingredientes(){
        const ingrediente_viejo_input = document.getElementById("elemento_editar");
        const ingrediente_viejo = ingrediente_viejo_input.value;

        const rubro_input = document.getElementById("rubro");
        const rubro = rubro_input.value;
        

        const ingrediente_nuevo_Input = document.getElementById("actualizado_editar");
        const ingrediente_nuevo = ingrediente_nuevo_Input.value;



        if (ingrediente_viejo.trim() !== "" && ingrediente_nuevo.trim() !== "") {
            axios.put(EDITAR_INGREDIENTE, { ingrediente_a_editar: ingrediente_viejo , ingrediente_actualizado:ingrediente_nuevo,rubro:rubro})
            .then(response => {
                console.log(response.data.mensaje);
                ingrediente_viejo_input.value = ""; // Limpiar el campo de entrada
                ingrediente_nuevo_Input.value = "";
                rubro_input.value="";


                fetchingredientesAPI(); // Actualizar lista de ingredientes
            })
            .catch(error => {
                console.log("Error al editar ingrediente:", error);
            });
        } else {
            alert("Por favor, ingresa un ingrediente.");
        }
    }

    // Añadir evento de clic al botón para agregar ingrediente
    document.getElementById("boton_editar").addEventListener("click", editar_ingredientes);




});

