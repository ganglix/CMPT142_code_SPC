"""
generation  ancestor
n   bees(n)
0   1
1   1
2   2
3   3
4   5
5   8
6   13
n   bees(n) = bees(n-1) + bees(n-2)
pattern
"""


def bees(n):
    if n == 0 or n == 1:
        return 1
    else:
        return bees(n - 1) + bees(n - 2)


# n_bees = []
# for i in range(21):
#     n_bees.append(bees(i))
# import matplotlib.pyplot as plt
# plt.plot(range(21), n_bees)
# plt.show()

# import time
# start = time.time()
# bees(20)
# end = time.time()
# n_calls = 2 ** 20
# time_per_call = (end-start) / n_calls   # second
#
# # bees(60)
# print("time needed for bees(60) [years]:", 2**60 * time_per_call / 60/60/24/365)

bees_n_cache = {}  # n : bees(n)
def bees_efficient(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n not in bees_n_cache:
            bees_n = bees_efficient(n - 1) + bees_efficient(n - 2)
            bees_n_cache[n] = bees_n
        return bees_n_cache[n]

print(bees_efficient(60))