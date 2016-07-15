# -*- coding: latin-1 -*-
from Algorithmus import *
import ScreenshotCutter as sc
from Translator import Translate
from Aufgaben import *
from ev3robot import *

def right(motx):
    #Nach rechts bewegen
    motx.moveTo(-bew_x,True)
    while motx.isMoving():
        pass
    return
def left(motx):
    #Nach links bewegen
    motx.moveTo(bew_x,True)
    while motx.isMoving():
        pass
    return
def top(moty):
    #Nach oben bewegen
    moty.rotateTo(-bew_y,True)
    while moty.isMoving():
        pass
    return
def bottom(moty):
    #Nach unten bewegen
    moty.rotateTo(bew_y,True)
    while moty.isMoving():
        pass
    return
def up(motz):
    #Stift nach oben bewegen
    motz.rotateTo(bew_z,True)
    while motz.isMoving():
        pass
    return
def down(motz):
    #Stift nach unten bewegen
    motz.rotateTo(-bew_z,True)
    while motz.isMoving():
        pass
    return

def solve(data, motx, moty, motz):
    #Aktuelle Position auf o/o
    x_n = y_n = 0

    #Fuer jede Farbe
    for col in data:
        #Start-Koordinaten
        x, y = eval(col.split("&")[0])
        
        #Solange x_Ziel kleiner als x_Jetzt --> nach links
        while x < x_n:
            left(motx)
            x_n -= 1
        #Solange x_Ziel groesser als x_Jetzt --> nach rechts
        while x > x_n:
            right(motx)
            x_n += 1
        #Solange y_Ziel kleiner als y_Jetzt --> nach oben
        while y < y_n:
            top(moty)
            y_n -= 1
        #Solange y_Ziel groesser als y_Jetzt --> nach unten
        while y > y_n:
            bottom(moty)
            y_n += 1
        #Stift herunterlassen
        down(motz)
        #Fuer jeden Buchstaben
        for s in col.split("&")[1]:
            # r = rechts
            # l = links
            # o = oben
            # u = unten
            if s == "r":
                right(motx)
                x_n += 1
            elif s == "l":
                left(motx)
                x_n -= 1
            elif s == "o":
                top(moty)
                y_n -= 1
            elif s == "u":
                bottom(moty)
                y_n += 1
        #Stift nach oben
        up(motz)
    #Zurueck zu Nullpunkt
    while 0 < x_n:
        left(motx)
        x_n -= 1
    while 0 > x_n:
        right(motx)
        x_n += 1
    while 0 < y_n:
        top(moty)
        y_n -= 1
    while 0 > y_n:
        bottom(moty)
        y_n += 1
    return


#Mit Roboter verbinden
robot = None 
try:
    robot = LegoRobot("10.0.2.1")
except:
    pass
    
#Konstanten fuer Bewegungen in jeweiliger Achse:
bew_x = 95
bew_y = 160
bew_z = 35

#Motoren & Sensoren
motx = Gear() #Automatisch Port A & B
moty = Motor(MotorPort.C)
motz = Motor(MotorPort.D)
ts = TouchSensor(SensorPort.S1)

#Speeds setzen
motx.setSpeed(1)
moty.setSpeed(100)
motz.setSpeed(20)
#Alle Motoren und Touch dem Roboter zuweisen
robot.addPart(motx)
robot.addPart(moty)
robot.addPart(motz)
robot.addPart(ts)

up(motz)
#Warten, bis Touch gedrueckt wird
robot.clearDisplay()
robot.drawString("Waiting for press",1,1)
while True:
    if ts.isPressed():
        break

robot.clearDisplay()
robot.drawString("Getting Aufgabe",1,1)
#Aufgabe = sc.get()
Aufgabe = Aufgabe11
robot.clearDisplay()
robot.drawString("Got Aufgabe",1,1)

Aufgabe=Sicher(Aufgabe)
if Test(Aufgabe,"E") != "Fertig":
    Aufgabe=Raten(Aufgabe,None)
robot.clearDisplay()
robot.drawString("Got Solution",1,1)
data = Translate(Aufgabe)
print data
robot.clearDisplay()
robot.drawString("Start plotting",1,1)
#data = [data[0],data[1]]
solve(data, motx, moty, motz)

down(motz)
up(motz)
down(motz)
robot.exit()
