import os
import subprocess
import time
from datetime import datetime

# folder paths
ldrawPath = "../ldraw"
ldrawPartsPath = ldrawPath + "/parts"
stlPartsPath = "../stl"
ldraw2stlPath = "ldraw2stl/bin/dat2stl"

def main():
	print("starting stl conversion")

	# get file names in ldraw parts folder
	for file in os.listdir(ldrawPartsPath):

		# get name and extension
		name, extension = os.path.splitext(file)

		# skip non-dats
		if extension != ".dat":
			print(f"non-dat file {file} skipped")
			continue

		currentStlPath = f"{stlPartsPath}/{name}.stl"
		currentLdrawPath = f"{ldrawPartsPath}/{file}"

		# check if already copied
		if os.path.exists(currentStlPath):
			# get last time that files were modified
			stlUpdateDate = os.path.getmtime(currentStlPath)
			ldrawUpdateDate = getLdrawDate(currentLdrawPath)

			# skip if stl is newer than ldraw
			if ldrawUpdateDate < stlUpdateDate:
				print(f"skipped part {name}, stl file is newer than its ldraw file")
				continue

		# use ldraw2stl through bash to convert into stl
		with open(currentStlPath, "w") as outfile:
			subprocess.run([
        		f"./{ldraw2stlPath}",
        		"--file", f"{ldrawPartsPath}/{file}",
        		"--ldrawdir", ldrawPath
    		], stdout=outfile, text=True)
	
		print(f"part {name} converted to stl")


def getLdrawDate(path):
	# read file lines
	lines = None
	with open(path, "r") as file:
		lines = file.readlines()

	updateDateLine = None

	for line in lines:
		# check if line is a history element
		if line.startswith("0 ! HISTORY"):
			updateDateLine = line.strip()

	updateDate = None

	# check if an update date was found
	if updateDateLine:
		# extract date
		parts = updateDateLine.split(" ")
		updateDate = parts[1]

		# convert to date format
		updateDate = datetime.strptime(updateDate, "%Y-%m-%d")

		# convert to unix
		updateDate = int(time.mktime(updateDate.timetuple()))

	return updateDate

main()