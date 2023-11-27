"""
N   F(N)
0   1
1   3
2   5
3   7
4   9
5   11
----------------
F(N) = F(N-1) + 2
"""

def F(n):
    # base case
    if n == 0:
        return 1
    else:
        # recursive case
        return F(n-1) + 2

print(F(5))
