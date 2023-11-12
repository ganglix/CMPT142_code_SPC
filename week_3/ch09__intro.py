# Control Flow: Repetition
# what is a computer good at?
# repeat till what? when?


# while loop starts and stops according to a condition
## things I want to mention: condition boolean, while/if, keep checking(eg.)

# counting example : 1~5
count = 1
# count += 1  # count = count + 1
# keep doing this
# until i = 5

while count < 5:  # preferred
    # condition is True, keep doing, until the condition becomes False
    count += 1
    print("inside the loop: ", count)

# condition = True
# while condition:
#     # condition is True, keep doing, until the condition becomes False
#     count += 1
#     print("inside the loop: ", count)
#     if count == 5:
#         condition = False

print("end of the loop: ", count)

# for : repeat over a sequence
## mention types of sequence: string, range, list, dict

for c in "cmpt 142":
    print(c)

for i in range(3):  # 0 1 2
    print(i)

for item in ["red", "green", "blue"]:
    print(item)

# flowtrace

i = 1
while i < 10:
    i = i * 2
print(i)

"""
i = 1
while 1 < 10:
    i = 1 * 2
while 2 < 10:
    i = 2 * 2
while 4 < 10:
    i = 4 * 2
while 8 < 10:
    i = 8 * 2
while 16 < 10:
print(16)
"""

# i = 1
# while i != 5:  # inf loop
#     i = i * 2
# print(i)

total = 0
for i in range(2):
    for j in range(2):
        total = total + 1
print(total)

"""
total = 0

for i in range(2):
    i = 0
    for j in range(2):
        j = 0
        total = 0 + 1
        j = 1
        total = 1 + 1
    i = 1
    for j in range(2):
        j = 0
        total = 2 + 1
        j = 1
        total = 3 + 1
        
print(4)
"""