let campers = Number(prompt("Cantidad total de campers")); 
while (isNaN(campers)) {
    alert('Por favor, ingrese un numero');
    campers = Number(prompt("Cantidad total de campers"));
} ;
let monitores = campers * 2 ; let pc = monitores / 2 ;

alert(`Para los ${campers} Campers se requiere lo siguiente:
        - PC: ${pc}
        - Monitores: ${monitores}`);
// SALIDA A HTML

document.getElementById("campers").innerHTML = `Cantidad: ${campers}`;
document.getElementById("pc").innerHTML = `PC\'s requeridos: ${pc}<br>Monitores requeridos: ${monitores}`