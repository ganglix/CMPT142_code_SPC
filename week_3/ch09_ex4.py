# Write a Python function that prints the (x, y) coordinates for a
# M by N image. e.g. Output for M = 10, N = 5:
"""
(0,0) (1,0) (2,0) (3,0) (4,0) (5,0) (6,0) (7,0) (8,0) (9,0)
(0,1) (1,1) (2,1) (3,1) (4,1) (5,1) (6,1) (7,1) (8,1) (9,1)
(0,2) (1,2) (2,2) (3,2) (4,2) (5,2) (6,2) (7,2) (8,2) (9,2)
(0,3) (1,3) (2,3) (3,3) (4,3) (5,3) (6,3) (7,3) (8,3) (9,3)
(0,4) (1,4) (2,4) (3,4) (4,4) (5,4) (6,4) (7,4) (8,4) (9,4)
"""
M = 10
N = 5

# # print first row
# y = 0
# for x in range(M): # 0 1 2... 9
#     print(f"({x},{y})", end = " ")

# print first row
for y in range(N):
    for x in range(M):  # 0 1 2... 9
        print(f"({x},{y})", end=" ")
    print()  # new line

