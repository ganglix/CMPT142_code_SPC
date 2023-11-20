# Read in the file data to create dictionary extensions that
# maps extension numbers to employees

# open
# absolute path: full directory
# r is used to say: this is a raw string (not formatted)
# path = r"C:\Users\gal894\Desktop\CMPT142_code_SPC\week_5\ext_directory_data.txt"
# relative path

path = "ext_directory_data.txt"   # by default, use the file name, if stored in the same folder

# .  means current folder
# .. means parent folder
# path = "./ext_directory_data.txt"
# path = "../week_5/ext_directory_data.txt"

# open
f = open(path, 'r') # r: read mode

# read and create the dictionary

extension = {}
for line in f:
    # at the end of a line, this is a '\n' formatting string, invisible
    line = line.rstrip()
    # parse the line
    line = line.split(',')
    ext = int(line[0])
    name = line[1]
    # adding content to dict
    extension[ext] = name

# close
f.close()

print(extension)
