#Class containing defintion of game characters like Mario, enemies, etc.
class Person:
	#Sets up the Person object
	gravity = [-3, -2, -1, 1, 2, 3]
	def __init__(self, X, Y, HEIGHT, WIDTH):
		self.X = X
		self.Y = Y
		self.height = HEIGHT
		self.width = WIDTH
		self.jump_state = 0
		self.jump_idx = 0

	#Changes the position of Person object
	def update(self, move_x, move_y, l_thresh):
		if self.X + move_x > l_thresh:
			self.X = self.X + move_x
		self.Y = self.Y + move_y
		if self.jump_state == 1:
			self.jump_idx = self.jump_idx + 1
		if self.jump_idx == 6:
			self.jump_idx = 0
			self.jump_state = 0