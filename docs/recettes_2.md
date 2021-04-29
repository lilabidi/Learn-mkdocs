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
    ```yaml
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

        Édit : Et pourquoi ne pas enlever l'extension `.md` si on tient à garder le fichier dons `docs/` ???

## Relayer `mkdocs serve` sur le réseau local

!!! tip "Vous n'avez pas de double écran, mais un téléphone (ou tablette) !"
    1. Déterminer votre adresse ip locale avec `#!console $ ifconfig`, elle ressemble probablement à `192.168.1.40` par exemple.
    2. Lancer depuis ce poste `#!console $ mkdocs serve --dev-addr=0.0.0.0:8000`
    3. Ouvrir depuis votre tablette un navigateur à l'adresse `192.168.1.40:8000`
    4. Avec un écran de plus, c'est toujours mieux !

## Créer ses propres admonitions

[Documentation (_en_)](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#custom-admonitions)

!!! savoir "Admonition personnelle"
    Prenons cet exemple-ci : un cœur animé de battements.

    - Ajouter à votre fichier de `CSS` personnel :
    ```css
    @keyframes heart {
        0%, 40%, 80%, 100% {
        transform: scale(1);
        }
        20%, 60% {
        transform: scale(1.1);
        }
    }
    .heart {
        animation: heart 1000ms infinite;
        color:firebrick
    }
    ```
    - Choisir son fichier d'icône dans `/home/francky/.local/lib/python3.8/site-packages/material/.icons` ou équivalent.
    - Ouvrir le fichier avec un éditeur de code et copier l'intégralité du fichier, une longue ligne qui ressemble à `#!html <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M462.3 62.6C407.5 ... 53-154.3-9.8-207.9z"/></svg>`
    - Ajouter à votre fichier CSS personnel, en remplaçant la balise `<svg xmlns...</svg>` par votre image :
    ```css linenums="1" hl_lines="16"
    :root {
    --md-admonition-icon--savoir: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z"/></svg>')
    }
    .md-typeset .admonition.savoir,
    .md-typeset details.savoir {
    border-color: rgb(219, 16, 16);
    }
    .md-typeset .savoir > .admonition-title,
    .md-typeset .savoir > summary {
    background-color: rgba(185, 27, 101, 0.1);
    border-color: rgb(219, 16, 16);
    }
    .md-typeset .savoir > .admonition-title::before,
    .md-typeset .savoir > summary::before {
    background-color: rgb(219, 16, 16);
    animation: heart 1000ms infinite;
    -webkit-mask-image: var(--md-admonition-icon--savoir);
            mask-image: var(--md-admonition-icon--savoir);
    }
    ```
    - Changer le nom (ici `savoir`), les couleurs et l'animation à votre goût.
    - Utiliser ainsi :
    !!! note "Entrée"
        ```markdown
        !!! savoir "À savoir"
            MkDocs c'est bluffant ; presque on aurait envie d'apprendre un peu de CSS !

            Ici, vous aurez le cœur proche de celui de la documentation, j'ai réduit un peu le coefficient d'agrandissement, pour le rendre légèrement plus discret.

            :octicons-heart-fill-24:{ .heart }
            :octicons-heart-fill-24:{ .heart }
            :octicons-heart-fill-24:{ .heart }
        ```

    !!! done "Rendu"
        !!! savoir "À savoir"
            MkDocs c'est bluffant ; presque on aurait envie d'apprendre un peu de CSS !

            Ici, vous aurez le cœur proche de celui de la documentation, j'ai réduit un peu le coefficient d'agrandissement, pour le rendre légèrement plus discret.

            :octicons-heart-fill-24:{ .heart }
            :octicons-heart-fill-24:{ .heart }
            :octicons-heart-fill-24:{ .heart }

## Relier un bouton à un code JavaScript maison

Possible ???




