# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:27:06 2023

@author: Leonardo Sanchez
"""

from PIL import Image, ImageEnhance

# Definir la cantidad de rotación en grados por iteración
grados_por_iteracion = 1

# Abre la imagen inicial y conviértela al modo "RGBA"
capa1 = Image.open("C:/Users/57314/Desktop/Python random/Python_html - copia/red.png").convert("RGBA")
# Abre la imagen que quieres pegar y conviértela al modo "RGBA"
capa2 = Image.open("C:/Users/57314/Desktop/Python random/Python_html - copia/nebula.png").convert("RGBA")
# Abre la imagen que quieres pegar y conviértela al modo "RGBA"
capa3 = Image.open("C:/Users/57314/Desktop/Python random/Python_html - copia/futuristic emerald.png").convert("RGBA")
# Abre la imagen que quieres pegar y conviértela al modo "RGBA"
capa4 = Image.open("C:/Users/57314/Desktop/Python random/Python_html - copia/center.png").convert("RGBA")

CantImg = int(360/grados_por_iteracion)
MovBrillo1 = 0.8/CantImg
Brillo1 = 1.8

MovBrillo2 = 0.5/CantImg
Brillo2 = 0.5
frame = []

# Realizar las modificaciones
for i in range(0,CantImg+1):
    print("creando imagen ",str(i)," de ", str(CantImg))

    # Brillo capa 1
    ajuste_brillo = ImageEnhance.Brightness(capa1)
    capa11 = ajuste_brillo.enhance(Brillo1)
    Brillo1 = Brillo1 - MovBrillo1

    # Brillo capa 2
    ajuste_brillo = ImageEnhance.Brightness(capa3)
    capa33 = ajuste_brillo.enhance(Brillo2)
    capa333 = capa33.rotate(grados_por_iteracion * i)
    Brillo2 = Brillo2 + MovBrillo2
    
    
    # Rotar imagen
    capa44 = capa4.rotate(grados_por_iteracion * 3 *i)
    
    #Capa2 
    capa22 = capa2.rotate(grados_por_iteracion * -2*i)
        
    # Combina las dos imágenes en una nueva imagen
    paso1 = Image.alpha_composite(capa11, capa22)
    paso2 = Image.alpha_composite(paso1, capa333)
    resultado = Image.alpha_composite(paso2, capa44)
    nombre ="C:/Users/57314/Desktop/Python random/Python_html - copia/imagen_"+str(i)+".png"
    
    #frame.append(resultado)
    resultado.save(nombre)


#capa22.putalpha(128)  # 128 es la mitad de 255 (el valor máximo de transparencia)
#import pickle
#with open("C:/Users/57314/Desktop/Python random/Python_html/frame,pkl", 'wb') as f:
#    pickle.dump(frame, f)

#with open("C:/Users/57314/Desktop/Python random/Python_html/frame,pkl", 'rb') as f:
#    mi_lista_recuperada = pickle.load(f)
#    mi_lista_recuperada[0]


#from PIL import Image, ImageEnhance
#frame = []
#for i in range(0,361):
#    img = Image.open("C:/Users/57314/Desktop/Python random/Python_html/imagen_"+str(i)+".png")
#    frame.append(img)
