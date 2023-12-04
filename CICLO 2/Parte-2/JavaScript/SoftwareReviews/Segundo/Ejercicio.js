// PROMPT
let activo = true;
let suma = 0;
let ingresos = 0;
let lista = document.getElementById("lista");

while (activo === true) {
    let prompts = Number(prompt("CALCULADOR PARA MEDIA DE VALORES\n\nIngrese cuantos numeros deseé, para calcular la media de ellos ingrese un numero negativo (Este ultimo no afectara la media)"));
// PARA DEPURAR =>    debugger; console.trace(prompts);
    if (isNaN(prompts)) {
        alert("Ingreso erroneo, deben ser numeros naturales.")
    } else if (prompts == ""){
        alert("Ingrese un valor.")
    } else if (prompts < 0) {
        alert(`MEDIA TOTAL\n\n${suma/ingresos}`);
        activo = false
    } else {
        suma += prompts;
        ingresos = ++ingresos;
        console.log(suma,ingresos)
        let li = document.createElement("li");
        li.textContent = `${suma} - ${ingresos}`;
        lista.appendChild(li);
        
    }
}
document.getElementById("media").innerHTML = `\nMEDIA:  ${suma / ingresos}`