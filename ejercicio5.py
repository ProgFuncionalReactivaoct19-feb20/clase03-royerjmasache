"""
	Ejercicios con Higher-orden functions
	@royerjmasache
"""
def vocal (a):
	vowels  = ["a", "e", "i", "o", "u"]
	if a in vowels:
		return True
	else:
		return False
data = ["e", "c", "u", "a", "d", "o", "r"]
result = filter(vocal, data)
print(list(result))
