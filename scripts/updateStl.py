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
	for ldrawFile in os.listdir(ldrawPartsPath):

		# get name and extension
		name, extension = os.path.splitext(ldrawFile)

		# skip non-dats
		if extension != ".dat":
			print(f"non-dat element {ldrawFile} skipped")
			continue

		currentStlPath = f"{stlPartsPath}/{name}.stl"
		currentLdrawPath = f"{ldrawPartsPath}/{ldrawFile}"

		# check if already copied
		if os.path.exists(currentStlPath):
			# get last time that files were modified
			stlUpdateDate = os.path.getmtime(currentStlPath)
			ldrawUpdateDate = os.path.getmtime(currentLdrawPath)

			# skip if stl is newer than ldraw
			if ldrawUpdateDate < stlUpdateDate:
				print(f"skipped part {name}, stl file is newer than its ldraw file")
				continue

		# use ldraw2stl through bash to convert into stl
		with open(currentStlPath, "w") as outfile:
			subprocess.run([
        		f"./{ldraw2stlPath}",
        		"--file", f"{ldrawPartsPath}/{ldrawFile}",
        		"--ldrawdir", ldrawPath
    		], stdout=outfile, text=True)
	
		print(f"part {name} converted to stl")

main()
print("stls updated")