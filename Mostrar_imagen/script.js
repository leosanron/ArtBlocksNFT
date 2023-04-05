var gif = document.getElementById("gif");

function reproducirGIF() {
  gif.src = "colorfart.gif";
}

setInterval(function() {
  gif.src = "colorfart.gif";
}, 500000);