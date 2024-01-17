export const d = document;
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

cursor.style.setProperty('--size', size+'px');
cursorF.style.setProperty('--size', sizeF+'px');

b.addEventListener('mousemove', function(e) {
    const rect = b.getBoundingClientRect();
    const x = e.clientX - rect.left + b.scrollLeft;
    const y = e.clientY - rect.top + b.scrollTop;

    pageX = x;
    pageY = y;

    cursor.style.left = x - size/2 + 'px';
    cursor.style.top = y - size/2 + 'px';
  });

function lerp(start, end, amount) {
  return (1-amount)*start+amount*end
}

function loop() {
  cursorX = lerp(cursorX, pageX, followSpeed);
  cursorY = lerp(cursorY, pageY, followSpeed);
  cursorF.style.top = cursorY - sizeF/5 + 'px';
  cursorF.style.left = cursorX - sizeF/5 + 'px';
  requestAnimationFrame(loop);
}

loop();

let startY;
let endY;
let clicked = false;
function mousedown(e) {
    gsap.to(cursor, {scale: 4.5});
    gsap.to(cursorF, {scale: .4});
  
    clicked = true;
  }
  
  function mouseup(e) {
    gsap.to(cursor, {scale: 1});
    gsap.to(cursorF, {scale: 1});
  
    clicked = false;
}

document.addEventListener('mousedown', mousedown, false);
document.addEventListener('mouseup', mouseup, false);

document.addEventListener('touchstart', mousedown, false);
document.addEventListener('touchend', mouseup, false);