# n = input("Enter a test of numbers: ")
# list = n.split()
#
# sum  = 0
#
# for i in list:
#     sum = sum + int(i)
# print(sum)

NumOfWord = 0
NumOfDigit = 0
NumOfLetter = 0

text = input("Enter the text : ")

for x in text:
    x = x.lower()
    if x >= 'a' and x<='z':
        NumOfLetter = NumOfLetter +1
    elif x >= '0' and x<='9':
        NumOfDigit = NumOfDigit +1
    elif x == ' ':
        NumOfWord = NumOfWord +1

print("Number of Letter: ", NumOfLetter)
print("Number of Digit: ",NumOfDigit)
print("NUmber od Word: ",NumOfWord + 1)