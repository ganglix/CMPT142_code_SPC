# How to import a module
# import math

# print(
#     math.log(1),  # math.log() is ln
#     math.log(math.e),
#     math.sin(math.pi/2), # math.sin expect rads
#     math.sin(math.radians(90)),
#     sep="\n"
# )

import math as m
m.sin(m.radians(90))

# real world engineering (my experience)
# scientific computing, maxtrix, array
import numpy as np
arr = np.linspace(0, 10, 100) # array of 100 data points between 0 and 10(inclusive)
# print(arr)

# visualization
import matplotlib.pyplot as plt
plt.plot(arr, np.sin(arr))
plt.show()
# plt.savefig("name.tiff", dpi=1200)

# import pandas as pd
# df = pd.read_excel("your spreadsheet.xlsx")


# if you want just sin from math
from math import sin
print(sin(0))

from math import *  # never do this!
# math.pi -> pi
