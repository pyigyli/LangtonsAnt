import numpy as np
import time
from tkinter import *
from math import cos, sin, radians
from logic import Logic

def start_playing():
	logic.set_config(colors, color_buttons)
	reset_button["state"] = "normal"
	for button in color_buttons:
		button["state"] = "disabled"

def toggle_playing():
	if play_button_text.get() == "Start":
			start_playing()
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
	for button in color_buttons:
		button["state"] = "normal"
	logic.reset()

screen_width = 800
screen_height = 800

root = Tk()
canvas = Canvas(root, width=screen_width + 1, height=screen_height + 1)
canvas.pack(side="left")
option_frame = Frame(root)
option_frame.pack(side="right", padx=5)
logic = Logic(screen_width, screen_height, canvas)

is_playing = BooleanVar(root, False)

play_button_text = StringVar(root, "Start",)
play_button = Button(option_frame, textvariable=play_button_text, command=toggle_playing, width=10)
play_button.grid(row=0, column=0)

reset_button = Button(option_frame, text="Reset", state="disabled", command=stop_playing, width=10)
reset_button.grid(row=0, column=1)

colors = ["white", "blue", "green", "yellow", "orange", "purple"]
color_buttons = []

color_1 = Canvas(option_frame, width=20, height=20)
color_1.create_rectangle(1, 1, 19, 19, fill=colors[0])
color_1.grid(row=1, column=0)
selection_1 = Spinbox(option_frame, values=("Turn left", "Turn right", "Go straight"))
selection_1.grid(row=1, column=1)
color_buttons.append(selection_1)

color_2 = Canvas(option_frame, width=20, height=20)
color_2.create_rectangle(1, 1, 19, 19, fill=colors[1])
color_2.grid(row=2, column=0)
selection_2 = Spinbox(option_frame, values=("Don't include color", "Turn left", "Turn right", "Go straight"))
selection_2.grid(row=2, column=1)
color_buttons.append(selection_2)

color_3 = Canvas(option_frame, width=20, height=20)
color_3.create_rectangle(1, 1, 19, 19, fill=colors[2])
color_3.grid(row=3, column=0)
selection_3 = Spinbox(option_frame, values=("Don't include color", "Turn left", "Turn right", "Go straight"))
selection_3.grid(row=3, column=1)
color_buttons.append(selection_3)

color_4 = Canvas(option_frame, width=20, height=20)
color_4.create_rectangle(1, 1, 19, 19, fill=colors[3])
color_4.grid(row=4, column=0)
selection_4 = Spinbox(option_frame, values=("Don't include color", "Turn left", "Turn right", "Go straight"))
selection_4.grid(row=4, column=1)
color_buttons.append(selection_4)

color_5 = Canvas(option_frame, width=20, height=20)
color_5.create_rectangle(1, 1, 19, 19, fill=colors[4])
color_5.grid(row=5, column=0)
selection_5 = Spinbox(option_frame, values=("Don't include color", "Turn left", "Turn right", "Go straight"))
selection_5.grid(row=5, column=1)
color_buttons.append(selection_5)

color_6 = Canvas(option_frame, width=20, height=20)
color_6.create_rectangle(1, 1, 19, 19, fill=colors[5])
color_6.grid(row=6, column=0)
selection_6 = Spinbox(option_frame, values=("Don't include color", "Turn left", "Turn right", "Go straight"))
selection_6.grid(row=6, column=1)
color_buttons.append(selection_6)

while True:
	logic.canvas.update_idletasks()
	logic.canvas.update()
	if is_playing.get():
		logic.canvas.delete(f"{logic.ant_pos_x}-{logic.ant_pos_y}")
		logic.canvas.after(1, logic.update())
