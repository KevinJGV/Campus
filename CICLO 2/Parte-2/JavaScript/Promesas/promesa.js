const promesa = new Promise((resolve,reject) => {
    setTimeout(() => {
        resolve("¡Operacion completa!");
    }, 2000);
});

console.log("Inicio de la operaciòn.");

promesa.then(resultado => {
    console.log(resultado);
}).catch(error => {
    console.error("Error:", error);
});

console.log("Tareas adicionales");