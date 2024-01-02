const d = document;
// debugger
const celsius = d.querySelector("#Celsius");
const farenheit = d.querySelector("#Farenheit");
//METODO DATE + EVENTOS
let updateOnC;
let updateOnF;
// celsius.addEventListener("change", () => updateOnC = Date.now());
// farenheit.addEventListener("change", () => updateOnF = Date.now());

//METODO ONCHANGE + BANDERA
let bandera;
function banderaC() {
    bandera = "c";
};
function banderaF() {
    bandera = "f";
};



const calcular = () => {
    //METODO DATE + EVENTOS
    if (updateOnC === undefined) {
        updateOnC = 0.0001;
    } else if (updateOnF === undefined) {
        updateOnF = 0.0001;
    };
    // const time = Date.now();
    // if (celsius.value === "" || isNaN(celsius.value)) {
    //     celsius.value = 0;
    // } else if (farenheit.value === "" || isNaN(farenheit.value)) {
    //     farenheit.value = 0;
    // }
    // if (time - updateOnC > time - updateOnF) {
    //     const calcCel = (farenheit.value - 32) * 5 / 9;
    //     celsius.value = calcCel.toFixed(2);
    // } else {
    //     const calcFar = (celsius.value * 9 / 5) + 32;
    //     farenheit.value = calcFar.toFixed(2);
    // }

    //METODO ONCHANGE + BANDERA
    // bandera === "c" ? farenheit.value = ((celsius.value * 9 / 5) + 32).toFixed(2) : celsius.value = ((farenheit.value - 32) * 5 / 9).toFixed(2);

    //METODO ONCHANGE + BANDERA + PLACEHOLDER (PREFERIDO <3)
    if (bandera === "c") {
        farenheit.value = "";
        celsius.setAttribute("placeholder", "");
        const calcFar = ((celsius.value * 9 / 5) + 32).toFixed(2);
        farenheit.setAttribute("placeholder", calcFar);
    } else {
        celsius.value = "";
        farenheit.setAttribute("placeholder", "");
        const calcCel = ((farenheit.value - 32) * 5 / 9).toFixed(2);
        celsius.setAttribute("placeholder", calcCel);
    }
}