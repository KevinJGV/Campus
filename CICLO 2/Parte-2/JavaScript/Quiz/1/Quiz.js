// Inicializacion de datos y definiciones

function proceso(prestamo, interes, cuotas) {
    //Definicion de datos valor
    debugger
    let interes_a = prestamo * interes;
    let interes_m = Number((interes_a / cuotas).toFixed(0));
    let capital = Number((prestamo / cuotas).toFixed(0));
    let total_deuda = prestamo + interes_a;
    let deuda_mensual = capital + interes_m;

    //Tabla 1 en la web
    const tabla1 = (prestamo, interes, cuotas, total_deuda, deuda_mensual) => {
        const tabla1 = document.querySelector("#tabla1");
        const fragmento = document.createDocumentFragment();
        const table = document.createElement("table");
        const tabla1map = new Map([["Monto del credito", prestamo],
        ["Tasa de interés (anual)", interes],
        ["Número de pagos (Mensuales)", cuotas],
        ["Valor total", total_deuda],
        ["Valor mensual", deuda_mensual]]);
        // Escritura en html
        tabla1map.forEach((valor, clave) => {
            const tr = document.createElement("tr");
            const td1 = document.createElement("td");
            td1.insertAdjacentText("afterbegin", clave);
            tr.insertAdjacentElement("afterbegin", td1);
            const td2 = document.createElement("td");
            td2.insertAdjacentText("afterbegin", valor);
            tr.insertAdjacentElement("beforeend", td2);
            table.insertAdjacentElement("beforeend", tr)
        });
        fragmento.insertAdjacentElement("afterbegin", table)
        tabla1.insertAdjacentElement("afterbegin", fragmento)
    };

    tabla1(prestamo, interes, cuotas, total_deuda, deuda_mensual);

    //Tabla 2 en la web
    const tabla2 = (prestamo, total_deuda, capital, interes_m, interes_a) => {
        //Preparacion de tabla
        const tabla2 = document.querySelector("#tabla2")
        const fragmento = document.createDocumentFragment();
        const table = document.createElement("table");
        //Encabezado
        const thead = document.createElement("thead");
        let row = document.createElement("tr");
        for (let i = 0; i < 6; i++) {
            let th = document.createElement("th");
            if (i == 0) {
                th.insertAdjacentText("afterbegin", "Mes");
                row.insertAdjacentElement("beforeend", th)
            } else if (i == 1) {
                th.insertAdjacentText("afterbegin", "Valor");
                row.insertAdjacentElement("beforeend", th)
            } else if (i == 2) {
                th.insertAdjacentText("afterbegin", "Valor total");
                row.insertAdjacentElement("beforeend", th)
            } else if (i == 3) {
                th.insertAdjacentText("afterbegin", "Capital");
                row.insertAdjacentElement("beforeend", th)
            } else if (i == 4) {
                th.insertAdjacentText("afterbegin", "Interes");
                row.insertAdjacentElement("beforeend", th)
            } else {
                th.insertAdjacentText("afterbegin", "Total");
                row.insertAdjacentElement("beforeend", th)
            }
        }
        thead.insertAdjacentElement("afterbegin", row)
        table.insertAdjacentElement("beforeend", thead)
        //Cuerpo
        const map = new Map();
        const bdd = new Array(prestamo, total_deuda, capital, interes_m, deuda_mensual);

        for (let itera = 1; itera < cuotas + 1; itera++) {
            if (itera == 1) {
                //Cuerpo de la tabla
                let bdd_copia = bdd.slice();
                map.set(itera, bdd_copia);
                let tbody = document.createElement("tbody");
                let row = document.createElement("tr");
                for (let i = 0; i < 6; i++) {
                    let th = document.createElement("th");
                    if (i == 0) {
                        th.insertAdjacentText("afterbegin", itera);
                        row.insertAdjacentElement("beforeend", th)
                    } else if (i == 1) {
                        th.insertAdjacentText("afterbegin", map.get(itera)[0]);
                        row.insertAdjacentElement("beforeend", th)
                    } else if (i == 2) {
                        th.insertAdjacentText("afterbegin", map.get(itera)[1]);
                        row.insertAdjacentElement("beforeend", th)
                    } else if (i == 3) {
                        th.insertAdjacentText("afterbegin", map.get(itera)[2]);
                        row.insertAdjacentElement("beforeend", th)
                    } else if (i == 4) {
                        th.insertAdjacentText("afterbegin", map.get(itera)[3]);
                        row.insertAdjacentElement("beforeend", th)
                    } else {
                        th.insertAdjacentText("afterbegin", map.get(itera)[4]);
                        row.insertAdjacentElement("beforeend", th)
                        break
                    }
                }
                tbody.insertAdjacentElement("afterbegin", row)
                table.insertAdjacentElement("beforeend", tbody)
            } else {
                bdd[0] -= capital;
                bdd[1] -= deuda_mensual;
                let bdd_copia = bdd.slice();
                map.set(itera, bdd_copia);
                let tbody = document.querySelector("tbody")
                let row = document.createElement("tr");
                for (let i = 0; i < 6; i++) {
                    let th = document.createElement("th");
                    if (i == 0) {
                        th.insertAdjacentText("afterbegin", itera);
                        row.insertAdjacentElement("beforeend", th)
                    } else if (i == 1) {
                        th.insertAdjacentText("afterbegin", map.get(itera)[0]);
                        row.insertAdjacentElement("beforeend", th)
                    } else if (i == 2) {
                        th.insertAdjacentText("afterbegin", map.get(itera)[1]);
                        row.insertAdjacentElement("beforeend", th)
                    } else if (i == 3) {
                        th.insertAdjacentText("afterbegin", map.get(itera)[2]);
                        row.insertAdjacentElement("beforeend", th)
                    } else if (i == 4) {
                        th.insertAdjacentText("afterbegin", map.get(itera)[3]);
                        row.insertAdjacentElement("beforeend", th)
                    } else {
                        th.insertAdjacentText("afterbegin", map.get(itera)[4]);
                        row.insertAdjacentElement("beforeend", th)
                        break
                    }
                }
                tbody.insertAdjacentElement("afterbegin", row)
                table.insertAdjacentElement("beforeend", tbody)
            }
        };
        fragmento.insertAdjacentElement("afterbegin", table)
        tabla2.insertAdjacentElement("afterbegin", fragmento)
    };
    tabla2(prestamo, total_deuda, capital, interes_m, interes_a);
}

const input_prestamo = document.querySelector("#prestamo");
const input_interes = document.querySelector("#intereses");
const input_pagos = document.querySelector("#pagos");

proceso(input_prestamo.value, input_interes.value, input_pagos.value)