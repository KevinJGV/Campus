const obj = {
    "empleados": [
        {
            "nombre": "Juan Perez",
            "apellido": "Lopez",
        },
        {
            "nombre": "Ana",
            "apellido": "Gonzalez",
        },
        {
            "nombre": "Pedro",
            "apellido": "Sanchez",
        },
    ],
    "nombreCompleto": function (pos) {
        return this.empleados[pos].nombre + " " + this.empleados[pos].apellido
    }
}

console.log(obj.empleados[2].apellido)
console.log(obj.nombreCompleto(2))
console.log(obj.empleados.length)