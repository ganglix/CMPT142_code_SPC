
# N! = N * (N-1)!
# 3! = 3 * 2 * 1  = 3 * 2!
# 2! = 2 * 1 = 2 * 1!
# 1! = 1 = 1 * 0!   # not special, still follow the rule
# 0! = 1   # special

def factorial_a(N):
    if N < 0:
        return None   # handle potenial unreasonable negative argument
    # base case
    elif N == 0:
        return 1
    else:
        # recursive case
        # reduced problem being delegated is factorial_a(N - 1)
        return factorial_a(N - 1) * N   # N!


# print(factorial_a(3))


# (a) What is the condition for the base case?

# (b) What is the condition for the recursive case?

# (c) What problem is being delegated?

# (d) How is the solution to the delegated problem used?


def factorial_b(N):
    # recursive case
    if N > 0:
        return factorial_b(N - 1) * N
    else:
        # base case ( most reduced case )
        return 1   # N = 0

print(factorial_b(3))



# which one is better?
# print(factorial_a(-1))  # error   # better (maybe)
# print(factorial_b(-1))    # returns 1, but wrong, because -1! is not defined