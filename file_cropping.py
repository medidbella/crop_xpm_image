import os
import utils

def set_xpm_rows_columns(line, data):
	splitted = []
	splitted = line.split(" ")
	line = splitted[2] + " " + splitted[3]
	line = str(data.line_len - data.trim_left - data.trim_right) + " " +  line
	line = str(data.lines_nb) + " " +  line
	return line

def crop_line(line, data):
	res = ""
	iter = data.trim_right
	limit = data.line_len - (data.trim_left - 1) - 2 - ("," in line)
	while iter < limit:
		res += line[iter]
		iter += 1

def write_cropped_data(data, FilePath):
	prev_line = ""
	result_file = utils.create_new_file(FilePath)
	data.file.seek(0)
	for line in data.file:
		if prev_line == "/* columns rows colors chars-per-pixel */\n":
			line = set_xpm_rows_columns(line, data)
		result_file.write(line)
		prev_line = line
		if (line == "/* pixels */\n"):
			break
	data.file.seek(data.start_offset)
	for line in data.file:
		if line != "};\n":
			result_file.write("\"")
			line = crop_line(line, data)
			result_file.write("\"")
			if "," in line:
				result_file.write(",\n")
			else:
				result_file.write("\n")
		result_file.write(line)