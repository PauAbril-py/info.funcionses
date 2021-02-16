def separar(lista):
	pares = []
	impares = []
	lista.sort()
	for i in lista:
		if i % 2 == 0:
			pares.append(i)
		else:
			impares.append(i)
	return pares, impares

l=[5,54,5,97,564,8,1,97,64,948,3,45,54]

print(separar(l))