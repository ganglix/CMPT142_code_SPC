# # Flowtrace with function
#
# status = "Healthy"
# def set_status(s):
#     # global status  # declares that status is the one from global scope
#     #                # DONT use this! Very bad.
#     status = s
#
# set_status("Poisoned")
# print(status)
#
# """
# status = "Healthy"
# set_status("Poisoned")
# ----------------inside the function, not visible from outside-------
# s = "Poisoned"
# status = "Poisoned"
# --------------------------------------------------------------------
# print("Healthy")
# """
#
# #~~(things I want to mention: scope, return, dangerous thing to do, inplace)

status = "Healthy"
def set_status(s):
    i_am_not_status = s
    return i_am_not_status

# returned_by_fun = set_status("Poisoned")
# status = returned_by_fun

status = set_status("Poisoned")

print(status)


##### global var can be SEEN from inside the func but can not be changed

another_par = 10
def add_fun(par1, par3):
    # do some calculation
    res = par1 + par3 + another_par   # par1, par3, res are local var
    return res
print(add_fun(1,2))
"""
another_par = 10
add_func(1,2)
---------------inside the function--------
par1 = 1
par3 = 2
res = 1 + 2 + 10 (another_par can not be found inside, continue to search from global)
return 13
-----------------------------------------
print(13)
"""