# Define a Python function called format_price that:
# (a) Has two integer parameters, indicating the cost in dollars
# and cents of an item
# (b) Returns a single string in the format "$D.C".
# (c) Example: if called with arguments 9 and 99, the function
# should return the string $9.99

def format_price(dollar, cent):  # with docstring: functionality(summary), parameter, return
    """
    This function takes two integers representing dollar and cent amount
    and returns the price in a format of $dollar.cents
    :param dollar: int, number of dollar amount
    :param cent: int, number of cent amount
    :return: str, formatted price
    """
    # formatted = "$" + str(dollar) + "." + str(cent)
    formatted = f"${dollar}.{cent}"
    return formatted

print( format_price(9, 99))
help(format_price)

# def format_price_no_args():
#     dollar = input("type the dollar amount") # input() always return a str
#     cent = input("type the cent amount")
#     formatted = "$"+ dollar + "." + cent
#     print(formatted)
#
# format_price_no_args()