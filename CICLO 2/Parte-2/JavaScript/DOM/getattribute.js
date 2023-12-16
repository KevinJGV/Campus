const enlace1 = document.getElementById("enlace1");
const url = enlace1.getAttribute("href");
console.log(url)

const enlace2 = document.getElementById("enlace2");
const set = enlace2.setAttribute("href", "https://cacorro.com");
const url2 = enlace2.getAttribute("href")
console.log(url2)

const elemento = document.getElementById("elemento");
const atributos = elemento.getAttributeNames();
console.log("Atributos: ", atributos);

let toggle = document.getElementsByClassName("toggle")
toggle.toggleAttribute("data-info");

console.log("Esta data-info?" + toggle.hasAttribute("data-info"));