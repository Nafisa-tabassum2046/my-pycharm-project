def encrypt(text, c):
    result = ""


    for i in range(len(text)):
        char = text[i]


        if (char.isupper()):
            result += chr((ord(char) + c - 65) % 26 + 65)


        else:
            result += chr((ord(char) + c - 97) % 26 + 97)

    return result



text = "abcd xyz"
c = 4
print("Text  : " + text)

print("Shift : " + str(c))
print("Cipher: " + encrypt(text, c))