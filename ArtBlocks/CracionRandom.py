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
