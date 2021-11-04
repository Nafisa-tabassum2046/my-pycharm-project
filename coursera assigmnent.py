# print("I LOVE PYTHON VERY MUCH")
# # print("Hello World")

# x = 1 + 2 * 3 - 8 / 4
# print(x)

# astr = 'Hello Bob'
# istr = int(astr)
# print('First', istr)
# astr = '123'
# istr = int(astr)
# print('Second', istr)


# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.
#
#
# hrs = input("Enter Hours:")
# h = float(hrs)
# xx = input("Enter the Rate:")
# x = float(xx)
# if h <= 40:
#  	print( h  * x)
# elif h > 40:
# 	print(40* x + (h-40)*1.5*x)

# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit.
# For the test, enter a score of 0.85.

#
# s = float(input("Enter the Score: "))
#
# if s >= 0.9:
# 	print("A")
# elif s >=0.8:
# 	print("B")
# elif s >= 0.7:
# 	print("C")
# elif s >= 0.6:
# 	print("D")
# elif s < 0.6:
# 	print("F")
# else:
# 	print("Out of the range")


#
# x = 5
# print('Hello')
# def print_lyrics():
#     print("I'm a iumberjack, and I'm okky.")
#     print("I'm a iumberjack, and I'm okky.")
# print('yo')
# print_lyrics()
# x = x +2
# print(x)
#
# big = max('Hello world')
# print(big)

#
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time- and -a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value.Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.

# def computepay(h, r):
#     if h > 40:
#         p = 1.5 * r * (h - 40) + (40 * r)
#     else:
#         p = h * r
#     return p
#
#
# hrs = input("Enter Hours:")
# hr = float(hrs)
# rphrs = input("Enter rate per hour:")
# rphr = float(rphrs)
#
# p = computepay(hr, rphr)
# print(p)


# a = -1
# print('Before', a)
# for b in [9,41,12,3,74,15]:
#     if b > a:
#         a = b
#     print(a,b)
# print('After ', a)

# zork = 0
# print('Before', zork)
# for thing in [9,41,12,3,74,15]:
#     zork = zork+1
#     print(zork,thing)
# print("After", zork)

# zork = 0
# print('Before', zork)
# for thing in [9,41,12,3,74,15]:
#     zork = zork+thing
#     print(zork,thing)
# print("After", zork)

# count = 0
# sum = 0
# print('Before', count,sum)
# for value in [9,41,12,3,74,15]:
#     count = count+1
#     sum = sum +value
#     print(count,sum,value)
# print("After", count,sum,sum/count)



# print('Before')
# for value in [9,41,12,3,74,15]:
#     if value>20:
#         print('large number', value)
# print('After')

# n = 0
# while n > 0 :
#     print('Lather')
#     print('Rinse')
# print('Dry off!')

# # Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# # Once 'done' is entered, print out the largest and smallest of the numbers.
# # If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# # Enter 7, 2, bob, 10, and 4 and match the output below.
#
#
# #
# numb = 0
# largest = -1
# smallest = None
# while True:
#     numb = input("Enter a number: ")
#     if numb == "done" :
#         break
#     try :
#         numb = int(numb)
#     except :
#         print('Invalid input')
#     if smallest is None :
#         smallest = numb
#     elif numb < smallest :
#         smallest = numb
#     elif numb > largest :
#         largest = numb
# print("Maximum is", largest)
# print("Minimum is", smallest)

#
# num = 0
# smallest = None
# largest = -1
# while True:
#     numb = input("Enter the number: ")
#     if numb == "done" :
#         break
#     try:
#         num = int(num)
#     except:
#         print('Invalid input')
#     if smallest is None:
#         smallest = num
#     elif num < smallest:
#         smallest = num
#     elif num > largest:
#         largest = num
# print("Maximun is: ", largest)
# print("Minimum is: ", smallest)
# # str1 = "Hello"
# str2 = 'there'
# bob = str1 + str2
# print(bob)
#
# x = '40'
# y = int(x) + 2
# print(y)

# x = 'From marquard@uct.ac.za'
# print(x[14:18])

# print(len('banana')*7)

# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])

# str  = 'X-DSPAM-Confidence: 0.8475'
#
# ipos = str.find(':')
# piece = str[ipos+2:]
# value = float(piece)
# print(value)
# print(value + 42.0)


# ab =  'with three words'
# stuff = ab.split()
# print(stuff)
# print(len(stuff))
# print(stuff[0])
#
# print()
#
# for w in stuff :
#     print(w)


