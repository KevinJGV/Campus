let choose = false;

async function seleccion(callback) {
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
    callback();
}

const unlockFight = () => {
    const button = document.querySelector("#figthbutton").removeAttribute("disabled")
}

async function figth() {

    const tiempoInicial = Date.now();
    let tiempoActual;
    while (tiempoActual = Date.now() - tiempoInicial <= 7000) {
        let random = Math.floor(Math.random() * 806)
        const url = `https://pokeapi.co/api/v2/pokemon/${random}`;
        await new Promise(resolve => setTimeout(resolve, 300));
        const respuesta = await fetch(url);
        const json = await respuesta.json();
        let img = document.getElementById("cpu").innerHTML = `<img src="${json.sprites.other["official-artwork"].front_default}" alt="noimage">`;
        choose = true;
        let name = document.getElementById("namecpu").innerHTML = `${json.name}`;
        let hp = document.getElementById("hpcpu").innerHTML = json.stats[0].base_stat;
        let att = document.getElementById("attcpu").innerHTML = json.stats[1].base_stat;
        let def = document.getElementById("defcpu").innerHTML = json.stats[2].base_stat;
        let spd = document.getElementById("spdcpu").innerHTML = json.stats[5].base_stat;
    };
    announceBattle();
}

async function announceBattle() {
    const div = document.querySelector(".announce");
    const arr = [3, 2, 1, "FIGTH"]
    for (let i = 0; i < arr.length; i++) {
        div.textContent = "";
        div.insertAdjacentText("afterbegin", arr[i])
        await new Promise(resolve => setTimeout(resolve, 1500));
    };
    div.classList.add("hidden");
    battle();
}

function battle() {
    debugger
    //StatsJugador
    let userName = document.querySelector("#name").innerHTML;
    let userHp = document.querySelector("#hp").innerHTML;
    let userAtt = document.querySelector("#att").innerHTML;
    let userDef = document.querySelector("#def").innerHTML;
    let userSpd = document.querySelector("#spd").innerHTML;

    //StatsCPU
    let cpuName = document.querySelector("#namecpu").innerHTML;
    let cpuHp = document.querySelector("#hpcpu").innerHTML;
    let cpuAtt = document.querySelector("#attcpu").innerHTML;
    let cpuDef = document.querySelector("#defcpu").innerHTML;
    let cpuSpd = document.querySelector("#spdcpu").innerHTML;

    //Controladores del algoritmo
    let flag = true;
    let user_ko = false;
    let cpu_ko = false;
    let hits = userSpd - cpuSpd;
    let turno;

    //Algoritmo
    if (hits >= 0) {
        turno = 1;
    } else {
        turno = 0;
    };
    while (flag) {
        if (user_ko === false && cpu_ko === false) {
            if (turno === 1) {
                for (let i; i <= hits; i++) {
                    cpuHp = cpuHp - (cpuDef * (1 + (userSpd / 100)) - userAtt);
                }
                if (cpuHp <= 0) {
                    cpu_ko = true;
                };
                userHp = userHp - (userDef * (1 + (cpuSpd / 100)) - cpuAtt);
                if (userHp <= 0) {
                    user_ko = true;
                };
            } else {
                hits *= -1;
                for (let i; i <= hits; i++) {
                    userHp = userHp - (userDef * (1 + (cpuSpd / 100)) - cpuAtt);
                }
                if (userHp <= 0) {
                    user_ko = true;
                };
                cpuHp = cpuHp - (cpuDef * (1 + (userSpd / 100)) - userAtt);
                if (cpuHp <= 0) {
                    cpu_ko = true;
                };
            }
        } else if (user_ko === false && cpu_ko === true) {

        } else {

        }
    }
}
