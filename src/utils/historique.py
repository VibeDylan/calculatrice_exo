# Créer une liste vide history dans le menu
def add_to_history(calcul:str, result:float, history:list):
	history.append({"calcul": calcul, "résultat": result})

def display_history(history):
	print("Opérations précédentes :")
	i = -1
	while i >= -3 and abs(i) <= len(history):
		if history[i]:
			print(f"{history[i]["calcul"]} = {history[i]["résultat"]}")
			i -= 1

# TESTS
# history = []
# add_to_history("5 + 2", 7, history)
# add_to_history("4 * 3", 12, history)
# add_to_history("6 / 2", 3, history)
# add_to_history("10 - 5", 5, history)
# display_history(history)