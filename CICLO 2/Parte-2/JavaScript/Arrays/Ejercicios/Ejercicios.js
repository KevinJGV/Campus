//1

let array = ["Casa", "Perro", "Home", "Dog", "Elefante", "Cake"]

let nuevo = array.filter(function(e) {
    for (e.length >= 4) {
        return e;
    }
})

//2

function checkInString(frase, buscar) {
    return frase.toLowerCase().includes(buscar.toLowerCase())
}

let input = "Cualquier Frase para checkear"
let encontrar = "frase"
let resultado = 