def merge(S1, S2):
    """
    combines two sorted sequences into single sorted sequence
    S1: sorted sequence to combine
    S2: other sorted sequence to combine
    return: single sorted sequence of S1, S2 combined
    """
    # let S be an empty sequence
    S = []
    # repeatedly move the smallest item to S
    while len(S1) > 0 and len(S2) > 0:
        if S1[0] < S2[0]:
            S.append(S1[0])
            del S1[0]
        else:
            S.append(S2[0])
            del S2[0]
    # once one of S1 or S2 is empty, append the remaining
    # non-empty sequence to S.
    if len(S1) > 0:
        S.extend(S1)
    else:
        S.extend(S2)
    return S



def merge_sort(S):
    """
    merge sort a list in ascending order and return it
    :param S: a list to be sorted
    :return: sorted list
    """
    # base case
    if len(S) <= 1:
        return S
    else:
        # recursive case
        # divide step
        mid_idx = len(S)//2    # [4, 5, 6]  mid_idx = 1   round down the number of left list
        left = S[0:mid_idx]    # S[0:1] is  [4]
        right = S[mid_idx:]
        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)
        # conquer step
        return merge(left_sorted, right_sorted)  # left, right position does not matter


print(merge_sort([2, 1, 4, 3]))
