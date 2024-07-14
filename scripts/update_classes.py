import os
import csv

MODULES_PATH = "../src/modules"
CHANGES = "Changes.txt" # https://github.com/SyndiShanX/Update-Classes/blob/main/Changes.txt

# Get all SCSS files and put them in a list
filelist = []
for (dirpath, subdirs, files) in os.walk(MODULES_PATH):
    for f in files:
        if ".scss" in f:
            filelist.append(os.path.join(dirpath,f))

# Find and replace operation
# For each SCSS file in the file list...
for file in filelist:
    # Open the file
    print("opening: ", file)
    with open(file, "r", encoding="utf-8") as file_obj:
        filedata = file_obj.read()

    # Open the changes file
    with open(CHANGES, 'r') as rawFile:
        rawText = "\n".join(line.rstrip() for line in rawFile).split('\n')

    # Start a counter
    i = 0
    classNum = len(rawText) - 1

    # Make changes
    while i < classNum:
        class1 = rawText[i]
        class2 = rawText[i + 1]

        filedata = filedata.replace(class1, class2)

        # Increment counter
        i = i + 2

    # Write the file out
    with open(file, "w", encoding="utf-8") as file_obj:
        file_obj.write(filedata)
