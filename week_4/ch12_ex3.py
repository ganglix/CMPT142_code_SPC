def is_valid_password(password):
    """
    determines if password meets these constraints:
    - 9-18 characters long
    - no Underscores or minus _,-
    password: string to check validity of
    return: True if password satisfies constraints
    """
    is_valid = True

    if len(password) < 9 or len(password) > 18:
        is_valid = False
    if "_" in password:
        is_valid = False
    if "-" in password:
        is_valid = False

    return is_valid


# Testing - white box
# white-box reasoning: make sure full coverage of the code
# full coverage: every branch, every iteration (0 times, 1 time, max times)

"""
inputs: "1"*8   # check the if-statement condition
outputs_expected: False  # figure out the outputs by look at the doctring/how function is supposed to behave, NOT through running the code
reason: trigger line 11 if condition to be true

inputs: "1_"   # check the if-statement condition
outputs_expected: False  # figure out the outputs by look at the doctring/how function is supposed to behave, NOT through running the code
reason: trigger line 13 if condition to be true

inputs: "1-"   # check the if-statement condition
outputs_expected: False  # figure out the outputs by look at the doctring/how function is supposed to behave, NOT through running the code
reason: trigger line 15 if condition to be true
"""