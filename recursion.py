
def isPalindrome(word):
	if len(word) <= 1:
		print("isPalindrome")
		return True
	elif word[0] == word[-1]:
		isPalindrome(word[1:-1])
	else:
		print("notPalindrome")
		return False

# def isPalindrome(s):
#     """Return True if s is a palindrome and False otherwise"""
#     if len(s) <=1:
#     		return True
#     else:
#     		return s[0] == s[-1] and isPalindrome(s[1:-1])

print(isPalindrome('aabaa'))


def fib(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print(fib(24))
