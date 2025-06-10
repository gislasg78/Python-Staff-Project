import re

def is_palindrome(phrase):
	forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
	backwards = forwards[::-1]

	return forwards == backwards


print("Program that checks if a string is palindromic.")

phrase = input("Enter a string of characters: ")
result = is_palindrome(phrase)

print("")
print(f"String entered: [{phrase}].")
print(f"Is the string a palindrome? : [{result}].")
