// Obtener los elementos por su clase
let topbg = document.querySelector(".topbg");
let mainlayer = document.querySelector(".mainlayer");

// Crear una función que cambie el tamaño de los elementos al hacer scroll
function cambiarTamaño() {
    // Obtener la posición actual del scroll
    let scrollPos = Window.pageYOffset;
    // Si el scroll es mayor que cero, cambiar el tamaño de los elementos
    if (scrollPos > 0) {
        topbg.style.transform = "scale(1)"; // El contenedor gris ocupa toda la pantalla
        mainlayer.style.transform = "translateX(0)"; // El contenido principal ocupa toda la pantalla
    } else {
        // Si el scroll es cero, volver al tamaño original
        topbg.style.transform = "scale(0.9)"; // El contenedor gris tiene un tamaño menor al de la pantalla
        mainlayer.style.transform = "translateX(-8%)"; // El contenido principal tiene un tamaño menor al de la pantalla
    }
}

// Añadir un evento que llame a la función cada vez que el usuario hace scroll
window.addEventListener("scroll", cambiarTamaño());