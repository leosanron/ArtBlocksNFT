# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:00:19 2023

@author: Leonardo Sanchez
"""

from PIL import Image, ImageEnhance
import time
import matplotlib.pyplot as plt


# Definir la cantidad de rotación en grados por iteración
grados_por_iteracion = 10
grados_por_brillo = 10


# Abre la imagen inicial y conviértela al modo "RGBA"
capa1 = Image.open("C:/Users/57314/Desktop/Python random/PurpleWaves.png").convert("RGBA")
# Abre la imagen que quieres pegar y conviértela al modo "RGBA"
capa2 = Image.open("C:/Users/57314/Desktop/Python random/frame4.png").convert("RGBA")
# Abre la imagen que quieres pegar y conviértela al modo "RGBA"
capa3 = Image.open("C:/Users/57314/Desktop/Python random/diamond glacier.png").convert("RGBA")
# Abre la imagen que quieres pegar y conviértela al modo "RGBA"
capa4 = Image.open("C:/Users/57314/Desktop/Python random/equilibrium.png").convert("RGBA")

Brillo1 = 0.82
Brillo2 = 1.18
frames = []

# Realizar las modificaciones
for i in range(0,36):

    # Brillo de la imagen
    if i % 2 == 0:
        ajuste_brillo = ImageEnhance.Brightness(capa1)
        capa11 = ajuste_brillo.enhance(Brillo1)
        Brillo1 + 0.01
        
    else:
        ajuste_brillo = ImageEnhance.Brightness(capa1)
        capa11 = ajuste_brillo.enhance(Brillo2)
        Brillo2 - 0.01
    
    # Rotar la imagen
    capa33 = capa3.rotate(grados_por_iteracion * i)
    
    # Combina las dos imágenes en una nueva imagen
    paso1 = Image.alpha_composite(capa11, capa2)
    paso2 = Image.alpha_composite(paso1, capa33)
    resultado = Image.alpha_composite(paso2, capa4)
    frame = resultado
    

    #guardar en data frame
    frames.append(frame)
    
    # Mostrar la imagen rotada en una ventana
    #fig, ax = plt.subplots()
    #ax.imshow(resultado)
    #ax.axis('off')
    #plt.show()
    
    # Esperar un segundo antes de continuar a la siguiente iteración
    #time.sleep(0.0001)
    
frames[0].save('C:/Users/57314/Desktop/Python random/gifart.gif', save_all=True, append_images=frames[1:], duration=200, loop=0)
    