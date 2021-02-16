import math

def area_circulo(radio):
	area = math.pi * radio ** 2
	return round(area, 2)

print(area_circulo(int(input('dime el radio de tu circulo:\t'))))