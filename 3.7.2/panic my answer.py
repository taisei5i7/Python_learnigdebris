phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

target = ["o", "n", "t", "a", "p"]
word = plist
found = []
for letter in word:
    if letter in target:
        if letter not in found:
            found.append(letter)
plist = found

found.remove("a") 
found.insert(2, " ")
found.insert(4, "a")

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
