# Write Python code which asks a user to input a string from
# the console until it is identical to pre-defined string passcode.
# When this occurs, print the number of attempts made to
# enter the correct string. e.g. "3 attempt(s) made."

passcode = "cmpt142"

# for the first time, ask
user_input = input("please enter your passcode: ")
count = 1  # 0  # use count to track number of inputs

while user_input != passcode:
    # keep asking
    user_input = input("please enter your passcode: ")
    count += 1

# User got the passcode correct
print(f"{count} attempt(s) made")