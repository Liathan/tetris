import tkinter as tk
from tkinter import ttk
import random as rnd
from pieces import *
from logic import *
import time

#
# window = tk.Tk()
board = tk.Frame(width = 400, height = 800,master = window, relief = tk.GROOVE, borderwidth = 5)
# info = tk.Frame(width = 150, height = 800, master = window)
board.pack(side = tk.LEFT, padx = 10, pady = 10)
info.pack(side= tk.LEFT, fill = tk.Y)
info.columnconfigure(0,minsize = 150)

nextLbl = tk.Label(text = "Next", master = info)
nextCanvas = tk.Canvas(master = info, width = 110, height = 110, bg = "Black")
separator1 = ttk.Separator(info, orient= 'horizontal')
separator2 = ttk.Separator(info, orient= 'horizontal')
separator3 = ttk.Separator(info, orient= 'horizontal')
pointStringLbl = tk.Label(text = "Points:", master = info, font = ("Helvetica", 15))
# pointNumLbl = tk.Label(text = "0", master = info)
linesStringLbl = tk.Label(text = "Lines:", master = info, font = ("Helvetica", 15))
# linesNumLbl = tk.Label(text = "0", master = info)
levelStringLbl = tk.Label(text = "Level", master = info, font = ("Helvetica", 15))
# levelNumLbl = tk.Label(text= "0", master = info)

nextLbl.grid(row = 0, column = 0, pady = 10)
nextCanvas.grid(row = 1, column = 0, pady = 10)
separator1.grid(row = 2, column = 0, pady  =10, sticky = "we")
pointStringLbl.grid(row = 3, column = 0)
pointNumLbl.grid(row = 4, column = 0, pady = 5)
separator2.grid(row = 5, column = 0, pady  =10, sticky = "we")
linesStringLbl.grid(row = 6, column = 0)
linesNumLbl.grid(row = 7, column = 0, pady = 5)
separator3.grid(row = 8, column = 0, pady = 10, sticky = "we")
levelStringLbl.grid(row = 9, column = 0)
levelNumLbl.grid(row = 10, column = 0, pady = 5)

mainCanvas = tk.Canvas(master = board, width = 400, height = 600, bg = "black")
mainCanvas.pack()
mainCanvas.focus_set()
#Left -> 37
#Up -> 38
#Right -> 39
#Down -> 40
newGame(mainCanvas, nextCanvas)
window.mainloop()
