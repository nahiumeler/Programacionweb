document.addEventListener("DOMContentLoaded", function () {
    const players = document.querySelectorAll('.jugador');

    players.forEach(player => {
        player.addEventListener('click', function () {
         
            const targetPage = this.getAttribute('data-target');

            window.location.href = targetPage;
        });
    });
});