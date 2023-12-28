const validar = (obj) => {
    let palabras;
    while (!palabras || palabras == 0) {
        palabras = prompt(obj);
        if (!palabras || palabras == 0) {
            alert("Siga las instrucciones dadas.");
        }
    }
    return palabras;
};

const palabras = validar("Ingrese una serie de palabras separadas por un espacio cada una").toLocaleLowerCase().split(" ");
let prefijo = RegExp("^" + validar("Prefijo"));
const result = palabras.reduce((total, elemento) => {
    debugger
    if (prefijo.test(elemento)) {
        total++;
    };
    return total
}, 0);

alert(`Coincidencias totales: ${result}`);
