
nbr1 = float(input("Entrez le premier nombre : "))
nbr2 = float(input("Entrez le deuxième nombre : "))


operation = input("Choisissez une opération (+, -, *, /) : ")
if operation == "+":
    resultat = nbr1 + nbr2
    print("Le résultat de l'addition est :", resultat)
elif operation == "-":
    resultat = nbr1 - nbr2
    print("Le résultat de la soustraction est :", resultat)
elif operation == "*":
    resultat = nbr1 * nbr2
    print("Le résultat de la multiplication est :", resultat)
elif operation == "/":    # Vérifier la division par zéro
    if nbr2 != 0:
        resultat = nbr1 / nbr2
        print("Le résultat de la division est :", resultat)
    else:
        print("Erreur : Division par zéro.")
else:
    print("Opération non valide. Veuillez choisir parmi +, -, *, /.")
