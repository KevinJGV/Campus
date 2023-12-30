//CREAR UN MARCABLE QUE ALTERNE ENTRE LAS 2 OPCIONES

// Opcion aleatoria
function toCapitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

function idSelect(arr) {
    let id = Math.floor(Math.random() * 1000) + 1;
    while (!arr.indexOf(id)) {
        id = Math.floor(Math.random() * 1000) + 1;
    };
    arr.push(id);
    return id
}

const d = document;
let descartes = [];
const switcher = () => {
    debugger
    const id = idSelect(descartes);
    const imgplace1 = d.querySelector("box1");
    const idplace1 = d.querySelector("id");
    const nameplace1 = d.querySelector("name");
    const url = "https://pokeapi.co/api/v2/pokemon/";
    fetch(`${url}${id}`)
        .then(res => res.json())
        .then(pokemon => {
            let name = pokemon.forms[0].name;
            name = toCapitalize(name);
            nameplace1.insertAdjacentText("afterbegin", name)
            idplace1.insertAdjacentText("afterbegin", id)
            const sprite = pokemon.sprites.front_default;
            imgplace1.setAttribute("src", sprite);
        })
}


// Opcion consecutiva

