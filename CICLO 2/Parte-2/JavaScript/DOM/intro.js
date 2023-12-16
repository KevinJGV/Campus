let elementos = document.getElementsByClassName("clase")
for (let i = 0; i < elementos.length; i++) {
    elementos[i].innerHTML = "Nuevo contenido para div " + (i+1);
}

let parrafos = document.getElementsByTagName("p")
for (let i = 0; i < parrafos.length; i++) {
    parrafos[i].innerHTML = "Nuevo contenido para p " + (i+1);
}

function cambio() {
    const presaltado = document.querySelector("#resaltado");

    presaltado.style.fontsize = "25px";

    const p5 = document.querySelector(".parrafo");

    p5.style.color = "green"    
}

function queryall() {
    let fsize = 18;
    const parrafo = document.querySelectorAll(".parrafo")
    parrafos.forEach(element => {
        parrafos.style.fontsize = `${fsize}px`
        fsize += 7
    });
}

