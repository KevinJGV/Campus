let str = "2, ";
for (let n=3 ; n <= 100 ; n+=2) {
    str+= `${n}, `
    document.getElementById("lista").innerHTML = str
}