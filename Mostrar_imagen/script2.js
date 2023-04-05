function reproducirGIF() {
  var gif = document.createElement("img");
  gif.src = "colorfart.gif";
  document.body.appendChild(gif);
}

var boton = document.getElementById("reproducir");
boton.addEventListener("click", reproducirGIF);