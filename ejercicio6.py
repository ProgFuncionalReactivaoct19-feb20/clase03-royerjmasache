"""
	Ejercicios con Higher-orden functions
	@royerjmasache
	* Dado un conjunto de palabras filtrar todas aquellas que sean palíndromas
"""
# Creación de lista
words = ["oro", "país", "ojo","oso", "radar", "sol", "seres"]
# Uso de función anónima para revertir los elementos y comparar
result = filter(lambda a: a == "".join(reversed(a)), words)
# Presentación de resultados
print(list(result))
