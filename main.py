import sys
import open_file

if len(sys.argv) != 2:
	print("input the xpm image path")
	exit(1)
else :
	FilePath = sys.argv[1]

def main():
	if not FilePath.endswith(".xpm"):
		print("the file should be in format .xpm")
		exit(1)
	FileData = open(FilePath, 'r')
	

main()