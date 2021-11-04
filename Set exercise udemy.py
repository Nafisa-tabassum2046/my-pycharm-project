# sts = {1,12,3,4,2,2,2,3,4,5,4,44,'python'}
# ss = set({12, 3, 4, 4, 3, 3, 23, 232, 3, 23})
# print(sts)
# print(ss)

# # Make sure to print the LIST after removing the duplicates in it
# lst = [ 0, 12, 3 ,4 ,12, 4, 12, 34, 12, 33, 7, 8 , 2, 90, 23, 45, 12, 33]
# lst = set(lst)
# l = list(lst)
# print(l)

# st1, st2 = {10,20,30},{90,100}
# st1.add(200)
# st1.remove(10)
# st1.discard(19)
# # If this value is not present or present not error using this function
# st1.update(st2)
# print(st1)

# st = { 1, 2, 4, 6, 8, 9, 12, 16, 15}
# st.remove(1)
# st.remove(9)
# st.remove(15)
# st.add(10)
# st.add(14)
# st.add(18)
# st.add(20)
# print(st)


# # Mathmatical
#
# st1, st2 = {1,2,3,4,5,6,9},{1,2,3,4,5,6,6,7,8}
# # union
# print(st1 | st2)
# #Intersection
# print(st1& st2)
# # Difference
# print(st1 - st2)
# print(st2 - st1)
# #  Syemetric Difference
# print(st1 ^ st2)

# discount  = {'ProductA','ProductC','ProductY','ProductX','ProductL'}
# whose_coupon = {'ProductY','ProductM','ProductR','ProductC','ProductE'}
# print(discount & whose_coupon)