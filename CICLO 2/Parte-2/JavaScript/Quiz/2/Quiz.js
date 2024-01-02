let choose = false;
const d = document;

async function seleccion(callback) {
    d.querySelector(".winner1").classList.add("hidden");
    d.querySelector(".winner2").classList.add("hidden");
    let random = Math.floor(Math.random() * 806)
    const url = `https://pokeapi.co/api/v2/pokemon/${random}`;
    const respuesta = await fetch(url);
    if (!respuesta.ok)
        throw new Error("Error. Pokemon no existe")
    const json = await respuesta.json();
    let img = d.getElementById("user").innerHTML = `<img src="${json.sprites.other["official-artwork"].front_default}" alt="noimage">`;
    choose = true;
    let name = d.getElementById("name").innerHTML = `${json.name}`;
    let hp = d.getElementById("hp").innerHTML = json.stats[0].base_stat;
    let att = d.getElementById("att").innerHTML = json.stats[1].base_stat;
    let def = d.getElementById("def").innerHTML = json.stats[2].base_stat;
    let spd = d.getElementById("spd").innerHTML = json.stats[5].base_stat;
    await callback();
    return json
}

const unlockFight = () => {
    const button = d.querySelector("#figthbutton").removeAttribute("disabled");
}

let jsonUser;

async function announceBattle() {
    const div = d.querySelector(".announce");
    div.classList.remove("hidden");
    const arr = [3, 2, 1, "FIGTH"]
    for (let i = 0; i < arr.length; i++) {
        div.textContent = "";
        div.insertAdjacentText("afterbegin", arr[i])
        await new Promise(resolve => setTimeout(resolve, 1500));
    };
    div.classList.add("hidden");
}

async function figth(callback) {
    let flag = Number(d.querySelector("#hp").textContent);
    if (flag > 0) {
        d.querySelector("#figthbutton").setAttribute("disabled", "");
        d.querySelector(".user").setAttribute("disabled", "");
        d.querySelector(".winner1").classList.add("hidden");
        d.querySelector(".winner2").classList.add("hidden");
        const tiempoInicial = Date.now();
        let tiempoActual;
        let json;
        while (tiempoActual = Date.now() - tiempoInicial <= 7000) {
            let random = Math.floor(Math.random() * 806)
            const url = `https://pokeapi.co/api/v2/pokemon/${random}`;
            await new Promise(resolve => setTimeout(resolve, 300));
            const respuesta = await fetch(url);
            json = await respuesta.json();
            let img = d.getElementById("cpu").innerHTML = `<img src="${json.sprites.other["official-artwork"].front_default}" alt="noimage">`;
            choose = true;
            let name = d.getElementById("namecpu").innerHTML = `${json.name}`;
            let hp = d.getElementById("hpcpu").innerHTML = json.stats[0].base_stat;
            let att = d.getElementById("attcpu").innerHTML = json.stats[1].base_stat;
            let def = d.getElementById("defcpu").innerHTML = json.stats[2].base_stat;
            let spd = d.getElementById("spdcpu").innerHTML = json.stats[5].base_stat;
        };
        await callback();
        return json;
    } else {
        alert("Tu pokemon a fallecido, aceptalo y escoge un nuevo pokemon, Ok?")
    }
}

let jsonCpu;

async function empateTurno() {
    let flag = true;
    while (flag) {
        let resultado;
        const empate = d.querySelector(".empate");
        empate.classList.toggle("hidden");
        await new Promise(resolve => d.querySelector("#empate_button").onclick = resolve);
        const eleccionUsuario = d.querySelector("input[name='juego']:checked").value;
        const opciones = ['Piedra', 'Papel', 'Tijera'];
        const tiempoInicial = Date.now();
        let tiempoActual;
        let DOMeleccionCPU = d.querySelector(".eleccionCPU");
        let BoxeleccionCPU = d.querySelector(".eleccionCPU_box");
        DOMeleccionCPU.classList.toggle("hidden");
        BoxeleccionCPU.classList.toggle("hidden");
        let eleccionCPU;
        while (tiempoActual = Date.now() - tiempoInicial <= 2000) {
            eleccionCPU = opciones[Math.floor(Math.random() * opciones.length)];
            DOMeleccionCPU.innerHTML = "";
            DOMeleccionCPU.insertAdjacentText("beforeend", eleccionCPU);
        };
        while (tiempoActual = Date.now() - tiempoInicial <= 2000) {
            eleccionCPU = opciones[Math.floor(Math.random() * opciones.length)];
            DOMeleccionCPU.innerHTML = "";
            DOMeleccionCPU.insertAdjacentText("beforeend", eleccionCPU);
            await new Promise(resolve => setTimeout(resolve, 400));
        };
        while (tiempoActual = Date.now() - tiempoInicial <= 2000) {
            eleccionCPU = opciones[Math.floor(Math.random() * opciones.length)];
            DOMeleccionCPU.innerHTML = "";
            DOMeleccionCPU.insertAdjacentText("beforeend", eleccionCPU);
            await new Promise(resolve => setTimeout(resolve, 550));
        };
        await new Promise(resolve => setTimeout(resolve, 800));
        const resultdraw = d.querySelector(".resultdraw");
        resultdraw.textContent = "";
        resultdraw.classList.toggle("hidden");
        if (eleccionUsuario === eleccionCPU) {
            resultdraw.insertAdjacentText("afterbegin", `EMPATE.\nJuega otra vez.`);
            empate.classList.toggle("hidden");
        } else if (
            (eleccionUsuario === 'Piedra' && eleccionCPU === 'Tijera') ||
            (eleccionUsuario === 'Papel' && eleccionCPU === 'Piedra') ||
            (eleccionUsuario === 'Tijera' && eleccionCPU === 'Papel')
        ) {
            resultdraw.insertAdjacentText("afterbegin", `¡SOS UN CAPO!\nEmpiezas tú.`);
            await new Promise(resolve => setTimeout(resolve, 3000));
            empate.classList.toggle("hidden");
            return resultado = 3
        } else {
            resultdraw.insertAdjacentText("afterbegin", `Pobre criaturita...\nResultado: Necesitas un baño de ruda.`);
            await new Promise(resolve => setTimeout(resolve, 3000));
            empate.classList.toggle("hidden");
            return resultado = 4
        }
    }
}

async function battle(json1, json2) {
    //DOM
    let DOMuserHp = d.querySelector("#hp");
    let DOMuserAtt = d.querySelector("#att");
    let DOMuserDef = d.querySelector("#def");
    let DOMuserSpd = d.querySelector("#spd");
    let DOMcpuHp = d.querySelector("#hpcpu");
    let DOMcpuAtt = d.querySelector("#attcpu");
    let DOMcpuDef = d.querySelector("#defcpu");
    let DOMcpuSpd = d.querySelector("#spdcpu");

    //StatsJugador
    let userHp = Number(DOMuserHp.innerHTML);
    let userHpTotal = userHp;
    let userAtt = Number(DOMuserAtt.innerHTML);
    let userDef = Number(DOMuserDef.innerHTML);
    let userSpd = Number(DOMuserSpd.innerHTML);
    let userXP = json1.base_experience;

    //StatsCPU
    let cpuHp = Number(DOMcpuHp.innerHTML);
    let cpuAtt = Number(DOMcpuAtt.innerHTML);
    let cpuDef = Number(DOMcpuDef.innerHTML);
    let cpuSpd = Number(DOMcpuSpd.innerHTML);
    let cpuXP = json2.base_experience;

    //Controladores del algoritmo
    let flag = true;
    let user_ko = false;
    let cpu_ko = false;
    let hits = userSpd - cpuSpd;
    let turno;

    //Algoritmo
    if (hits > 0) {
        turno = 1;
        if (hits >= 30) {
            hits = 3;
        } else if (hits >= 15 && hits <= 29) {
            hits = 2;
        } else {
            hits = 1;
        }
    } else if (hits < 0) {
        turno = 0;
        hits *= -1;
        if (hits >= 30) {
            hits = 3;
        } else if (hits >= 15 && hits <= 29) {
            hits = 2;
        } else {
            hits = 1;
        }
    } else {
        turno = 2;
    }
    while (flag) {
        if (!user_ko && !cpu_ko) {
            if (turno === 1) {
                for (let i = 1; i <= hits; i++) {
                    cpuHp = Number((cpuHp - (((cpuDef * (1 + (userSpd / 100))) + userAtt) / 10)).toFixed(0));
                    DOMcpuHp.textContent = "";
                    DOMcpuHp.insertAdjacentText("afterbegin", cpuHp);
                    await new Promise(resolve => setTimeout(resolve, 1000));
                    if (cpuHp <= 0) {
                        cpu_ko = true;
                        userHp = userHpTotal;
                        userHp = Number(((userHp / 2) * (1 + (userXP / 100))).toFixed(0));
                        const winner1 = d.querySelector(".winner1");
                        winner1.classList.toggle("hidden");
                        await new Promise(resolve => setTimeout(resolve, 1000));
                        DOMuserHp.textContent = "";
                        DOMuserHp.insertAdjacentText("afterbegin", userHp);
                        const button = d.querySelector("#figthbutton").removeAttribute("disabled");
                        d.querySelector(".user").removeAttribute("disabled");
                        return userHp;
                    };
                };
                if (!cpu_ko) {
                    userHp = Number((userHp - (((userDef * (1 + (cpuSpd / 100))) + cpuAtt) / 10)).toFixed(0));
                    DOMuserHp.textContent = "";
                    DOMuserHp.insertAdjacentText("afterbegin", userHp);
                    await new Promise(resolve => setTimeout(resolve, 1000));
                    if (userHp <= 0) {
                        user_ko = true;
                        flag = false;
                        const winner2 = d.querySelector(".winner2");
                        winner2.classList.toggle("hidden");
                        const button = d.querySelector("#figthbutton").removeAttribute("disabled");
                        d.querySelector(".user").removeAttribute("disabled");
                    };
                };
            } else if (turno === 0) {
                for (let i = 1; i <= hits; i++) {
                    userHp = Number((userHp - (((userDef * (1 + (cpuSpd / 100))) + cpuAtt) / 10)).toFixed(0));
                    DOMuserHp.textContent = "";
                    DOMuserHp.insertAdjacentText("afterbegin", userHp);
                    await new Promise(resolve => setTimeout(resolve, 1000));
                    if (userHp <= 0) {
                        user_ko = true;
                        flag = false;
                        const winner2 = d.querySelector(".winner2");
                        winner2.classList.toggle("hidden");
                        const button = d.querySelector("#figthbutton").removeAttribute("disabled");
                        d.querySelector(".user").removeAttribute("disabled");
                        break
                    };
                };
                if (!user_ko) {
                    cpuHp = Number((cpuHp - (((cpuDef * (1 + (userSpd / 100))) + userAtt) / 10)).toFixed(0));
                    DOMcpuHp.textContent = "";
                    DOMcpuHp.insertAdjacentText("afterbegin", cpuHp);
                    await new Promise(resolve => setTimeout(resolve, 1000));
                    if (cpuHp <= 0) {
                        cpu_ko = true;
                        userHp = userHpTotal;
                        userHp = Number(((userHp / 2) * (1 + (userXP / 100))).toFixed(0));
                        const winner1 = d.querySelector(".winner1");
                        winner1.classList.toggle("hidden");
                        await new Promise(resolve => setTimeout(resolve, 1000));
                        DOMuserHp.textContent = "";
                        DOMuserHp.insertAdjacentText("afterbegin", userHp);
                        const button = d.querySelector("#figthbutton").removeAttribute("disabled");
                        d.querySelector(".user").removeAttribute("disabled");
                        return userHp;
                    };
                }
            } else {
                turno = await empateTurno();
                while (flag) {
                    if (turno === 3) {
                        cpuHp = Number((cpuHp - (((cpuDef * (1 + (userSpd / 100))) + userAtt) / 10)).toFixed(0));
                        DOMcpuHp.textContent = "";
                        DOMcpuHp.insertAdjacentText("afterbegin", cpuHp);
                        await new Promise(resolve => setTimeout(resolve, 1000));
                        if (cpuHp <= 0) {
                            cpu_ko = true;
                            userHp = userHpTotal;
                            userHp = Number(((userHp / 2) * (1 + (userXP / 100))).toFixed(0));
                            const winner1 = d.querySelector(".winner1");
                            winner1.classList.toggle("hidden");
                            await new Promise(resolve => setTimeout(resolve, 1000));
                            DOMuserHp.textContent = "";
                            DOMuserHp.insertAdjacentText("afterbegin", userHp);
                            const button = d.querySelector("#figthbutton").removeAttribute("disabled");
                            d.querySelector(".user").removeAttribute("disabled");
                            return userHp;
                        };
                        if (!cpu_ko) {
                            userHp = Number((userHp - (((userDef * (1 + (cpuSpd / 100))) + cpuAtt) / 10)).toFixed(0));
                            DOMuserHp.textContent = "";
                            DOMuserHp.insertAdjacentText("afterbegin", userHp);
                            await new Promise(resolve => setTimeout(resolve, 1000));
                            if (userHp <= 0) {
                                user_ko = true;
                                flag = false;
                                const winner2 = d.querySelector(".winner2");
                                winner2.classList.toggle("hidden");
                                const button = d.querySelector("#figthbutton").removeAttribute("disabled");
                                d.querySelector(".user").removeAttribute("disabled");
                            };
                        };
                    } else {
                        userHp = Number((userHp - (((userDef * (1 + (cpuSpd / 100))) + cpuAtt) / 10)).toFixed(0));
                        DOMuserHp.textContent = "";
                        DOMuserHp.insertAdjacentText("afterbegin", userHp);
                        await new Promise(resolve => setTimeout(resolve, 1000));
                        if (userHp <= 0) {
                            user_ko = true;
                            flag = false;
                            const winner2 = d.querySelector(".winner2");
                            winner2.classList.toggle("hidden");
                            const button = d.querySelector("#figthbutton").removeAttribute("disabled");
                            d.querySelector(".user").removeAttribute("disabled");
                        };
                        if (!user_ko) {
                            cpuHp = Number((cpuHp - (((cpuDef * (1 + (userSpd / 100))) + userAtt) / 10)).toFixed(0));
                            DOMcpuHp.textContent = "";
                            DOMcpuHp.insertAdjacentText("afterbegin", cpuHp);
                            await new Promise(resolve => setTimeout(resolve, 1000));
                            if (cpuHp <= 0) {
                                cpu_ko = true;
                                userHp = userHpTotal;
                                userHp = Number(((userHp / 2) * (1 + (userXP / 100))).toFixed(0));
                                const winner1 = d.querySelector(".winner1");
                                winner1.classList.toggle("hidden");
                                await new Promise(resolve => setTimeout(resolve, 1000));
                                DOMuserHp.textContent = "";
                                DOMuserHp.insertAdjacentText("afterbegin", userHp);
                                const button = d.querySelector("#figthbutton").removeAttribute("disabled");
                                d.querySelector(".user").removeAttribute("disabled");
                                return userHp;
                            }
                        };
                    }
                }
            }
        }
    }
}

let program;

//Ejecucion del programa

d.querySelector(".user").addEventListener("click", async () => {
    // debugger
    jsonUser = await seleccion(unlockFight);
});
d.querySelector("#figthbutton").addEventListener("click", async () => {
    jsonCpu = await figth(announceBattle);
    program = battle(jsonUser, jsonCpu);
});
document.addEventListener("DOMContentLoaded", function () {
    d.querySelector("#figthbutton").setAttribute("disabled", "");
});

