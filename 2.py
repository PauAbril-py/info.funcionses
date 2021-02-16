def relacion(a, b):
	if a > b: return 1
	if a < b: return -1
	if a == b: return 0

print(relacion(
	input('dime el primer numero'),
	input('dime el segundo numero')))