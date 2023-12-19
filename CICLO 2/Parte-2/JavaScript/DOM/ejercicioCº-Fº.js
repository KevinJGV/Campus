const d = document
/////////////////////////////////

const calcular = () => {
    const celsius = d.querySelector("#Celsius");
    const farenheit = d.querySelector("#Farenheit");
    const def = new Date();
    if (def < farenheit.valueAsDate) {
        const calcCel = (farenheit.value - 32) * 5 / 9;
        celsius.value = calcCel.toFixed(2);
    } else if (def >= farenheit.valueAsDate) {
        const calcFar = (celsius.value * 9 / 5) + 32;
        farenheit.value = calcFar.toFixed(2);
    }
}

NOTA::::::::::::::::::..

- SOLUCION A: UTILIZAR BANDERAS PARA IDENTIFICAR CUAL ES EL INPUT QUE SE ACTUALIZO
- SOLUCION B: UTILIZAR Date() COMO CONTADOR COMPARATIVO
- SOLUCION C: UTILIZAR onchange
- SOLUCION D: UTILIZAR EL ATRIBUTO PLACEHOLDER PARA MOSTRAR LOS RESULTADOS