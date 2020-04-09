vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Please input words, and I look for vowels in the words.")

found = {}


for letter in word:
    if letter in vowels:
        found[letter] += 1
        
for k, v in sorted(found.items()):
    print(k, 'appered', v, 'times')
