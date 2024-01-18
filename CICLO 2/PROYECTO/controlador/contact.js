const d = document;
const b = d.querySelector("body");

// function resetPage() {
//     b.scrollTo(0, 0);
// }

// document.addEventListener("DOMContentLoaded", resetPage);

// const cursor = document.createElement('div');
// cursor.className = 'cursor';
// const cursorF = document.createElement('div');
// cursorF.className = 'cursor-f';

// let cursorX = 0;
// let cursorY = 0;
// let pageX = 0;
// let pageY = 0;

// let size = 8;
// let sizeF = 36;

// let followSpeed = .16;

// document.body.appendChild(cursor);
// document.body.appendChild(cursorF);

// if ('ontouchstart' in document) {
//     cursor.style.display = 'none';
//     cursorF.style.display = 'none';
// }

// cursor.style.setProperty('--size', size + 'px');
// cursorF.style.setProperty('--size', sizeF + 'px');

// b.addEventListener('mousemove', function (e) {
//     const rect = b.getBoundingClientRect();
//     const x = e.clientX - rect.left + b.scrollLeft;
//     const y = e.clientY - rect.top + b.scrollTop;

//     pageX = x;
//     pageY = y;

//     cursor.style.left = x - size / 2 + 'px';
//     cursor.style.top = y - size / 2 + 'px';
// });

// function lerp(start, end, amount) {
//     return (1 - amount) * start + amount * end
// }

// function loop() {
//     cursorX = lerp(cursorX, pageX, followSpeed);
//     cursorY = lerp(cursorY, pageY, followSpeed);
//     cursorF.style.top = cursorY - sizeF / 5 + 'px';
//     cursorF.style.left = cursorX - sizeF / 5 + 'px';
//     requestAnimationFrame(loop);
// }

// loop();

// let startY;
// let endY;
// let clicked = false;
// function mousedown(e) {
//     gsap.to(cursor, { scale: 4.5 });
//     gsap.to(cursorF, { scale: .4 });

//     clicked = true;
// }

// function mouseup(e) {
//     gsap.to(cursor, { scale: 1 });
//     gsap.to(cursorF, { scale: 1 });

//     clicked = false;
// }

// document.addEventListener('mousedown', mousedown, false);
// document.addEventListener('mouseup', mouseup, false);

// document.addEventListener('touchstart', mousedown, false);
// document.addEventListener('touchend', mouseup, false);


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

//Banderas
let tier;

//Botones menos-mas e Inputs Mentoria

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

const countinputarrU = [CountU, inputCountU1, inputCountU2, inputCountU3];
const countmorearrU = [CountUmore, CountUEl1more, CountUEl2more, CountUEl3more];
const countlessarrU = [CountUless, CountUEl1less, CountUEl2less, CountUEl3less];
//Eventos de click

añadir1.addEventListener("click", () => {
    subtier1.classList.toggle("hidden");
    tier2.classList.toggle("hidden");
    couching.classList.toggle("hidden");
    shop.classList.toggle("hidden");
    CountU.value = 1;
    añadir1.classList.toggle("hidden");
    updateCart(CountU);
    tier = 1;
});

for (let counter of countmorearrU) {
    counter.addEventListener("click", () => {
        const index = countmorearrU.indexOf(counter);
        const input = countinputarrU[index];
        let InputValue = Number(input.value);
        InputValue += 1;
        input.value = InputValue;
        updateCart(input);
    })
};

for (let counter of countlessarrU) {
    counter.addEventListener("click", () => {
        const index = countlessarrU.indexOf(counter);
        const input = countinputarrU[index];
        let InputValue = Number(input.value);
        if (index === 0) {
            InputValue--;
            if (InputValue === 0) {
                for (let input of countinputarrU) {
                    input.value = "";
                };
                subtier1.classList.toggle("hidden");
                tier2.classList.toggle("hidden");
                couching.classList.toggle("hidden");
                shop.classList.toggle("hidden");
                añadir1.classList.toggle("hidden");
                updateCart(input);
                tier = undefined;
            } else {
                input.value = InputValue;
                updateCart(input);
            }
        } else {
            InputValue--;
            if (InputValue < 0) {
                input.value = 0;
            } else {
                input.value = InputValue;
            }
        }
    })
};

//Botones menos-mas e Inputs Consultoría

const CountE = d.querySelector("#inputCountE");
const CountEmore = d.querySelector("#añadir2_more");
const CountEless = d.querySelector("#añadir2_less");
const inputCountE1 = d.querySelector("#inputCountE_1");
const CountEEl1more = d.querySelector("#añadir2_op1_more");
const CountEEl1less = d.querySelector("#añadir2_op1_less");
const inputCountE2 = d.querySelector("#inputCountE_2");
const CountEEl2more = d.querySelector("#añadir2_op2_more");
const CountEEl2less = d.querySelector("#añadir2_op2_less");
const inputCountE3 = d.querySelector("#inputCountE_3");
const CountEEl3more = d.querySelector("#añadir2_op3_more");
const CountEEl3less = d.querySelector("#añadir2_op3_less");

const countinputarrE = [CountE, inputCountE1, inputCountE2, inputCountE3];
const countmorearrE = [CountEmore, CountEEl1more, CountEEl2more, CountEEl3more];
const countlessarrE = [CountEless, CountEEl1less, CountEEl2less, CountEEl3less];

//Eventos de click

añadir2.addEventListener("click", () => {
    subtier2.classList.toggle("hidden");
    tier1.classList.toggle("hidden");
    consults.classList.toggle("hidden");
    shop.classList.toggle("hidden");
    CountE.value = 1;
    añadir2.classList.toggle("hidden");
    updateCart(CountE);
    tier = 2;
});

for (let counter of countmorearrE) {
    counter.addEventListener("click", () => {
        const index = countmorearrE.indexOf(counter);
        const input = countinputarrE[index];
        let InputValue = Number(input.value);
        InputValue++;
        input.value = InputValue
        if (index === 0) {
            updateCart(input);
        }
    })
};

for (let counter of countlessarrE) {
    counter.addEventListener("click", () => {
        const index = countlessarrE.indexOf(counter);
        const input = countinputarrE[index];
        let InputValue = Number(input.value);
        if (index === 0) {
            InputValue--;
            if (InputValue === 0) {
                for (let input of countinputarrE) {
                    input.value = "";
                };
                subtier2.classList.toggle("hidden");
                tier1.classList.toggle("hidden");
                consults.classList.toggle("hidden");
                shop.classList.toggle("hidden");
                añadir2.classList.toggle("hidden");
                b.scrollTo(0, 500);
                updateCart(input);
                tier = undefined;
            } else {
                input.value = InputValue;
                updateCart(input);
            }
        } else {
            InputValue--;
            if (InputValue < 0) {
                input.value = 0;
            } else {
                input.value = InputValue;
            }
        }
    })
};

// d.addEventListener("DOMContentLoaded", () => {
//     const allInputs = d.querySelectorAll("input");
//     for (let input of allInputs) {
//         input.value = "";
//     }
// })

// Añadir al carrito
const query = d.querySelector(".query");
const mobilequery = d.querySelector(".mobilecartdata");
const mobilequery_background = d.querySelector(".mobilecart");
const totalCount = d.querySelector(".tierShoppedCantidad");
const inputflags = [CountE, CountU];

function updateCart(elem) {
    const event = new Event('input');
    elem.dispatchEvent(event);
}

for (let input of inputflags) {
    input.addEventListener("input", () => {
        mobilequery.textContent = "";
        query.textContent = "";
        totalCount.textContent = "";
        query.insertAdjacentText("afterbegin", input.value);
        mobilequery.insertAdjacentText("afterbegin", input.value);
        totalCount.insertAdjacentText("afterbegin", `x${input.value}`)
        if (mobilequery.textContent !== "") {
            mobilequery_background.style.backgroundColor = "#00FF5B"
        } else {
            mobilequery_background.style.backgroundColor = "#FFF"
        }
    })
}

//Shop-Data


