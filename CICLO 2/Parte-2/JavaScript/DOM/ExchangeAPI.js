const d = document;
// debugger
const euro = d.querySelector("#euro");
const dolar = d.querySelector("#dolar");

let bandera;
function banderaE() {
    bandera = "e";
};
function banderaD() {
    bandera = "d";
};

const calcular = async () => {
    // debugger
    if (euro.value === "" && dolar.value === "") {
        dolar.setAttribute("placeholder", "0.00");
        euro.setAttribute("placeholder", "0.00");
    } else {
        const res1 = await fetch("https://cdn.dinero.today/api/ecb.json");
        const json1 = await res1.json();
        const res2 = await fetch("http://data.fixer.io/api/latest?access_key=065b7f517bad6f20f0c39bb96fafd4e5&format=1");
        const json2 = await res2.json();
        const eur = json1.rates.EUR;
        const usd = json2.rates.USD;
        if (bandera === "e") {
            dolar.value = "";
            euro.setAttribute("placeholder", "");
            const calcD = (euro.value * usd).toFixed(2);
            dolar.setAttribute("placeholder", calcD);
        } else {
            euro.value = "";
            dolar.setAttribute("placeholder", "");
            const calcE = (dolar.value * eur).toFixed(2);
            euro.setAttribute("placeholder", calcE);
        }
    }
}