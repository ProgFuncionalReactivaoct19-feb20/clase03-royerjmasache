"""
	Ejercicios con Higher-order functions
	@royerjmasache
"""
# Creación de lista
capitals = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala",  "Portoviejo", "Macas"]
# Uso de función anónima que captura el tamaño de los elementos y evalúa
function = filter(lambda a: len(a) % 2 == 0, capitals)
# Presentación de resultados
print(list(function))

	
