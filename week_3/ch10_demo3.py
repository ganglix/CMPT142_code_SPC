# Up until now, only immutable data types have been passed
# as arguments to functions. What happens when we pass
# mutable data?
# Let us observe the effect on an input variable before,
# during, and after a function call that changes the value.

def update_grades(grades):
    grades[0] = grades[0] + 2

classgrades = [48, 53, 95, 72]

new_grades = update_grades(classgrades)






# -----------------------------------------
# # does this operation create a new list?

