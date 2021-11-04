# fname = input("Enter file name: ")
# fhand = open("mbox-short.txt")
# count = 0
# for line in fhand:
#     line = line.rstrip()
#     if line == "":
#         continue
#
#     words = line.split()
#     if words[0] != "From":
#         continue
#
#     print(words[1])
#     count = count + 1
#
# print("There were", count, "lines in the file with From as the first word")

# fname = input("Enter file name: ")
# fh = open("mbox-short.txt")
# count = 0
# for line in fh:
#     if not line.startswith('From'):
#         continue
#     if line.startswith('From:'):
#         continue
#     else:
#         line = line.split()
#         line = line[1]
#         print(line)
#     count += 1
# print("There were",count,"lines in the file with From as the first word")

#
# jeba = open("mbox-short.txt")
# count =0
# for han in jeba:
#     han = han.rstrip()
#     wrds = han.split()
#     if len(wrds)< 1:
#         continue
#     if wrds[0] != 'From':
#         continue
#     print(wrds[1])
#     count = count + 1
# print(count)


# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.' \
# ' After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#
# fname =  input("Enter the file: ")
# if len(fname) < 1:
#     name = "mbox-short.txt"
# hand  =  open(fname)
#



# fname = input("Enter file:")
# if len(fname) < 1 :
#     name = "mbox-short.txt"
# hand = open(fname)
#
# lst = list()
#
# for line in hand:
#     if not line.startswith("From:"):
#         continue
#     line = line.split()
#     lst.append(line[1])
#
# counts = dict()
# for word in lst:
#     counts[word] = counts.get(word,0) + 1
#
# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigcount = count
#         bigword = word
#
# print (bigword,bigcount)


#
# name = input("Enter file:")
# fh = open(name)
#
# master = dict()
#
# for lines in fh:
#     if not 'From ' in lines:
#         continue
#     else:
#         recipient = lines.split()
#         emails = recipient[1]
#         master[emails] = master.get(emails, 0) + 1
#
# bigcount = None
# bigword = None
#
# for word,totalcount in master.items():
#     if bigcount is None or totalcount > bigcount:
#         bigword = word
#         bigcount = totalcount
#
# print(bigword, bigcount)
#
#
# name = input("Enter file:")
# if len(name) < 1 :
# name = "mbox-short.txt"
# try:
# handle = open(name)
# except:
# print('Cannot open file', name)
# quit()
# ddd = dict()
# for line in handle:
# if line.startswith('From:'): continue
# if not line.startswith('From'): continue
# words = line.split()
# w = words[1]
# ddd[w] = ddd.get(w, 0) + 1
#
# bigcount = None
# bigword = None
#
# for k,v in ddd.items(): #k is word, v is its count
# if bigcount is None or v > bigcount:
# bigword = k
# bigcount = v
#
# print(bigword, bigcount)
#
#
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# words = list()
# count = dict()
#
# for line in handle:
# line = line.rstrip()
# if line.startswith('From ') :
# line = line.split()
# words.append(line[1])
#
# for w in words:
# count[w]= count.get(w,0)+1
#
# bigcount =None
# bigword = None
# for key,values in count.items():
# if bigcount is None or values>bigcount:
# bigcount = values
# bigword = key
# print(bigword,bigcount)






# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# lst = list()
#
# for line in handle:
#     if not line.startswith("From:"):
#         continue
#     line = line.split()
#     lst.append(line[1])




# name = input("Enter the file: ")
# # if len(name) <1:
# #     name = "mbox-short.txt"
#
# handle = open(name)
# d =dict()
#
# for line in handle:
#     if not line.startswith("From "):
#         continue
#
#     else:
#         line = line.split()
#         line = line[5]
#         line = line[0:2]
#         d[line] = d.get(line, 0) + 1
#
# lst = list()
# for value, count in d.items():
#     lst.append((value, count))
#
# lst.sort()
# for value, count in lst:
#     print(value, count)


# name = input("Enter file:")
# # if len(name) < 1 :
# #     name = "mbox-short.txt"
# handle = open(name)
# d=dict()
# for line in handle:
#     if not line.startswith("From "):
#         continue
#     else:
#         line=line.split()
#         line=line[5]
#         line=line[0:2]
#         d[line]=d.get(line,0)+1
#
# lst=list()
# for value,count in d.items():
#     lst.append((value,count))
#
# lst.sort()
# for value,count in lst:
#     print (value,count)

# print('Learn\n Python')





# Udmey
# Master
# Master has tried
# beginner has failed
# failed
# more

# Str = '''Master has failed more,
# than the beginner has tried'''
#
# print( Str[0:6])
# print(Str[0:11] + Str[46:])
# print( Str[-18:-10] + Str[6:17])
# print( Str[11:17])
# print( Str[18:22])


# Udmey
# Master
# Master has tried
# beginner has failed
# failed
# more



# Str = '''Master has failed more,
# than the beginner has tried'''
# print(Str[0:6])
# print(Str[0:10]+Str[-6:])
# print(Str[-18:-9]+Str[7:17])
# print(Str[11:17])
# print(Str[18:22])

# print(chr(88))
# print(ord('Z'))

#
#
# Str = 'Life is not a race or game, it is lie'
# print(Str[14:18].capitalize())
# print(Str[22:26].upper())
# print(Str[0:4].swapcase())
# print(Str[28:].capitalize())



# Str = 'Life is not a race or game, it is lie'
# print(Str[14:18].capitalize())
# print(Str[22:26].upper())
# print(Str[0:4].swapcase())
# print(Str[28:].capitalize())
# print(Str.rstrip())


# # Start of by creating variables
# num1 = 112
# num2 = 20.45
# num3 = 7 + 3j
# num4 = 0
# sum = num1 + num2 + num3
# print(sum)
# print(num2, num3)
# num3, num4 = 0, 7 + 3j
# print(num4)
#
# # temp = num3
# # num3 = num4
# # num4 = temp
# # print(num4)
# print(round(num1 % num2, 2))
# print(num4.imag, 2)




#
# # Start of by creating variables
# num1 = 112
# num2 = 20.45
# num3 = 7 + 3j
# sum = num1 + num2 + num3
# print(sum)
# num4 = num2*num3
# print(num4)
# print(round(num1 % num2, 2))
# print(round(num4.imag, 2))

# num1 = 8
# num2 = 10
# print(bool(num1<= num2))
# print(bool(num2 == num1))

# lst1 = ['red', 'green', 'blue']
# lst2 = ['white', 'black']
# print([lst1, lst2])

# # Create the list
# clr1 = [ 'Red', 'Green', 'Violet']
# clr2 = [ 'Blue', 'Black', 'Orange']
# clr3 = [ 'Yellow', 'White']
# num = (*clr1 , *clr2 , *clr3)
# print(num)







# #
# # Practice
# odd = [1,3,5,7]
# even = [0,2,4,6]
# num = [*odd, *even]
# # num.sort()
# # num.append(9)
# del(num[5])
# num.remove(5)
# num.pop(5)
# num.reverse()
# print(num)
# print(num.index(3))
# print(num.count(3))
# print(num.clear())
# num = num+[1]
# print(num)
# print(len(num))
# print(bool(5 not in num))

# list excirsice

# lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# lst.remove("cherry")
# lst.remove("melon")
# lst.remove("kiwi")
# lst.append("guava")
# lst.append("peach")
# lst.reverse()
# print(lst)
# print(len(lst))

