# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:27:06 2023

@author: Leonardo Sanchez
"""

from PIL import Image, ImageEnhance

# Definir la cantidad de rotación en grados por iteración
grados_por_iteracion = 1


Background = ["C:/Users/57314/Desktop/Python random/ArtBlocks/1. BACKGROUND/black.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/1. BACKGROUND/blue.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/1. BACKGROUND/green.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/1. BACKGROUND/holographic.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/1. BACKGROUND/magenta.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/1. BACKGROUND/purple.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/1. BACKGROUND/red.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/1. BACKGROUND/spirals.png"]

Degraded = ["C:/Users/57314/Desktop/Python random/ArtBlocks/2. DEGRADED/above.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/2. DEGRADED/around.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/2. DEGRADED/center.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/2. DEGRADED/floating.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/2. DEGRADED/left.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/2. DEGRADED/right.png"]

Lines = ["C:/Users/57314/Desktop/Python random/ArtBlocks/3. LINES/another space.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/3. LINES/galactic.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/3. LINES/galaxy waves.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/3. LINES/Interplanetary.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/3. LINES/nebula.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/3. LINES/stellar.png"]

Stones = ["C:/Users/57314/Desktop/Python random/ArtBlocks/4. STONES/amethyst journey.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/4. STONES/futuristic emerald.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/4. STONES/gemstone.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/4. STONES/glass stone.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/4. STONES/sapphire world.png",
         "C:/Users/57314/Desktop/Python random/ArtBlocks/4. STONES/stranger rubi.png"]

Generadas = []
import random

while len(Generadas) != 10:
    x = random.choice(Background)
    y = random.choice(Degraded)
    z = random.choice(Lines)
    l = random.choice(Stones)
    Nombre =("NFT "
          +str(Background.index(x))
          +str(Degraded.index(y))
          +str(Lines.index(z))
          +str(Stones.index(l)))
    
    if Nombre in Generadas:
        pass
    else: 
        capa1 = Image.open(x).convert("RGBA")
        
        # Abre la imagen que quieres pegar y conviértela al modo "RGBA"    
        capa2 = Image.open(y).convert("RGBA")
        if capa2.size != capa1.size:
            capa2 = capa2.resize(capa1.size)
            
        # Abre la imagen que quieres pegar y conviértela al modo "RGBA"
        capa3 = Image.open(z).convert("RGBA")
        if capa3.size != capa1.size:
            capa3 = capa3.resize(capa1.size)
            
        # Abre la imagen que quieres pegar y conviértela al modo "RGBA"
        capa4 = Image.open(l).convert("RGBA")
        if capa4.size != capa1.size:
            capa4 = capa4.resize(capa1.size)
            
        # Combina las dos imágenes en una nueva imagen
        paso1 = Image.alpha_composite(capa1, capa2)
        paso2 = Image.alpha_composite(paso1, capa3)
        resultado = Image.alpha_composite(paso2, capa4)
        
        Generadas.append(Nombre)
        resultado.save("C:/Users/57314/Desktop/Python random/ArtBlocks/NFT/"+Nombre+".png")
        print(Nombre)
    

"""


#Seleccion aleatoria



for i in range (0,3):
    # Abre la imagen inicial y conviértela al modo "RGBA"
    capa1 = Image.open(random.choice(Background)).convert("RGBA")
    # Abre la imagen que quieres pegar y conviértela al modo "RGBA"
    capa2 = Image.open(Degraded[1]).convert("RGBA")
    # Abre la imagen que quieres pegar y conviértela al modo "RGBA"
    capa3 = Image.open(Lines[1]).convert("RGBA")
    # Abre la imagen que quieres pegar y conviértela al modo "RGBA"
    capa4 = Image.open(Stones[0]).convert("RGBA")

    # Combina las dos imágenes en una nueva imagen
    paso1 = Image.alpha_composite(capa1, capa2)
    paso2 = Image.alpha_composite(paso1, capa3)
    resultado = Image.alpha_composite(paso2, capa4)

    resultado.show()



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
"""
