// Inicializacion de datos y definiciones

function proceso(prestamo, interes, cuotas) {
    //Definicion de datos valor
    //    debugger
    let interes_a = prestamo * interes;
    let interes_m = interes_a / cuotas; interes_m = Number(interes_m.toFixed(0))
    let capital = prestamo / cuotas; capital = Number(capital.toFixed(0))
    let total_deuda = prestamo + interes_a;
    let deuda_mensual = capital + interes_m;
    //Bases de datos
    const map = new Map();
    const bdd = new Array(prestamo, total_deuda, capital, interes_m, deuda_mensual);

    for (let i = 1; i < cuotas + 1; i++) {
        if (i == 1) {
            let tabla = document.getElementById("tabla2").innerHTML = "<table><thead><tr><th>MES</th><th>VALOR</th><th>VALOR TOTAL</th><th>CAPITAL</th><th>INTERES</th><th>TOTAL</th></tr></thead></table>"
            let bdd_copia = bdd.slice();
            map.set(i, bdd_copia);

        } else {
            bdd[0] = bdd[0] - capital;
            bdd[1] = bdd[1] - deuda_mensual;
            let bdd_copia = bdd.slice();
            map.set(i, bdd_copia);
        }
    };
    console.log(map);

}

const input_prestamo = Number(prompt("Simulador de prestamo\n\nMonto del credito"));
const input_interes = Number(prompt("Interés% (Anual)"));
const input_pagos = Number(prompt("Número de pagos (Mensuales)"));

///Escritura en html




proceso(input_prestamo, input_interes, input_pagos)