phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)


word = plist[1:3] + plist[5:3:-1] + plist[7:5:-1]

new_phrase = ''.join(word)

print(plist)
print(new_phrase)




