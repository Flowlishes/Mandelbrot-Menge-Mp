"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 21.02.2017
"""

#Modul für die graphische Darstellung
import tkinter

#Mathematikmodul, beispielsweise für das Quadrieren benötigt
import math

#eigenes Modul für die Farbwahl, siehe farben.py
import farben


#Falls Änderung der Größe des Fensters, alle weiteren Angaben sind relativ
xwidth = 500
yheight = 500


#Initialisierung Variablen
deltax = None
deltay = None


#Erzeugung des Fensters aus dem tkinter-Modul
#Fenster bleibt, Canvas immer überschrieben
fenster = tkinter.Tk()
#Titel des erzeugten Fensters
fenster.title("Die Mandelbrot-Menge.")

#Erzeugen der Zeichenoberfläche aus dem tkinter-Modul
#Bedeutung der Parameter:
    #fenster: Canvas befindet sich im oben erstellen Fenster
    #width und height: oben festgelegte Höhe und Breite
w = tkinter.Canvas(fenster, width=xwidth, height=yheight)
#Ohne .pack() wird diese nicht korrekt dargestellt
w.pack()


#Endlosschleife
while True:
    #Eingabe, Anzeige gibt Abstand zur vorherigen Eingabe --> bessere Darstellung
    print("""\
    \n
-----------------------------------
Eingabe des anzuzeigenden Bereichs:
-----------------------------------
""")
    #-------------
    #Möglichkeit bei jeder Eingabe Programm sicher zu beenden
    #Eingabe wird in float(), also Gleitkommazahl umgewandelt
    #-------------
    try:
        xmin = float(input("xMin eingeben: "))
    #Falls Eingabe nicht in float() umgewandelt werden kann
    except ValueError:
        entscheidung = str(input("Programm beenden? (ja/nein) "))
        if entscheidung == "ja":
            break
        else:
            print("Erneute Eingabe von xMin:")
            xmin = float(input("xMin eingeben: "))
    try:
        xmax = float(input("xMax eingeben: "))
    #Falls falscher Eingabewert
    except ValueError:
        entscheidung = str(input("Programm beenden? (ja/nein) "))
        if entscheidung == "ja":
            break
        else:
            print("Erneute Eingabe von xMax:")
            xmax = float(input("xMax eingeben: "))
    try:
        ymin = float(input("yMin eingeben: "))
    #Falls falscher Eingabewert
    except ValueError:
        entscheidung = str(input("Programm beenden? (ja/nein) "))
        if entscheidung == "ja":
            break
        else:
            print("Erneute Eingabe von yMin:")
            ymin = float(input("yMin eingeben: "))

    #Löschen aller Objekte auf der Zeichenoberfläche
    #Überschreibung beim Zoom nötig
    w.delete("all")
    #Berechnung ymax --> eine Eingabe weniger
    ymax = (xmax - xmin) + ymin
    #Berechnung der beiden Deltas --> Schritte
    deltax = (xmax - xmin)/xwidth
    deltay = (ymax - ymin)/yheight

    #Durchgehen der einzelnen Pixel in Form einer 2-dimensionalen Liste
    for xpixel in range(0, xwidth):
        #Berechnung des Realteils des Parameters c
        cr = xmin + (xpixel * deltax)
        for ypixel in range(0, xwidth):
            #Berechnung Imaginärteil des Parameters c
            ci = ymin + (ypixel * deltay)
            #-------------
            #Position des Pixels ist jetzt bekannt (cr/ci))
            #-------------
            #Iterationschritte für jeden Pixel --> rekursive Folge durchlaufen
            #-------------
            #Wert des Realteils
            zi = 0
            #Wert des Imaginärteils
            zr = 0

            #Entweder Abstand (Betrag der komplexen Zahl )zum Ursprung größer als 2 --> divergiert mit Sicherheit
            #oder maximal 100 Iterationsschritte, bis dahin keine Divergenz --> innerhalb der Menge
            #je schneller der Wert konvergiert, desto dunkler die Farbe des Pixels --> Verweis Farbmodul

            #Zähler Iterationsschritte initialisiert
            n = 0

            #Abbruchbedingung
            while ((zr**2 + zi**2)<=2) and n <= 100:
                #-------------
                #Rekursive Folge lautet: z_(n+1) = z_(n)^2 + c
                #Komplexe Multiplikation durchführen
                #-------------

                #Neuer Realteil
                zrneu = zr * zr - zi * zi + cr
                #Neuer Imaginärteil
                zineu = 2 * zr * zi + ci

                #Übergeben der Werte für die nächste Iteration
                zr = zrneu
                zi = zineu
                #Erhöhung Iterationschritt
                n += 1
            #-------------
            #Vergeben der Farbe des Pixels wenn die Schleife abbricht --> Wert divergiert, geht gegen unendlich
            #Modul (Aufruf über .farbwahl) gibt über return(color) die Farbe zurück
            #-------------
            color = farben.farbwahl(n)
            #Erzeugung des Pixels einzelnen Pixels an der Position (cr/ci)
            #Bedeutung der Paramter der rectangle-Funktion:
                #Wert 1 und 2: Koordinaten der "Startposition"
                #Wert 2 und 3: Koordinaten der "Endposition"
                #die beiden Punkte spannen die Ecken des Rechtecks auf
                #fill: Füllfarbe, die das Modul übergibt
                #width: Dicke des Randes, der standardmäßig schwarz ist, width=0 --> keinen Rand
            # w. bezieht sich auf die Zeichenfläche (Canvas, oben erstellt)
            w.create_rectangle(xpixel, ypixel, xpixel, ypixel , fill=color, width=0)
