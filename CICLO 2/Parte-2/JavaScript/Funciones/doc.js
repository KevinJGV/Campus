// Apuntes en desarrollo

// CLAUSULAS
//Para crear una clausura:

// Primero defines una función externa que declara e inicializa una o más variables.
// Dentro de esta función externa, defines una función interna que hace referencia a estas variables.
// La función externa retorna la función interna.
// En lugar de invocar la función externa de forma independiente, asignas el resultado de su invocación (que es la función interna) a una nueva variable.
// De esta manera, cada vez que invocas la función interna a través de la nueva variable, tiene acceso al entorno original en el que fue creada, incluyendo las variables de la función externa. Esto permite que las variables “recuerden” su valor entre diferentes invocaciones de la función interna, creando una clausura.

function crearContador() {
    let contador = 0;
    return function () {
        contador += 1;
        return contador;
    }
}

let miContador = crearContador();

console.log(miContador()); // Imprime: 1
console.log(miContador()); // Imprime: 2
console.log(miContador()); // Imprime: 3


//FUNCIONES FLECHA

const funcT = function () {
    return "Función tradicional.";
};

const funcF = () => {
    return "Función flecha.";
};

// las funciones flechas tienen algunas ventajas a la hora de simplificar código bastante interesantes:

// Si el cuerpo de la función sólo tiene una línea, podemos omitir las llaves({}).
//     Además, en ese caso, automáticamente se hace un return de esa única línea, por lo que podemos omitir también el return.
// En el caso de que la función no tenga parámetros, se indica como en el ejemplo anterior: () =>.
// En el caso de que la función tenga un solo parámetro, se puede indicar simplemente el nombre del mismo: e =>.
// En el caso de que la función tenga 2 ó más parámetros, se indican entre paréntesis: (a, b) =>.
// Si queremos devolver un objeto, que coincide con la sintaxis de las llaves, se puede englobar con paréntesis: ({ name: 'Manz' }).
// Por lo tanto, el ejemplo anterior se puede simplificar aún más:

const funcF1 = () => "Función flecha."; // 0 parámetros: Devuelve "Función flecha"
const funcF2 = (e) => e + 1; // 1 parámetro: Devuelve el valor de e + 1
const funcF3 = (a, b) => a + b; // 2 parámetros: Devuelve el valor de a + b