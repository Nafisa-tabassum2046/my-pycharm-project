# num1= 1
# num2 = 2
# num3 = 3
# if num1 == num2:
#     print("Num1 is not equal Num2")
#     num3 = 0
# print(num3)


# # tot = 1010
# tot = int(input("Enter the total amount:"))
# bought_sale = True
#
# # bought_sale = bool(input("Enter the value: "))
# dis =0
# # or means if any one is ture he got the discount
# # if tot >= 1000 or bought_sale :
# #     thats and means two condition is true then he got the discount
# if tot >= 1000 and bought_sale:
#
#     dis =10
#
# total = tot - tot*dis/100
# discount = tot*dis/100
# print(discount)
# print(total)



#
# name = 'nafisa'
# age = int(input("Enter the age: "))
#
# status = 'Minor'
# if age >=65:
#     status = 'senior cititzen'
# elif age >= 18 and age <= 64:
#     status = 'Adult'
# print(status)


#
# tot = 1000.561
# dis = 0
# if tot >= 1000:
#     dis = 10
#
# else:
#     dis = 2
# total = tot - tot*dis/100
# print(tot*dis/100)
# print(total)
# print(tot)


# Str = 'It\'s python'
# if 'p' in Str:
#     Str = "It's a python"
#
# elif 'I' in Str:
#     Str.capitalize()
# print(Str)


# lst = ['python', 'c', 'c++','Jeva']
#
# print(lst)
# if 'python'  not in lst:
#     lst.append('python')
# elif 'Jeva' not in lst:
#     lst.append('Jeva')
# elif 'HTML' not in lst:
#     lst.append('HTML')
# else:
#     lst.append('JS')
# print(lst)


# total = 515
# discount =0
# if total > 500:
#     discount =10
# else:
#     pass
# total = total - total*discount/100
# print(total)


# total = 870
# discount = 0
# if total > 500:
#     discount = 5
# elif total > 100:
#     discount = 10
# else:
#     pass
# total = total - total*discount/100
# discount = total*discount/100
# # Discount = discount% OFF - discount
# print(discount)
# print(total)

#
# # 2nd exercise
#
# total = 870
# discount = 0
# dis="0% OFF"
# if total > 500 and total < 1000:
#     discount = 5
#     dis="5% OFF"
#
# elif total > 1000 :
#     discount = 10
#     dis = "10% OFF"
# else:
#     discount = 0
#     dis="0% OFF"
#
# discount=total*(discount/100)
# total=total-discount
# print(f"Discount : {dis} - {discount}")
# print(f"total : {total}")


total = 760
promo_iten_bought = True
discount = 0
dis = '0% OFF'
if total > 500:
    discount = 5
    dis = '5% OFF'
elif total > 1000 or promo_iten_bought:
    discount = 10
    dis ='10% OFF'
else:
    discount = 0
    dis= '0% OFF'

discount = total*discount/100
total = total - discount
print(f"Discount : {dis} -{discount}")
print(f"Total : {total}")