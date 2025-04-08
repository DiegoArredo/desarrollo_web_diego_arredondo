function cerrarModal() {
    const modal = document.getElementById("myModal");
    modal.style.display = "none";
};
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
//tomar por el tag img que al apretar se abra el modal con la imagen seleccionada
var modal = document.getElementById("myModal");
var img = document.getElementsByTagName("img");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
for (var i = 0; i < img.length; i++) {
    img[i].onclick = function () {
        modal.style.display = "block";
        modalImg.src = this.src;
        modalImg.alt = this.alt;
        modalImg.style.width = "800px";
        modalImg.style.height = "600px";
    }
}