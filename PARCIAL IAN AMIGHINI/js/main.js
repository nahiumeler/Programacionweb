document.addEventListener('DOMContentLoaded', function () {
    const messiImage = document.querySelector('#jugadores img[alt="Lionel Messi"]');
    
    if (messiImage) {
        messiImage.addEventListener('click', function () {
            // Abrir la página de detalle para Messi
            window.location.href = '../messi.html';
        });
    }
});

//no me salioS