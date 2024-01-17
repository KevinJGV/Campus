const d = document;
const b = d.querySelector("body");

function resetPage() {
    b.scrollTo(0, 0);
}

document.addEventListener("DOMContentLoaded", resetPage);

const cursor = document.createElement('div');
cursor.className = 'cursor';
const cursorF = document.createElement('div');
cursorF.className = 'cursor-f';

let cursorX = 0;
let cursorY = 0;
let pageX = 0;
let pageY = 0;

let size = 8;
let sizeF = 36;

let followSpeed = .16;

document.body.appendChild(cursor);
document.body.appendChild(cursorF);

if ('ontouchstart' in document) {
    cursor.style.display = 'none';
    cursorF.style.display = 'none';
}

cursor.style.setProperty('--size', size + 'px');
cursorF.style.setProperty('--size', sizeF + 'px');

b.addEventListener('mousemove', function (e) {
    const rect = b.getBoundingClientRect();
    const x = e.clientX - rect.left + b.scrollLeft;
    const y = e.clientY - rect.top + b.scrollTop;

    pageX = x;
    pageY = y;

    cursor.style.left = x - size / 2 + 'px';
    cursor.style.top = y - size / 2 + 'px';
});

function lerp(start, end, amount) {
    return (1 - amount) * start + amount * end
}

function loop() {
    cursorX = lerp(cursorX, pageX, followSpeed);
    cursorY = lerp(cursorY, pageY, followSpeed);
    cursorF.style.top = cursorY - sizeF / 5 + 'px';
    cursorF.style.left = cursorX - sizeF / 5 + 'px';
    requestAnimationFrame(loop);
}

loop();

let startY;
let endY;
let clicked = false;
function mousedown(e) {
    gsap.to(cursor, { scale: 4.5 });
    gsap.to(cursorF, { scale: .4 });

    clicked = true;
}

function mouseup(e) {
    gsap.to(cursor, { scale: 1 });
    gsap.to(cursorF, { scale: 1 });

    clicked = false;
}

document.addEventListener('mousedown', mousedown, false);
document.addEventListener('mouseup', mouseup, false);

document.addEventListener('touchstart', mousedown, false);
document.addEventListener('touchend', mouseup, false);


/// CODIGO DE FUNCIONALIDADES


//Botones
const tier1 = d.querySelector("#tier1");
const añadir1 = d.querySelector("#añadir1");
const subtier1 = d.querySelector("#subtier1");
const couching = d.querySelector(".couchingCounter");
const tier2 = d.querySelector("#tier2");
const añadir2 = d.querySelector("#añadir2");
const subtier2 = d.querySelector("#subtier2");
const consults = d.querySelector(".consultingCounter");
const shop = d.querySelector(".shop");

//Botones menos-mas e Inputs

const CountU = d.querySelector("#inputCountU");
const CountUmore = d.querySelector("#añadir1_more");
const CountUless = d.querySelector("#añadir1_less");
const inputCountU1 = d.querySelector("#inputCountU_1");
const CountUEl1more = d.querySelector("#añadir1_op1_more");
const CountUEl1less = d.querySelector("#añadir1_op1_less");
const inputCountU2 = d.querySelector("#inputCountU_2");
const CountUEl2more = d.querySelector("#añadir1_op2_more");
const CountUEl2less = d.querySelector("#añadir1_op2_less");
const inputCountU3 = d.querySelector("#inputCountU_3");
const CountUEl3more = d.querySelector("#añadir1_op3_more");
const CountUEl3less = d.querySelector("#añadir1_op3_less");

//Eventos de click

añadir1.addEventListener("click", () => {
    subtier1.classList.toggle("hidden");
    tier2.classList.toggle("hidden");
    couching.classList.toggle("hidden");
    shop.classList.toggle("hidden");
});

añadir2.addEventListener("click", () => {
    subtier2.classList.toggle("hidden");
    tier1.classList.toggle("hidden");
    consults.classList.toggle("hidden");
    shop.classList.toggle("hidden");
});

CountUmore.addEventListener("click", () => {
    const InputValue = Number(CountU.value);
    
})