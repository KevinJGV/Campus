const promesa = new Promise((resolve,reject) => {
    setTimeout(() => {
        const exito = true;
        if (exito) {
            resolve("¡Operacion completa!");
        } else {
            reject("Hubo un error al cumplir la promesa")
        }
    }, 2000);
});

promesa.then(resultado => {
    console.log(resultado);
}).catch(error => {
    console.error("Error:", error);
});