# What Is This?
This is an unofficial repository to hold all of the models from [LDraw](https://www.ldraw.org/) in both their native .DAT format as well as in the .STL format for easier manipulation and 3D printing.

.DAT files are stored in the ldraw directory (it's a mirror of LDraw's part library), specifically in ldraw/parts. .STL files are stored in the stl folder. The dimensions of each part are also stored as .JSON files in the dimensions directory.

A list of all part names can be found in the partsList file. This will be their file names in each folder (of course, with a file extension added).

# Updating the Library
The repository can be updated by running updateLibrary.sh in the scripts directory. This will load any updates from LDraw's website and update data in the library accordingly.
