
grille_tarifaire = {
    'A': {'taux_horaire': 200, 'prime': 1000, 'heures_prime': 20},
    'B': {'taux_horaire': 150, 'prime': 800, 'heures_prime': 20},
    'C': {'taux_horaire': 120, 'prime': 500, 'heures_prime': 15},
    'D': {'taux_horaire': 100, 'prime': 350, 'heures_prime': 15},
    'E': {'taux_horaire': 80, 'prime': 100, 'heures_prime': 10}
}

grade = input("Entrez le grade de l'employé (A, B, C, D, E) : ")

if grade not in grille_tarifaire:
    print("Grade invalide. Veuillez choisir parmi A, B, C, D, E.")
else:
    heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))

    taux_horaire = grille_tarifaire[grade]['taux_horaire']
    prime = grille_tarifaire[grade]['prime']
    heures_prime = grille_tarifaire[grade]['heures_prime']

    salaire = (taux_horaire * heures_travaillees) + (prime * (heures_travaillees // heures_prime))

    print(f"Le salaire de l'employé est de : {salaire} DH.")
