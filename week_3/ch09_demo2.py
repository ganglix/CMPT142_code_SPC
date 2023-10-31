# while vs. for
# In this demonstration, we’ll see a situation where using a
# while-loop is preferable to using a for-loop.

# password example

# initiate param
passcode = "cmpt142"
max_attempts = 5

# ask user to input passcode
# for the first time, ask
user_input = input("please enter your passcode: ")
count = 1  # 0  # use count to track number of inputs

while (user_input != passcode) and (count < max_attempts):
    # keep asking
    user_input = input("please enter your passcode: ")
    count += 1

# when while loop is done, (user_input != passcode) and (count < max_attempts) is False

# print message to user

# #there are two outcomes,
# (user_input != passcode) is False, user got the right passcode
if user_input == passcode:
    print(f"passcode is correct, {count} attempt(s) made")
else:
    print(f"maximum number of trial reached; you are locked out. Forgot your password?")




