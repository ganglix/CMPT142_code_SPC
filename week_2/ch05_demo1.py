# In this demonstration we will show how to use the console
# display on console

# print("hello world")
#
# returned_value = print("hello world")
#
# print("returned_value:", returned_value)


# input function to obtain answers to simple questions and
# # example 1

# convert the input to the desired data type.
# user_input = float(input("please type a number:"))  # input() always return a string
# print("Your number is:", user_input)
# print("the square root of your number is", user_input**(1/2))


# example 2

# title
print("If I Were Super Wealthy Simulator")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()   # prints an empty newline

# prompt user for their name
name = input("What is your name?: ")
print("Hello", name, "! We're going to gather some data on you and predict your life")
print()

# prompt user for some more data about themselves
animal = input("What is your favourite animal?: ")
number = int(input("What is your favourite number (please give an integer)?"))
float_number = float(input("What is another number you like (this time, give a float number)?"))
print()

# print out the scenario
print("Hello", name, ". If you were super wealthy, my guess is you would buy", number, animal)
print("You would make sure that they live in", float_number, "degree celsius weather.")
print("Should we be concerned? Possibly")
