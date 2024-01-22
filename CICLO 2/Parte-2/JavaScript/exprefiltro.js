const ex = [
    { "id": "1" },
    { "id": "1" },
    { "id": "2" }
];

function fn(op, elem, callback) {
    switch (op) {
        case 1:
            callback(elem)
    }
}

function caso1(elem) {
    let res = {};
    let newIds = [];
    for (let e of elem) {
        if (newIds.length === 0) {
            newIds.push([])
        }
    }
}