fetch("http://localhost:3001/trainers/2", {
	method: "PATCH",
	body: JSON.stringify({
		"sexo": "f",
	}),
	headers: {
		"Content-Type": "application/json; charset=UTF-8",
	},
})
	.then((res) => res.json())
	.then((data) => console.log(data))
	.catch((err) => console.error(err));
