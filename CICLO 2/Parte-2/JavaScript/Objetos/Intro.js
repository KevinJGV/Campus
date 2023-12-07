const persona = {
    nombre: "Dani",
    edad: 30,
    Trabajador: true,
    familia: ["miguel", "maria"],
    direccion: {
        calle: "Calle de los estudiantes",
        numero: 1,
        ciudad: "Bucaramanga",
    },
    caminar: function () {
        console.log(this.nombre + "Está caminando")
    }
}

console.log(persona);
console.log(persona.edad);
persona.caminar();

persona.nombre = "Daniela";
console.log(persona.nombre)
const cadenaJSON = JSON.stringify(persona);
console.log(cadenaJSON)

const objetoJSON = JSON.parse(cadenaJSON)
console.log(objetoJSON)