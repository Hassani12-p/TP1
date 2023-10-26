# Fonction pour saisir une note et son coefficient
def saisir_note():
    note = float(input("Entrez la note : "))
    coefficient = int(input("Entrez le coefficient : "))
    return note, coefficient

# Initialisation des variables
total_notes = 0
total_coefficients = 0

# Boucle pour saisir les notes et coefficients
for i in range(1, 5):
    print(f"Matière {i}:")
    note, coef = saisir_note()
    total_notes += note * coef
    total_coefficients += coef

# Calcul de la moyenne pondérée
moyenne = total_notes / total_coefficients

# Affichage de la moyenne
print(f"Moyenne de ces 4 notes : {moyenne:.2f}")

# Vérification de la validation du semestre
if moyenne >= 10:
    print("Semestre validé")
elif 7 <= moyenne < 10:
    print("Rattrapage")
else:
    print("Semestre non validé")
