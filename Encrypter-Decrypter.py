import random
import string

text = input("Enter String ")
choice = input("1. for encryption\n2. for decryption ")

if (choice == "1"):
    words = text.split(" ")
    newtext=""

    for word in words:
        
        if (len(word)>=3):
            r1 = random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
            r2 = random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
            nword = r1 + word[len(word)-1] + word[:len(word)-1] + r2 +" "
        else:
            nword = word[::-1] + " "

        newtext += nword 
        
    print(newtext)

else:
    words = text.split(" ")
    newtext=""

    for word in words:
        
        if (len(word)>=3):
            nword = word[3:-3]
            nword = nword[1:] + nword[0]
        else:
            nword = word[::-1]

        newtext += nword + " "
        
    print(newtext)
