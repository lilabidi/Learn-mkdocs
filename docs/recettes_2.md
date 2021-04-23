# Livre de recettes élaborées

## Info-bulle sur un acronyme

--8<-- "includes/acronymes.md"

> D'après la documentation sur [_Abbreviations_](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)

!!! abstract "Acronymes"
    On souhaite avoir un glossaire d'acronymes et leur définition donnée par survol.

!!! done "Exemple"
    La spécification du HTML est maintenue par le W3C.

??? tip "Méthode"
    Dans `docs/mkdocs.yml`
    ```yml
    markdown_extensions:
      - abbr
      - pymdownx.snippets
    ```

    Le glossaire dans `includes/acronymes.md`
    ```markdown
    *[HTML]: Hyper Text Markup Language
    *[W3C]: World Wide Web Consortium
    ```

    Pour chaque page où l'on souhaite cet effet, on ajoute à la source Markdown la ligne seule (au début ou à la fin, peu importe)
    ```markdown
    --8<-- "includes/acronymes.md"
    ```

    !!! faq "Pourquoi `includes/` en dehors de `docs/` ?"
        Tout fichier `.md` dans `docs/` qui n'est pas utilisé dans `nav` de `mkdocs.yml` provoque un warning de `mkdocs serve`. Raison pour laquelle on place `acronymes.md` (ou autre du même genre) en dehors :wink:
