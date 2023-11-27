# Write a recursive function to find the smallest value in a list of
# numbers.


# 1 base case
# 2 recursive case (reduced problem, how to reduce)
# 3 relationship between the problem and the reduced problem

# def smallest(L):
#     """
#     returns the smallest number of a list of numbers
#     :param L: list, a list of numbers
#     :return: int or float, the smallest number in the list L
#     """
#     if len(L) == 0:
#         return None   # handle the empty list
#     # base case:
#     elif len(L) == 1:
#         return L[0]
#     else:
#         # recursive case L[1:]
#         small = smallest(L[1:])
#         if L[0] < small:
#             return L[0]
#         else:
#             return small

def smallest(L):
    """
    returns the smallest number of a list of numbers
    :param L: list, a list of numbers
    :return: int or float, the smallest number in the list L
    """
    if len(L) == 0:
        return None   # handle the empty list
    # base case:
    elif len(L) == 1:
        return L[0]
    else:
        # recursive case: cut the list into halves
        mid_idx = len(L) // 2  # 0 1 2 3 4 5, len=6, (len)//2: 3
        small_left = smallest(L[:mid_idx])
        small_right = smallest(L[mid_idx:])

        if small_left < small_right:
            return small_left
        else:
            return small_right


print(smallest([2,1,1,4]))