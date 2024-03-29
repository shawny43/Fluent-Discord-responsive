import os
import csv

MODULES_PATH = "../src/modules"
CLASS_MAP = "classes_mapping.csv" # https://github.com/NyxIsBad/discordscripts/blob/master/classes_mapping.csv

# Get all SCSS files and put them in a list
filelist = []
for (dirpath, subdirs, files) in os.walk(MODULES_PATH):
    for f in files:
        if ".scss" in f:
            filelist.append(os.path.join(dirpath,f))

# Find and replace operation
# For each SCSS file in the file list...
for file in filelist:
    # Open the file in memory
    print("opening: ", file)
    with open(file, "r", encoding="utf-8") as file_obj:
        filedata = file_obj.read()

    # Open the CSV
    with open(CLASS_MAP, encoding="utf-8") as f:
        csv_reader = csv.DictReader(f)
        next(csv_reader) # Skips the header

        # Find and replace old class with new class
        for line in csv_reader:
            # print("finding: ", line["class_old"])
            filedata = filedata.replace(line["class_old"], line["class_new"])

    # Write the file out
    with open(file, "w", encoding="utf-8") as file_obj:
        file_obj.write(filedata)
