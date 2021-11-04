print("enter your number: ")
mark = int(input())

if(80 <= mark <= 100):
    print("A+")
elif(70<= mark <=79):
    print("A")
elif(60<= mark <=69):
    print("A-")
elif(50<= mark <=59):
    print("B+")
elif(40<= mark <=49):
    print("B-")
elif(33<= mark <=39):
    print("C")
else:
    print("Fail")