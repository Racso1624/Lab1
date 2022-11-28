#Oscar Fernando López Barrios
#Carné 20679
#Gráficas Por Computadora
#Lab1

from gl import Render
from texture import *
from math import *
from vector import *

r = Render()

r.glCreateWindow(1024, 1024)

r.glClearColor(0.5, 0.6, 0.8)

r.glClear()

r.glColor(1, 1, 0)

polygon1 = ((165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383))

r.fillPolygon(polygon1)

r.glColor(1, 0, 0)

polygon2 = ((321, 335), (288, 286), (339, 251), (374, 302))

r.fillPolygon(polygon2)

r.glColor(0, 1, 0)

polygon3 = ((377, 249), (411, 197), (436, 249))

r.fillPolygon(polygon3)

r.glColor(0, 0, 0)

polygon4 = ((413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180))

r.fillPolygon(polygon4)

r.glColor(0.5, 0.6, 0.8)

polygon5 = ((682, 175), (708, 120), (735, 148), (739, 170))

r.fillPolygon(polygon5)

r.glFinish("lab1.bmp")