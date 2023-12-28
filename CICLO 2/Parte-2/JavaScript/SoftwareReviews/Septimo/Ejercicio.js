function procesarTexto(msj) {
    // debugger
    let texto = prompt(msj)
    const regex = /[.,:;/ ]/;
    texto = texto.toLowerCase().split(regex);
    return texto
}

function operacion(texto) {
    const map = new Map();
    texto.forEach(element => {
        if (!map.has(element)) {
            let value = texto.filter(palabra => palabra === element);
            map.set(element, value.length);
        };
    });
    console.table([...map]);
}

let texto = operacion(procesarTexto("Ingrese el texto a evaluar"));