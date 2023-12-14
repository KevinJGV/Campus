const bdd = new Map();
const bdd_contador = new Map();
let reg = 0;
let pagadas = 0;
let program = true;
while (program === true) {
    let op = prompt("ADMINISTRADOR DE FACTURAS\n1 - Ingresar facturas\n2 - Pagar facturas\n3 - Ver facturas\n0 - Salir");
    //debugger
    switch (op) {
        case "1":
            while (op == "1") {
                let key = prompt("Numero de factura");
                if (key != "") {
                    let value_title = prompt("Titular");
                    let value_amount = prompt("Valor a pagar");
                    value_amount = " " + value_amount
                    let arr = [value_title, value_amount];
                    bdd.set(key, arr); bdd_contador.set(key, arr); reg += 1;
                    let listado = "Facturas registradas\n\n";
                    for (let [clave, valor] of bdd) {
                        listado += clave + ": " + valor + "\n";
                    };
                    alert(listado);
                    let flag = prompt("Continuar? y/n");
                    if (flag == "n") {
                        break;
                    }
                } else {
                    alert("Ingrese una factura válida.")
                }
            }
            break;
        case "2":
            while (op == "2") {
                let key = prompt("Numero de factura");
                if (bdd.has(key)) {
                    let userConfirm = confirm("Confirmar pago de factura y/n")
                    if (userConfirm) {
                        bdd.delete(key)
                        pagadas += 1
                        let listado = "Facturas registradas\n\n";
                        for (let [clave, valor] of bdd) {
                            listado += clave + ": " + valor + "\n";
                        };
                        alert("Factura pagada exitosamente.")
                    } else {
                        alert("Operación abortada.")
                    }
                } else {
                    alert("Factura inexistente.")
                    break;
                }
                let flag = prompt("Continuar? y/n");
                if (flag == "n") {
                    break;
                }
            }
            break;
        case "3":
            let listado_glob = "Facturas registradas\n\n";
            for (let [clave, valor] of bdd) {
                listado_glob += clave + ": " + valor + "\n";
            };
            if (listado_glob === "Facturas registradas\n\n") {
                alert("No hay facturas registradas.")
            } else {
                alert(listado_glob);
            }
            break;
        case "0":
            program = false;
            break;
    }
}
let listado_final = "Facturas total registradas\n\n";
for (let [clave, valor] of bdd_contador) {
    listado_final += clave + ": " + valor + "\n";
};
alert(listado_final)
alert(`Facturas registradas: ${reg}\nFacturas pagadas: ${pagadas}\nPendientes de cobro: ${bdd.size}`)