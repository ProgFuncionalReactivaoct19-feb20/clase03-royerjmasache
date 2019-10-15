"""
	Ejercicios con Higher-order functions
	@royerjmasache
"""
data = [18, 19, 20, 10, 11, 12]
result = filter(lambda a: a >= 18 or a <= 10, data)
print(result)
print(list(result))
