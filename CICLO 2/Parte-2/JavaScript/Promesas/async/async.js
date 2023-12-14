// const fs = require("fs").promise;

//         async function fetchData() {
//             try {
//                 const data = await fs.readfile("robots.txt", "utf-8");
//                 console.log(data);
//             } catch (error) {
//                 console.error("Error inesperado: ", error.message)
//             }
//         }
//         console.log("Codigo asincrono.");
//         fetchData();

async function getNombre(nomusu) {
    const url = `https://pokeapi.co/api/v2/pokemon/${nomusu}`;
    const rta = await fetch(url);
    const json = await rta.json()

    console.log(json.sprites.front_default)
}

getNombre("turtwig");