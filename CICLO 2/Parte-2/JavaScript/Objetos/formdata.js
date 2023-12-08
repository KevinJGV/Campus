function send() {
    const form = document.querySelector("form")
    const formData = new FormData(form)
    for (const elem of formData) {
        alert(elem)
    }
    
}


