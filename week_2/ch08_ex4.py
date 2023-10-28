# Given pre-defined variables:
n_fins # number of animal ’s fins (integer)
n_wings # number of animal ’s wings (integer)
n_stripes # number of animal ’s stripes (integer)
n_spots # number of animal ’s spots (integer)
has_tail # whether animal has tail (Boolean)

# Write Python expressions to determine if an animal:
# (a) does not have wings


# (b) has more stripes than spots or has exactly five spots


# (c) has five or less stripes and does not have more stripes than spots


# (d) does not have fins or spots


# (e) has a tail or has exactly two fins and two wings





#~~~~~~~~~~~~~~~~~~~~~~



# alternative solutions
# Part (a)
not n_wings > 0
# Part (b)
n_stripes > n_spots or n_spots == 5
# Part (c)
n_stripes <= 5 and not n_stripes > n_spots
# Part (d)
not(n_fins > 0 or n_spots > 0)
# Part (e)
has_tail or (n_fins == 2 and n_wings == 2)