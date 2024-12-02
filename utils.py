def is_empty_column(line, transparent_pixel):
	if line.count(transparent_pixel) * len(transparent_pixel) == len(line) - 3 - (line.endswith(",\n")):
		return True
	return False

def data_init(left_empty_rows, right_empty_rows, file, offset, lines_len):
	line = file.readline()
	left_empty_rows[0] = len(line)
	right_empty_rows[0] = len(line)
	lines_len[0] = len(line)
	file.seek(offset[0])
