# Search algorithm


# search for a number from a list of numbers

# generate an array to work with

import numpy as np




# linear search
def linear_membership_search(c, target_key):
    """
    a linear membership search for the target key

    c:          a sequence of numbers or strings
    target_key: the target key for the search
    return: True if target key is in the collection
    """
    # base case
    if len(c) == 0:
        return False
    else:
        # recursive case
        if c[0] == target_key:
            return True
        else:
            return linear_membership_search(c[1:], target_key)

# c = np.random.uniform(0,9, size=5).astype(int)
# print(c)
# print(linear_membership_search(c, 4))


# binary search

def binary_membership_search(c, target_key):
    """
    A binary membership search function
    :param c: list, collection of data, sorted by its search keys
    :param target_key: target key to search for
    :return: True if target key is in the collection
    """
    if len(c) == 0:
        return False
    else:
        mid_idx = len(c)//2
        if c[mid_idx] == target_key:
            return True
        elif c[mid_idx] > target_key:
            return binary_membership_search(c[:mid_idx], target_key)
        else:
            return binary_membership_search(c[mid_idx + 1:], target_key)


c = np.random.uniform(0,9, size=5).astype(int)
c.sort()
print(c)
print(binary_membership_search(c, 4))
