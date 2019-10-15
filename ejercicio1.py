"""
	Ejercicios con Higher-order functions
	@royerjmasache
"""
def sum (a, b):
	return a + b
def product (a, b):
	return a * b
def trigger (f, a, b):
	print(f(a, b))
trigger(product, 1, 10)
