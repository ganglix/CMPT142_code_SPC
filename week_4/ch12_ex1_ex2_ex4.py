def is_valid_username(username):
    """
    determines if username meets these constraints:
    - 1-18 characters long
    - can be letters and/or numbers
    - underscore is allowed if it’s not the first character
    username: string to check validity of
    return: True if username satisfies constraints
    """

# Testing - black box
# black-box reasoning: test what has been promised in the docstring

# Test cases that test the length requirement is satisfied
"""
inputs: ""
outputs_expected: False
reason: username is empty string, length is zero

inputs: "a"
outputs_expected: True   # figure out the expected output by look at the whole docstring
reason: username length is one

inputs: "a"*18
outputs_expected: True   # figure out the expected output by look at the whole docstring
reason: username length is 18

inputs: "a"*19
outputs_expected: False   # figure out the expected output by look at the whole docstring
reason: username length is 19, out of range, which makes the username invalid
"""

# • Test cases that test the letters-or-numbers-only requirement is satisfied

"""
inputs: "0"*18
outputs_expected: True
reason: only numbers in username, which is valid

inputs: "0a1"
outputs_expected: True
reason: username has both letters annd numbers, which is valid

inputs: "a+1"
outputs_expected: False
reason: username has special character (other than _), which is invalid
"""

# Test cases that test the underscore constraint is satisfied
"""
inputs: "_12"
outputs_expected: False
reason: username has leading _, which is invalid

inputs: "1_2"
outputs_expected: True
reason: username has _ in the middle, which is valid

inputs: "12_"
outputs_expected: True
reason: username has trailing _, which is valid

"""



# test driver example
# test driver is a program that runs the test cases

"""
inputs: ""
outputs_expected: False
reason: username is empty string, length is zero
"""

inputs = ""
outputs_expected = False
reason = "username is empty string, length is zero"

result = is_valid_username(inputs)
if result != outputs_expected:
    print("fault found!",
          f"the input is {inputs}",
          f"the expected output is {outputs_expected}",
          f"the function returned {result}",
          f"test case reasoning: {reason}")


# ~~~~~~~~~~~~~~~~after dictionary~~~~~~~~~~~~~~~~~~~~

# dictionary of test case suite to feed into test driver loop
test_suite = [
    # call for length -zero username (empty string)
    {"inputs": [""],
     "outputs": False,
     "reason": "length must be be 1-18 characters"},

    # call for length -one username of invalid character
    {"inputs": ["+"],
     "outputs": False,
     "reason": "username can only contain letters , numbers , underscores"},

    # call for length -one username of a letter
    {"inputs": ["a"],
     "outputs": True,
     "reason": "username is allowed to have letters"},

    # call for length -18 username of numbers only with trailing underscore
    {"inputs": ["0" * 17 + "_"],
     "outputs": True,
     "reason": "username is allowed to have numbers and trailing underscore"},

    # call for length -three username with letter , number , underscore
    {"inputs": ["a_0"],
     "outputs": True,
     "reason": "username is allowed to have letters , numbers , underscore"},

    # call for length -three username with letter , number , starting underscore
    {"inputs": ["_a0"],
     "outputs": False,
     "reason": "can’t start with underscore"},

    # call for length -18+ username of letters and numbers
    {"inputs": ["a0" * 18],
     "outputs": False,
     "reason": "can’t have more than 18 characters"}
]
# a generic loop for test drivers
# the inputs are in a list , so it has to be modified
for test in test_suite:
    inputs = test["inputs"]
    result = is_valid_username(inputs[0])

    if result != test["outputs"]:
        print(f"Testing fault: is_valid_username () returned {result} on inputs {inputs}"
              f"\ntest reason: {test['reason']})\n")
