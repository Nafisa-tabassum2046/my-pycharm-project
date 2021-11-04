# i =0
# while i != 4:
#     print('i')
#     i = i +1
#
# num = 0
# i = 0
# while i<4:
#     num = int(input("Number_"))
#     if num == 0:
#         print("Square: 0")
#         i += 1
#         continue
#     if num == 1:
#         print("Program Exit")
#         break
#     sq = str(num*num)
#     print("Square: " +sq)
#
#     # i = i +1
#     i +=1
# else:
#     print("done")


# c = 4
# e = 7
# while c != 7 or e > 4 :
#   print('loop')
#   c += 1
#   e -= 1
# l = 45
# while l <= 100 :
#   print('loop')
#   l *= 1.25

### Do not use the list.clear() method
lst = [ 1, 4, 56, 2, 4 , 12,  6, 89 ,11, 0]
# print(len(lst))

while len(lst) > 0:
    p = lst.pop()
print(lst)

