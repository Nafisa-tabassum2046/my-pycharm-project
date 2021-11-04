# fname = input("Enter file name: ")
# a = open("words.txt")
# # content = a.read()
# # print(content.upper())
# for b in a:
#     b = b.rstrip()
#     print(b.upper())
# 
# a.close()
# #
# # Write a program that prompts for a file name, then opens that file and reads through the file,
# # looking for lines of the form:
# # X-DSPAM-Confidence:    0.8475
# # Count these lines and extract the floating point values from each of the lines and compute
# # the average of those values and produce an output as shown below. Do not use the sum() function
# # or a variable named sum in your solution.
# # You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing
# # below enter mbox-short.txt as the file name.
# #
# # Use the file name mbox-short.txt as the file name
# #

# fname = raw_input("Enter file name: ")
# fh = open('mbox-short.txt')
# count = 0
# total = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     t=line.find("0")
#     number= float(line[t:])
#     count = count + 1
#     total = total + number
#
# average = total/count
# print ("Average spam confidence:",average)


# abc =  'with three words'
# stuff = abc.split()
# # print(stuff)
# # print(len(stuff))
# # print(stuff[0])
# for w in stuff:
#     print(w)
#
#
# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list
# and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

#
# fname = input("Enter file name: ")
# fh = open("romeo.txt")
#
# lst = list.()
# for line in fh:
#     print(line.rstrip())


fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()                       # list for the desired output
for line in fh:                    # to read every line of file romeo.txt
    word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:           # check every element in word
        if element in lst:         # if element is repeated
            continue               # do nothing
        else :                     # else if element is not in the list
            lst.append(element)    # append
lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print (lst)




# fname = input("Enter file name: ")
# fh = open('romeo.txt')
# lst = list()
# for line in fh:
#     line = line.rstrip()
#     line = line.split()
#     for i in line:  # observe indentation here
#         if i not in lst:
#             lst.append(i)
#
# lst.sort()  # observe indentation here.  this is where i made mistakes..
# print(lst)