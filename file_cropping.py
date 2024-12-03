import os
import utils

def set_xpm_rows_columns(line, data):
	splitted = []
	splitted = line.split(" ")
	line = splitted[2] + " " + splitted[3]
	line = str(data.lines_nb) + " " +  line
	line = "\"" + str((int)((data.line_len - 4) / data.pixel_len) - data.trim_left - data.trim_right) + " " +  line
	line += " \",\n"
	return line

def crop_line(line, data):
	if line == "};\n":
		return line
	res = "\""
	iter = (data.trim_left * data.pixel_len) + 1
	limit = data.line_len - 3 - ("," in line) - (data.trim_right * data.pixel_len)
	while iter <= limit and iter < len(line):
		res += line[iter]
		iter += 1
	res += "\""
	if "," in line:
		res += ",\n"
	else:
		res += "\n"
	return res

def write_cropped_data(data, FilePath):
	count = 0
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
		line = crop_line(line, data)
		result_file.write(line)
		count += 1
		if count == data.lines_nb:
			break
	result_file.write("};\n")
	return
