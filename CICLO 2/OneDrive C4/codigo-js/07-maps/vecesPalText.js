//Contar el numero de veces que aparece una palabra en un texto
const vecesPal = function (pal) {
    const vpals = pal.split(" ")
    const mPals = new Map()

    vpals.forEach(pal => (mPals.has(pal)) ? mPals.set(pal, mPals.get(pal) + 1) : mPals.set(pal, 1));
    return mPals
}

const texto = "Este es un ejemplo de un texto que es ideal para procesar"
console.log(vecesPal(texto))