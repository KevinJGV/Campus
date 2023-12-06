const frutas = new Map([["Manzanas", 2500],["Peras", 2000],["Banano",1500]])
console.log(frutas)
console.log("cantidad de frutas: " + frutas.size)

frutas.set("Pitahaya", 5000)
frutas.set("Mango", 3000)
console.log(frutas)

console.log("Fruta favorita: " + frutas.get("Mango"))

console.log(frutas.delete("Pepino"))
console.log(frutas.delete("Pitahaya"))

console.log("cantidad de frutas: " + frutas.size)

console.log("El mango existe?: " + frutas.has("Mango"))
console.log("La Pitahaya existe?: " + frutas.has("Pitahaya"))

frutas.forEach((precio, fruta) => {
    console.log(`${fruta} cuesta ${precio}$`)
})

for (const e of frutas.entries()) {
    console.log(`${e[0]} cuesta ${e[1]}$`)
}