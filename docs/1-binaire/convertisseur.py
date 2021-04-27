def ascii_vers_binaire(texte):
    sortie = []
    for lettre in texte:
        code_ascii = ord(lettre)
        if 0 <= code_ascii < 128:
            sortie.append(bin(code_ascii)[2:])
        else:
            return "Il y avait un caractère non ASCII !"
    return "".join(sortie)

"""
# Consignes

- Exécuter le script
- Utiliser-le dans la console comme par exemple

>>> ascii_vers_binaire("Salut toi !")

>>> ascii_vers_binaire("Bonjour à tous ;-)")

- Trouve le caractère non ASCII du second exemple
"""
