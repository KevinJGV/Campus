function toCapitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

async function idSelect(arr) {
    let id = Math.floor(Math.random() * 1000) + 1;
    while (!arr.indexOf(id)) {
        id = Math.floor(Math.random() * 1000) + 1;
    };
    arr.push(id);
    return id
}

async function OrdIdSelect(arr, i) {
    while (arr.indexOf(i) !== -1) {
        i++;
    };
    arr.push(i);
    return i
}

const d = document;
let descartes = [];
const switcher = async () => {
    debugger
    const check = d.querySelector("#check");
    if (check.checked) {
        // Opcion aleatoria
        let id = await idSelect(descartes);
        let imgplace1 = d.querySelector(".box1");
        let idplace1 = d.querySelector("#id1");
        idplace1.textContent = "";
        let nameplace1 = d.querySelector("#name1");
        nameplace1.textContent = "";
        const url = "https://pokeapi.co/api/v2/pokemon/";
        await fetch(`${url}${id}`)
            .then(res => res.json())
            .then(pokemon => {
                let name = pokemon.forms[0].name;
                name = toCapitalize(name);
                nameplace1.insertAdjacentText("afterbegin", name)
                idplace1.insertAdjacentText("afterbegin", `#${id}`)
                const sprite = pokemon.sprites.front_default;
                imgplace1.setAttribute("src", sprite);
            });
        id = await idSelect(descartes);
        let imgplace2 = d.querySelector(".box2");
        let idplace2 = d.querySelector("#id2");
        idplace2.textContent = "";
        let nameplace2 = d.querySelector("#name2");
        nameplace2.textContent = "";
        fetch(`${url}${id}`)
            .then(res => res.json())
            .then(pokemon => {
                let name = pokemon.forms[0].name;
                name = toCapitalize(name);
                nameplace2.insertAdjacentText("afterbegin", name)
                idplace2.insertAdjacentText("afterbegin", `#${id}`)
                const sprite = pokemon.sprites.front_default;
                imgplace2.setAttribute("src", sprite);
            });
    } else {
        // Opcion consecutiva
        let id = 1;
        id = await OrdIdSelect(descartes, id);
        let imgplace1 = d.querySelector(".box1");
        let idplace1 = d.querySelector("#id1");
        idplace1.textContent = "";
        let nameplace1 = d.querySelector("#name1");
        nameplace1.textContent = "";
        const url = "https://pokeapi.co/api/v2/pokemon/";
        await fetch(`${url}${id}`)
            .then(res => res.json())
            .then(pokemon => {
                let name = pokemon.forms[0].name;
                name = toCapitalize(name);
                nameplace1.insertAdjacentText("afterbegin", name)
                idplace1.insertAdjacentText("afterbegin", `#${id}`)
                const sprite = pokemon.sprites.front_default;
                imgplace1.setAttribute("src", sprite);
            });
        id = await OrdIdSelect(descartes, id);
        let imgplace2 = d.querySelector(".box2");
        let idplace2 = d.querySelector("#id2");
        idplace2.textContent = "";
        let nameplace2 = d.querySelector("#name2");
        nameplace2.textContent = "";
        fetch(`${url}${id}`)
            .then(res => res.json())
            .then(pokemon => {
                let name = pokemon.forms[0].name;
                name = toCapitalize(name);
                nameplace2.insertAdjacentText("afterbegin", name)
                idplace2.insertAdjacentText("afterbegin", `#${id}`)
                const sprite = pokemon.sprites.front_default;
                imgplace2.setAttribute("src", sprite);
            });
    }
}
