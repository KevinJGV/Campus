// Declaracion de funciones

function calcularmin(user, pc) {
    min = Math.floor(user / pc); return min
}

function calcularmod(user, pc) {
    mod = (user % pc); return mod
}

//Codigo

let oldcampers = Number(prompt("Campers antiguos:")); let newcampers = Number(prompt("Campers nuevos:")); let pc = Number(prompt("PC\'s de la empresa:")); let totalcampers = oldcampers + newcampers; let jornadas = Math.ceil(totalcampers / pc); let bandera = true; let minimonuevos = calcularmin(newcampers, pc); let restante = calcularmod(newcampers, pc);



if (pc < totalcampers) {
    alert('Hay más Campers que pcs disponibles en CampusLands, es necesario seccionar por jornadas para dar una solución a la diferencia.');
    while (bandera === true) {
        let jornadas = 1
        let pcflag = pc
        while (oldcampers > 0 || newcampers > 0) {
            for (pcflag; pcflag > 0; pcflag--) {
                let equipo = 0
                if (equipo === 0) {
                    if (oldcampers > 0) {
                        equipo++
                        oldcampers--
                    } else if (equipo === 0) {
                        if (newcampers > 0) {
                            equipo++
                            newcampers--
                        }
                    }
                }
            }
            if (oldcampers > 0 || newcampers > 0) {
                jornadas++
                pcflag = pc
            }
        };
        if (restante === 0) {
            alert(`(UTILIZANDO CONDICIONALES PARA RESPUESTA DE JORNADAS)\nSe deben crear ${minimonuevos} usuarios en ${pc} computadoras.\nTotal de jornadas necesarias: ${jornadas}`);
            document.getElementById("campers").innerHTML = `<brSe deben crear ${minimonuevos} usuarios en ${pc} computadoras.<br>Total de jornadas necesarias: ${jornadas}`
        } else {
            alert(`(UTILIZANDO CONDICIONALES PARA RESPUESTA DE JORNADAS)\nSe deben crear ${minimonuevos} usuarios en ${pc - restante} computadoras y ${minimonuevos + 1} usuarios en ${restante} computadoras\nTotal de jornadas necesarias: ${jornadas}`);
            document.getElementById("campers").innerHTML = `<br>Se deben crear ${minimonuevos} usuarios en ${pc - restante} computadoras y ${minimonuevos + 1} usuarios en ${restante} computadoras<br>Total de jornadas necesarias: ${jornadas}`;
        }
        bandera = false
    };
}
if (restante === 0) {
    alert(`(RESPUESTA DE JORNADAS CON OPERACIONES MATEMATICAS)\nSe deben crear ${minimonuevos} usuarios en ${pc} computadoras.\nTotal de jornadas necesarias: ${jornadas}`);
    document.getElementById("campers").innerHTML = `<br>Se deben crear ${minimonuevos} usuarios en ${pc} computadoras.<br>Total de jornadas necesarias: ${jornadas}`
} else {
    alert(`(RESPUESTA DE JORNADAS CON OPERACIONES MATEMATICAS)\nSe deben crear ${minimonuevos} usuarios en ${pc - restante} computadoras y ${minimonuevos + 1} usuarios en ${restante} computadoras\nTotal de jornadas necesarias: ${jornadas}`);
    document.getElementById("campers").innerHTML = `<br>Se deben crear ${minimonuevos} usuarios en ${pc - restante} computadoras y ${minimonuevos + 1} usuarios en ${restante} computadoras<br>Total de jornadas necesarias: ${jornadas}`
}
