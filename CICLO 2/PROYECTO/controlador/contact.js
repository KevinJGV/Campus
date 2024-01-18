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


//Funciones
async function fetchjson(index, op, elem, indexelem, target) {
    try {
        let response = await fetch('http://localhost:3000/tiers', {
            method: 'GET',
            headers: {
                'Content-type': 'application/json; charset=UTF-8',
            }
        });
        const json = await response.json();
        const objeto = Object.keys(json[index].elementos);
        const propiedad = objeto[indexelem]
        const elemento = json[index].elementos[propiedad];

        switch (op) {
            case 1:
                elem.textContent = "";
                elem.insertAdjacentHTML("afterbegin", elemento.img);
                break
            case 2:
                elem.textContent = propiedad;
                break
            case 3:
                const tierShopped = d.querySelector(".tierShopped");
                const tierPrecio = d.querySelector(".tierPrecio");
                tierShopped.textContent = json[index].nombre;
                tierPrecio.textContent = `$${json[index].valor} C/U`;
                break
            case 4:
                elem.textContent = "";
                elem.insertAdjacentText("afterbegin", propiedad);
                break
            case 5:
                elem.textContent = "";
                elem.insertAdjacentText("afterbegin", elemento.def);
                break
            case 6:
                const x = Number(elem.value);
                const res = x * JSON.parse(json[index].valor);
                total_flag = res;
                target.textContent = `$${res}`;
                break
        }
    } catch (e) {
        console.error("Ocurrió un error con JSON-SERVER", e);
    }
};

function updateCart(elem) {
    const event = new Event('input');
    elem.dispatchEvent(event);
}

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
const shop_body = d.querySelector(".shop_body");

const añadir = [añadir1, añadir2]
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

//Tier1 tienda
const tier1_img1 = d.querySelector("#tier1_img1");
const tier1_img2 = d.querySelector("#tier1_img2");
const tier1_img3 = d.querySelector("#tier1_img3");
const tier1_p1 = d.querySelector("#tier1_p1");
const tier1_p2 = d.querySelector("#tier1_p2");
const tier1_p3 = d.querySelector("#tier1_p3");

const tier1_imgs = [tier1_img1, tier1_img2, tier1_img3];
const tier1_ps = [tier1_p1, tier1_p2, tier1_p3];

for (let img of tier1_imgs) {
    const index = tier1_imgs.indexOf(img);
    fetchjson(0, 1, img, index);
};
for (let p of tier1_ps) {
    const index = tier1_ps.indexOf(p);
    fetchjson(0, 2, p, index);
}
const tierShopped = d.querySelector(".tierShopped");
let total_flag;
const total = d.querySelector("#totalamount");
//Eventos de click

for (let boton of añadir) {
    const index = añadir.indexOf(boton);
    if (index === 0) {
        boton.addEventListener("click", () => {
            subtier1.classList.toggle("hidden");
            tier2.classList.toggle("hidden");
            couching.classList.toggle("hidden");
            shop.classList.toggle("hidden");
            CountU.value = 1;
            total.textContent = `$${99}`;
            total_flag = 99;
            boton.classList.toggle("hidden");
            updateCart(CountU);
            tier = 0;
            fetchjson(index, 3)
        });
    } else {
        boton.addEventListener("click", () => {
            subtier2.classList.toggle("hidden");
            tier1.classList.toggle("hidden");
            consults.classList.toggle("hidden");
            shop.classList.toggle("hidden");
            CountE.value = 1;
            total.textContent = `$${199}`;
            total_flag = 199
            boton.classList.toggle("hidden");
            updateCart(CountE);
            tier = 1;
            fetchjson(index, 3)
        });
    }
};

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
                shop_body.classList.add("hidden");
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
        updateCart(input);
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
const countinputarrEitems = [inputCountE1, inputCountE2, inputCountE3];
const countmorearrE = [CountEmore, CountEEl1more, CountEEl2more, CountEEl3more];
const countlessarrE = [CountEless, CountEEl1less, CountEEl2less, CountEEl3less];

//Tier2 tienda
const tier2_img1 = d.querySelector("#tier2_img1");
const tier2_img2 = d.querySelector("#tier2_img2");
const tier2_img3 = d.querySelector("#tier2_img3");
const tier2_p1 = d.querySelector("#tier2_p1");
const tier2_p2 = d.querySelector("#tier2_p2");
const tier2_p3 = d.querySelector("#tier2_p3");

const tier2_imgs = [tier2_img1, tier2_img2, tier2_img3];
const tier2_ps = [tier2_p1, tier2_p2, tier2_p3];

for (let img of tier2_imgs) {
    const index = tier2_imgs.indexOf(img);
    fetchjson(1, 1, img, index);
};
for (let p of tier2_ps) {
    const index = tier2_ps.indexOf(p);
    fetchjson(1, 2, p, index);
}


//Eventos de click

for (let counter of countmorearrE) {
    counter.addEventListener("click", () => {
        const index = countmorearrE.indexOf(counter);
        const input = countinputarrE[index];
        let InputValue = Number(input.value);
        InputValue++;
        input.value = InputValue
        updateCart(input);
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
                shop_body.classList.add("hidden");
                añadir2.classList.toggle("hidden");
                b.scrollTo(0, 500);
                updateCart(input);
                tier = undefined;
            } else {
                input.value = InputValue;
                for (let input of countinputarrEitems) {
                    input.value = 0;
                }
                updateCart(input);
            }
        } else {
            InputValue--;
            if (InputValue < 0) {
                input.value = 0;
            } else {
                input.value = InputValue;
                for (let input of countinputarrEitems) {
                    input.value = 0;
                }
            }
        }
        updateCart(input);
    })
};


// Añadir al carrito
const query = d.querySelector(".query");
const mobilequery = d.querySelector(".mobilecartdata");
const mobilequery_background = d.querySelector(".mobilecart");
const totalCount = d.querySelector(".tierShoppedCantidad");
const inputflags = [CountU, CountE];
const checkout = d.querySelector(".checkout");
const salir = d.querySelector(".cancelar");

for (let input of inputflags) {
    input.addEventListener("input", () => {
        mobilequery.textContent = "";
        query.textContent = "";
        totalCount.textContent = "";
        query.insertAdjacentText("afterbegin", input.value);
        mobilequery.insertAdjacentText("afterbegin", input.value);
        totalCount.insertAdjacentText("afterbegin", `x${input.value} `)
        if (mobilequery.textContent !== "") {
            mobilequery_background.style.backgroundColor = "#00FF5B"
        } else {
            mobilequery_background.style.backgroundColor = "#FFF"
        }

    })
}

// mobilequery_background.addEventListener("click", () => {
//     checkout.classList.toggle("hidden");
// })

salir.addEventListener("click", () => {
    checkout.classList.toggle("hidden");
})

//Shop-Data
const item1Cantidad = d.querySelector("#item1Cantidad");
const item2Cantidad = d.querySelector("#item2Cantidad");
const item3Cantidad = d.querySelector("#item3Cantidad");
const element1img = d.querySelector("#element1img");
const element2img = d.querySelector("#element2img");
const element3img = d.querySelector("#element3img");
const element1name = d.querySelector("#element1name");
const element2name = d.querySelector("#element2name");
const element3name = d.querySelector("#element3name");
const element1des = d.querySelector("#element1des");
const element2des = d.querySelector("#element2des");
const element3des = d.querySelector("#element3des");
const element1 = d.querySelector("#element1");
const element2 = d.querySelector("#element2");
const element3 = d.querySelector("#element3");
const itemsCantidad = [item1Cantidad, item2Cantidad, item3Cantidad];
const elementImgs = [element1img, element2img, element3img];
for (let img of elementImgs) {
    const index = elementImgs.indexOf(img);
    for (let boton of añadir) {
        boton.addEventListener("click", () => {
            fetchjson(tier, 1, img, index)
        })
    }
};
const elementNames = [element1name, element2name, element3name];
for (let name of elementNames) {
    const index = elementNames.indexOf(name);
    for (let boton of añadir) {
        boton.addEventListener("click", () => {
            fetchjson(tier, 4, name, index)
        })
    }
};
const elementDes = [element1des, element2des, element3des];
for (let des of elementDes) {
    const index = elementDes.indexOf(des);
    for (let boton of añadir) {
        boton.addEventListener("click", () => {
            fetchjson(tier, 5, des, index)
        })
    }
};
const elements = [element1, element2, element3]
const countBox1Arr = [inputCountU1, inputCountE1];
const countBox2Arr = [inputCountU2, inputCountE2];
const countBox3Arr = [inputCountU3, inputCountE3];
const AllSubInputarr = [inputCountU1, inputCountU2, inputCountU3, inputCountE1, inputCountE2, inputCountE3];

for (let input of countBox1Arr) {
    input.addEventListener("input", () => {
        if (input.value === "0" || input.value === "") {
            element1.classList.add("hidden");
        } else {
            element1.classList.remove("hidden");
        }
        item1Cantidad.textContent = "";
        item1Cantidad.insertAdjacentText("afterbegin", `x${input.value} `)
    })
}

for (let input of countBox2Arr) {
    input.addEventListener("input", () => {
        if (input.value === "0" || input.value === "") {
            element2.classList.add("hidden");
        } else {
            element2.classList.remove("hidden");
        }
        item2Cantidad.textContent = "";
        item2Cantidad.insertAdjacentText("afterbegin", `x${input.value} `)
    })
}

for (let input of countBox3Arr) {
    input.addEventListener("input", () => {
        if (input.value === "0" || input.value === "") {
            element3.classList.add("hidden");
        } else {
            element3.classList.remove("hidden");
        }
        item3Cantidad.textContent = "";
        item3Cantidad.insertAdjacentText("afterbegin", `x${input.value} `)
    })
}


for (let input of AllSubInputarr) {
    input.addEventListener("input", () => {
        let condicion = AllSubInputarr.every(i => i.value.trim() === "" || i.value === "0");
        if (condicion) {
            shop_body.classList.add("hidden");
        } else {
            shop_body.classList.remove("hidden");
        }
    })
}





const morebuttons = [CountUEl1more, CountUEl2more, CountUEl3more, CountEEl1more, CountEEl2more, CountEEl3more];

for (let input of AllSubInputarr) {
    input.addEventListener("input", updateButtons);
}

for (let flag of inputflags) {
    flag.addEventListener("input", updateButtons);

}

function updateButtons() {
    let maxSum = 0;
    for (let flag of inputflags) {
        maxSum += 2 * Number(flag.value);
    }
    let sum = AllSubInputarr.reduce((a, b) => a + Number(b.value), 0);
    for (let button of morebuttons) {
        if (sum === maxSum) {
            button.setAttribute("disabled", "");
        } else {
            button.removeAttribute("disabled");
        }
    }
}


for (let flag of inputflags) {
    const index = inputflags.indexOf(flag);

    flag.addEventListener("input", () => fetchjson(tier, 6, flag, index, total))
}

//GO CHECK

const gocheck = d.querySelector(".gocheck");
gocheck.addEventListener("click", () => checkout.classList.toggle("hidden"));

function fetchpay(total, servicio) {
    // const pay_form = d.querySelector("#pay_form");
    const username = d.querySelector("#checkout_nombre");
    const email = d.querySelector("#checkout_email");
    const contacto = d.querySelector("#contacto");
    const fecha = d.querySelector("#fecha");
    const descripcion = d.querySelector("#descripcion_final");
    const f1 = d.querySelector(".frame1");
    const f2 = d.querySelector(".frame2");
    const datos = {
        "username": username.value,
        "email": email.value,
        "contacto": contacto.value,
        "fecha": fecha.value,
        "descripcion": descripcion.value,
        "servicio": servicio.textContent,
        "total": total,
    };
    json = JSON.stringify(datos);
    f1.classList.add("hidden");
    f2.classList.remove("hidden");
    fetch('http://localhost:3000/citas_agendadas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=UTF-8',
        },
        body: json,
    })
        .then(res => res.json())
        .then(data => {
            console.log('Éxito:', datos);
        }).catch(e => console.error("Ocurrió un error Enviando su formulario."));
};

const pago = d.querySelector("#pago");

pago.addEventListener("click", () => fetchpay(total_flag, tierShopped))


async function fetchmsj() {
    const nombre = d.querySelector("#nombre");
    const email = d.querySelector("#email");
    const contacto = d.querySelector("#contacto");
    const fecha = d.querySelector("#fecha");
    const descripcion = d.querySelector("#descripcion");
    const datos = {
        "username": nombre.value,
        "email": email.value,
        "descripcion": descripcion.value,
    };
    json = JSON.stringify(datos);
    await new Promise(resolve => setTimeout(resolve, 2000));
    fetch('http://localhost:3000/mensajes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=UTF-8',
        },
        body: json,
    })
        .then(res => res.json())
        .then(data => {
            console.log('Éxito:', datos);
        }).catch(e => console.error("Ocurrió un error Enviando su formulario."));
};

const mensaje = d.querySelector("#mensaje");

mensaje.addEventListener("click", fetchmsj)

d.addEventListener("DOMContentLoaded", () => {
    const allInputs = d.querySelectorAll("input");
    const text = d.querySelectorAll("textarea");
    for (let input of allInputs) {
        input.value = "";
    };
    for (let input of text) {
        input.value = "";
    }
})