import utils
def get_transparent_pixel_val(offset, file):
	splitted = []
	for line in file:
		offset[0] += len(line)
		if "None" in line:
			if "  " in line:
				return " "
			splitted = line.split(' ')
			return splitted[0][1:]
	return None

def skip_to_pixels(offset, file):
	for line in file:
		offset[0] += len(line)
		if line == "/* pixels */\n":
			return True
	return False

def get_empty_rows(line, left_empty_rows, right_empty_rows, transparent_pixel):
	iter = 1
	count = 0
	if utils.is_empty_column(line, transparent_pixel):
		return
	while iter < len(line) - 1 - ("," in line):
		if transparent_pixel == line[iter:iter + len(transparent_pixel)]:
			count += 1
			iter += len(transparent_pixel)
		else:
			break
	if (left_empty_rows[0] > count):
		left_empty_rows[0] = count
	iter = len(line) - 2 - ("," in line)
	count = 0
	while iter != 0:
		if transparent_pixel == line[iter - len(transparent_pixel):iter]:
			count += 1
			iter -= len(transparent_pixel)
		else:
			break
	if right_empty_rows[0] > count:
		right_empty_rows[0] = count
	return

def	get_cropping_data(file, transparent_pixel, left_empty_rows, right_empty_rows):
	count = 0
	empty = 0
	for line in file:
		get_empty_rows(line, left_empty_rows, right_empty_rows, transparent_pixel)
		if utils.is_empty_column(line, transparent_pixel):
			empty += 1
		elif line != "};\n":
			count += empty + 1
			empty = 0
	return count
