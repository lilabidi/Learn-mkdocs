# Livre de recettes simples

## QCM à cocher, solution en regard

> Par Franck CHAMBON

!!! abstract "QCM à cocher"
    On souhaite proposer un QCM, auto corrigé.

!!! done "Exemple 1"
    Pour cet exercice sur Python,
     on ne regarde que **si l'identifiant est valide**,
     il pourrait être mal choisi.

    === "Cocher les identifiants valides"
        - [ ] `as`
        - [ ] `Roi`
        - [ ] `2ame`
        - [ ] `v413t`
        - [ ] `dix`
        - [ ] `n'œuf`
        - [ ] `huit`
        - [ ] `Sète`
        - [ ] `carte_six`
        - [ ] `_5`
        - [ ] `%4`
        - [ ] `quatre-moins-un`
        - [ ] `2!`
        - [ ] `_`

    === "Solution"
        - ❌ `as` ; c'est un mot réservé.
        - ✅ `Roi`
        - ❌ `2ame` ; interdit de commencer par un chiffre.
        - ✅ `v413t`
        - ✅ `dix`
        - ❌ `n'œuf` ; interdit d'utiliser `'`
        - ✅ `huit`
        - ✅ `Sète`
        - ✅ `carte_six`
        - ✅ `_5`
        - ✅ `_`
        - ❌ `%4` ; interdit d'utiliser `%`
        - ❌ `quatre-moins-un` ; interdit d'utiliser `-`
        - ❌ `2!` ; interdit d'utiliser `!`
        - ✅ `_`

??? tip "Méthode 1"
    - On utilise les cases à cocher avec l'option cliquable.
    - On utilise des caractères Unicode pour les réponses, ❌ et ✅.
    - On utilise les [SuperFences](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/)

    Dans `mkdocs.yml`
    ```yml
    markdown_extensions:
      - pymdownx.tabbed
      - pymdownx.superfences
    ```

    Dans le source
    ```markdown
        Pour cet exercice sur Python,
         on ne regarde que **si l'identifiant est valide**,
         il pourrait être mal choisi.

        === "Cocher les identifiants valides"
            - [ ] `as`
            - [ ] `Roi`
            - [ ] `2ame`
            - [ ] `v413t`
            - [ ] `dix`
            - [ ] `n'œuf`
            - [ ] `huit`
            - [ ] `Sète`
            - [ ] `carte_six`
            - [ ] `_5`
            - [ ] `%4`
            - [ ] `quatre-moins-un`
            - [ ] `2!`
            - [ ] `_`

        === "Solution"
            - ❌ `as` ; c'est un mot réservé.
            - ✅ `Roi`
            - ❌ `2ame` ; interdit de commencer par un chiffre.
            - ✅ `v413t`
            - ✅ `dix`
            - ❌ `n'œuf` ; interdit d'utiliser `'`
            - ✅ `huit`
            - ✅ `Sète`
            - ✅ `carte_six`
            - ✅ `_5`
            - ✅ `_`
            - ❌ `%4` ; interdit d'utiliser `%`
            - ❌ `quatre-moins-un` ; interdit d'utiliser `-`
            - ❌ `2!` ; interdit d'utiliser `!`
            - ✅ `_`
    ```

!!! done "Exemple 2"
    Cocher le meilleur identifiant pour une variable Python.

    !!! faq "Propositions"
        - [ ] `pv`
        - [ ] `p_vie`
        - [ ] `points_vie`
        - [ ] `les_points_de_vie`

    ??? done "Réponse"
        - ❌ `pv`
        - ❌ `p_vie`
        - ✅ `points_vie`
        - ❌ `les_points_de_vie`

??? tip "Méthode 2"
    - On utilise les cases à cocher avec l'option cliquable
    - On utilise des caractères Unicode pour les réponses, ❌ et ✅
    - On utilise les [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
        - Avec la possibilité `details`

    Dans `mkdocs.yml`
    ```yml
    markdown_extensions:
      - admonition
      - pymdownx.details
    ```

    Dans le source
    ```markdown
    !!! done "Exemple 2"
        Cocher le meilleur identifiant pour une variable Python.

        !!! faq "Propositions"
            - [ ] `pv`
            - [ ] `p_vie`
            - [ ] `points_vie`
            - [ ] `les_points_de_vie`

        ??? done "Réponse"
            - ❌ `pv`
            - ❌ `p_vie`
            - ✅ `points_vie`
            - ❌ `les_points_de_vie`
    ```

## Coloration syntaxique des sections mathématiques

> Par Franck CHAMBON

!!! abstract "Colorer les maths"
    On peut colorer Python en ligne avec `` `#!python for i in range(10): print(i)` ``

    - Ce qui donne `#!python for i in range(10): print(i)`

    On souhaite pouvoir faire `` `#!math $\mathrm{e}^{\mathrm{i}\pi} + 1 = 0$` ``

    - Mais le résultat `#!math $\mathrm{e}^{\mathrm{i}\pi} + 1 = 0$` est non coloré...
    - De même en utilisant `` `#!mardown $\mathrm{e}^{\mathrm{i}\pi} + 1 = 0$` ``

!!! done "Exemple"
    On aimerait avoir `#!latex $\mathrm{e}^{\mathrm{i}\pi} + 1 = 0$`

??? tip "Méthode"
    On utilise le [lexer](https://fr.wikipedia.org/wiki/Analyse_lexicale) `latex` à la place de `math`.

    Solution `` `#!latex $\mathrm{e}^{\mathrm{i}\pi} + 1 = 0$` ``

    De même pour les maths en mode équation.

