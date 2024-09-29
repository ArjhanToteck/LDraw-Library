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

		# get stl mesh and vectors
		vectors = mesh.Mesh.from_file(f"{stlPartsPath}/{stlFile}").vectors

		# get min and max point
		minPoint = numpy.min(vectors, axis=(0, 1))
		maxPoint = numpy.max(vectors, axis=(0, 1))

		# get dimensions
		dimensions = maxPoint - minPoint

		# write dimensions to file
		with open(f"{dimensionsPath}/stlPartsPath", "w") as dimensionsFile:
			dimensionsFile.write(dimensions)

main()