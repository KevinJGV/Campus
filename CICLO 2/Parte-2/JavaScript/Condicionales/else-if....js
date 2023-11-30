let edad = Number(prompt("Edad: "))

if (edad<18) {
    alert("Eres muy joven, no puede ingresar a CampusLands");
} else if (edad >= 18 && edad < 29) {
    alert("Bienvenido a CampusLands.");
} else {
    alert ("Eres demasiado mayor, no puedes entrar al CampusLands");
}