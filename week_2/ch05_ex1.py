blanket_cost = 8
pillow_cost = 12
cash = 50

# For each print function call:
# 1) how many arguments do you see?
# 2) How many expression operators do you see?
# 3) Why use str() in b)?
# 4) What will be "wrong" about c)?

# # (a)
# print("A blanket is", blanket_cost, "dollars")
#
# # (b)
# print("Four pillows will cost " + str(pillow_cost * 4) + ".")
# print("Four pillows will cost ", pillow_cost * 4, ".")

#
# (c)
print("One blanket and two pillows will cost $",
      blanket_cost + pillow_cost * 2, ". If I pay with $", cash,
      ", I will have $", (cash - (blanket_cost + pillow_cost * 2)),
      " left.")  # by default print(a, b) will print a space between these arguments

print("One blanket and two pillows will cost $",
      blanket_cost + pillow_cost * 2, ". If I pay with $", cash,
      ", I will have $", (cash - (blanket_cost + pillow_cost * 2)),
      " left.", sep="")

# starting python 3.6 f-string, formatted string
price = 1000
print("This computer costs me", "$", price, '.')
print("This computer costs me " + "$" + str(price) + '.')
print("This computer costs me ", "$", price, '.', sep="")

# f-string
print(f"This computer costs me ${price}.")


print(f"One blanket and two pillows will cost ${blanket_cost + pillow_cost * 2}. If I pay with ${cash}.")

