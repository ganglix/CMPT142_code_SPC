"""
N   F(N)
0   1
1   2
2   4
3   7
4   11  F(4) = 7 + 4 = F(3) + 4
5   16  F(5) = 11 + 5 = F(4) + 5
N-1 F(N-1)
N   F(N)
------
F(N) = F(N-1) + N
"""
def F(n):
    # base case
    if n == 0:
        return 1
    else:
        # recursive case
        return F(n-1) + n

print(F(5))


