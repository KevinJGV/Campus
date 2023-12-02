
/*
function hola(a) {
    for (Range(a)) {alert("hola")}
}


let cantidad = Number(5)

hola(cantidad)

//FUNCION FLECHA

const hola = a => alert(a)
*/
/*
const anonima = function(n1,n2) {
    if (n1 > n2) {
        alert(`Suma: ${n1+n2}\nResta: ${n1-n2}`)
    } else if (n1 < n2) {
        alert(`Divisiòn: ${n1+n2}\nMultip.: ${n1-n2}`)
    }
}


let num1 = Number(prompt("Ingrese Primer numero:"))
let num2 = Number(prompt("Ingrese Segundo numero:"))
anonima(num1,num2)
*/

const totalatletas = Number(prompt("Ingrese cantidad de atletas"))
let ganador = ""
let salto = 0
let record = 15.50
let newrecord = false
for (let i=0;i<totalatletas;i++) {
    let nombre = prompt("ingrese el nombre del atleta")
    let marca = Number(prompt("Marca del salto en metros"))
    if (marca > salto) {
        ganador = nombre
        salto = marca
        } else if (salto > record) {
        salto = record
        newrecord = true
    } }
if (newrecord = true){
    alert(`El ganador es ${ganador}, con un salto de ${salto}mts, ha roto el record anterior y tiene una recompensa de $500M`)
} else if (newrecord = false) {
    alert(`El ganador es ${ganador}, con un salto de ${salto}mts`)
}
