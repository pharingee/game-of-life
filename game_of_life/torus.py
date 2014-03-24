import random

class Torus:
	cells = []
	__torus_width = 5
	__torus_height = 5
	__temp_cells = []
	__previous_campaigns = []

	def __init__(self, torus_width, torus_height, live_percent):
		self.__torus_height, self.__torus_width = torus_height, torus_width
		self.__populate_cells(live_percent)

	def __value_yielder(self, percentage):
		'''
		Return a generator with random variables
		'''
		values = []
		for x in xrange(self.__torus_width*self.__torus_height):
			if (float(x)/float(self.__torus_width*self.__torus_height))*100 < percentage:
				values.append(True)
			else:
				values.append(False)
	        
		for _ in values:
			yield random.choice(values)

	def __populate_cells(self, live_percent):
		'''
	    Populate the cells global variable
		'''	    
		y = self.__value_yielder(live_percent)
		self.cells = [[y.next() for x in xrange(self.__torus_width)] for x in xrange(self.__torus_height)]

	def check_live_neighbours(self, cell_x, cell_y):
		'''
		Finds and Returns the number of live cells out of the 8 neighbour cells
		'''
		live_count = 0
		cell_around_x = []
		cell_around_y = []

		cell_around_x.append(self.__torus_width - 1 if not cell_x else (cell_x%self.__torus_width) - 1)
		cell_around_y.append(self.__torus_height - 1 if not cell_y else (cell_y%self.__torus_height) - 1)

		cell_around_x.append(cell_x)
		cell_around_y.append(cell_around_y[0])

		cell_around_x.append(cell_x + 1 if cell_x < self.__torus_width - 1 else 0)
		cell_around_y.append(cell_around_y[0])

		cell_around_x.append(self.__torus_width - 1 if not cell_x else (cell_x%self.__torus_width) - 1)
		cell_around_y.append(cell_y)

		cell_around_x.append(cell_x + 1 if cell_x < self.__torus_width - 1 else 0)
		cell_around_y.append(cell_y)

		cell_around_x.append(self.__torus_width - 1 if not cell_x else (cell_x%self.__torus_width) - 1)
		cell_around_y.append(cell_y + 1 if cell_y < self.__torus_height - 1 else 0)

		cell_around_x.append(cell_x)
		cell_around_y.append(cell_y + 1 if cell_y < self.__torus_height - 1 else 0)

		cell_around_x.append(cell_x + 1 if cell_x < self.__torus_width - 1 else 0)
		cell_around_y.append(cell_y + 1 if cell_y < self.__torus_height - 1 else 0)

		count = 0
		while count < len(cell_around_x):
			if self.cells[cell_around_y[count]][cell_around_x[count]]:
				live_count += 1

			count += 1

		return live_count

	def calculate_fate(self, cell_x, cell_y):
		'''
		Actual determination of fate from corners
		This is where the rules are set
		Rule 1
		-------
		A cell lives if it is neither overpopulated, nor undernourished.
		A living cell will live in the next round,
		if it has at most three and at least two living neighbor cells.

		Rule 2
		-------
		A dead cell will only be revived in the next round,
		if it has exactly three living neighbors.

		Corners is a list of 9 boolean variables

		Returns True is cell is alive, and false otherwise
		'''
		live_cells = self.check_live_neighbours(cell_x, cell_y)

		if self.cells[cell_y][cell_x]:
			if 2 <= live_cells <=3:
				self.__temp_cells[cell_y][cell_x] = True
			else:
				self.__temp_cells[cell_y][cell_x] = False
		else:
			if live_cells == 3:
				self.__temp_cells[cell_y][cell_x] = True
			else:
				self.__temp_cells[cell_y][cell_x] = False

	def next_step(self):
		'''Move the game to the next step

		To accomodate for simaultaneous changes, temp cells was created
		changes are made to temp cells using cells and then copied back over
		'''
		self.__temp_cells = [[False for x in xrange(self.__torus_width)] for x in xrange(self.__torus_height)]

		self.__previous_campaigns.append(self.cells[:])

		count_y = 0

		while count_y < self.__torus_height:
			count_x = 0
			while count_x < self.__torus_width:
				self.calculate_fate(count_x, count_y)
				count_x += 1
			
			count_y += 1

		self.cells = self.__temp_cells[:]

	def previous(self):
		try:
			self.cells = self.__previous_campaigns.pop()
		except IndexError:
			pass

	def __str__(self):
		for cell in self.cells:
			print cell