
sec= int(input("Entrez le nombre de secondes : "))
h = sec // 3600
min= (sec% 3600) // 60
sec_rest = (sec % 3600) % 60


print("{} secondes équivalent à {}h {}min {}sec.".format(sec, h, min, sec_rest))