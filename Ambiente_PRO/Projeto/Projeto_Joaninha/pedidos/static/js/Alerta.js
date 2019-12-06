function Enviar() {
 
    var nome = document.getElementById("id_nome_cliente");
 
    if (nome.value != "") {
        alert('Obrigado sr(a) ' + nome.value + ' seu pedido foi realizado com sucesso');
    }
 
}