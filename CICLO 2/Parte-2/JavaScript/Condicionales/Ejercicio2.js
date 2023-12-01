alert("Validador de fechas, ingrese una fecha en formato DD/MM/AAAA");
let dia = Number(prompt("Ingrese dia:"));
if (isNaN(dia)) {
    alert("Error, por favor ingresa una fecha valida");
    throw new Error('Input inválido');
} else if (dia < 1 || dia > 31) {
    alert("Dia fuera de rango");
    throw new Error('Input inválido');
}
let mes = Number(prompt("Ingrese mes:"));
if (isNaN(mes)) {
    alert("Error, por favor ingresa una fecha valida");
    throw new Error('Input inválido');
} else if (mes < 1 || mes > 12) {
    alert("Mes fuera de rango");
    throw new Error('Input inválido');
} 
let año = Number(prompt("Ingrese mes:"));
if (isNaN(año)) {
    alert("Error, por favor ingresa una fecha valida");
    throw new Error('Input inválido');
}
