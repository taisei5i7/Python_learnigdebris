vowels = set('aeiou')
words = input("Please input words, and I look for vowels in the words.")

i = vowels.intersection(set(words))
i_list = sorted(list(i))

for vowels in i_list:
    print(vowels)
