# CS 480 Project 1
# Written by: Elias Mote and Justin Ramos

# Initializing the sudoku
sudoku = [[0 for x in range(9)] for y in range(9)]
"""for m in range(9):
	for n in range(9):
		sudoku[m][n] = (m+n)%9+1
		print sudoku[m][n],
	print"""

# Initial example sudoku
# This may be replaced by a call to read a file later
sudoku[0][0] = 5
sudoku[1][0] = 3
sudoku[4][0] = 7

sudoku[0][1] = 6
sudoku[3][1] = 1
sudoku[4][1] = 9
sudoku[5][1] = 5

sudoku[1][2] = 9
sudoku[2][2] = 8
sudoku[7][2] = 6


sudoku[0][3] = 8
sudoku[4][3] = 6
sudoku[8][3] = 3

sudoku[0][4] = 4
sudoku[3][4] = 8
sudoku[5][4] = 3
sudoku[8][4] = 1

sudoku[0][5] = 7
sudoku[4][5] = 2
sudoku[8][5] = 6


sudoku[1][6] = 6
sudoku[6][6] = 2
sudoku[7][6] = 8

sudoku[3][7] = 4
sudoku[4][7] = 1
sudoku[5][7] = 9
sudoku[8][7] = 5

sudoku[4][8] = 8
sudoku[7][8] = 7
sudoku[8][8] = 9

# Checks if a row is good
def checkRow(row):
	for n in range(1,10):
		numExists = False
		for c in range(9):
			if(sudoku[row][c] == n):
				if (numExists == False):
					numExists = True
				else:
					return False
	return True

# Checks if a column is good
def checkCol(col):
	for n in range(1,10):
		numExists = False
		for r in range(9):
			if(sudoku[r][col] == n):
				if (numExists == False):
					numExists = True
				else:
					return False
	return True

# Checks if a square is good
def checkSqr(row,col):
	for n in range(1,10):
		numExists = False
		for r in range(row,row+3):
			for c in range(col,col+3):
				if(sudoku[r][c] == n):
					if (numExists == False):
						numExists = True
					else:
						return False
	return True

# Backtracking function
def backtracking(s):
	# Check each row
	for r in range(9):
		if(checkRow(r) == False):
			return False

	# Check each column
	for c in range(9):
		if(checkCol(c) == False):
			return False

	# Check each square
	for r in range(0,9,3):
		for c in range(0,9,3):
			if(checkSqr(r,c) == False):
				return False

	# The sudoku is finished until we find empty cells (0's)
	isDone = True

	# For each row
	for r in range(9):

		# For each column
		for c in range(9):

			# If we find an empty cell
			if(s[r][c] == 0):

				# Mark that we aren't yet finished
				isDone = False

				# Try the sudoku with each possible number
				for num in range(1,10):

					# Make a copy of the sudoku
					copy_s = list(s)

					# Set the empty cell to the test number
					copy_s[r][c] = num

					# Print the sudoku
					#for m in range(9):
						#for n in range(9):
							#print copy_s[m][n],
						#print
					#print

					# TODO: Fix recursive calls comparing the backtracking 
					# results.
					# Recursively call the backtracking function
					backtracking(copy_s)

	# Return whether we finished or not
	return isDone

# Get the finished sudoku, if one exists
sudoku = backtracking(sudoku)

# If the sudoku exists, print it out
if(sudoku != False):
	for m in range(9):
		for n in range(9):
			print sudoku[m][n],
		print
else:
	print "No possible sudoku"