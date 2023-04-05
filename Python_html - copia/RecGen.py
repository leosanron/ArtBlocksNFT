# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 20:14:29 2023

@author: Leonardo Sanchez
"""

from flask import Flask, request, jsonify, send_file
from io import BytesIO
from PIL import Image, ImageEnhance

app = Flask(__name__)

@app.route('/modificar-imagen', methods=['POST'])

def modificar_imagen():
    
    # Verificar que se envió una imagen en el request
    if 'imagen' not in request.files:
        return 'No se envió ninguna imagen', 400
    # Recibe la imagen enviada desde el cliente
    imagen = request.files['capa1'].read()
    
    # Realiza las modificaciones
    capa1 = Image.open(imagen).convert("RGBA")
    capa1.show()
    capa2 = Image.open("C:/Users/57314/Downloads/pulsar.png").convert("RGBA")
    capa2.show()
    capa3 = Image.open("C:/Users/57314/Downloads/frame 3.png").convert("RGBA")
    capa4 = Image.open("C:/Users/57314/Downloads/mercury nebula.png").convert("RGBA")
    
    grados_por_iteracion = 45
    CantImg = int(360/grados_por_iteracion)
    MovBrillo = 0.5/CantImg
    Brillo1 = 0.5
    Brillo2 = 1.5
    frame = []

    for i in range(0,CantImg+1):
        # Brillo capa 1
        ajuste_brillo = ImageEnhance.Brightness(capa1)
        capa11 = ajuste_brillo.enhance(Brillo1)
        Brillo1 = Brillo1 + MovBrillo

        # Brillo capa 2
        ajuste_brillo = ImageEnhance.Brightness(capa3)
        capa33 = ajuste_brillo.enhance(Brillo2)
        capa333 = capa33.rotate(grados_por_iteracion * i)
        Brillo2 = Brillo2 - MovBrillo
        
        # Rotar imagen
        capa44 = capa4.rotate(grados_por_iteracion * -i)
        
        #Capa2 
        capa22 = capa2.rotate(grados_por_iteracion * 2*i)
            
        # Combina las dos imágenes en una nueva imagen
        paso1 = Image.alpha_composite(capa11, capa22)
        paso2 = Image.alpha_composite(paso1, capa333)
        resultado = Image.alpha_composite(paso2, capa44)
        
        # Agrega la imagen resultante al arreglo de frames
        frame.append(resultado)
    
    # Devuelve la última imagen generada
    #img_bytes = frame[-1].tobytes()
    #response = {'imagen': img_bytes}
    
    return send_file(BytesIO(resultado), mimetype='image/png')

if __name__ == '__main__':
    app.run() #debug=True
    