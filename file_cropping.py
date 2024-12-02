import os

def set_xpm_rows_columns(line, data):
	splitted = []
	splitted = line.split(" ")
	line = splitted[2] + " " + splitted[3]
	line = str(data.lines_len - data.trim_left - data.trim_right) + " " +  line
	line = str(data.lines_nb) + " " +  line
	return

def create_new_file(data, FilePath):
	prev_line = ""
	if not os.path.isdir("results"):
		os.makedirs("results")
	result_file = open("results/" + FilePath, 'x')
	data.og_file.seek(0)
	for line in data.file:
		if prev_line == "/* columns rows colors chars-per-pixel */":
			set_xpm_rows_columns()
		result_file.write(line)
		if (line == "/* pixels */"):
			break
		prev_line = line
	return
