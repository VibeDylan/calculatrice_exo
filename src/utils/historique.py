def add_to_history(calcul:str, result:float, history:list):
	history.append({"calcul": calcul, "résultat": result})

def display_history(history):
	print("Opérations précédentes :")
	i = -1
	while i >= -3 and abs(i) <= len(history):
		if history[i]:
			print(f"{history[i]["calcul"]} = {history[i]["résultat"]}")
			i -= 1