// Inicializacion de datos

const input_prestamo = Number(prompt("Simulador de prestamo\n\nMonto del credito"));
const input_interes = Number(prompt("Interés% (Anual)"));
const input_pagos = Number(prompt("Número de pagos (Mensuales)"));




function proceso(prestamo,interes,cuotas) {
    //Definicion de datos valor
    debugger
    let interes_a = prestamo*interes;
    let interes_m = interes_a/cuotas; interes_m = Number(interes_m.toFixed(0))
    let capital = prestamo/cuotas; capital = Number(capital.toFixed(0))
    let total_deuda = prestamo+interes_a;
    let deuda_mensual = capital+interes_m;
    //Bases de datos
    const map = new Map()
    const bdd = new Array(prestamo, total_deuda, capital, interes_m, deuda_mensual)
    for (let i = 1; i < cuotas+1;i++) {
        if (i == 1) {
            map.set(i, bdd)
        } else {
            bdd[0] = bdd[0] - capital
            bdd[1] = bdd[1] - deuda_mensual
            map.set(i, bdd)
        }
        
    }
    console.log(map)
}

proceso(input_prestamo,input_interes,input_pagos)