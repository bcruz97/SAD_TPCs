A = ["1P", "1C", "1O", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE"]

deck = [][]

for i in A:
	print(i)
	for r in deck[r][c]:
		for c in deck[r][c]:
			if A[i] in deck[r][c]:
				print("Já existe")
			elif A[i] not in deck[r][c]:
				print("Não existe")
				