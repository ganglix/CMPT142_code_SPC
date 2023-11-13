# demo1
# Tower Name Location
# Tokyo Skytree Japan
# Canton Tower China
# CN Tower Canada

tower = {
    "Tokyo Skytree": "Japan",
    "CN Tower": "Canada",
    "Canton Tower": "China",
}

print(tower)

# Let’s modify the dictionary:
# (a) Remove the entry whose location is "Canada"
# for k in tower:
#     if tower[k] == 'Canada':
#         tower.pop(k)
# print(tower)

for k in tower.copy():
    if tower[k] == 'Canada':
        tower.pop(k)
print(tower)



# (b) Add a new entry with tower name "Eiffel Tower" and
# location "Paris"

tower['Eiffel Tower'] = "Paris"

# (c) Oops! Update the tower entry "Eiffel Tower" to have
# location "France"

tower['Eiffel Tower'] = "France"
print(tower)

