from gpanel import *
#Aufloesung:
# Breite: 1368
# Hoehe:    768

def get():
    hoehe = 768
    breite = 1368
    
    feld_size = 80
    
    os.system("java -jar taker.jar screenshot.png")
    
    img = getImage("screenshot.png")
    #image(img,0,hoehe)
    
    #Oben:
    #105
    #Unten:
    #580
    #Links:
    #446
    #Rechts:
    #921
     
    img = GBitmap.crop(img,446,580,921,105)
    breite = img.getWidth()
    hoehe = img.getHeight()
    
    images = [
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""]]
    
    def most_common(lst):
        return max(set(lst), key=lst.count)
    
    def getColorFromCenter(img):
        x = img.getWidth()//2
        y = img.getHeight()//2
        colors = []
        for x2 in range(-2,2):
            for y2 in range(-2,2):
                colors.append(img.getPixelColor(x+x2,y+y2))
        col = most_common(colors)
        
        #Returne richtige Farbe
        if col.getRed()==0 and col.getBlue()==0 and col.getGreen()==0:
            return ""
        elif col.getRed()==238 and col.getBlue()==0 and col.getGreen()==238:
            return "gelb"
        elif col.getRed()==255 and col.getBlue()==0 and col.getGreen()==0:
            return "rot"
        elif col.getRed()==0 and col.getBlue()==0 and col.getGreen()==128:
            return "grun"
        elif col.getRed()==0 and col.getBlue()==255 and col.getGreen()==0:
            return "blau"
        elif col.getRed()==255 and col.getBlue()==0 and col.getGreen()==127:
            return "orange"
        elif col.getRed()==0 and col.getBlue()==255 and col.getGreen()==255:
            return "hellbl"
        elif col.getRed()==255 and col.getBlue()==255 and col.getGreen()==0:
            return "violet"
        else:
            return ""
    
    #Crop Images
    cols = []
    for y in range(6):
        for x in range(6):
            string = getColorFromCenter(GBitmap.crop(img,x*feld_size,(y+0)*feld_size,(x+1)*feld_size,(y+1)*feld_size))
            str1 = string + "1"
            if not len(string) == 0:
                #Farbe mit 1 falls nicht schon in Liste, sonst mit 2 am Schluss
                if str1 in cols:
                    images[y][x]=string + "2"
                else:
                    images[y][x] = string + "1"
                    cols.append(string+"1")
    return images  