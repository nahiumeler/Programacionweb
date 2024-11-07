document.addEventListener('DOMContentLoaded', function () {
// document.addEventListener: Este método se utiliza para escuchar eventos en el objeto document (es decir, la página web).
//'DOMContentLoaded': Este evento se dispara cuando el documento HTML ha sido completamente cargado y procesado, pero antes de que las imágenes, hojas de estilo, o subrecursos como scripts externos hayan terminado de cargar. Esto es útil para ejecutar código tan pronto como la estructura de la página esté disponible para ser manipulada.
//function () { ... }: Esta es una función anónima (sin nombre) que se ejecutará cuando se dispare el evento 'DOMContentLoaded'. El código dentro de esta función se ejecutará justo después de que el documento esté listo.
    
    const messiImage = document.querySelector('#jugadores img[alt="Lionel Messi"]');
// const: Declara una variable constante, es decir, su valor no puede ser reasignado más tarde.
//document.querySelector: Este método selecciona el primer elemento del DOM (Document Object Model) que coincide con el selector CSS proporcionado. En este caso:
//#jugadores: Selecciona un elemento con el ID jugadores (un contenedor o div).
//img: Busca dentro de ese contenedor una etiqueta <img>, es decir, una imagen.
//[alt="Lionel Messi"]: Este es un selector de atributo, que filtra las imágenes que tengan un atributo alt con el valor "Lionel Messi". El atributo alt en una imagen generalmente contiene una descripción alternativa que se muestra si la imagen no se puede cargar o para accesibilidad.
//El resultado de querySelector será el primer elemento img dentro del contenedor #jugadores que tenga el atributo alt="Lionel Messi". Este elemento se almacena en la variable messiImage.
    if (messiImage) {
// Este es un condicional que verifica si la variable messiImage no es null ni undefined. En otras palabras, comprueba si se ha encontrado realmente una imagen con el atributo alt="Lionel Messi". Si la imagen existe en el DOM, el bloque de código dentro del if se ejecutará.
        messiImage.addEventListener('click', function () {
// messiImage.addEventListener('click', function () {: Aquí se está agregando un escuchador de eventos a la imagen messiImage.
//'click': Especifica que el evento que estamos escuchando es un clic del usuario sobre la imagen.
//function () { ... }: Esta es una función que se ejecutará cada vez que el usuario haga clic en la imagen de Messi. El bloque de código dentro de esta función manejará la acción a realizar al hacer clic.
            // Abrir la página de detalle para Messi
            window.location.href = '../messi.html';
        });
    }
});

// window.location.href: location.href es una propiedad del objeto window que permite manipular o acceder a la URL de la página actual.
//Asignando un valor a location.href, cambiamos la URL de la página actual y, por lo tanto, redirigimos al navegador a esa nueva página.
//En este caso, estamos asignando '../messi.html', que es una URL relativa. Esto indica que la página debe redirigir al archivo messi.html que se encuentra un nivel arriba en la estructura de carpetas (en relación con la página actual).
//En resumen, al hacer clic en la imagen de Messi, el navegador redirige al usuario a una nueva página llamada messi.html.

// Este cierre de paréntesis y llave marca el fin de la función que se ejecuta cuando se hace clic en la imagen de Messi.

// });: El primer paréntesis cierra la función anónima pasada a addEventListener, y la última llave cierra el bloque del if que verifica si la imagen de Messi está presente en el DOM.