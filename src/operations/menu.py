from addition import addition
from soustraction import soustraction
from multiplication import multiply_numbers
from division import divide_numbers
from puissance import puissance
from racine_carree import racine_carree

def menu():
    continuer = True 
    while continuer:
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Puissance")
        print("6. Racine carrée")
        print("7. Historique")
        print("0. Quitter")

        operation = input("Choisissez une opération : ")

        match operation:
            case "0":
                print("Fin")
                break
            case "1" | "2" | "3" | "4" | "5":
     
                a = float(input("Entrez le premier nombre : "))
                b = float(input("Entrez le deuxième nombre : "))
   
                match operation:
                    case "1":
                        addition(a, b)
                    case "2":
                        soustraction(a, b)
                    case "3":
                        multiply_numbers(a, b)
                    case "4":
                        divide_numbers(a, b)
                    case "5":
                        print(f"Résultat : {puissance(a, b)}")

            case "6":
                a = float(input("Entrez le nombre : "))
                print(f"Résultat : {racine_carree(a)}")
            
            case "7":
                print("Historique")

            case _:
                print("Erreur")
                continue

        choix_continuer = input("Voulez-vous continuer ? (o/n) : ").lower()
        if choix_continuer != "o":
            print("Fin")
            break

if __name__ == "__main__":
    menu()