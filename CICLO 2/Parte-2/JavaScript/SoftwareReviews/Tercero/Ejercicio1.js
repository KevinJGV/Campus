function validartext(msj) {
  let flag = true;
  debugger
  input = prompt(msj)
  while (flag === true) {
    if (input === 0 || !isNaN(input) || input === "") {
      alert("Error en los datos ingresados, ingreselo nuevamente");
      input = prompt(msj);
    } else {
      flag = false;
      return input;
    }
  }
}

function validarnum(msj) {
    let flag = true;
    debugger
    input = Number(prompt(msj))
    while (flag === true) {
      if (input === 0 || isNaN(input) || input === "") {
        alert("Error en los datos ingresados, ingreselo nuevamente");
        input = prompt(msj);
      } else {
        flag = false;
        return input;
      }
    }
  }

let flag = true;
while (flag === true) {
  prompt1 = validartext("CALCULADORA DE PRECIO TOTAL\nNombre del articulo");
  prompt2 = validarnum("CALCULADORA DE PRECIO TOTAL\nPrecio individual del articulo");
  prompt3 = validarnum("CALCULADORA DE PRECIO TOTAL\nCantidad del articulo");
  total = prompt3 * prompt2
  alert(`FACTURA\t\nArticulo: ${prompt1}\nPrecio individual: ${prompt2}\nCantidad: ${prompt3}\nPrecio a pagar(sin IVA): ${total}`)

}
