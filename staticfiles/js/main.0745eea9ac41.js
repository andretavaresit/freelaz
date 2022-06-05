const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);


function iniciaModal(modalID){

    const avaliar = document.getElementById('avaliar')
    console.log(avaliar)

    if (avaliar != null){

        const modal = document.getElementById(modalID);

        modal.classList.add('mostrar');

        modal.addEventListener('click',(e)=>{
            if(e.target.id==modalID || e.target.className=='fechar'){
                modal.classList.remove('mostrar')
            }
        })

        console.log(modal);

    }   

    

}