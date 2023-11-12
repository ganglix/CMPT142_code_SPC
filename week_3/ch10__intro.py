# lists and tuples

# create a list
L = [1, 2, 3]
# array
import numpy as np

arr = np.array(L)

print(L * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(arr * 3)  # [3 6 9]

lis = [1, 2, 'apple', max, arr, L, []]  # container for anything

# indexing and slicing, same as string, or other sequences
print(L[0])
print(L[1:])
print(L[-1])

# methods
# add an item: .append(), +, .extend()
print("before", L)
L.append("item")  # does not return anything! it adds "item" to the list
print("after", L)
# list is our first mutable data type, change happens "in-place"

L.extend(["garbage1", "garbage2"])  # same as +
print(L)

# remove an item: .remove(), del, .pop()
L.remove("garbage1")  # remove by value
whats_popped = L.pop(-1)  # remove by index, remove the item and return it
# by default .pop() remove the last item
print(whats_popped)
print(L)

del L[-1]  # remove last item
print(L)

# locating an item: index()
# print(L.index('garbage1'))


# sorting: .sort()
L.append(-1)
L.sort()  # sorting in-place
print(L)
L.sort(reverse=True)
print(L)

new_L = sorted(L)  # sort and return a sorted list, and does not change L
print(L)
print(new_L)

# # let do an attempt to use .sort() without changing the old L
# print(L)
# L2 = L   # does not create a new L identical to L, you just give a new name L2 to the old data named L
# print("L before", L)
# print("L2 before", L2)
# L2.sort()
# print("L2 should be sorted:", L2)
# print("L should not change:", L)

# let use .sort() without changing the old L [right way]
print(L)
L2 = L.copy()  # create a new L (clone) identical to L
# another way to create a clone is L[:], but this method does not work for array
print("L before", L)
print("L2 before", L2)
L2.sort()
print("L2 should be sorted:", L2)
print("L should not change:", L)

# list is mutable ! more examples in flowtrace observations


# flowtrace

L = [1, 2, 3, 4, 5, 6]
for value in L:
    L.remove(value)
print(L)

"""
L = [1, 2, 3, 4, 5, 6]
for value in [1, 2, 3, 4, 5, 6]:
    value = 1 # first  of [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6].remove(1)
    value = 3 # second of [2, 3, 4, 5, 6]
    [2, 3, 4, 5, 6].remove(3)
    value = 5 # third of [2, 4, 5, 6]
    [3, 4, 5, 6].remove(5)
print([2, 4, 6])
"""
