vowels = ['a', 'i', 'u', 'e', 'o']
words = "Hello World, Good Night World."
found = []
for letter in words:
    if letter in vowels:
        if letter not in found:
             found.append(letter)
for vowels in found:
    print(vowels)
