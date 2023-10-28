# creating functions: parameter, arguments, return

def add_fun(par1, par3):
    # do some calculation
    res = par1 + par3   # par1, par3, res are local var
    return res

added = add_fun(1,2)
print(added)

# added = add_fun(1,2)
#--------------local, not visible from outside-------------------------
# under the hood (inside the function)
# par1 = 1
# par3 = 2
# res = 1 + 2
# return 3
# -----------------local-----------------
# added = 3
# print(3)


