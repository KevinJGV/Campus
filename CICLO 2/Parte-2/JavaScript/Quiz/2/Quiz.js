let choose = false;

async function seleccion() {
    let random = Math.floor(Math.random() * 806)
    const url = `https://pokeapi.co/api/v2/pokemon/${random}`;
    const respuesta = await fetch(url);
    if (!respuesta.ok)
        throw new Error("Error. Pokemon no existe")
    const json = await respuesta.json();
    let img = document.getElementById("user").innerHTML = `<img src="${json.sprites.other["official-artwork"].front_default}" alt="noimage">`;
    choose = true;
    let name = document.getElementById("name").innerHTML = `${json.name}`;
    let hp = document.getElementById("hp").innerHTML = json.stats[0].base_stat;
    let att = document.getElementById("att").innerHTML = json.stats[1].base_stat;
    let def = document.getElementById("def").innerHTML = json.stats[2].base_stat;
    let spd = document.getElementById("spd").innerHTML = json.stats[5].base_stat;
}

async function seleccioncpu() {
    let random = Math.floor(Math.random() * 806)
    const url = `https://pokeapi.co/api/v2/pokemon/${random}`;
    const respuesta = await fetch(url);
    if (!respuesta.ok)
        throw new Error("Error. Pokemon no existe")
    const json = await respuesta.json();
    let img = document.getElementById("cpu").innerHTML = `<img src="${json.sprites.other["official-artwork"].front_default}" alt="noimage">`;
    choose = true;
    let name = document.getElementById("namecpu").innerHTML = `${json.name}`;
    let hp = document.getElementById("hpcpu").innerHTML = json.stats[0].base_stat;
    let att = document.getElementById("attcpu").innerHTML = json.stats[1].base_stat;
    let def = document.getElementById("defcpu").innerHTML = json.stats[2].base_stat;
    let spd = document.getElementById("spdcpu").innerHTML = json.stats[5].base_stat;
}
let loquesea = true

async function figth() {
    if (choose === true) {
        setTimeout(function () {
            while (loquesea === true) {
                seleccioncpu()
            };
        }, 7000)
    }
}