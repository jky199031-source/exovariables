# exo 1
# faire une phrase (dynamique = avec des données changeantes)
# "je suis Jacky j'habite à Léognan et j'ai 36"
# Jacky, Léognan, 36 ans seront dans des variables

# exo 2
# Print une phrase le total est de TOTAL euros
# vous avez acheté une baguette et un croissant
# le montant de ces articles sont dans des variables

# Exo3 
# Lors d'un jeu vous avez dix points
# Faire un print de vos points 
# Au premier tour vous perdez 1 pts
# au deuxieme tour vous en gagnez 5
# au dernier tour vous en perdez la moitié
# faire un print de votre nouveau total de points a chaque tours


# exo1
mot = "Jacky"
mot1 = "Léognan"
mot2 = "36 ans"

print ("Je suis", mot, "j'habite à", mot1, "et j'ai", mot2)

# exo2

baguette = "1.20"
croissant = "1.80"
print("La baguette vaut", baguette, "et le croissant vaut", croissant, )

# Exo 3
point = 10
print("Départ", point)
point = point - 1
print ("premier tour", point)
point = point + 5
print ("deuxième tour", point)
point = point // 2
print ("dernier tour", point)
