let pageHeight = window.innerHeight;
btf = document.getElementById("move")
btb = document.getElementById("back")

console.log(pageHeight)

btf.addEventListener("click", () => {
    window.scrollBy(0, pageHeight);
})

btb.addEventListener("click", () => {
    window.scrollBy(0, -pageHeight);
})