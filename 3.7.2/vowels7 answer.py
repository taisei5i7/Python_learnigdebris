vowels = set('aeiou')
words = input("Please input words, and I look for vowels in the words.")

i = vowels.intersection(set(words))

for vowels in i:
    print(vowels)
