from __future__ import print_function
from random import choice

my_input = " \
  	3, 0, 6,    5, 0, 8,    4, 0, 0, \
  	5, 2, 0,    0, 0, 0,    0, 0, 0, \
  	0, 8, 7,    0, 0, 0,    0, 3, 1, \
  									 \
  	0, 0, 3,    0, 1, 0,    0, 8, 0, \
  	9, 0, 0,    8, 6, 3,    0, 0, 5, \
  	0, 5, 0,    0, 9, 0,    6, 0, 0, \
  									 \
  	1, 3, 0,    0, 0, 0,    2, 5, 0, \
  	0, 0, 0,    0, 0, 0,    0, 7, 4, \
  	0, 0, 5,    2, 0, 6,    3, 0, 0  \
  "

"""
my_input = " \
	0, 0, 0,    0, 0, 0,    0, 0, 0, \
	0, 0, 0,    0, 0, 0,    0, 0, 0, \
	0, 0, 0,    0, 0, 0,    0, 0, 0, \
									 \
	0, 0, 0,    0, 0, 0,    0, 0, 0, \
	0, 0, 0,    0, 0, 0,    0, 0, 0, \
	0, 0, 0,    0, 0, 0,    0, 0, 0, \
									 \
	0, 0, 0,    0, 0, 0,    0, 0, 0, \
	0, 0, 0,    0, 0, 0,    0, 0, 0, \
	0, 0, 0,    0, 0, 0,    0, 0, 0  \
"
"""

# my_input = " \
# 	6, 3, 9,    5, 7, 4,    1, 8, 2, \
# 	5, 4, 1,    8, 2, 9,    3, 7, 6, \
# 	7, 8, 2,    6, 1, 3,    9, 5, 4, \
# 									 \
# 	1, 9, 8,    4, 6, 7,    5, 2, 3, \
# 	3, 6, 5,    9, 8, 2,    4, 1, 7, \
# 	4, 2, 7,    1, 3, 5,    8, 6, 9, \
# 									 \
# 	9, 5, 6,    7, 4, 8,    2, 3, 1, \
# 	8, 1, 3,    2, 9, 6,    7, 4, 5, \
# 	2, 7, 4,    3, 5, 1,    6, 9, 8  \
# "
box_map = {
	(0, 0): 0, (1, 0): 1, (2, 0): 2,
	(0, 1): 3, (1, 1): 4, (2, 1): 5,
	(0, 2): 6, (1, 2): 7, (2, 2): 8
}


def main():
	sudoku_grid = GetMyInput(my_input)
	res = Backtrack(sudoku_grid, 0)
	if(res):
		PrintSudokuGrid(sudoku_grid)
	else:
		print("no solution")


def PrintSudokuGrid(sudoku_grid):
	# Prints the top border
	for i in range(9):
		print("++++", end="")
	print("+")
	for i in range(9):
		print("+", end="")
		for j in range(9):
			print(" " + str(sudoku_grid[(i * 9) + j]) + " ", end="")
			if(j % 3 == 2):
				print("+", end="")
			else:
				print("|", end="")
		print()
		if(i % 3 == 2):
			for j in range(9):
				print("++++", end="")
			print("+")
		else:
			for j in range(9):
				if(j % 3 == 0):
					print("+", end="")
				else:
					print("-", end="")
				print("---", end="")
			if(i % 3 == 0):
				print("+")
			else:
				print("-")


def Backtrack(sudoku_grid, starting):
	if(IsValid(sudoku_grid)):
		return True
	if(starting >= len(sudoku_grid)):
		return False
	for i in range(starting, len(sudoku_grid)):
		if(sudoku_grid[i] == 0):
			possible_inputs = GetPossibleInputsForPos(sudoku_grid, i)
			if(len(possible_inputs) != 0):
				for j in range(len(possible_inputs)):
					num = choice(possible_inputs)
					sudoku_grid[i] = num
					res = Backtrack(sudoku_grid, i + 1)
					if(res):
						# We've found a correct sequence of numbers, return it!
						return True
					possible_inputs.remove(num)
			# We get to here if there were no possible inputs
			# or if none of the possible inputs we tried produced
			# a valid sequence of numbers to return True
			sudoku_grid[i] = 0
			return False


def IsValid(sudoku_grid):
	return AllRowsValid(sudoku_grid) and AllColumnsValid(sudoku_grid) and AllBoxesValid(sudoku_grid)


def AllRowsValid(sudoku_grid):
	for i in range(0, len(sudoku_grid), 9):
		nums = []
		for j in range(i, i + 9):
			if(sudoku_grid[j] == 0 or sudoku_grid[j] in nums):
				return False
			else:
				nums.append(sudoku_grid[j])

	return True


def AllColumnsValid(sudoku_grid):
	for i in range(9):
		nums = []
		for j in range(i, len(sudoku_grid), 9):
			if(sudoku_grid[j] == 0 or sudoku_grid[j] in nums):
				return False
			else:
				nums.append(sudoku_grid[j])

	return True


def AllBoxesValid(sudoku_grid):

	for box in range(9):
		x = box % 3
		y = box / 3

		nums = []

		for r in range(y * 3, (y + 1) * 3):
			for c in range(x * 3, (x + 1) * 3):
				if(sudoku_grid[(9 * r) + c] == 0 or sudoku_grid[(9 * r) + c] in nums):
					return False
				else:
					nums.append(sudoku_grid[(9 * r) + c])

	return True


def GetPossibleInputsForPos(sudoku_grid, pos):
	possible_inputs = []
	for num in range(1, 10):
		if(CanPlaceNumberHere(sudoku_grid, pos, num)):
			possible_inputs.append(num)

	return possible_inputs

def CanPlaceNumberHere(sudoku_grid, pos, num):
	return not (ColumnContainsNumber(sudoku_grid, pos, num) or RowContainsNumber(sudoku_grid, pos, num) or BoxContainsNumber(sudoku_grid, pos, num))


def ColumnContainsNumber(sudoku_grid, pos, num):
	for i in range(pos % 9, len(sudoku_grid), 9):
		if(sudoku_grid[i] == num):
			return True

	return False


def RowContainsNumber(sudoku_grid, pos, num):
	for i in range((pos / 9) * 9, ((pos / 9) * 9) + 9):
		if(sudoku_grid[i] == num):
			return True

	return False


def BoxContainsNumber(sudoku_grid, pos, num):
	box = GetBoxFromPos(pos)

	x = box % 3
	y = box / 3

	for r in range(y * 3, (y + 1) * 3):
		for c in range(x * 3, (x + 1) * 3):
			if(sudoku_grid[(9 * r) + c] == num):
				return True

	return False


def GetBoxFromPos(pos):
	row = (pos / 9) / 3
	col = (pos % 9) / 3
	res = box_map[col, row]

	return res


def GetMyInput(sudoku_input):
	return map(int, sudoku_input.replace('\t', '').replace(',', '').split())






main()