def divide_numbers(a, b):
	a = input("Entrez un premier nombre :")
	b = input("Entrez un autre nombre :")

	if b == 0:
		print("Un nombre ne peut être divisé par zéro")
	else:
		try:
			a = float(a)
			b = float(b)
		except:
			print("Veuillez entrer des nombres")

		result = a / b
		print(f"{a} / {b} = {result}")