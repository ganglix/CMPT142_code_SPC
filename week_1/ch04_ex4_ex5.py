#      [           ]
#    _______
#    7654321
#    0123456

s = "Fiction"
print(
    s[1:3],

    s[-4:10],   # when you have mixture of +/- indices you only look at the position
                # [wrong]-4 -3 -2 -1, 0, 1...6,    ! 7 8, 9

    s[0:len(s):2],

    s[0:len(s):-1],  # returns "", slice indices do not make sense, return ""

    s[len(s):-8:-1], # right(out of range) to left(out of range)

    sep="\n"  # newline, meaning print a newline between the items printed
)


#    ___________
#    BA987654321
#    0123456789A        note: A is 10    B is 11
s = "Green Arrow"

# (a) the first five characters of s, i.e. "Green"


# (b) the fourth to eighth characters of s inclusive, i.e. "en Ar"


# (c) the last five characters of s, i.e. "Arrow"


# (d) every third character of s from the second character
# onwards, i.e. "rnrw"


# (e) the last five characters of s in reverse, i.e. "worrA".
