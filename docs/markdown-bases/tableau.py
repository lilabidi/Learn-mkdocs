def tableau_markdown(liste: list) -> str:
    lignes = []
    ajout = lignes.append
    # ... à compléter
    return "\n".join(lignes)


"""
# Exercice

Compléter à partir de la ligne 8, puis exécuter le code.

Ne pas modifier ce qu'il y a en dessous de cette ligne.

"""

# test 1
assert tableau_markdown([0, 1, 1, 2, 3, 5, 8, 13]) == \
       '|n|0|1|2|3|4|5|6|7|\n|-|-|-|-|-|-|-|-|-|\n|u_n|0|1|1|2|3|5|8|13|\n'

# test 2
assert tableau_markdown([42, 1337]) == '|n|0|1|\n|-|-|-|\n|u_n|42|1337|\n'

print("Bravo")
