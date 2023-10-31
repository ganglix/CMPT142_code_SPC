# Write a Python function that uses a for-loop to print the
# number of times each lowercase vowel (a,e,i,o,u) occurs in a
# string s. e.g. "piece" prints "a:0 e:2 i:1 o:0 u:0".

s = "piece"
# print(f"e:{s.count('e')}")   # use str method

# for loop code
count_a = 0
count_e = 0

for c in s:
    if c == "e":
        count_e += 1
    elif c == "a":
        count_a += 1

# count_a = 0
# for c in s:
#     if c == "a":
#         count_a += 1

print(f"a:{count_a} e:{count_e}")