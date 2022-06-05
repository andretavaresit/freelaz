const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);


function iniciaModal(modalID){
    const modal = document.getElementById(modalID);

    modal.classList.add('mostrar');

    console.log(modal);

    

}