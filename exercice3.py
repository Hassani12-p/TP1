
distance_km = float(input("Entrez la distance en km : "))
temps_minutes = float(input("Entrez le temps en min: "))

distance_metres = distance_km * 1000
temps_secondes = temps_minutes * 60
vitesse = distance_metres / temps_secondes

print("La vitesse est de {:.2f} m/s.".format(vitesse))
