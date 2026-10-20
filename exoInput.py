# Exo
# Faire un programme, qui récupère l'année de naissance d'un utilisateur et son prénom.
# Faites un print dynamique avec la phrase : 
# "Bonjour PRENOM, vous avez aujourd'hui AGE"

# je récupère l'année de naissance ( avec la fonction input )
# ensuite je transforme la réponse qui est du texte en nombre entier avec la fonction int
birthday = int(input("Votre année de naissance ?"))

# je récupère le prénom avec la fonction input
name = input("votre prénom ?")
# variable qui contient l'année en cours
years = 2026

# calcul de l'age de l'utilisateur, année actuelle moins son année de naissance
userAge = years - birthday

print(f"Bonjour {name}, vous avez {userAge} ans")
