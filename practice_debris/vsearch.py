def search_for_vowels(word):
    """入力された単語内の母音を表示する"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
	    print(vowel)
