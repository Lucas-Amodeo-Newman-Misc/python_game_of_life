import random
# import sys


size = 20

grid = [[0 for i in range(size)] for i in range(size)]

# for i in range(size):
# 	for j in range(size):
# 		print grid[i][j]
	
def initialize():
	grid = [[0 for i in range(size)] for i in range(size)]
	for i in range(size):
		for j in range(size):
			grid[i][j] = random.randrange(2)
	return grid			
	
def sum_neighbors(index, grid):
	
	
	a, b = index
	total = 0
	
# 	print '************'
# 	print a, b 
# 	print '***'
	
	for i in range(max(0, a-1), min(a+2, size)):
		for j in range(max(0, b-1), min(b+2, size)):
			total += grid[i][j]
			# print i, j
# 			print grid[i][j]
	total -= grid[a][b]
	# print 'total', total
	return total
			
def update(grid):
	new_grid = [[0 for i in range(size)] for i in range(size)]
	boolean_grid = [[0 for i in range(size)] for i in range(size)]
	for i in range(size):
		for j in range(size):
			a = sum_neighbors((i, j), grid)
			if grid[i][j] == 0:
				if a == 3:
					boolean_grid[i][j] = 1
			if grid[i][j] == 1:
				if a < 2 or a > 3:
					boolean_grid[i][j] = 1
			
	for i in range(size):
		for j in range(size):
			if boolean_grid[i][j] == 1:
				if grid[i][j] == 1:
					new_grid[i][j] = 0
				else:
					new_grid[i][j] = 1
				
			else:
				new_grid[i][j] = grid[i][j]
			
	return new_grid
				

def print_grid(grid):
	grid_list = []
	for i in grid:
		grid_list += i
		
	graphic = []
	for i in grid_list:
		if i == 1:
			graphic.append('*')
		else:
			graphic.append(' ')
	
# 	
# 	print """
# 	%s|%s|%s|%s|%s
# 	%s|%s|%s|%s|%s
# 	%s|%s|%s|%s|%s
# 	%s|%s|%s|%s|%s
# 	%s|%s|%s|%s|%s
# 	""" % tuple(grid_list)
	
	
	print	"""
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s
	""" % tuple(graphic)
	
	

grid = initialize()

blah = 0
while blah != 'p':
	# sys.stderr.write("\x1b[2J\x1b[H")
	print_grid(grid)
	grid = update(grid)
	blah = raw_input()
	
		
				
		