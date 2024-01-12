const d = document;
const url = "https://rickandmortyapi.com/api/character";

const promise = fetch(url);

promise
    .then(res => res.json())
    .then(json => {
        let arr = json.results;
        for (let pj of arr) {
            console.log(pj)
            const main = d.querySelector("main");
            const fragment = d.createDocumentFragment();
            const card = d.createElement("div");
            card.classList.add("card");
            const img = d.createElement("img");
            img.setAttribute("src", pj.image);
            img.setAttribute("alt", "pj.image");
            card.insertAdjacentElement("afterbegin", img);
            const h2 = d.createElement("h2");
            h2.classList.add("name");
            h2.insertAdjacentText("afterbegin", pj.name);
            card.insertAdjacentElement("beforeend", h2);
            const p = d.createElement("p");
            p.classList.add("status");
            p.insertAdjacentText("afterbegin", pj.status);
            card.insertAdjacentElement("beforeend", p);
            fragment.appendChild(card);
            main.appendChild(fragment);
        }
    })
    .catch(err => console.error(err))
    .finally(action => "")
