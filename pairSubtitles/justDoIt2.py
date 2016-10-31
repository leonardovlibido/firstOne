import os, re
ri = re.compile(r'S\d\dE\d\d', re.S)
ext = re.compile(r'(\.[^.]*)')
for filename in os.listdir("."):
    ID = ri.findall(filename)
    fileExtension = ext.findall(filename)
    if ID and fileExtension:
        newFilename = ID[0]+fileExtension[-1]
        os.rename(filename, newFilename)
