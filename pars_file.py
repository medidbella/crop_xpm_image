
def get_transparent_pixel_val(file):
	splited = []
	for line in file:
		if "None" in line:
			splited = line.split(' ')
			return splited[0][1:]
	return None