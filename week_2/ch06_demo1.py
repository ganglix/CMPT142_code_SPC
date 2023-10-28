# Write a docstring for the following function definition (abs()
# returns the absolute value of a number):

def print_smaller_absolute(num1, num2):
    """
    return and display the absolute value of the smaller number of the given two numbers.
    :param num1: int or float, the first number to compare
    :param num2: int or float, the second number to compare
    :return: int or float, absolute value of the smaller number
    """
    small_abs = abs(min(num1, num2))
    print("Absolute value of smaller number: ", small_abs)
    return small_abs



# who cares about docstring

# things not to do.
# afraid to lose marks
# engineering example?
# style

