# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:08:38 2023

@author: Leonardo Sanchez
"""
import matplotlib
matplotlib.use("Agg") # Cambiar el backend a "Agg"

import matplotlib.pyplot as plt
import matplotlib.animation as animation

images = []
for i in range(0,3):
    #filename = f"C:/Users/57314/Desktop/Python random/Python_html/imagen_{0}.png"
    img = plt.imread("C:/Users/57314/Desktop/Python random/Python_html/imagen_"+str(i)+".png")
    images.append(img)
    
def update(frame):
    plt.imshow(images[frame])

fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=len(images), interval=200)
ani.save("animacion.mp4", writer='ffmpeg')
plt.show()
