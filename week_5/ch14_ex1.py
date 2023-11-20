# Topic(s): Reading Files
# read file and create a list of dictionaries to store data
# looks like this:
# scientists = [{"name": "Isaac Newton",
#                "birth_year": 1643,
#                "death_year": 1727},
#               {"name": "Albert Einstein",
#                "birth_year": 1879,
#                "death_year": 1955}]

# ~~~~~~~~~~~~open~~~~~~~read~~~~~~close~~~~routine~~~~~~~~

# open file for reading
path = "./subfolder/scientists_data.txt"
f = open(path, 'r')
# read in all scientist data and put in a list of records
records = []  # to store {}s
for line in f:
    line = line.rstrip().split(",")
    records.append({"name": line[0],
                    "birth_year": int(line[1]),
                    "death_year": int(line[2])})

# done reading , close file
f.close()



















# ~~~~~~~ use with statement~~~~~~~~~~~~~~~~~

# # open file for reading
# with open("./subfolder/scientists_data.txt", "r") as f:
#     # read in all scientist data as list of records
#     # create scientist record
#     scientist = []
#     for line in f:
#         # removing trailing newline & parse data as list
#         line = line.rstrip().split(",")
#         # add scientist record to scientists listing
#         scientist.append({"name": line[0],
#                           "birth_year": line[1],
#                           "death_year": line[2]})
