a = False
b = False
c = True

print(
    not b,
    c and b,
    a or b,
    not b and c,
    b or not c,
    b and c or a,
    c or b and a  # do and first then or  # NAO, use redundant () to ensure and then or
)

