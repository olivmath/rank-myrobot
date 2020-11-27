var iron = "img/Iron.png";
var bronze = "img/Bronze.png";
var silver = "img/Silver.png";
var gold = "img/Gold.png";
var adamantium = "img/Adamantium.png";
var tungstenium = "img/Tugstenium.png";
var vibranium = "img/Vibranium.png";
/*
    <li>
        <div class="flex-item">
            <p class="name" style="color: #FF1616;">Israel</p>
            <p class="score">1700</p>
            <img src="img/Bronze.png" alt="Bronze">
        </div>
    </li>
*/

rank = {'rank':[
    {'user': 'Lucas',  'color': '#545454', 'score': 19000},
    {'user': 'Israel',    'color': '#FF1616', 'score': 8000},
    {'user': 'Saymon',    'color': '#aaff11', 'score': 7000},
    {'user': 'Henrico',   'color': '#FF7637', 'score': 4000},
    {'user': 'Benjamin',  'color': '#F9B11F', 'score': 2300},
    {'user': 'Milena',    'color': '#38B6FF', 'score': 1200},
    {'user': 'Gustavo',   'color': '#8C52FF', 'score': 600}
    ]
}


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

// renderUsers(rank);
