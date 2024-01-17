import { d } from "./codigoBase";
const añadir1 = d.querySelector("#añadir1");
const subtier1 = d.querySelector("#subtier1");
añadir1.addEventListener("click", () => subtier1.classList.toggle("hidden"));