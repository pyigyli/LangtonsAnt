import numpy as np
import time
from tkinter import *
from math import cos, sin, radians
from logic import Logic

def toggle_playing():
	reset_button["state"] = "normal"
	if is_playing.get():
		is_playing.set(False)
		play_button_text.set("Continue")
	else:
		is_playing.set(True)
		play_button_text.set("Pause")

def stop_playing():
	is_playing.set(False)
	play_button_text.set("Start")
	reset_button["state"] = "disabled"
	logic.reset()

screen_width = 800
screen_height = 800

root = Tk()

canvas = Canvas(root, width=screen_width + 1, height=screen_height + 1)
canvas.grid(row=0, column=0)

is_playing = BooleanVar(root, False)

play_button_text = StringVar(root, "Start",)
play_button = Button(root, textvariable=play_button_text, command=toggle_playing, width=10)
play_button.grid(row=0, column=1)

reset_button = Button(root, text="Reset", state="disabled", command=stop_playing, width=10)
reset_button.grid(row=0, column=2)

logic = Logic(screen_width, screen_height, canvas)

while True:
	logic.canvas.update_idletasks()
	logic.canvas.update()
	if is_playing.get():
		logic.canvas.delete(f"{logic.ant_pos_x}-{logic.ant_pos_y}")
		logic.canvas.after(5, logic.update())
