import os
import numpy
from stl import mesh

stlPartsPath = "../stl"
dimensionsPath = "../dimensions"

def main():
	print("starting parts list update")

	# get file names in stl parts folder
	for stlFile in os.listdir(stlPartsPath):

		# get name and extension
		name, extension = os.path.splitext(stlFile)

		# skip non-dats
		if extension != ".stl":
			print(f"non-stl element {stlFile} skipped")
			continue

		currentDimensionsPath = f"{dimensionsPath}/stlPartsPath", "w"
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

		# get min and max point
		minPoint = numpy.min(vectors, axis=(0, 1))
		maxPoint = numpy.max(vectors, axis=(0, 1))

		# get dimensions
		dimensions = maxPoint - minPoint

		# write dimensions to file
		with open(currentDimensionsPath) as dimensionsFile:
			dimensionsFile.write(dimensions)

main()