const d = document;
const b = d.querySelector("body");
const topbg = d.querySelector(".topbg");
const mainlayer = d.querySelector(".mainlayer");
const container = d.querySelector(".containermainlayer");
const porfolio = d.querySelector(".porfolio");
const nav = d.querySelector(".navcontainer");
const lateralbar = d.querySelector(".lateralbar");

let isTrusted;

if (window.innerWidth <= 767) {
    topbg.style.removeProperty("transition");
    mainlayer.style.removeProperty("transition");
    nav.style.removeProperty("transition");
    lateralbar.style.removeProperty("transition");
    porfolio.style.removeProperty("transition");
    topbg.style.width = '100vw';
    topbg.style.top = '0';
    topbg.style.borderRadius = '0';
    mainlayer.style.right = "8%";
    nav.style.top = '20px';
    lateralbar.style.left = '60px';
    lateralbar.style.height = '95%';
    porfolio.style.paddingRight = "0";
    b.removeEventListener('scroll', expandBox);
}

// debugger
function expandBox(e) {
    for (let i = 0; i <= 1; i++) {
        if (isTrusted === undefined) {
            isTrusted = 1
            return
        };
    };
    if (isTrusted === 1) {
        topbg.style.width = '100vw';
        topbg.style.top = '0';
        topbg.style.borderRadius = '0';
        mainlayer.style.right = "8%";
        nav.style.top = '20px';
        lateralbar.style.left = '60px';
        lateralbar.style.height = '95%';
        porfolio.style.paddingRight = "0";
        this.removeEventListener('scroll', expandBox);
    };
};

b.addEventListener("scroll", expandBox);

function resetPage() {
    if (b.scrollTop === 0) {
        isTrusted = 1
    };
    b.scrollTo(0, 0);
}

document.addEventListener("DOMContentLoaded", resetPage);

// Crear un nuevo elemento div para el cursor
const cursor = document.createElement('div');
cursor.className = 'cursor';

// Crear un nuevo elemento div para el efecto de seguimiento del cursor
const cursorF = document.createElement('div');
cursorF.className = 'cursor-f';

// Inicializar variables para las posiciones del cursor y del ratón
let cursorX = 0;
let cursorY = 0;
let pageX = 0;
let pageY = 0;

// Inicializar variables para el tamaño del cursor y su efecto de seguimiento
let size = 8;
let sizeF = 36;

// Velocidad a la que el efecto de seguimiento se mueve hacia el cursor
let followSpeed = .05;

// Añadir los elementos del cursor al cuerpo del documento
document.body.appendChild(cursor);
document.body.appendChild(cursorF);

// Si el dispositivo soporta eventos táctiles, ocultar los elementos del cursor
if ('ontouchstart' in document) {
    cursor.style.display = 'none';
    cursorF.style.display = 'none';
}

// Establecer el tamaño inicial de los elementos del cursor
cursor.style.setProperty('--size', size + 'px');
cursorF.style.setProperty('--size', sizeF + 'px');

// Añadir un evento de escucha para el movimiento del ratón
b.addEventListener('mousemove', function (e) {
    // Obtenemos las coordenadas del ratón relativas al elemento que se desplaza
    const rect = b.getBoundingClientRect();
    const x = e.clientX - rect.left + b.scrollLeft;
    const y = e.clientY - rect.top + b.scrollTop;

    // Actualizar la posición del ratón
    pageX = x;
    pageY = y;

    // Mover el cursor a la posición actual del ratón
    cursor.style.left = x - size / 2 + 'px';
    cursor.style.top = y - size / 2 + 'px';
});

// Esta función es una función de interpolación lineal que se utiliza para suavizar el movimiento del efecto de seguimiento del cursor.
function lerp(start, end, amount) {
    return (1 - amount) * start + amount * end
}

// Iniciar un bucle que mueve suavemente el efecto de seguimiento hacia la posición actual del ratón
function loop() {
    cursorX = lerp(cursorX, pageX, followSpeed);
    cursorY = lerp(cursorY, pageY, followSpeed);
    cursorF.style.top = cursorY - sizeF / 5 + 'px';
    cursorF.style.left = cursorX - sizeF / 5 + 'px';
    requestAnimationFrame(loop);
}

loop();

// Inicializar variables para el seguimiento de los eventos de pulsación del ratón
let startY;
let endY;
let clicked = false;

// Función para manejar el evento de pulsación del ratón
function mousedown(e) {
    // Aumentar el tamaño del cursor
    gsap.to(cursor, { scale: 4.5 });
    gsap.to(cursorF, { scale: .4 });

    // Marcar que el botón del ratón está pulsado
    clicked = true;
}

// Función para manejar el evento de liberación del ratón
function mouseup(e) {
    // Restaurar el tamaño original del cursor
    gsap.to(cursor, { scale: 1 });
    gsap.to(cursorF, { scale: 1 });

    // Marcar que el botón del ratón ha sido liberado
    clicked = false;
}

// Añadir eventos de escucha para los eventos de pulsación y liberación del ratón
document.addEventListener('mousedown', mousedown, false);
document.addEventListener('mouseup', mouseup, false);

// Añadir eventos de escucha para los eventos táctiles equivalentes
document.addEventListener('touchstart', mousedown, false);
document.addEventListener('touchend', mouseup, false);

