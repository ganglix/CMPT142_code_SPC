import numpy as np

# Create a signed 8-bit integer array
# with the single data item 10.
x = np.array([10]).astype('int32')   # int8  _ _ _ _ _ _ _ _

# x[0] starts at 10 and gets larger with each loop iteration.

x_list = []
for i in range(512):
    x[0] = x[0] + 1
    x_list.append(x[0])
    # print(x[0])

import matplotlib.pyplot as plt

plt.plot(range(512), x_list)
plt.show()

# print(sum([ 2**0, 2**1, 2**2, 2 ** 3, 2**4, 2**5, 2**6  ]))   #  seven bits used for number , and one used for sign