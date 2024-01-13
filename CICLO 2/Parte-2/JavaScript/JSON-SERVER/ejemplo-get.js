fetch("http://localhost:3001/trainers", {
	method: "GET",
	headers: {
		"Content-Type": "application/json; charset=UTF-8",
	},
})
	.then((res) => res.json())
	.then((data) => console.log(data));
