const d = document;
// const all = d.querySelectorAll("*");
const b = d.querySelector("body");
const topbg = d.querySelector(".topbg");
const mainlayer = d.querySelector(".mainlayer");
const container = d.querySelector(".containermainlayer");
const porfolio = d.querySelector(".porfolio");
const nav = d.querySelector(".navcontainer");
const lateralbar = d.querySelector(".lateralbar");

let isTrusted;

// debugger
function expandBox(e) {
    for (let i = 0; i <= 1; i++) {
        // if (i === 1) {
        //     i = 0;
        // };
        if (isTrusted === undefined) {
            isTrusted = 1
            return
        };
    };
    if (isTrusted === 1) {
        topbg.style.width = '100vw';
        topbg.style.top = '0';
        topbg.style.borderRadius = '0';
        mainlayer.style.right = "8%";
        nav.style.top = '20px';
        lateralbar.style.left = '60px';
        lateralbar.style.height = '95%';
        porfolio.style.paddingRight = "0";
        this.removeEventListener('scroll', expandBox);
    };
};

b.addEventListener("scroll", expandBox);

function resetPage() {
    if (b.scrollTop === 0) {
        isTrusted = 1
    };
    b.scrollTo(0, 0);
}

document.addEventListener("DOMContentLoaded", resetPage);
