
# #
# a =  78
# if (a>33):
#     print("pass")
#
# else:
#     print("fail")
#
# # greater then less than number print
#
# a = 20
# b= 10
# if (a>b):
#     print("a is greater then b")
#
# else:
#     print("b is greater then a")
#
# # odd even number check:
#
# a = 10
#
# if(a%2==0):
#     print("even")
#
# else:
#     print("odd")
#

# 3 ta number ar maje ckeck

# a= 90
#
# if(a>80):
#     print("A+")
# elif(a>70):
#     print("A")
# elif(a>60):
#     print("A-")
# elif(a>50):
#     print("B")
# elif(a>40):
#     print("C")
# else:
#     print("fail")




# # 3 ta number ar maje greater middle less check

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

if(a>b and a>c):
    if(b>c):
        print("a is greater number")
        print("b is middle number")
        print("c is small number")

    else:
        print("a is greater number")
        print("c is middle number")
        print("b is small number")
elif(b>c and b>a):
    if(a>c):
        print("b is greater number")
        print("a is middle number")
        print("c is small number")


    else:

        print("b is greater number")
        print("c is middle number")
        print("a is small number")

else:
    if(a>b):
        print("c is greater number")
        print("a is middle number")
        print("b is small number")

    else:
        print("c is greater number")
        print("b is middle number")
        print("a is small number")



