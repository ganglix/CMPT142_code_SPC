# Write a Python function that accepts string parameter s and
# prints whether s has an even or odd amount of characters.
# Sample function console output:
# "Dog" has an odd number of characters.

def check_char(s):
    if len(s)%2 == 0: # even
        check = "even"
    else:
        check ="odd"
    print(f"{s} has an {check} number of chars")


def check_char_user_input():
    s = input("please type a word: ").strip()
    if len(s)%2 == 0: # even
        check = "even"
    else:
        check ="odd"
    print(f"{s} has an {check} number of letters")

check_char_user_input()