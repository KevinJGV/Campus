const d = document;

const login = d.querySelector(".checkout");
const funcionario_screen = d.querySelector(".funcionario");
const login_nombre = d.querySelector("#checkout_nombre");
const login_pass = d.querySelector("#pass");
const login_button = d.querySelector("#login");



login_button.addEventListener('click', async () => {
    try {
        let response = await fetch('http://localhost:4001/usuarios', {
            method: 'GET',
            headers: {
                'Content-type': 'application/json; charset=UTF-8',
            }
        });
        const json = await response.json();
        const usuario = login_nombre.value;
        const pass = login_pass.value;
        for (let user of json) {
            if (user.id === usuario && user.pass === pass) {
                if (user.tipoId === 2) {
                    login.classList.toggle("hidden");
                    funcionario_screen.classList.toggle("hidden");
                } else if (user.tipoId === 3) {
                    break
                }
            }
        }
    } catch (e) {
        console.error("Ocurrió un error con JSON-SERVER", e);
    }
});

//Funcionario

const consulta_input = d.querySelector("#input_consulta");
const consultar = d.querySelector("#consultar");
const cliente = d.querySelector(".contenido");

consultar.addEventListener("submit", async (e) => {
    try {
        let response = await fetch('http://localhost:4001/usuarios', {
            method: 'GET',
            headers: {
                'Content-type': 'application/json; charset=UTF-8',
            }
        });
        const json = await response.json();
        const usuario = consulta_input.value;
        for (let user of json) {
            if (user.id === usuario && user.tipoId === 3) {
                cliente.classList.remove("hidden");
            } else {
                let bandera = true;
                let new_id = Number(prompt("USUARIO NO REGISTRADO\n\nInicio de registro de usuario\n\nCédula del cliente"));
                if (isNaN(new_id) || new_id <= 0 || new_id > 2000000000) {
                    while (bandera) {
                        new_id = Number(prompt("ERROR, INGRESO INVÁLIDO\n\nCédula del cliente"));
                        if (!isNaN(new_id)) {
                            bandera = false;
                        }
                    }
                }
                let new_name = prompt("USUARIO NO REGISTRADO\n\nNombre del cliente");
                let new_pass = Number(prompt("USUARIO NO REGISTRADO\n\nContraseña del cliente con màs de 5 caractéres"));
                if (new_pass.length < 6) {
                    while (bandera) {
                        new_id = Number(prompt("ERROR, INGRESO INVÁLIDO\n\nContraseña del cliente con màs de 5 caractéres"));
                        if (new_pass.length >= 6) {
                            bandera = false;
                        }
                    }
                }
                const datos = {
                    "id": new_id,
                    "pass": new_pass,
                    "nombre": new_name,
                    "tipoId": 3
                };
                response = await fetch('http://localhost:4001/usuarios', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json; charset=UTF-8',
                    },
                    body: datos,
                });
                e.preventDefault()
            }
        }
    } catch (e) {
        console.error("Ocurrió un error con JSON-SERVER", e);
    }
});







d.addEventListener("DOMContentLoaded", () => {
    const allInputs = d.querySelectorAll("input");
    for (let input of allInputs) {
        input.value = "";
    };
})