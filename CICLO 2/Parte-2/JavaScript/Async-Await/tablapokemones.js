const d = document;
const target = d.querySelector("tbody");
const frag = d.createDocumentFragment();
const API = "https://pokeapi.co/api/v2/pokemon/";

function toCapitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
};

for (let i = 1; i <= 100; i++) {
    fetch(`${API}${i}`)
        .then(resultado => resultado.json())
        .then(pokemon => {
            let name = pokemon.forms[0].name;
            name = toCapitalize(name);
            const sprite = pokemon.sprites.front_default;
            const row = d.createElement("tr");
            const cell1 = d.createElement("td");
            cell1.insertAdjacentText("beforeend", i);
            row.insertAdjacentElement("beforeend", cell1);
            const cell2 = d.createElement("td");
            cell2.insertAdjacentText("beforeend", name);
            row.insertAdjacentElement("beforeend", cell2);
            const cell3 = d.createElement("td");
            const img = d.createElement("img");
            img.setAttribute("src", sprite);
            cell3.insertAdjacentElement("beforeend", img);
            row.insertAdjacentElement("beforeend", cell3);
            frag.appendChild(row);
            target.appendChild(frag);
        })
}
