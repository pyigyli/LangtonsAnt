from math import cos, sin, radians
from tkinter import *

class Logic():
	def __init__(self, screen_width, screen_height, canvas):
		self.canvas = canvas

		self.grid_width = 100
		self.grid_height = 100

		self.edgeSide_x = screen_width / self.grid_width
		self.edgeSide_y = screen_height / self.grid_height

		self.grid = []
		for i in range(self.grid_width):
			row = []
			for j in range(self.grid_height):
				row.append("white")
			self.grid.append(row)
		self.grid[self.grid_width // 2][self.grid_height // 2] = "red"

		self.ant_pos_x = self.grid_width // 2
		self.ant_pos_y = self.grid_height // 2
		self.ant_direction = 0

		self.color_rotation = ["white", "blue"]
		self.color_map = {
			"white": "turn_left",
			"blue": "turn_right"
		}
		self.stored_color = "white"
		self.draw_grid()
	
	def set_config(self, colors, color_map):
		self.color_rotation = []
		self.color_map.clear()
		for i in range(len(colors)):
			if color_map[i].get() == "Turn left":
				self.color_rotation.append(colors[i])
				self.color_map[colors[i]] = "turn_left"
			elif color_map[i].get() == "Turn right":
				self.color_rotation.append(colors[i])
				self.color_map[colors[i]] = "turn_right"
	
	def reset(self):
		for i in range(self.grid_width):
			for j in range(self.grid_height):
				if self.grid[i][j] != "white":
					self.grid[i][j] = "white"
					self.ant_pos_x = i
					self.ant_pos_y = j
					self.canvas.delete(f"{i}-{j}")
					self.draw_current_rect()
		self.ant_pos_x = self.grid_width // 2
		self.ant_pos_y = self.grid_height // 2
		self.grid[self.ant_pos_x][self.ant_pos_y] = "red"
		self.draw_current_rect()

		self.ant_pos_x = self.grid_width // 2
		self.ant_pos_y = self.grid_height // 2
		self.ant_direction = 0

	def update(self):
		if self.ant_pos_x >= 0 and self.ant_pos_x < self.grid_width and self.ant_pos_y >= 0 and self.ant_pos_y < self.grid_height:
			if self.color_map[self.stored_color] == "turn_left":
				self.ant_direction -= 1
			elif self.color_map[self.stored_color] == "turn_right":
				self.ant_direction += 1
			self.ant_direction %= 4

			self.grid[self.ant_pos_x][self.ant_pos_y] = self.stored_color
			self.draw_current_rect()

			if self.ant_direction == 0:
				self.ant_pos_x -= 1
			elif self.ant_direction == 1:
				self.ant_pos_y -= 1
			elif self.ant_direction == 2:
				self.ant_pos_x += 1
			elif self.ant_direction == 3:
				self.ant_pos_y += 1
				
			if self.ant_pos_x >= 0 and self.ant_pos_x < self.grid_width and self.ant_pos_y >= 0 and self.ant_pos_y < self.grid_height:
				self.stored_color = self.color_rotation[(self.color_rotation.index(self.grid[self.ant_pos_x][self.ant_pos_y]) + 1) % len(self.color_rotation)]
				self.grid[self.ant_pos_x][self.ant_pos_y] = "red"
			self.draw_current_rect()

	def draw_grid(self):
		for i in range(self.grid_width):
			for j in range(self.grid_height):
				x = i * self.edgeSide_x + 2
				y = j * self.edgeSide_y + 2
				bbox = (x, y, x + self.edgeSide_x, y + self.edgeSide_y)
				self.canvas.create_rectangle(*bbox, fill=self.grid[i][j], tags=f"{i}-{j}")

	def draw_current_rect(self):
		x = self.ant_pos_x * self.edgeSide_x + 2
		y = self.ant_pos_y * self.edgeSide_y + 2
		bbox = (x, y, x + self.edgeSide_x, y + self.edgeSide_y)
		self.canvas.create_rectangle(*bbox, fill=self.grid[self.ant_pos_x][self.ant_pos_y], tags=f"{self.ant_pos_x}-{self.ant_pos_y}")
