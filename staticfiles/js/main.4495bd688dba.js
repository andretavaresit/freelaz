const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);


function acao(){
    console.log('entrei funcao')
    let modal = document.querySelector('.wrapper')

    modal.style.display = 'block';

    let fundo = document.querySelector('.py-5 text-white')

    modal.style.opacity = '50%';


}