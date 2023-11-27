# recursion
# "the family chain of new phones"


# problem solving - delegation metaphor
# 1 find the base case (easy)
# 2 find a way to reduce the problem (not easy): reduce steps of procedure, quantity of a number, size of a list
# 3 find the relationship between the solution of the reduced problem and the original proble


# def is_even(n):
#     """ returns True if n (non-negative) is an even number, otherwise return False.
#     """
#     # base case
#     if n == 0:
#         return True
#     elif n == 1:
#         return False
#     else:
#         # recursive case (n-2)
#         is_previous_number_even = is_even(n-2) # returns if n-2 is even
#         # for case n, it has the same solution as n-2 case.
#         return is_previous_number_even

def is_even(n):
    """ returns True if n (non-negative) is an even number, otherwise return False.
    """
    # base case
    if n == 0:
        return True
    # elif n == 1:   # this base case merges with the recursive case
    #     return False
    else:
        # recursive case (n-1)
        is_previous_number_even = is_even(n-1) # returns if n-2 is even
        # for case n, it has the opposite solution as n-1 case.
        is_current_number_even = not is_previous_number_even
        return is_current_number_even


print(is_even(2))

""" flowtrace for is_even(2)
is_even(2)
n = 2
if n == 0:
    is_previous_number_even = is_even(2-1)
                              n = 1
                              if n == 0:
                                  is_previous_number_even = is_even(1-1)
                                                            n = 0
                                                            if n ==0:
                                                            return True
                                  is_current_number_even = not True
                                  return False
    is_current_number_even = not False
    return True
"""


# # recursion depth
for i in range(10000):
    try:
        is_even(i)
    except:
        print(f"max recursion number reached: {i}")
        break
