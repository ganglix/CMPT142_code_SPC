import numpy as np

np.random.seed(1)
c = np.random.uniform(0,1000,1000).astype(int)
import random

success_count = []

for i in range(10000):
    item_idx = random.randint(0, 999)
    count = 1
    target_key = 554
    max_count = int(1e8)
    while c[item_idx] != target_key and count < max_count:
        item_idx = random.randint(0, 999)
        count += 1

    # if count < max_count:
    #     print(f"search is done, item found at {count} trial")
    # else:
    #     print("exceeded the max count, probably target is not in the list")
    success_count.append(count)

import matplotlib.pyplot as plt

plt.hist(success_count, bins = 50)
plt.xlabel("number of trials to find the item")
plt.show()