import os
import numpy
from stl import mesh

stlPartsPath = "../stl"
dimensionsPath = "../dimensions"

def main():
	print("starting dimensions update")

	# get file names in stl parts folder
	for stlFile in os.listdir(stlPartsPath):

		# get name and extension
		name, extension = os.path.splitext(stlFile)

		# skip non-dats
		if extension != ".stl":
			print(f"non-stl element {stlFile} skipped")
			continue

		currentDimensionsPath = f"{dimensionsPath}/{name}.json"
		currentStlPath = f"{stlPartsPath}/{stlFile}"

		# check if already copied
		if os.path.exists(currentDimensionsPath):
			# get last time that files were modified
			dimensionsUpdateDate = os.path.getmtime(currentDimensionsPath)
			stlUpdateDate = os.path.getmtime(currentStlPath)

			# skip if dimensions is newer than stl
			if stlUpdateDate < dimensionsUpdateDate:
				print(f"skipped part {name}, dimensions file is newer than its stl file")
				continue

		# get stl mesh and vectors
		vectors = mesh.Mesh.from_file(currentStlPath).vectors

		# default to 0 if no vectors
		dimensions = "[0, 0, 0]"

		if len(vectors) > 0:
			# get min and max points
			minPoint = numpy.min(vectors, axis=(0, 1))
			maxPoint = numpy.max(vectors, axis=(0, 1))

			# get dimensions and join into string
			dimensions = maxPoint - minPoint
			dimensions = dimensions.tolist()
			dimensions = f"[{', '.join(map(str, dimensions))}]"

		# write dimensions to file
		with open(currentDimensionsPath, "w") as dimensionsFile:
			dimensionsFile.write(dimensions)

main()
print("dimensions updated")