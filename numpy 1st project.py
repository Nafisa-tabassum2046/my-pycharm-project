import numpy as np

# var1 = np.array([(2,4,6),(1,3,5)])
# var2 = np.array([(2,4,6),(1,3,5)])
#
# print(var1+var2)

# var3 = np.array([2,4,6,8,0,3,4,5,5])
# var3 = np.array([(2,4,6,8),(2,4,6,8),(2,4,6,8),(2,4,6,8)])
# var3 = var3.reshape(4,4)
# print(var3)
# print(var3.itemsize)
# print(var3.sum())
# print(var3.dtype)
# print(var3.ndim)
# print(var3.size)
# print(var3.shape)

# var3 = np.array([(1,4,6,8),(2,45,6,8),(2,14,6,8),(2,24,6,8)])
# print(var3[0:,1])
# print(var3.max())
# print(var3.min())
# print(var3.sum())
#
# var4 = np.linspace(18,50,6)
# print(var4)


var5 = np.array([(2,4,6),(1,3,5)])
var6 = np.array([(12,14,16),(11,13,15)])

# print("Sum = ",var5+var6)
# print("Sub = ", var6 - var5)
# print("Mul = ", var5*var6)
# print("Div = ", var5/var6)
# print("Mol = ", var6 % var5)
# print(var6.ravel())
# print(var6.sum(axis=0))
# print(var6.sum(axis=1))
# print(np.sqrt(var5))
# print(np.std(var5))
print("EXP=",np.exp(var5))
print("LOG= ",np.log(var5))


