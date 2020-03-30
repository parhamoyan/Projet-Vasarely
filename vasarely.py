import turtle
import math
from deformation import deformation

def list_pos(c, longueur):
    p1 = (c[0]+longueur, c[1])
    p2 = (c[0]+longueur*math.cos(math.pi/3), c[1]+longueur*math.sin(math.pi/3))
    p3 = (c[0]-longueur*math.cos(math.pi/3), c[1]+longueur*math.sin(math.pi/3))
    p4 = (c[0]-longueur, c[1])
    p5 = (c[0]-longueur*math.cos(math.pi/3), c[1]-longueur*math.sin(math.pi/3))
    p6 = (c[0]+longueur*math.cos(math.pi/3), c[1]-longueur*math.sin(math.pi/3))
    p7 = (c[0]+longueur, c[1])
    return [p1,p2,p3,p4,p5,p6,p7]

def hexagone(point, longueur, col, centre, rayon):
    turtle.penup()
    listpos = list_pos(point, longueur)
    turtle.speed(1)
    x = point[0]
    y = point[1]
    point1 = (x, y, 0)
    point2 = deformation(point1, centre, rayon)
    turtle.goto(point2[0], point2[1])
    for i in range(3):
        turtle.goto(point2[0], point2[1])
        turtle.color(col[i])
        turtle.begin_fill()
        for pos in listpos[i*2:i*2+3]:
            p = deformation((pos[0],pos[1], 0), centre, rayon)
            turtle.goto(p[0], p[1])
        turtle.goto(point2[0], point2[1])
        turtle.end_fill()
    turtle.down()

def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    distance_x = longueur*3
    distance_y = longueur * 3**0.5/2
    sup_droit1 = sup_droit
    sup_droit2 = int(sup_droit + 1.5*longueur)
    inf_gauche2 = int(inf_gauche - 1.5*longueur)
    ligne = 1
    while sup_droit1 > inf_gauche:
        if ligne % 2 == 1:
            for x in range(inf_gauche, sup_droit, distance_x):
                point = (x, sup_droit1)
                hexagone(point,longueur,col,centre, rayon)
            ligne+=1
        elif ligne % 2 == 0:
            for x in range(inf_gauche2, sup_droit2, distance_x):
                point = (x, sup_droit1)
                hexagone(point, longueur, col, centre, rayon)
            ligne+=1
        sup_droit1 -= distance_y



# test :
inf_gauche = -200 
sup_droit = 200 
longueur = 20
col = ["blue", "black", "red"]
centre = (0, 0, 0)
rayon = 200
pavage(inf_gauche, sup_droit, longueur, col, centre, rayon)
turtle.done()
