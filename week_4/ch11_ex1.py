"""
Algorithm:
sum up all the numbers
divide the sum with the number of numbers
count how many numbers are above the average

Pseudocode:
create function: aboveAverage
input: a list of numbers
output: a count of numbers above average

initiate sum = 0
for number in the list
    add that number to sum

set the average as the sum divided by length of the list
initiate count = 0
for number in the list
    if number is above the average
       add one to count
return count
"""


def aboveAverage(lis):
    """
    Calculate the number count above the average of the input list
    :param lis: a list of numbers
    :return: a count of numbers above average
    """
    # sum up all the numbers
    sum = 0
    for number in lis:
        sum = sum + number

    # divide the sum with the number of numbers
    avg = sum / len(lis)

    # count how many numbers are above the average
    count = 0
    for number in lis:
        if number > avg:
            count += 1

    return count
