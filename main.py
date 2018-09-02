from __future__ import print_function
from random import choice


# Used to determine subgrid location
box_map = {
	(0, 0): 0, (1, 0): 1, (2, 0): 2,
	(0, 1): 3, (1, 1): 4, (2, 1): 5,
	(0, 2): 6, (1, 2): 7, (2, 2): 8
}


# Gets the sudoku puzzle from a file and completes it
def main():
	sudoku_grid = GetMyInput("input.txt")
	backup_sudoku = list(sudoku_grid)
	res = Backtrack(sudoku_grid, 0)
	if(res):
		PrintSudokuGrid(sudoku_grid, backup_sudoku)
	else:
		print("no solution")


# Prints the sudoku grid in a nice, pretty looking format.
# Don't ask how it works, please.
def PrintSudokuGrid(sudoku_grid, backup_sudoku):
	for i in range(9):
		print(TextColors.BOLD + "++++" + TextColors.END, end="")
	print(TextColors.BOLD + "+" + TextColors.END)
	for i in range(9):
		print(TextColors.BOLD + "+" + TextColors.END, end="")
		for j in range(9):
			print(" ", end="")
			if(backup_sudoku[(i * 9) + j] != 0):
				print(TextColors.WHITE, end="")
			else:
				print(TextColors.BLUE, end="")
			print(str(sudoku_grid[(i * 9) + j]) + TextColors.END + " ", end="")
			if(j % 3 == 2):
				print(TextColors.BOLD + "+" + TextColors.END, end="")
			else:
				print("|", end="")
		print()
		if(i % 3 == 2):
			for j in range(9):
				print(TextColors.BOLD + "++++" + TextColors.END, end="")
			print(TextColors.BOLD + "+" + TextColors.END)
		else:
			for j in range(9):
				if(j % 3 == 0):
					print(TextColors.BOLD + "+" + TextColors.END, end="")
				else:
					print("-", end="")
				print("---", end="")
			print(TextColors.BOLD + "+" + TextColors.END)


# Performs the backtracking function to find the sudoku solution
def Backtrack(sudoku_grid, starting):
	# If the sudoku grid is valid, we can just return what we have
	if(IsValid(sudoku_grid)):
		return True
	# If we no longer have any empty spaces to examine (and the previous
	# check for validity failed) then return False, meaning the sudoku
	# puzzle has no possible solution
	if(starting >= len(sudoku_grid)):
		return False
	for i in range(starting, len(sudoku_grid)):
		if(sudoku_grid[i] == 0):
			possible_inputs = GetPossibleInputsForPos(sudoku_grid, i)
			if(len(possible_inputs) != 0):
				for j in range(len(possible_inputs)):
					# The randomness was added here because it was a simple change
					# that added really cool functionality into the program. If you
					# give the sudoku solver an empty grid (all 0s) then because this
					# part randomly chooses valid numbers, you can actually just generate
					# a valid sudoku puzzle from nothing.
					num = choice(possible_inputs)
					# We'll overwrite the current value with a possible value because this
					# makes it easier to check future iterations and because once we find
					# a valid solution, we can just return the sudoku grid as is since it
					# already contains the solutions. If it turns out that this "tree" of
					# choices had no valid solutions then we'll just set the original cell
					# back to 0 (and hope some previous recursive call of Backtrack can find
					# a valid solution)
					sudoku_grid[i] = num
					res = Backtrack(sudoku_grid, i + 1)
					if(res):
						# We've found a correct sequence of numbers, return it!
						return True
					# Check the next possible valid number
					possible_inputs.remove(num)
			# We get to here if there were no possible inputs
			# or if none of the possible inputs we tried produced
			# a valid sequence of numbers to return True
			sudoku_grid[i] = 0
			return False


# Checks if a sudoku grid is valid
def IsValid(sudoku_grid):
	# Iterate through every row/column/subgrid at once
	for i in range(9):
		# Iterate through all the values each row/column/subgrid MUST contain
		for j in range(1, 10):
			# Make sure all columns only contain 1-9
			if (not ColumnContainsNumber(sudoku_grid, i, j)):
				return False
			# Make sure all rows only contain 1-9
			if (not RowContainsNumber(sudoku_grid, i * 9, j)):
				return False
			# Make sure all subgrids only contain 1-9
			if (not BoxContainsNumber(sudoku_grid, 10 + (i * 3), j)):
				return False

	# If we get here then the grid is valid
	return True


# Gets which inputs can be used in a particular cell
def GetPossibleInputsForPos(sudoku_grid, pos):
	possible_inputs = []
	for num in range(1, 10):
		if(CanPlaceNumberHere(sudoku_grid, pos, num)):
			possible_inputs.append(num)

	return possible_inputs


# Collection of function calls that can be used to determine
# if a specific number can be placed in a specific cell
def CanPlaceNumberHere(sudoku_grid, pos, num):
	return not (ColumnContainsNumber(sudoku_grid, pos, num) 
		or RowContainsNumber(sudoku_grid, pos, num) 
		or BoxContainsNumber(sudoku_grid, pos, num))


# Checks if a column contains a particular number we are looking for
def ColumnContainsNumber(sudoku_grid, pos, num):
	for i in range(pos % 9, len(sudoku_grid), 9):
		if(sudoku_grid[i] == num):
			return True

	return False


# Checks if a row contains a particular number we are looking for
def RowContainsNumber(sudoku_grid, pos, num):
	for i in range((pos / 9) * 9, ((pos / 9) * 9) + 9):
		if(sudoku_grid[i] == num):
			return True

	return False


# Checks if a box contains a particular number we are looking for
def BoxContainsNumber(sudoku_grid, pos, num):
	box = GetBoxFromPos(pos)

	x = box % 3
	y = box / 3

	for r in range(y * 3, (y + 1) * 3):
		for c in range(x * 3, (x + 1) * 3):
			if(sudoku_grid[(9 * r) + c] == num):
				return True

	return False


# Returns which box the position refers to
def GetBoxFromPos(pos):
	row = (pos / 9) / 3
	col = (pos % 9) / 3
	res = box_map[col, row]

	return res


# Read an input file
def GetMyInput(sudoku_input):
	with open(sudoku_input) as fp:
		input_str = fp.read()
	return map(int, input_str.replace('\t', '').replace(',', '').split())


# Small class containing variables used to color text
class TextColors:
	WHITE = '\033[37m'
	PINK = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	END = '\033[0m'


# Runs the whole sudoku solving function
main()