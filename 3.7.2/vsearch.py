def search4vowels():
	vowels = set('aeiou')
	word = input("Please input words, and I look for vowels in the words.")
	found = vowels.intersection(set(word))
	for vowel in found:
		print(vowel)
