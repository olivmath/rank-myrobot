const inputName = document.querySelector("#name");
const inputColor = document.querySelector("#color");
const inputScore = document.querySelector("#score");
const button = document.querySelector("#btn");








function get_user(){
    let Name = inputName.value;
    let Color = inputColor.value;
    let Score = inputScore.value;
    inputName.value = "";
    inputColor.value = "";
    inputScore.value = "";

    alert(`Nome: ${Name}, Cor: ${Color}, Pontos: ${Score}\nEnviado com sucesso!`)
}


button.onclick = get_user;
