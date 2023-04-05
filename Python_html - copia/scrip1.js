// Define un array con las rutas de las imágenes
var imagenes = [];
    for (var i = 0; i <= 360; i++) {
    var ruta = "imagen_" + i + ".png";
    imagenes.push(ruta);
    }
// Obtiene la imagen por su ID
var imagen = document.getElementById("imagen");

// Define un contador para llevar el seguimiento de la imagen actual
var contador = 0;

// Define una función que cambie la imagen y reinicie el temporizador
function cambiarImagen() {
  // Incrementa el contador y asegura que no se exceda del número de imágenes
  contador = (contador + 1) % imagenes.length;

  // Cambia la ruta de la imagen
  imagen.src = imagenes[contador];

  // Verifica si se llegó a la ultima imagen
  if (contador === imagenes.length - 1) {
    imagen.src = imagenes[360]
    // No reinicia el temporizador y deja de cambiar la imagen
    return;
  }

  // Espera 0.09 segundos y cambia la imagen
  setTimeout(cambiarImagen, 200);
}

// Inicia el temporizador
setTimeout(cambiarImagen, 100);