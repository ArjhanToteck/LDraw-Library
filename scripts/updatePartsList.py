import os

ldrawPath = "../ldraw"
ldrawPartsPath = ldrawPath + "/parts"
partsListPath = "../partsList"

def main():
	print("starting parts list update")

	# open parts list file
	with open(partsListPath, "w") as partsList:
		# get file names in ldraw parts folder
		for file in os.listdir(ldrawPartsPath):

			# get name and extension
			name, extension = os.path.splitext(file)

			# skip non-dats
			if extension != ".dat":
				print(f"non-dat file {file} skipped")
				continue

			partsList.write(name + "\n")

	print("done")

main()