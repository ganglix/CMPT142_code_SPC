# Indexing and Slicing of !Sequences!
name = "cmpt 142" # str
['c','m','p','t',' ', 142]  # list
(1, 2, 3)   # tuple

# •What is indexing used for?
# •What does a positive index mean?
# •What does a negative index mean?

#  ________
#  87654321  (negative)
#  01234567
# "cmpt 142"
print("'" + "cmpt 142"[4] + "'")
# print("cmpt 142"[8]) # out of range, error
print("cmpt 142"[5])

# •What is slicing used for?
# •What are the meanings of the First, second, and third
# numbers in a slicing operation?
# [start : end(exclusive) : step(default=1)]

#  ________
#  87654321  (negative)
#  01234567
# "cmpt 142"
print("cmpt 142"[0:7])  # [0123456] cmpt 14
slice = "cmpt 142"[0:7]
print(len(slice))

slice = "cmpt 142"[0:9] # out of range, no error

#  [         ]
#  01234567
# "cmpt 142"
print(slice)

slice = "cmpt 142"[ : ]  # omission, meaning boundary
print(type(slice))

slice = "cmpt 142"[1: :2]  # start at 1 till end(include) step is 2
print(slice)

slice = "cmpt 142"[-1:-6:-1]
print("negative slice",slice)

slice = "cmpt 142"[ : :-1] # reverse
print(slice)

# I want to mention omitted value, index out of range, and range of slice
