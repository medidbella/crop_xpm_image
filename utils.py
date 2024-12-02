import os

def is_empty_column(line, transparent_pixel):
	if line.count(transparent_pixel) * len(transparent_pixel) == len(line) - 3 - (line.endswith(",\n")):
		return True
	return False

def data_init(left_empty_rows, right_empty_rows, file, offset, lines_len):
	line = file.readline()
	left_empty_rows[0] = len(line)
	right_empty_rows[0] = len(line)
	lines_len[0] = len(line) - 4
	file.seek(offset[0])

def set_start_offset(file, transparent_pixel, offset):
	for line in file:
		offset[0] += len(line)
		if not is_empty_column(line, transparent_pixel):
			offset[0] -= len(line)
			break

def create_new_file(FilePath):
	old_name = FilePath.split("/")[len(FilePath.split("/")) -1]
	if not os.path.isdir("results"):
		os.makedirs("results")
	result_file = open("results/" + old_name, 'w')
	return result_file
