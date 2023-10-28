# Write a Python function which accepts integer parameter
# grade and prints to the console:
# • "A+" if grade is between 100 and 95
# • "A" if grade is between 94 and 85
# • "B" if grade is between 84 and 75
# • "C" if grade is between 74 and 65
# • "D" if grade is between 64 and 50
# • "F" otherwise

# check my attempt:
# def letter_grade(grade):
#     """
#     Return the letter grade of a number grade
#     :param grade: int, numeric grade
#     :return: str, letter grade
#     """
#     if grade <= 100 and grade >= 95:
#         print("A+")
#     if grade <= 94 and grade >= 85:
#         print("A")
#     if grade <= 84 and grade >= 75:
#         print("B")
#     if grade <= 74 and grade >= 65:
#         print("C")
#     if grade <= 64 and grade >= 50:
#         print("D")
#     else:
#         print("F")

# def letter_grade(grade):  # good
#     """
#     Return the letter grade of a number grade
#     :param grade: int, numeric grade
#     :return: str, letter grade
#     """
#     if grade <= 100 and grade >= 95:
#         print("A+")
#     elif grade <= 94 and grade >= 85:
#         print("A")
#     elif grade <= 84 and grade >= 75:
#         print("B")
#     elif grade <= 74 and grade >= 65:
#         print("C")
#     elif grade <= 64 and grade >= 50:
#         print("D")
#     else:
#         print("F")

# def letter_grade(grade): # correct, but not good, this one checks all if s, which is not efficient
#     """
#     Return the letter grade of a number grade
#     :param grade: int, numeric grade
#     :return: str, letter grade
#     """
#     if grade <= 100 and grade >= 95:
#         print("A+")
#     if grade <= 94 and grade >= 85:
#         print("A")
#     if grade <= 84 and grade >= 75:
#         print("B")
#     if grade <= 74 and grade >= 65:
#         print("C")
#     if grade <= 64 and grade >= 50:
#         print("D")
#     if grade <= 49:
#         print("F")
#
# letter_grade((95))

def letter_grade(grade):  # good
    """
    Return the letter grade of a number grade
    :param grade: int, numeric grade
    :return: str, letter grade
    """
    # grade = round
    if grade <= 100 and grade >= 95:
        print("A+")
    elif grade <= 94 and grade >= 85:
        print("A")
    elif grade <= 84 and grade >= 75:
        print("B")
    elif grade <= 74 and grade >= 65:
        print("C")
    elif grade <= 64 and grade >= 50:
        print("D")
    else:
        print("F")

