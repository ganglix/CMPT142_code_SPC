# Write a Python program that uses a for-loop to print all
# integers between 300 and 600 (inclusive) that are divisible
# by both 3 and 5. Print how many of these numbers were
# found

count = 0
for n in range(300, 600+1):  # the end is not included
    if n % 3 == 0 and n % 5 == 0:  # better, readable, related to the question description
    # if n % 15 == 0:   # equivalent
        print(n)
        count += 1  # every time we found a qualified number

print(f"{count} numbers found!")