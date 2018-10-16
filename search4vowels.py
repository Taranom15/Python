###   1st V not using "set"
#vowels = ['a', 'e', 'i', 'o', 'u']
#word = input("Provide a word to search for vowels: ")
#found = []
#for letter in word:
#	if letter in vowels:
#		if letter not in found:
#			found.append(letter)
#for vowel in found:
#	print(vowel)


vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))
for vowel in found:
	print(vowel)



### Function V of the code 
#def search4letters(phrase:str, letters:str='aeiou') -> set:
#	return set(letters).intersection(set(phrase))