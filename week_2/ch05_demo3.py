# This demonstration shows you how to call methods on string objects.


# initialize some variables to play with
url = "www.engineering.usask.ca"

# find the location of the first period in the url
location = url.find(".")
print(location)
help(url.find)

# find the location of the second period
print(   url.find(".", url.find(".") +1, len(url) )  )

# similar to .find(), we have .index()
print(url.find("z"))  # return -1
# print(url.index("z"))  # cause an error


# count the number of periods in the url
# (function not covered in readings)
print(url.count("."))
#

# remove white space
s = "  CMPT 142  "
print(s.rstrip())    # removes trailing white space, \n, \r
print(s.lstrip())
print(s.strip())

# what if we want to remove all spaces

print(s.replace(" ", ""))  # replace " " by empty string

# count the number of characters in the url after removing "www."
# (gotta be careful - don’t just assume a function does what you think!)
print(url.lstrip("www.")) # this removes "garbage chars" w and .
print(url.lstrip("ww."))  # this removes "garbage chars" w and .
print(url.lstrip("w."))   # this removes "garbage chars" w and .
help(url.lstrip)

# # more methods:
print(url.upper())
# .lower()
# url.title()


# when are they useful
# immutable, they create a copy


# how do I know what kind of methods are out there? How do I know the syntax/usage?

print(dir(s))