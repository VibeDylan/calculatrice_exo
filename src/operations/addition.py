def addition():
    a = input("Entrez le premier nombre : ")
    b = input("Entrez le second nombre : ")
    
    try: 
        a = float(a)
        b = float(b)
    except ValueError:
        print("Erreur: Vous devez entrer uniquement des nombres.")
        return

    result = a + b
    print(f"Résultat : {result}")