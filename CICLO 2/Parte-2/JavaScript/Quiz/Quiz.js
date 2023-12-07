// Inicializacion de datos

let input_prestamo = prompt("Simulador de prestamo\n\nMonto del credito");
let input_interes = prompt("Interés% (Anual)");
let input_pagos = prompt("Número de pagos (Mensuales)");
let interes_a = input_prestamo*input_interes;
let interes_m = interes_a/input_pagos;
let capital = input_prestamo/input_pagos;
let total_deuda = input_prestamo+interes_a;
let deuda_mensual = capital+interes_m;

let bdd = new Map()

function proceso(prestamo,interes,cuotas) {
    let map = new Map()
    for (let i = 1; i == cuotas;i++) {
        return 
    }
}