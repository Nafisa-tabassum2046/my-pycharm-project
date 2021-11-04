counts = dict()

line = input('Enter a line of text: ')


words = line.split()

print('words:', words)
print('counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('counts', counts)


# counts = {'chuck' : 1, 'fred' : 7, 'jeba' : 100}
# for key in counts:
#     print(key, counts[key])

jjj =  {'chuck' : 1, 'fred' : 7, 'jeba' : 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())