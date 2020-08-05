from pieces import *
import random as rnd
import tkinter as tk

window = tk.Tk()
info = tk.Frame(width = 150, height = 800, master = window)
pointNumLbl = tk.Label(text = "0", master = info, font = ("Helvetica", 15))
linesNumLbl = tk.Label(text = "0", master = info, font = ("Helvetica", 15))
levelNumLbl = tk.Label(text= "0", master = info, font = ("Helvetica", 15))


afterID = 0
mat = [[0 for i in range(0,400,25)] for j in range(0,600,25)]
cases = {0:drawStraightPiece, 1:drawSquarePiece, 2: drawTPiece, 3: drawSPiece, 4: drawZPiece, 5: drawJPiece, 6: drawLPiece}
places = {0: (40, 5), 1: (30, 30), 2: (20, 50), 3: (20, 50), 4: (20, 30), 5: (20, 30), 6: (20, 30)}
actual = 0
next = 0
linesCleared = 0
level = 0
points = 0
TICKPERSECOND = 1

#only to be used on nextCanvas
def drawRandPiece(canvas):
    global actual, next
    actual = next
    next = rnd.randrange(7)
    cases[next](canvas,places[next][0], places[next][1])

def cleanCanvas(canvas):
    for id in canvas.find_all():
        canvas.delete(id)

def gameOver(canvas, nextCanvas):
    print("Lost")
    global afterID
    window.after_cancel(afterID)
    canvas.delete(tk.ALL)
    canvas.unbind("<Up>")
    canvas.unbind("<Left>")
    canvas.unbind("<Right>")
    canvas.unbind("<Down>")
    canvas.unbind("<space>")
    color = {0: "#003333", 1: "#333300", 2: "#300030", 3: "#003000", 4: "#330000", 5: "#331100", 6: "#000033"}
    for i in range(0, 400, 25):
        for j in range(0, 600, 25):
            canvas.create_rectangle(i, j, i+25, j+25, fill = color[rnd.randint(0,6)])
    canvas.create_text(200, 200, text = "GAME OVER", font = ("Impact", 60), fill = "white")
    canvas.create_text(200, 300, text = "New Game?", font = ("Impact", 45), fill = "white")
    canvas.create_text(200, 400, text = "Press Any Key", font = ("Impact", 45), fill = "gold")


    canvas.bind("<Key>",lambda event : newGame(canvas, nextCanvas))

def newGame(mainCanvas, nextCanvas):
    mainCanvas.unbind("<Key>")
    mainCanvas.delete(tk.ALL)
    mainCanvas.bind("<Up>", rotate)
    mainCanvas.bind("<Left>", moveLeft)
    mainCanvas.bind("<Right>", moveRight)
    mainCanvas.bind("<Down>", moveDown)
    mainCanvas.bind("<space>", lambda event: fall(event, nextCanvas))

    global linesCleared, points, level, TICKPERSECOND,mat, afterID
    mat = [[0 for i in range(0,400,25)] for j in range(0,600,25)]
    linesCleared = 0
    points = 0
    level = 0
    TICKPERSECOND = 1
    linesNumLbl.config(text = str(linesCleared))
    pointNumLbl.config(text = str(points))
    levelNumLbl.config(text = str(level))

    drawRandPiece(nextCanvas)
    cleanCanvas(nextCanvas)
    drawRandPiece(nextCanvas)
    cases[actual](mainCanvas, 175, 25)
    afterID = window.after(1000,tick, mainCanvas, nextCanvas, window)

def checkRow(row):
    for j in range(400 // 25):
        if mat[row][j] == 0:
            return False
    return True

def removeRow(canvas, toRemove):
    for row in toRemove:
        canvas.delete("row"+str(row))
        for j in range(400 // 25):
            mat[row][j] = 0
    for row in sorted(toRemove):
        for rowToLower in range(row -1, 0, -1):
            canvas.move("row"+str(rowToLower),0,25)
            for j in range(400 // 25):
                mat[rowToLower + 1][j] = mat[rowToLower][j]
            for id in canvas.find_withtag("row"+str(rowToLower)):
                canvas.dtag(id,"row"+str(rowToLower))
                canvas.addtag("row"+str(rowToLower +1),"withtag", id)

def updatePointLvlLines(howMany):
    global linesCleared, points, level, TICKPERSECOND
    linesCleared += howMany
    multiplier = {1: 1, 2: 2.5, 3: 7.5, 4: 30}
    points += (level + 1) * 40 * multiplier[howMany]
    level = linesCleared // 10
    TICKPERSECOND = max(level,1)
    linesNumLbl.config(text = str(linesCleared))
    pointNumLbl.config(text = str(points))
    levelNumLbl.config(text = str(level))

def stopPiece(canvas, nextCanvas):
    falling = canvas.find_withtag("falling")
    rowsToRemove = set({})
    for id in falling:
        canvas.dtag(id,"falling")
        coord = canvas.coords(id)
        row = int(coord[1]) // 25
        mat[row][int(coord[0]) // 25] = 1
        canvas.addtag("row"+str(row),"withtag",id)
        if checkRow(row):
            rowsToRemove.add(row)
    if len(rowsToRemove):
        updatePointLvlLines(len(rowsToRemove))
    removeRow(canvas, rowsToRemove)
    dtagAll(canvas)
    cleanCanvas(nextCanvas)
    drawRandPiece(nextCanvas)
    cases[actual](canvas, 175, 25)
    if checkHitOtherPiece(canvas):
        return True
    return False

# BUG: Quando faccio game over e il gameOver è stato chiamato da fall e reinizio subito fa due tick anzichè uno WTF
# Questo perchè lo scheduling del prossimo tick viene fatto in tick, e quindi esiste ancora se faccio in fall

def tick(canvas, nextCanvas, window):
    global mat, afterID
    print("tick")
    lost  = False
    canvas.move("falling",0,25)
    if not checkInBound(canvas) or checkHitOtherPiece(canvas):
        canvas.move("falling",0,-25)
        lost = stopPiece(canvas, nextCanvas)
    if not lost:
        afterID = window.after(1000 // TICKPERSECOND, tick, canvas, nextCanvas, window)
    else:
        gameOver(canvas, nextCanvas)

#return True se ha colpito un altro pezzo
def checkHitOtherPiece(canvas):
    falling = canvas.find_withtag("falling")
    for a in falling:
        coord = canvas.coords(a)
        #se la cella in cui è è occupata return True
        #coord[0] sono le x, quindi le colonne
        #coord[1] sono le y, quindi le righe
        if mat[int(coord[1]) // 25][int(coord[0]) // 25] == 1:
            return True
    return False
#Maybe: Controllare dove va fuori e gestire di conseguenza
# Del tipo: se nella rotate va fuori a destra, muoverlo a sinistra fino a che è dentro
def checkInBound(canvas):
    falling = canvas.find_withtag("falling")
    for a in falling:
        coord = canvas.coords(a)
        if coord[0] < 0 or coord[2] > 400 or coord[3] > 600:
            return False
    return True

def rotate(event):
    canvas = event.widget
    tags = canvas.gettags("falling")
    if "I" in tags:
        rotateStraigth(canvas)
        if not checkInBound(canvas) or checkHitOtherPiece(canvas):
            rotateStraigth(canvas)
    elif "Sqaure" in tags:
        pass
    elif "S" in tags:
        rotateS(canvas)
        if not checkInBound(canvas) or checkHitOtherPiece(canvas):
            rotateS(canvas)
    elif "Z" in tags:
        rotateZ(canvas)
        if not checkInBound(canvas) or checkHitOtherPiece(canvas):
            rotateZ(canvas)
    elif "T" in tags:
        rotateTRight(canvas)
        if not checkInBound(canvas) or checkHitOtherPiece(canvas):
            rotateTLeft(canvas)
    elif "J" in tags:
        rotateJRight(canvas)
        if not checkInBound(canvas) or checkHitOtherPiece(canvas):
            rotateJLeft(canvas)
    elif "L" in tags:
        rotateLRight(canvas)
        if not checkInBound(canvas) or checkHitOtherPiece(canvas):
            rotateLLeft(canvas)

def moveLeft(event):
    event.widget.move("falling", -25, 0)
    if not checkInBound(event.widget) or checkHitOtherPiece(event.widget):
        event.widget.move("falling", 25, 0)

def moveRight(event):
    event.widget.move("falling", 25, 0)
    if not checkInBound(event.widget) or checkHitOtherPiece(event.widget):
        event.widget.move("falling",-25, 0)

def moveDown(event):
    event.widget.move("falling", 0, 25)
    if not checkInBound(event.widget) or checkHitOtherPiece(event.widget):
        event.widget.move("falling", 0, -25)

def fall(event, nextCanvas):
    while checkInBound(event.widget) and not checkHitOtherPiece(event.widget):
        event.widget.move("falling", 0, 25)
    event.widget.move("falling", 0, -25)
    if stopPiece(event.widget, nextCanvas):
        gameOver(event.widget, nextCanvas)











#cose
