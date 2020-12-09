const iron = "img/Iron.png";
const bronze = "img/Bronze.png";
const silver = "img/Silver.png";
const gold = "img/Gold.png";
const adamantium = "img/Adamantium.png";
const tungstenium = "img/Tugstenium.png";
const vibranium = "img/Vibranium.png";
const url = "http://127.0.0.1:5000/";
const rank = "rank"


function patent(score) {
    switch (true) {
        case score >= 10000:
            return vibranium;
            break;
        case score >= 7500:
            return tungstenium;
            break;
        case score >= 5000:
            return adamantium;
            break;
        case score >= 3000:
                return gold;
                break;
        case score >= 2000:
                return silver;
                break;
        case score >= 1000:
            return bronze;
            break;
        default:
            return iron;
            break;
    }
}


function generatorUser(data) {
    let color = data['color'];
    let name = data['user'];
    let score = data['score'];
    let img = patent(score);

    let li = document.createElement('li');
    let div = document.createElement('div');
    let nameTag = document.createElement('p');
    let scoreTag = document.createElement('p');
    let imgTag = document.createElement('img');


    div.setAttribute("class", "flex-item");
    nameTag.textContent = name;
    nameTag.setAttribute("class", "name");
    nameTag.setAttribute("style", color);
    scoreTag.textContent = score;
    scoreTag.setAttribute("class", "score");
    imgTag.setAttribute("src", img);

    div.appendChild(nameTag);
    div.appendChild(scoreTag);
    div.appendChild(imgTag);
    li.appendChild(div);

    return li
}

function renderUsers(data) {
    for (data of data['rank']) {
        let user = generatorUser(data);
        document.querySelector('ol').appendChild(user);
    }
}



fetch(url+rank)
.then(response => response.json())
.then(jsonBody => {
    renderUsers(jsonBody)
})

