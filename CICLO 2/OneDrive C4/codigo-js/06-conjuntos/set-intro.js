//Creara el conjunto
let letras = new Set()

//Agregar elementos
letras.add("b")
letras.add("c")
letras.add("y")
console.log(letras)

//Borrar elementos
console.log(letras.delete('a'))
console.log(letras.delete('y'))
console.log(letras)

// si el elemento existe dentro conjunto
console.log(letras.has('y'))
console.log(letras.has('c'))

// Recorrido con foreach
letras.forEach(l => console.log(l))

// recorrido con for of
for (const l of letras) {
    console.log(l)
}

console.log("Tamaño del conjunto: " + letras.size)
