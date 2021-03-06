## import tkinter as tk
#######################  Drawing    ##########################
def drawStraightPiece(canvas, X, Y):
    ########  Straigth piece    ########### 40 5
    canvas.create_rectangle((X, Y, X + 25, Y + 25), fill = 'cyan', tags = ("falling","A","I"))
    canvas.create_rectangle((X, Y + 25, X + 25, Y + 50), fill = 'cyan', tags = ("falling","B","I"))
    canvas.create_rectangle((X, Y + 50, X + 25, Y + 75), fill = 'cyan', tags = ("falling","C","I"))
    canvas.create_rectangle((X, Y + 75, X + 25, Y + 100), fill = 'cyan', tags = ("falling","D","I"))

def drawSquarePiece(canvas, X, Y):
    ########    Square Piece   ############ 30 30
    canvas.create_rectangle((X, Y, X +25, Y +25), fill = "yellow", tags = ("falling","A","Square"))
    canvas.create_rectangle((X +25, Y, X +50, Y +25), fill = "yellow", tags = ("falling","B","Square"))
    canvas.create_rectangle((X, Y +25, X +25, Y +50), fill = "yellow", tags = ("falling","C","Square"))
    canvas.create_rectangle((X +25, Y +25, X +50, Y +50), fill = "yellow", tags = ("falling","D","Square"))

def drawTPiece(canvas, X, Y):
    #######    T piece        ############ 20 50
    canvas.create_rectangle((X, Y, X +25, Y +25), fill = "purple", tags = ("falling","A","T"))
    canvas.create_rectangle((X +25, Y -25, X +50, Y), fill = "purple", tags = ("falling","B","T"))
    canvas.create_rectangle((X +25, Y, X +50, Y +25), fill = "purple", tags = ("falling","C","T"))
    canvas.create_rectangle((X +50, Y, X +75, Y +25), fill = "purple", tags = ("falling","D","T"))

def drawSPiece(canvas, X, Y):
    ########     S piece       ############ 20 50
    canvas.create_rectangle((X, Y, X +25, Y +25), fill = "green", tags = ("falling","A","S"))
    canvas.create_rectangle((X +25, Y -25, X +50, Y), fill = "green", tags = ("falling","B","S"))
    canvas.create_rectangle((X +25, Y, X +50, Y +25), fill = "green", tags = ("falling","C","S"))
    canvas.create_rectangle((X +50, Y -25, X +75, Y), fill = "green", tags = ("falling","D","S"))

def drawZPiece(canvas, X, Y):
    #######     Z piece       ############ 20 30
    canvas.create_rectangle((X, Y, X +25, Y +25), fill = "red", tags = ("falling","A","Z"))
    canvas.create_rectangle((X +25, Y, X +50, Y +25), fill = "red", tags = ("falling","B","Z"))
    canvas.create_rectangle((X +25, Y +25, X +50, Y+50), fill = "red", tags = ("falling","C","Z"))
    canvas.create_rectangle((X +50, Y +25, X +75, Y +50), fill = "red", tags = ("falling","D","Z"))

def drawLPiece(canvas, X, Y):
    ########     L piece       ############ 20 30
    canvas.create_rectangle((X, Y, X +25, Y +25), fill = "orange", tags = ("falling","A","L"))
    canvas.create_rectangle((X +25, Y, X +50, Y +25), fill = "orange", tags = ("falling","B","L"))
    canvas.create_rectangle((X +50, Y, X +75, Y +25), fill = "orange", tags = ("falling","C","L"))
    canvas.create_rectangle((X, Y +25, X +25, Y +50), fill = "orange", tags = ("falling","D","L"))

def drawJPiece(canvas, X, Y):
    ########     J piece       ############ 20 30
    canvas.create_rectangle((X, Y, X +25, Y +25), fill = "blue", tags = ("falling","A","J"))
    canvas.create_rectangle((X +25, Y, X +50, Y +25), fill = "blue", tags = ("falling","B","J"))
    canvas.create_rectangle((X +50, Y, X +75, Y +25), fill = "blue", tags = ("falling","C","J"))
    canvas.create_rectangle((X +50, Y +25, X +75, Y +50), fill = "blue", tags = ("falling","D","J"))
################ Rotating ######################
def rotateStraigth(canvas):
    a, c, d, e, f, g = canvas.find_withtag("A"), canvas.find_withtag("C"), canvas.find_withtag("D"), canvas.find_withtag("E"), canvas.find_withtag("F"), canvas.find_withtag("G")
    canvas.move(a,-25, 25)
    canvas.move(c, 25, -25)
    canvas.move(d, 50, -50)
    canvas.move(e, 25, -25)
    canvas.move(f,-25, 25)
    canvas.move(g,-50, 50)
    canvas.addtag("E","withtag",a)
    canvas.addtag("A","withtag",e)
    canvas.addtag("C","withtag",f)
    canvas.addtag("F","withtag",c)
    canvas.addtag("D","withtag",g)
    canvas.addtag("G","withtag",d)
    canvas.dtag(a,"A")
    canvas.dtag(c,"C")
    canvas.dtag(d,"D")
    canvas.dtag(e,"E")
    canvas.dtag(f,"F")
    canvas.dtag(g,"G")

def rotateTRight(canvas):
    a, b, d, e = canvas.find_withtag("A"),canvas.find_withtag("B"),canvas.find_withtag("D"),canvas.find_withtag("E")
    canvas.move(a,25, -25)
    canvas.move(b, 25, 25)
    canvas.move(d, -25, 25)
    canvas.move(e, -25, -25)
    canvas.addtag("B","withtag",a)
    canvas.addtag("D","withtag",b)
    canvas.addtag("E","withtag",d)
    canvas.addtag("A","withtag",e)
    canvas.dtag(a,"A")
    canvas.dtag(b,"B")
    canvas.dtag(d,"D")
    canvas.dtag(e,"E")

def rotateTLeft(canvas):
    a, b, d, e = canvas.find_withtag("A"),canvas.find_withtag("B"),canvas.find_withtag("D"),canvas.find_withtag("E")
    canvas.move(a, 25, 25)
    canvas.move(b, -25, 25)
    canvas.move(d, -25, -25)
    canvas.move(e, 25, -25)
    canvas.addtag("B","withtag",d)
    canvas.addtag("D","withtag",e)
    canvas.addtag("E","withtag",a)
    canvas.addtag("A","withtag",b)
    canvas.dtag(a,"A")
    canvas.dtag(b,"B")
    canvas.dtag(d,"D")
    canvas.dtag(e,"E")

def rotateS(canvas):
    b, d, e, f = canvas.find_withtag("B"), canvas.find_withtag("D"), canvas.find_withtag("E"), canvas.find_withtag("F")
    canvas.move(b, -25, 0)
    canvas.move(d, -25, 50)
    canvas.move(e, 25, 0)
    canvas.move(f, 25, -50)
    canvas.addtag("E", "withtag",b)
    canvas.addtag("B", "withtag",e)
    canvas.addtag("F", "withtag",d)
    canvas.addtag("D", "withtag",f)
    canvas.dtag(b,"B")
    canvas.dtag(d,"D")
    canvas.dtag(e,"E")
    canvas.dtag(f,"F")

def rotateZ(canvas):
    c, d, e, f = canvas.find_withtag("C"), canvas.find_withtag("D"), canvas.find_withtag("E"), canvas.find_withtag("F")
    canvas.move(c, -25, 0)
    canvas.move(d, -25, -50)
    canvas.move(e, 25, 0)
    canvas.move(f, 25, +50)
    canvas.addtag("E", "withtag",c)
    canvas.addtag("C", "withtag",e)
    canvas.addtag("F", "withtag",d)
    canvas.addtag("D", "withtag",f)
    canvas.dtag(c,"C")
    canvas.dtag(d,"D")
    canvas.dtag(e,"E")
    canvas.dtag(f,"F")

def rotateLLeft(canvas):
    a, c, c1, d, e, f, f1, g, h, m = canvas.find_withtag("A"), canvas.find_withtag("C"), canvas.find_withtag("C2"), canvas.find_withtag("D"), canvas.find_withtag("E"), canvas.find_withtag("F"), canvas.find_withtag("F2"), canvas.find_withtag("G"), canvas.find_withtag("H"),canvas.find_withtag("M")
    canvas.move(a, +25, -25)
    canvas.move(c, 0, 25)
    canvas.move(c1, -50, -25)
    canvas.move(d, +25, 0)
    canvas.move(e, -25, +25)
    canvas.move(f, +25, -50)
    canvas.move(f1, -25, 0)
    canvas.move(g, 0, -25)
    canvas.move(h, -25, 50)
    canvas.move(m, 50, +25)
    canvas.addtag("A", "withtag",e)
    canvas.addtag("E", "withtag",a)
    canvas.addtag("G", "withtag",c)
    canvas.addtag("C2", "withtag",g)
    canvas.addtag("M", "withtag",c1)
    canvas.addtag("C", "withtag",m)
    canvas.addtag("F2", "withtag",h)
    canvas.addtag("H", "withtag",f)
    canvas.addtag("F", "withtag",d)
    canvas.addtag("D", "withtag",f1)
    canvas.dtag(a,"A")
    canvas.dtag(c,"C")
    canvas.dtag(c1,"C2")
    canvas.dtag(d,"D")
    canvas.dtag(e,"E")
    canvas.dtag(f,"F")
    canvas.dtag(f1,"F2")
    canvas.dtag(g,"G")
    canvas.dtag(h,"H")
    canvas.dtag(m,"M")

def rotateLRight(canvas):
    a, c, c1, d, e, f, f1, g, h, m = canvas.find_withtag("A"), canvas.find_withtag("C"), canvas.find_withtag("C2"), canvas.find_withtag("D"), canvas.find_withtag("E"), canvas.find_withtag("F"), canvas.find_withtag("F2"), canvas.find_withtag("G"), canvas.find_withtag("H"),canvas.find_withtag("M")
    canvas.move(a, +25, -25)
    canvas.move(c, -50, -25)
    canvas.move(c1, 0, 25)
    canvas.move(d, +25, 0)
    canvas.move(e, -25, +25)
    canvas.move(f, -25, 0)
    canvas.move(f1, +25, -50)
    canvas.move(g, 0, -25)
    canvas.move(h, -25, 50)
    canvas.move(m, 50, +25)
    canvas.addtag("A", "withtag",e)
    canvas.addtag("E", "withtag",a)
    canvas.addtag("M", "withtag",c)
    canvas.addtag("C2", "withtag",m)
    canvas.addtag("G", "withtag",c1)
    canvas.addtag("C", "withtag",g)
    canvas.addtag("F", "withtag",h)
    canvas.addtag("D", "withtag",f)
    canvas.addtag("F2", "withtag",d)
    canvas.addtag("H", "withtag",f1)
    canvas.dtag(a,"A")
    canvas.dtag(c,"C")
    canvas.dtag(c1,"C2")
    canvas.dtag(d,"D")
    canvas.dtag(e,"E")
    canvas.dtag(f,"F")
    canvas.dtag(f1,"F2")
    canvas.dtag(g,"G")
    canvas.dtag(h,"H")
    canvas.dtag(m,"M")

def rotateJLeft(canvas):
    a, c, d, e, f, g, h, m = canvas.find_withtag("A"), canvas.find_withtag("C"), canvas.find_withtag("D"), canvas.find_withtag("E"), canvas.find_withtag("F"), canvas.find_withtag("G"), canvas.find_withtag("H"), canvas.find_withtag("M")
    canvas.move(a, +25, -25)
    canvas.move(c, -25, +25)
    canvas.move(d, 0, -50)
    canvas.move(e, -25, 25)
    canvas.move(f, 25, -25)
    canvas.move(g, 50, 0)
    canvas.move(h, -50, 0)
    canvas.move(m, 0, 50)
    canvas.addtag("A","withtag",e)
    canvas.addtag("E","withtag",a)
    canvas.addtag("C","withtag",f)
    canvas.addtag("F","withtag",c)
    canvas.addtag("H","withtag",d)
    canvas.addtag("M","withtag",h)
    canvas.addtag("G","withtag",m)
    canvas.addtag("D","withtag",g)
    canvas.dtag(a,"A")
    canvas.dtag(c,"C")
    canvas.dtag(d,"D")
    canvas.dtag(e,"E")
    canvas.dtag(f,"F")
    canvas.dtag(g,"G")
    canvas.dtag(h,"H")
    canvas.dtag(m,"M")

def rotateJRight(canvas):
    a, c, d, e, f, g, h, m = canvas.find_withtag("A"), canvas.find_withtag("C"), canvas.find_withtag("D"), canvas.find_withtag("E"), canvas.find_withtag("F"), canvas.find_withtag("G"), canvas.find_withtag("H"), canvas.find_withtag("M")
    canvas.move(a, +25, -25)
    canvas.move(c, -25, +25)
    canvas.move(d, -50, 0)
    canvas.move(e, -25, 25)
    canvas.move(f, 25, -25)
    canvas.move(g, 0, -50)
    canvas.move(h, 0, 50)
    canvas.move(m, 50, 0)
    canvas.addtag("A","withtag",e)
    canvas.addtag("E","withtag",a)
    canvas.addtag("C","withtag",f)
    canvas.addtag("F","withtag",c)
    canvas.addtag("G","withtag",d)
    canvas.addtag("D","withtag",h)
    canvas.addtag("H","withtag",m)
    canvas.addtag("M","withtag",g)
    canvas.dtag(a,"A")
    canvas.dtag(c,"C")
    canvas.dtag(d,"D")
    canvas.dtag(e,"E")
    canvas.dtag(f,"F")
    canvas.dtag(g,"G")
    canvas.dtag(h,"H")
    canvas.dtag(m,"M")

#Toglie tutti i tag A, B, ..., a tutti i pezzi presenti sul canvas
#usare solo quando un pezzo si ferma
def dtagAll(canvas):
    a, b, c, d, e, f, g, h, m, c2, f2 = canvas.find_withtag("A"), canvas.find_withtag("B"), canvas.find_withtag("C"), canvas.find_withtag("D"), canvas.find_withtag("E"), canvas.find_withtag("F"), canvas.find_withtag("G"), canvas.find_withtag("H"), canvas.find_withtag("M"), canvas.find_withtag("C2"), canvas.find_withtag("F2")
    canvas.dtag(a,"A")
    canvas.dtag(b,"B")
    canvas.dtag(c,"C")
    canvas.dtag(d,"D")
    canvas.dtag(e,"E")
    canvas.dtag(f,"F")
    canvas.dtag(g,"G")
    canvas.dtag(h,"H")
    canvas.dtag(m,"M")
    canvas.dtag(c2,"C2")
    canvas.dtag(f2,"F2")







#cose
