obj = {
    "Empleados": [{
        "nombre": "Juan",
        "apellido": "Lopez",
        nombreCompleto: function () {
            return this.nombre + " " + this.apellido
        }
    },
    {
        "nombre": "Ana",
        "apellido": "Gonzalez",
        nombreCompleto: function () {
            return this.nombre + " " + this.apellido
        }
    },
    {
        "nombre": "Pedro",
        "apellido": "Sanchez",
        nombreCompleto: function () {
            return this.nombre + " " + this.apellido
        }
    },
    ]
}

const clonePerson = Object.assign({}, obj)
const clon2 = {...obj}
const o1 = {a:1} 
const o2 = {b:2} 
const o3 = {c:3} 
const ot = {...o1, ...o2, ...o3}
console.log(clonePerson)
console.log(clon2)
console.log(ot)