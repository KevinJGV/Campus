const persona = {
    nombre: 'Dani',
    edad: 30,
    esTrabajador: true,
    familia: ["Miguel", "Maria"],
    dirección: {
        calle: "Calle de los estudiantes",
        numero: 13,
        ciudad: "Bucaramanga"
    },
    caminar: function () {
        console.log(this.nombre + ' está caminando');
    }
};

console.log(persona);
console.log(persona.nombre);
persona.caminar();

persona.nombre = "Daniela";
console.log(persona.nombre);
persona.caminar();

const cadPersona = JSON.stringify(persona);
console.log(cadPersona);

const objPer = JSON.parse(cadPersona);
console.log(objPer);