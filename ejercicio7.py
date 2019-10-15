"""
	Ejercicios con Higher-order functions
	@royerjmasache
"""
def plate (a):
	# Lista para cumplir la condición
	letters = ["l", "p", "e", "a", "i"]
	# Ciclo repetitivo para recorrer la lista
	if a[0] in letters:
		return True
	else:
		return False
# Lista que contiene las placas de los vehículos
plates = ["lba-001", "gma-002", "azx-003", "ess-004", "oro-100", "mab-001", "iaj-002"]
# Filtrado de resultados
result = filter(plate, plates)
# Presentación de  resultadoss
print(list(result))
