
#
# from random import randint
#
# # import random
# for i in range(1,9):
#     GuessNumber = int(input("Enter your GuessNumber Between 1 to 5 : "))
# # RandomNumber = random.randint(1,5)
# # RandomNumber = random.random() * 100
#     RandomNumber = randint(1,5)
#     if GuessNumber == RandomNumber:
#         print("you have won")
#     else:
#         print("you have lost")
#         print("Random number was : ", RandomNumber)


from random import randint
for i in range(1,11):
    guessnumber = int(input("Enter the guessnumber between 1 to 10: "))
    randomnumber = randint(1,10)

    if (guessnumber == randomnumber):
        print("win")
    else:
        print("loss")
        print("Random number is ", randomnumber)