# Python program to sort the words in lexicographical

def sortLexo(my_string):
	words = my_string.split()
	words.sort()
	for i in words:
		print( i )
if __name__ == '__main__':
	my_string = input("Enter a sentence:")
	sortLexo(my_string)
