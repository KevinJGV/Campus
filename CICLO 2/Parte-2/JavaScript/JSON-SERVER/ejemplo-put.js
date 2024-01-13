fetch("http://localhost:3001/trainers/2", {
	method: "PUT",
	body: JSON.stringify({
		"id": "1",
		"nombre": "carlos",
		"apellidos": "rueda",
		"especialidad": "backend-java",
		"edad": "25",
		"sexo": "m",
	}),
	headers: {
		"Content-Type": "application/json; charset=UTF-8",
	},
})
	.then((res) => res.json())
	.then((data) => console.log(data))
	.catch((err) => console.error(err));
