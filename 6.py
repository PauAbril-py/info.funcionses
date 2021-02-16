def eliminat(llista):
	llista_final = []
	print(llista)
	for i in llista:
		for j in i:
			

		if i == 3 or i == 5 or i == 7:
			pass
		else:
			llista_final.append(i)
			print(llista_final)
	print()
	return(llista_final)

print(eliminat([15,1,23,54,3,2,4,2,5,5,7,97]))