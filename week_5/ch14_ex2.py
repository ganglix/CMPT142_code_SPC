# Topic(s): Writing Files
# store’s item inventory to write (no "stock" means not carried by store)

# expected output
# Healing Herb,Heals minor wounds,25,0.25,5
# Smoke Cloud,Creates distraction,65,1.15,

inventory = [
    {"name": "Healing Herb", "desc": "Heals minor wounds",
     "cost": 25, "weight": 0.25, "stock": 5},
    {"name": "Antidote Vial", "desc": "Cures poisonous wounds",
     "cost": 50, "weight": 1.25, "stock": 3},
    {"name": "Paralysis Herb", "desc": "Paralyzes enemy when thrown",
     "cost": 75, "weight": 0.35},
    {"name": "Smoke Cloud", "desc": "Creates distraction for escape",
     "cost": 65, "weight": 1.15},
    {"name": "Fairie Dust", "desc": "Casts light in the darkness",
     "cost": 100, "weight": 0.4, "stock": 3},
]

# open file for writing


# for every item in inventory , write out its details on its own line

# done writing , so close the file
















# #~~~~~~~~~~ advanced dictionary .get() method not covered in the textbook ~~~~~~~~~~~~~
# # example: .get method
# print(
#     {"name": "Smoke Cloud", "desc": "Creates distraction for escape",
#      "cost": 65, "weight": 1.15}.get('stock', '')  # return value corresponding to key"stock", if not key found, return ''
# )



# for item in inventory:
#     line_to_write = ','.join([item.get("name"),
#                               item.get("desc"),
#                               str(item.get("cost")),
#                               str(item.get("weight")),
#                               str(item.get("stock",''))])
#     f.write(line_to_write)
#     f.write('\n')
