def multiply_numbers(a, b):
	a = input("Entrez un premier nombre :")
	b = input("Entrez un autre nombre :")

	try:
		a = float(a)
		b = float(b)
	except:
		print("Veuillez entrer des nombres")

	result = a * b
	print(f"{a} x {b} = {result}")