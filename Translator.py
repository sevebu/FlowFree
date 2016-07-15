# -*- coding: latin-1 -*-
from copy import deepcopy
from Algorithmus import Nachbar
def Translate(L):
    data = [] #Output
    colors = [] #StartPunkte der Farben
    for y in range(len(L)):
        for x in range(len(L[y])):
            N = [] #Nachbarn ohne Zahl
            #Füge i ohne Zahl hinzu, i ist nicht = "none" und i ist von der Form FARBE1 oder FARBE2
            [N.append(i[:-1]) for i in Nachbar(L,x,y) if i != "none"]
            #Falls Farbe in Nachbarn nur 1mal vorkommt n(Ende einer Leitung) und die Farbe noch nicht schon hinzugefügt wurde
            if len([s for s in N if L[y][x][:-1] in s])==1 and L[y][x][:-1] not in [t[0] for t in colors]:
                colors.append([L[y][x][:-1],x,y])
    for col in colors: #Für jede Farbe
        dat = "("+str(col[1])+","+str(col[2])+")&"
        x, y = col[1],col[2] #Startkoordinaten der Farbe
        while True:
            N = Nachbar(L,x,y)
            L[y][x] = "none" #Aktuelles Feld auf None, damit beim Naechsten nicht zurück geht
            if col[0] in N[0]:
                dat += "r" #Nachbar rechts
                x += 1
            elif col[0] in N[1]:
                dat += "u" #Nachbar unten
                y += 1
            elif col[0] in N[2]:
                dat += "l" #Nachbar links
                x -= 1
            elif col[0] in N[3]:
                dat += "o" #Nachbar oben
                y -=1
            else:
                break #Kein Nachbar mehr --> Ende der Farbe, aus while heraus
        data.append(dat) #String der Farbe an Output hinzufügen     
    return data