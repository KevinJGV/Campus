function o(num,concat) {
    let r = Number(String(num).repeat(concat))
    console.log(r)
}
let suma = 0
function superdigit(num) {
    let l = num.length
    if (l > 1){
    for (let i = 0; i < l; i++) {
        suma += Number(num[i])
    }} else {
        console.log(num)
        suma = 0
    }
   return suma
}

console.log(superdigit("8"))
o(958,5)
