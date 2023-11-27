import numpy as np

np.random.seed(1)
c = np.random.uniform(0,1000,1000).astype((int))

print(c)
import random
item = -1 # wrong guess
count = 0
target_key = 555
max_count = int(1e8)
while item != target_key and count < max_count:
    item = random.randint(0, 1000)
    count += 1

if count < max_count:
    print(f"search is done, item found at {count} trial")
else:
    print("exceeded the max count, probably target is not in the list")