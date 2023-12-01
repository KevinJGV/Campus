let random = Math.ceil(Math.random() * 100)
adivinado = false
while (adivinado === false) {
    rta = Number(prompt("Adivina el numero del 1 al 100"));
    if (rta === 0) {
        alert(`Respuesta: ${random}`);
    } else if (rta == random) {
        alert('¡Correcto! El número era ' + random);
        adivinado = true;
    } else if (rta < random) {
        alert('El nùmero es mayor.')
    } else if (rta > random) {
        alert('El nùmero es menor.');
    }
}