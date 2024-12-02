import sys
import pars_file
import utils
import file_cropping

if len(sys.argv) != 2:
	print("pass the xpm image path as an argument")
	exit(1)
else :
	FilePath = sys.argv[1]
class data:
	def __init__(self, start_offset, line_len, lines_nb, trim_left,
			trim_right, file):
		self.start_offset = start_offset
		self.line_len = line_len
		self.lines_nb = lines_nb
		self.trim_left = trim_left
		self.trim_right = trim_right
		self.file = file

def main():
	if not FilePath.endswith(".xpm"):
		print("the file should be in format .xpm")
		exit(1)
	FileData = open(FilePath, 'r')
	offset = [0]
	empty_columns = 0
	lines_len = [0]
	cropped_lines = 0
	left_empty_rows = [0]
	right_empty_rows = [0]
	transparent_pixel = pars_file.get_transparent_pixel_val(offset, FileData)
	if not transparent_pixel:
		print("the image has no transparent_pixel")
		exit(1)
	if not pars_file.skip_to_pixels(offset, FileData):
		print("no pixels in file (invalid format)")
		exit(1)
	empty_columns = pars_file.get_top_empty_columns(FileData, transparent_pixel, offset)
	utils.data_init(left_empty_rows, right_empty_rows, FileData, offset, lines_len)
	cropped_lines = pars_file.get_cropping_data(FileData, transparent_pixel,
		left_empty_rows, right_empty_rows)
	crop_data = data(offset[0], lines_len[0], cropped_lines,
		left_empty_rows[0], right_empty_rows[0], FileData)
	file_cropping.create_new_file(crop_data, FilePath)
	# print("empty_columns = " + str(empty_columns))
	# print("cropped_lines = " + str(cropped_lines))
	# print("left_empty cols = " + str(left_empty_rows[0]))
	# print("right_empty cols = " + str(right_empty_rows[0]))
main()