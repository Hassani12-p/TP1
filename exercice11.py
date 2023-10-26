def calcul_imc(poids, taille):
    return poids / (taille ** 2)

def interpretation_imc(imc):
    plages = [16.5, 18.5, 25, 30, 35, 40]
    interpretations = [
        "Famine",
        "Maigreur",
        "Corpulence normale",
        "Surpoids",
        "Obésité modérée",
        "Obésité sévère",
        "Obésité morbide ou massive"
    ]


    for i, plage in enumerate(plages):
        if imc < plage:
            interpretation = interpretations[i]
            break

    return interpretation

poids = float(input("Entrez votre poids en kilogrammes : "))
taille = float(input("Entrez votre taille en mètres : "))

imc = calcul_imc(poids, taille)
interpretation = interpretation_imc(imc)

print(f"Votre IMC est {imc:.2f}, ce qui correspond à : {interpretation}.")
