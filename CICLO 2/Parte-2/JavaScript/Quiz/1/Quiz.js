function proceso() {
    try {
        const input_prestamo = Number(document.querySelector("#prestamo").value);
        const input_interes = Number(document.querySelector("#intereses").value);
        const input_pagos = Number(document.querySelector("#pagos").value);

        //Throw error
        if (input_prestamo === 0 || isNaN(input_prestamo) || input_interes === 0 || isNaN(input_interes) || input_pagos === 0 || isNaN(input_pagos)) {
            throw new Error("Valores incorrectos, ingrese valores númericos.");
        };
        //Definicion de datos valor
        let interes_a = Number(((input_prestamo * input_interes) / 100).toFixed(0));
        let interes_m = Number((interes_a / input_pagos).toFixed(0));
        let capital = Number((input_prestamo / input_pagos).toFixed(0));
        let total_deuda = input_prestamo + interes_a;
        let deuda_mensual = capital + interes_m;
        const validartablas = () => {
            const tabla1 = document.querySelector("#tabla1");
            const tabla2 = document.querySelector("#tabla2");
            while (tabla1.firstChild) {
                tabla1.removeChild(tabla1.firstChild);
            };
            while (tabla2.firstChild) {
                tabla2.removeChild(tabla2.firstChild);
            }
        };
        validartablas();
        //Tabla 1 en la web
        const tabla1 = (prestamo, interes, cuotas, total_deuda, deuda_mensual) => {
            const tabla1 = document.querySelector("#tabla1");
            const fragmento1 = document.createDocumentFragment();
            const table = document.createElement("table");
            const tabla1map = new Map([["Monto del credito", prestamo],
            ["Tasa de interés (anual)", interes],
            ["Número de pagos (Mensuales)", cuotas],
            ["Valor total", total_deuda],
            ["Valor mensual", deuda_mensual]]);
            // Escritura en html
            let css = 0
            // debugger
            tabla1map.forEach((valor, clave) => {
                const tr = document.createElement("tr");
                const td1 = document.createElement("td");
                td1.insertAdjacentText("afterbegin", clave);
                tr.insertAdjacentElement("afterbegin", td1);
                const td2 = document.createElement("td");
                td2.insertAdjacentText("afterbegin", valor);
                tr.insertAdjacentElement("beforeend", td2);
                if (css % 2 == 0) {
                    tr.classList.add("fila-impar");
                    css++;
                } else {
                    css++
                }
                table.insertAdjacentElement("beforeend", tr);
            });
            fragmento1.appendChild(table);
            tabla1.appendChild(fragmento1);
        };

        tabla1(input_prestamo, input_interes, input_pagos, total_deuda, deuda_mensual);

        //Tabla 2 en la web
        const tabla2 = (prestamo, total_deuda, capital, interes_m, interes_a) => {
            //Preparacion de tabla
            const tabla2 = document.querySelector("#tabla2");
            const fragmento2 = document.createDocumentFragment();
            const table = document.createElement("table");
            //Encabezado
            const thead = document.createElement("thead");
            let row = document.createElement("tr");
            for (let i = 0; i < 6; i++) {
                let th = document.createElement("th");
                if (i == 0) {
                    th.insertAdjacentText("afterbegin", "Mes");
                    row.insertAdjacentElement("beforeend", th);
                } else if (i == 1) {
                    th.insertAdjacentText("afterbegin", "Valor");
                    row.insertAdjacentElement("beforeend", th);
                } else if (i == 2) {
                    th.insertAdjacentText("afterbegin", "Valor total");
                    row.insertAdjacentElement("beforeend", th);
                } else if (i == 3) {
                    th.insertAdjacentText("afterbegin", "Capital");
                    row.insertAdjacentElement("beforeend", th);
                } else if (i == 4) {
                    th.insertAdjacentText("afterbegin", "Interes");
                    row.insertAdjacentElement("beforeend", th);
                } else {
                    th.insertAdjacentText("afterbegin", "Total");
                    row.insertAdjacentElement("beforeend", th);
                }
            }
            thead.insertAdjacentElement("afterbegin", row);
            table.insertAdjacentElement("beforeend", thead);
            //Cuerpo
            const map = new Map();
            const bdd = new Array(prestamo, total_deuda, capital, interes_m, deuda_mensual);
            const tbody = document.createElement("tbody");
            for (let itera = 1; itera < input_pagos + 1; itera++) {
                if (itera == 1) {
                    //Cuerpo de la tabla
                    let bdd_copia = bdd.slice();
                    map.set(itera, bdd_copia);
                    let row = document.createElement("tr");
                    row.classList.add("fila-impar");
                    for (let i = 0; i < 6; i++) {
                        let th = document.createElement("th");
                        if (i == 0) {
                            th.insertAdjacentText("afterbegin", itera);
                            row.insertAdjacentElement("beforeend", th);
                        } else if (i == 1) {
                            th.insertAdjacentText("afterbegin", map.get(itera)[0]);
                            row.insertAdjacentElement("beforeend", th);
                        } else if (i == 2) {
                            th.insertAdjacentText("afterbegin", map.get(itera)[1]);
                            row.insertAdjacentElement("beforeend", th)
                        } else if (i == 3) {
                            th.insertAdjacentText("afterbegin", map.get(itera)[2]);
                            row.insertAdjacentElement("beforeend", th);
                        } else if (i == 4) {
                            th.insertAdjacentText("afterbegin", map.get(itera)[3]);
                            row.insertAdjacentElement("beforeend", th);
                        } else {
                            th.insertAdjacentText("afterbegin", map.get(itera)[4]);
                            row.insertAdjacentElement("beforeend", th);
                        }
                    }
                    tbody.insertAdjacentElement("afterbegin", row);
                } else {
                    bdd[0] -= capital;
                    bdd[1] -= deuda_mensual;
                    let bdd_copia = bdd.slice();
                    map.set(itera, bdd_copia);
                    let row = document.createElement("tr");
                    if (itera % 2 != 0) {
                        row.classList.add("fila-impar");
                    };
                    for (let i = 0; i < 6; i++) {
                        let th = document.createElement("th");
                        if (i == 0) {
                            th.insertAdjacentText("afterbegin", itera);
                            row.insertAdjacentElement("beforeend", th);
                        } else if (i == 1) {
                            th.insertAdjacentText("afterbegin", map.get(itera)[0]);
                            row.insertAdjacentElement("beforeend", th);
                        } else if (i == 2) {
                            th.insertAdjacentText("afterbegin", map.get(itera)[1]);
                            row.insertAdjacentElement("beforeend", th);
                        } else if (i == 3) {
                            th.insertAdjacentText("afterbegin", map.get(itera)[2]);
                            row.insertAdjacentElement("beforeend", th);
                        } else if (i == 4) {
                            th.insertAdjacentText("afterbegin", map.get(itera)[3]);
                            row.insertAdjacentElement("beforeend", th);
                        } else {
                            th.insertAdjacentText("afterbegin", map.get(itera)[4]);
                            row.insertAdjacentElement("beforeend", th);
                            break
                        }
                    };
                    tbody.insertAdjacentElement("beforeend", row);
                };
            };
            table.insertAdjacentElement("beforeend", tbody);
            //Pie
            const footer = document.createElement("tfoot");
            const rowf = document.createElement("tr");
            const cellcapital = document.createElement("th");
            cellcapital.insertAdjacentText("afterbegin", `$${capital}`);
            rowf.insertAdjacentElement("beforeend", cellcapital);
            const cellinteres = document.createElement("th");
            cellinteres.insertAdjacentText("afterbegin", `$${interes_a}`);
            rowf.insertAdjacentElement("beforeend", cellinteres);
            const celltotal = document.createElement("th");
            celltotal.insertAdjacentText("afterbegin", `$${total_deuda}`);
            rowf.insertAdjacentElement("beforeend", celltotal);
            for (let i = 0; i < rowf.children.length; i++) {
                rowf.children[i].classList.add("pie");
            };
            for (let i = 0; i < 3; i++) {
                let cell = document.createElement("th");
                rowf.insertAdjacentElement("afterbegin", cell)
            }
            footer.insertAdjacentElement("afterbegin", rowf);
            table.insertAdjacentElement("beforeend", footer);
            fragmento2.appendChild(table);
            tabla2.appendChild(fragmento2);
        };
        tabla2(input_prestamo, total_deuda, capital, interes_m, interes_a);
    } catch (error) {
        console.error(error);
        alert(error);
    } finally {
        document.querySelector("#prestamo").value = "";
        document.querySelector("#intereses").value = "";
        document.querySelector("#pagos").value = "";
    }
}