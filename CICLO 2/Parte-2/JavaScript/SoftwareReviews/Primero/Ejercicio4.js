input = Number(prompt("DE 24hr a 12hr\nIngrese hora en sistema horario 24 Hrs, es decir entre 0 a 24, se le dira que tipo de hora es en el sistema horario 12 Hrs (Am-Pm) (Pulsar F12)"));
if (input < 0 || input > 24 || input === "" || isNaN(input)) {
    console.log("Su ingreso es incorrecto o nulo, ingrese un valor en el rango solicitado.")
} else {
    if (input <= 11) {
        console.log("AM")
    } else {
        console.log("PM")
    }
}