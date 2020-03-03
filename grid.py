from math import cos, sin, radians
from tkinter import Canvas

class Grid():
	def __init__(self, screen_width, screen_height, root):
		self.canvas = Canvas(root, width=screen_width + 1, height=screen_height + 1)
		self.canvas.pack(side="bottom")

		self.grid_width = 50
		self.grid_height = 50

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

		self.edgeSide_x = screen_width / self.grid_width
		self.edgeSide_y = screen_height / self.grid_height

		self.color_rotation = ["white", "blue"]
		self.color_map = {
			"white": "turn_left",
			"blue": "turn_right"
		}
		self.stored_color = "white"
		self.draw()

	def update(self):
		if self.ant_pos_x >= 0 and self.ant_pos_x < self.grid_width and self.ant_pos_y >= 0 and self.ant_pos_y < self.grid_height:
			
			if self.color_map[self.stored_color] == "turn_left":
				self.ant_direction -= 1
			elif self.color_map[self.stored_color] == "turn_right":
				self.ant_direction += 1
			self.ant_direction %= 4

			self.grid[self.ant_pos_x][self.ant_pos_y] = self.stored_color

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
		self.draw()

	def draw(self):
		for i in range(self.grid_width):
			for j in range(self.grid_height):
				polygonPoints = []
				x = i * self.edgeSide_x + 2
				y = j * self.edgeSide_y + 2
				angle = 0
				for _ in range(4):
					polygonPoints.append(x)
					polygonPoints.append(y)
					x += self.edgeSide_x * cos(radians(angle))
					y += self.edgeSide_y * sin(radians(angle))
					angle += 360 / 4
				self.canvas.create_polygon(polygonPoints, outline="black", fill=self.grid[i][j], width=1)