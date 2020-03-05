import numpy as np
import time
from tkinter import *
from math import cos, sin, radians
from grid import Grid

screen_width = 800
screen_height = 800

root = Tk()

menuButton = Menubutton(root, text="Settings")
menuButton.menu = Menu(menuButton)
menuButton.event_add("<<ButtonRelease>>", "Start/Stop")
menuButton["menu"] =  menuButton.menu
menuButton.pack(side="top")

grid = Grid(screen_width, screen_height, root)

while True:
	grid.canvas.update_idletasks()
	grid.canvas.update()
	grid.canvas.delete(f"{grid.ant_pos_x}-{grid.ant_pos_y}")
	grid.canvas.after(5, grid.update())
