function utilizouHoraExtra(id){

    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    valor = document.getElementById('desmarcar').value;
    console.log(valor)

    $.ajax({
        type: 'POST',
        url:'/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
            reverter: valor

        },
        success: function(result){
            console.log('Sucesso');
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }

    })
}
