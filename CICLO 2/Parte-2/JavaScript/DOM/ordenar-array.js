const d = document;
const arrdom = d.querySelector("#arr");
const input_button = d.querySelector("#input_button");
const box_text = d.querySelector("#box_text");
const box_button = d.querySelector("#box_button");
const regex = /[.,:;/ *+|]/;

function toCapitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

input_button.addEventListener("click", () => {
    let arr = arrdom.value;
    arr = arr.split(regex);
    arr = arr.map(element => toCapitalize(element));
    arr = arr.filter(element => element !== "");
    let box = box_text.value;
    box = box.split(regex);
    box = box.filter(element => element !== "");
    box = [...arr, ...box];
    box = [...new Set(box)];
    box = (box.sort()).join(", ");
    box_text.value = box;
});

box_button.addEventListener("click", () => {
    box_text.value = "";
})
