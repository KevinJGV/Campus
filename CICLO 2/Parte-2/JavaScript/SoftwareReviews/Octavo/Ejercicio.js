function tiempo() {
    let fecha = new Date();
    let hora = fecha.getHours();
    let minutos = fecha.getMinutes();
    let segundos = fecha.getSeconds();
    return `${hora}:${minutos}:${segundos}`;
};
const d = document;
const container = d.querySelector(".container");
const displaya = d.createElement("div");
displaya.classList.add("item");
displaya.insertAdjacentText("afterbegin", `A [Enviado de: 1] apareció en ` + tiempo());
container.insertAdjacentElement("beforeend", displaya);
const displayb = d.createElement("div");
displayb.classList.add("item");
displayb.insertAdjacentText("afterbegin", `B [Enviado de: 2] apareció en ` + tiempo());
container.insertAdjacentElement("beforeend", displayb);
setTimeout(function displayF() {
    const displayf = d.createElement("div");
    displayf.classList.add("item");
    displayf.insertAdjacentText("afterbegin", `F [Enviado de: 3] apareció en ` + tiempo());
    container.insertAdjacentElement("beforeend", displayf);
}, 7000);
setTimeout(function displayC() {
    const displayc = d.createElement("div");
    displayc.classList.add("item");
    displayc.insertAdjacentText("afterbegin", `C [Enviado de: 4] apareció en ` + tiempo());
    container.insertAdjacentElement("beforeend", displayc);
}, 5000);
setTimeout(function delayD() {
    setTimeout(function displayD() {
        const displayd = d.createElement("div");
        displayd.classList.add("item");
        displayd.insertAdjacentText("afterbegin", `D [Enviado de: 5] apareció en ` + tiempo());
        container.insertAdjacentElement("beforeend", displayd);
        setTimeout(function displayE() {
            const displaye = d.createElement("div");
            displaye.classList.add("item");
            displaye.insertAdjacentText("afterbegin", `E [Enviado de: 6] apareció en ` + tiempo());
            container.insertAdjacentElement("beforeend", displaye);
            setTimeout(function displayG() {
                const displayg = d.createElement("div");
                displayg.classList.add("item");
                displayg.insertAdjacentText("afterbegin", `G [Enviado de: 7] apareció en ` + tiempo());
                container.insertAdjacentElement("beforeend", displayg);
                setTimeout(function displayH() {
                    const displayh = d.createElement("div");
                    displayh.classList.add("item");
                    displayh.insertAdjacentText("afterbegin", `H [Enviado de: 8] apareció en ` + tiempo());
                    container.insertAdjacentElement("beforeend", displayh);
                }, 3000);
            }, 2000);
        }, 2000);
    }, 0.6 * 1000 + (Math.floor(Math.random() * 2) * 1000));
}, 2000);
