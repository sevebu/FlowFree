# -*- coding: latin-1 -*-
import copy, time

# Funktion um Sichere Leitungen zu bauen
def Sicher(Liste):
    Vergleich=copy.deepcopy(Liste) # Kopie erstellen um zu vergleichen
    Liste=Eckpunkte(Liste) # Zuege in die Ecken ausfuehren
    
    # Fuer alle Elemente der Liste
    for y in range(len(Liste)):
        for x in range(len(Liste)):
            objekt=Liste[y][x]
            # Wenn objekt ein aktives Ende ist
            if objekt.upper()!=objekt:
                Nachbarn=Nachbar(Liste,x,y) # Speichere Nachbarn von objekt
                objekt=objekt[0:len(objekt)-1] # Zahl vom objekt abschneiden
                boolean=False # Wird True, wenn zwei aktive Enden nebeneinander liegen
                for i in Nachbarn:
                    if objekt in i: boolean=True
                # Wenn nur ein freier Nachbar und keine eigene kleine Farbe neben sich
                if Nachbarn.count("")==1 and not boolean:
                    # Verschiebe das aktive Ende
                    index = Nachbarn.index("")
                    if index==0: # Rechts
                        Liste[y][x+1]=Liste[y][x]
                    if index==1: # Unten
                        Liste[y+1][x]=Liste[y][x]
                    if index==2: # Links
                        Liste[y][x-1]=Liste[y][x]
                    if index==3: # Oben
                        Liste[y-1][x]=Liste[y][x]
                    # Mache ehemaliges aktives Feld zu einem Passiven.
                    Liste[y][x]=Liste[y][x].upper()
                    
                # Wenn zwei aktive Enden nebeneinander liegen
                elif boolean:
                    # Suche die Richtung des aktiven Nachbars
                    for i in Nachbarn: 
                        if objekt in i: index = Nachbarn.index(i)
                    # Mache aktiven Nachbar passiv
                    if index==0: # Rechts
                        Liste[y][x+1]=Liste[y][x+1].upper()
                    if index==1: # Unten
                        Liste[y+1][x]=Liste[y+1][x].upper()
                    if index==2: # Links
                        Liste[y][x-1]=Liste[y][x-1].upper()
                    if index==3: # Oben
                        Liste[y-1][x]=Liste[y-1][x].upper()
                    # Mache objekt selber passiv
                    Liste[y][x]=Liste[y][x].upper()
    
    # Wenn etwas veraendert wurde                
    if Vergleich!=Liste: return Sicher(Liste) # Fuehre Sicher nocheinmal aus
    # Sonst: gebe Liste zurueck
    else: return Liste 

# Funktion, um die Ecken zu fuellen
def Eckpunkte(Liste): 
    grosse=len(Liste)-1
    # Ecke oben links
    if not(Liste[1][0]=="" and Liste[0][1]=="") and Liste[0][0]=="":  # Wenn ein Nachbar gefuellt ist und Ecke leer ist
        # wenn der leere Nachbar unten ist
        if Liste[1][0]!="": 
            Liste[0][0]=Liste[1][0]
            Liste[1][0]=Liste[1][0].upper()
        else: # rechts
            Liste[0][0]=Liste[0][1]
            Liste[0][1]=Liste[0][1].upper()
    # Ecke unten links
    if not(Liste[grosse][1]=="" and Liste[grosse-1][0]=="") and Liste[grosse][0]=="":  
        if Liste[grosse][1]!="": # rechts
            Liste[grosse][0]=Liste[grosse][1]
            Liste[grosse][1]=Liste[grosse][1].upper()
        else: #oben
            Liste[grosse][0]=Liste[grosse-1][0]
            Liste[grosse-1][0]=Liste[grosse-1][0].upper()
    # Ecke unten rechts
    if not(Liste[grosse][grosse-1]=="" and Liste[grosse-1][grosse]=="") and Liste[grosse][grosse]=="": 
        if Liste[grosse][grosse-1]!="": # links
            Liste[grosse][grosse]=Liste[grosse][grosse-1]
            Liste[grosse][grosse-1]=Liste[grosse][grosse-1].upper()
        else: # oben
            Liste[grosse][grosse]=Liste[grosse-1][grosse]
            Liste[grosse-1][grosse]=Liste[grosse-1][grosse].upper()
    # Ecke oben rechts
    if not(Liste[0][grosse-1]=="" and Liste[1][grosse]=="") and Liste[0][grosse]=="":
        if Liste[0][grosse-1]!="": # links
            Liste[0][grosse]=Liste[0][grosse-1]
            Liste[0][grosse-1]=Liste[0][grosse-1].upper()
        else: # unten
            Liste[0][grosse]=Liste[1][grosse]
            Liste[1][grosse]=Liste[1][grosse].upper()
    return Liste # Gib Liste zurueck

# Funktion, um den "Sinn" eines Versuches zu testen
def Test(Liste, Richtung):
    Fehler="Fertig" # Variable, die den aktuellen "Sinn" der Aufgabe speichert
    # Fuer jedes Objekt in der Liste
    for y in range(len(Liste)):
        for x in range(len(Liste)):
            if Fehler!="Fehler":
                # Nachbarn speichern aber ohne Zahl
                Nachbarn=[]
                # Nachbar Rechts
                if x<len(Liste[y])-1: Nachbarn.append(Liste[y][x+1][:-1])
                else: Nachbarn.append("none")
                # Nachbar Unten
                if y<len(Liste)-1: Nachbarn.append(Liste[y+1][x][:-1])
                else: Nachbarn.append("none")
                # Nachbar Links
                if x>0:  Nachbarn.append(Liste[y][x-1][:-1])
                else: Nachbarn.append("none")
                # Nachbar Oben
                if y>0: Nachbarn.append(Liste[y-1][x][:-1])
                else: Nachbarn.append("none")
                # Wenn kein gleicher Nachbar
                if not Liste[y][x][:-1] in Nachbarn: Fehler="Weiter"
                
                # Fehler 1: Leeres Feld mit nur unterschiedlichen Nachbarn
                if Liste[y][x]=="" and not "" in Nachbarn:
                    Leer_Feld=True
                    for i in Nachbarn:
                        if i !="none" and i.upper()!=i and Nachbarn.count(i)==2:
                            Leer_Feld=False
                    if Leer_Feld:Fehler="Fehler"
                
                # Fehler 2: aktives Feld ist eingeschlossen
                if Liste[y][x]==Liste[y][x].lower() and Liste[y][x]!="": #Aktives Ende
                    if Nachbarn.count("")==0: Fehler="Fehler"
                
                # Fehler 3: Keine Gleichfarbenen Nachbarn
                if Liste[y][x]!="":
                    Feld=True
                    for i in Nachbarn:
                        if i.lower() in Liste[y][x].lower():
                            Feld=False
                    if Feld: Fehler="Fehler"
                
                # Fehler 4: Feld hat mehr als 2 gleichfarbene Nachbarn
                if Liste[y][x] != "":
                    counter=0
                    for i in Nachbarn:
                        if i != "" and i.lower() in Liste[y][x].lower():
                            counter+=1
                    if counter > 2:
                        Fehler="Fehler"
    
    # Mit dem Argument Richtung gibt Test "Fehler" zurueck. Somit kann Test auch aus der Funktion Sicher gesteuert werden. 
    if Richtung == "none": Fehler="Fehler"
                
    return Fehler

# Funktion, um Nachbarn des Elementes Liste[y][x] zu bekommen
def Nachbar(Liste, x, y):
    Nachbarn=[]
    # Nachbar Rechts
    if x<len(Liste[y])-1: Nachbarn.append(Liste[y][x+1])
    else: Nachbarn.append("none") # Ist der Nachbar eine Wand wird "none" hinzugefuegt
    # Nachbar Unten
    if y<len(Liste)-1: Nachbarn.append(Liste[y+1][x])
    else: Nachbarn.append("none")
    # Nachbar Links
    if x>0:  Nachbarn.append(Liste[y][x-1])
    else: Nachbarn.append("none")
    # Nachbar Oben
    if y>0: Nachbarn.append(Liste[y-1][x])
    else: Nachbarn.append("none")
    return Nachbarn

def Raten(Grid,z):
    Farben = [] # hat die Anfaenge der Leitungen gespeichert
    for y in Grid: 
        for x in y: 
            if x !="" and x.upper() != x: Farben.append(x)
    # Schon geloeste Leitungen aus Farben entfernen
    for Farbe in list(Farben): # list(), da sonst nur jedes zweite entfernt wird
        boolean=True # Wird false, wenn aktive Enden gefunden
        for a in range(len(Grid)):
            for b in range(len(Grid)):
                if Farbe == Grid[a][b]: boolean = False
        if boolean or "2" in Farbe: Farben.remove(Farbe)   
    
    index_farben = 0 # Index, welche Farbe aus Farben verwendet werden soll
    # Suche die Koordinaten des aktiven Endes Farben[index_farben]
    for a in range(len(Grid)):
        for b in range(len(Grid)):
            if Grid[a][b]==Farben[index_farben]: y=a; x=b
        
    Verlauf = [[Grid, "E", x, y]] # [0]:Aufgabe  [1]:Richtung in welche zu gehen ist  [2]:x  [3]:y 
    Boolean = True # Level fertig: False -> Faellt aus while-Schlaufe
    Farbe_fertig = False # Macht, dass ein neues x,y definiert wird
    Richtungen = ["E","S","W","N"] # Liste mit den moeglichen Richtungen
        
    while Boolean:
#        z.show(Verlauf[-1][0])
#        time.sleep(0.5)
        Operation=Test(Verlauf[-1][0],Verlauf[-1][1]) # Letzten Versuch testen
        if Operation=="Weiter":
            # Wenn im letzten Versuch eine Leitung vollendent wurde, muessen neue Koordinaten gesucht werden
            if Farbe_fertig:
                index_farben+=1
                for a in range(len(Grid)):
                    for b in range(len(Grid)):
                        if Verlauf[-1][0][a][b]==Farben[index_farben]: y=a; x=b
                Verlauf.append([Verlauf[-1][0], "E", x, y])
                Farbe_fertig = False
            
            # Neuen Versuch machen 
            Info=Bauen(copy.deepcopy(Verlauf[-1][0]),x,y, Verlauf[-1][1])
            # aenderungen speichern
            Verlauf[-1][1]=Info[3]
            if Info[3] != "none":
                x = Info[1]
                y = Info[2]
                Verlauf.append([Info[0],"E",x,y])  
                        
        if Operation=="Fehler":
            Farbe_fertig=False
            Verlauf.remove(Verlauf[-1]) # Letzten Versuch loeschen
            # Wenn im letzten Versuch alle Optionen versucht wurden, entferne auch diese Versuche
            while Verlauf[-1][1]=="N":
                Verlauf.remove(Verlauf[-1])
            # Setze die Richtung des letzten Versuches ein Index nach oben
            Verlauf[-1][1]=Richtungen[Richtungen.index(Verlauf[-1][1]) + 1]
            # Speichere Koordinaten
            x = Verlauf[-1][2]
            y = Verlauf[-1][3]
            # index_farben richten
            if Farben[index_farben] != Verlauf[-1][0][y][x].lower():
                index_farben-=1
            
        if Operation=="Fertig":
            Boolean=False
            return Verlauf[-1][0]
        
        # Testen, ob zwei Enden nebeneinander liegen
        Nachbarn=Nachbar(Verlauf[-1][0],x,y)
        for i in Nachbarn:
            # Ist der Nachbar ein aktives Ende der selben Farbe
            if i !="" and i[:-1] in Verlauf[-1][0][y][x]:
                # Setzte aktiven Nachbar auf Passiv
                # Rechts
                if Nachbarn.index(i) == 0: Verlauf[-1][0][y][x+1]=Verlauf[-1][0][y][x+1].upper()
                # Unten
                if Nachbarn.index(i) == 1: Verlauf[-1][0][y+1][x]=Verlauf[-1][0][y+1][x].upper()
                # Links
                if Nachbarn.index(i) == 2:  Verlauf[-1][0][y][x-1]=Verlauf[-1][0][y][x-1].upper()
                # Oben
                if Nachbarn.index(i) == 3: Verlauf[-1][0][y-1][x]=Verlauf[-1][0][y-1][x].upper()
                # Setze objekt auf Passiv
                Verlauf[-1][0][y][x]=Verlauf[-1][0][y][x].upper()
                Farbe_fertig=True

def Bauen(Grid, x,y, Richtung):
    # Ist Grid[y][x] ein aktives Ende
    if Grid[y][x].upper() != Grid[y][x]:
        # Extrudieren nach rechts
        if Richtung=="E":
            if x<len(Grid[y])-1 and Grid[y][x+1]=="":
                Grid[y][x+1]=Grid[y][x]
                Grid[y][x]=Grid[y][x].upper()
                x+=1
            else: Richtung="S"
        # Extrudieren nach unten
        if Richtung=="S":
            if y<len(Grid)-1 and Grid[y+1][x]=="":
                Grid[y+1][x]=Grid[y][x]
                Grid[y][x]=Grid[y][x].upper()
                y+=1
            else: Richtung="W"
        # Extrudieren nach links
        if Richtung=="W":
            if x>0 and Grid[y][x-1]=="":
                Grid[y][x-1]=Grid[y][x]
                Grid[y][x]=Grid[y][x].upper()
                x-=1
            else: Richtung="N"
        # Extrudieren nach oben
        if Richtung=="N":
            if y>0 and Grid[y-1][x]=="":
                Grid[y-1][x]=Grid[y][x]
                Grid[y][x]=Grid[y][x].upper()
                y-=1
            else: Richtung="none"
    return Grid, x,y, Richtung