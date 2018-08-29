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
box_map = {
	(0, 0): 0, (1, 0): 1, (2, 0): 2,
	(0, 1): 3, (1, 1): 4, (2, 1): 5,
	(0, 2): 6, (1, 2): 7, (2, 2): 8
}

assumptions = {}


def main():
	sudoku_grid = GetMyInput(my_input)
	possible_inputs_map = GetPossibleInputs(sudoku_grid)
	print(possible_inputs_map)





def GetPossibleInputs(sudoku_grid):
	possible_inputs_map = []

	for i in range(len(sudoku_grid)):
		if(sudoku_grid[i] == 0):
			possible_inputs = []
			for num in range(1, 10):
				if(CanPlaceNumberHere(sudoku_grid, i, num)):
					possible_inputs.append(num)
			possible_inputs_map.append((i, possible_inputs))

	return possible_inputs_map

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