function send() {
    const form = document.querySelector("form")
    const formData = new FormData(form)
    console.log(formData)
    for (const elem of formData) {
        if (edad >= 17) {
            console.log ("Puedes entrar a campus")
        }
    }
    formData.append("nombre", "Oscar")
    const nombres = formData.getAll("nombre")
    console.log(nombres)
}


