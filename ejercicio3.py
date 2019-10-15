"""
	Ejercicios con Higher-order functions
	@royerjmasache
"""
data = [1, 2, 10, 11, 12, 13]
result = filter(lambda a: a % 2 == 0, data)
print(result)
print(list(result))
