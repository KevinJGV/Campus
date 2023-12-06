function contains(num) {
    let targets = ["**","*","/","-","+",]
    let flag = false
    let op = undefined
    for (let i = 0; i < targets.length; i++) {
        if (num.includes(targets[i])) {
            op = targets[i]
            flag = true
            break
        } 
    }
    if (flag === true) {
        let arr = num.split(op);
        let num1 = parseFloat(arr[0]);
        let num2 = parseFloat(arr[1]);
        switch (op) {
            case "+":
                return num1 + num2;
            case "-":
                return num1 - num2;
            case "*":
                return num1 * num2;
            case "/":
                return num1 / num2;
            case "**":
                return num1 ** num2;
        }
    } else {
        return num
    }
}

function makest(num,concat) {
    let r = contains(num)
    r = String(r).repeat(Number(concat))
    return r
}

function superdigit(num, concat) {
    // debugger
    let r = makest(num,concat)
    let l = r.length
    let suma = 0
    if (l > 1){
    for (let i = 0; i < l; i++) {
        suma += Number(r[i])
    }} else {
        console.log(r)
        suma = 0
    }
   return console.log(suma)
}

console.log(superdigit("1**500","8"))

