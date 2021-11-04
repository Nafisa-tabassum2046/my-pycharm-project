# import scipy as sp
# import numpy as np
# from scipy import fft
#
# var1 = np.array(([2,4,6],[1,3,5]))
#
# trans1 =sp.fft(var1)
#
# print(trans1)

import scipy as sp
import numpy as np
from scipy import linalg

var2 = np.array(([1,3],[2,4]))
var3 = np.array(([5,9],[6,8]))

# function1 = sp.linalg.solve(var2,var3)
function2=sp.linalg.inv(var2)
print(function2)
