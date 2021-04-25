# Markdown pour MkDocs

Pour ces expériences, on va utiliser...

??? example "... le fichier `mkdocs.yml` suivant"
    ```yml
    site_name: "Premières expériences avec MkDocs"

    nav:
      - "Accueil": index.md
      - "Page 1": page_1.md
      - "Page 2": page_2.md

    theme:
      name: material
      font: false
      language: fr
      features:
        - navigation.instant
        - navigation.tabs
        - navigation.expand
        - navigation.top
        - toc.integrate
        - header.autohide

      palette:
        # Light mode
        - media: "(prefers-color-scheme: light)"
          scheme: default
          primary: indigo
          accent: indigo
          toggle:
            icon: material/toggle-switch-off-outline
            name: Mode sombre

        # Dark mode
        - media: "(prefers-color-scheme: dark)"
          scheme: slate
          primary: blue
          accent: blue
          toggle:
            icon: material/toggle-switch
            name: Mode clair


    markdown_extensions:
      - meta
      - abbr
      - admonition
      - def_list
      - attr_list
      - footnotes
      - pymdownx.caret
      - pymdownx.mark
      - pymdownx.tilde
      - pymdownx.snippets
      - pymdownx.details
      - pymdownx.highlight:
          linenums: false
      - pymdownx.tasklist:
          custom_checkbox: false
          clickable_checkbox: true
      - pymdownx.inlinehilite
      - pymdownx.superfences
      - pymdownx.keys
      - pymdownx.tabbed
      - pymdownx.emoji:
          emoji_index: !!python/name:materialx.emoji.twemoji
          emoji_generator: !!python/name:materialx.emoji.to_svg
      - toc:
          permalink: ⚓︎
          toc_depth: 3


    plugins:
      - search

    extra:
      social:
        - icon: fontawesome/solid/paper-plane
          link: mailto:quelqun@ailleurs.grd
          name: Écrire à l'auteur

    ```

## Les admonitions

!!! info "Pourquoi ?"
    Elles permettent de délimiter des blocs de contenu
      avec une touche de couleur, sans créer de nouvelles
      entrées dans la table des matières.
    
    Elles structurent donc sans alourdir les onglets de navigation.

!!! example "Exemples"
    !!! note "Entrée"
        ```markdown
        !!! info "Pourquoi ?"
            Elles permettent de délimiter des blocs de contenu
             avec une touche de couleur, sans créer de nouvelles
             entrées dans la table des matières.
            
            Elles structurent donc sans alourdir les onglets de navigation.
        ```
    !!! done "Rendu"
        !!! info "Pourquoi ?"
            Elles permettent de délimiter des blocs de contenu
             avec une touche de couleur, sans créer de nouvelles
             entrées dans la table des matières.
            
            Elles structurent donc sans alourdir les onglets de navigation.

    👍 Il s'agit du code pour produire le paragraphe précédent !

!!! faq "Comment l'avoir enroulée, à dérouler ?"
    En remplaçant `!!!` par `???`. Cela correspond à la balise `<details>` en HTML.

    Comme l'exemple d'introduction qui contient le fichier `mkdocs.yml`.

    `???+` permet de l'avoir déroulée à l'ouverture de la page, et qu'elle
    puisse être ensuite enroulée.

### Les types de boites

=== "`note`"
    !!! note "Pour une note"
        `note` ou `seealso`
        ````markdown
        ```markdown
        !!! note "Pour une note"
            `note` ou `seealso`
        ```
        ````

=== "`tldr`"
    !!! tldr "Pour un résumé"
        `tldr`, `summary` ou `abstract`
        ````markdown
        ```markdown
        !!! tldr "Pour un résumé"
            `tldr`, `summary` ou `abstract`
        ```
        ````

=== "`info`"
    !!! info "Pour une information"
        `info` ou `todo`
        ````markdown
        ```markdown
        !!! info "Pour une information"
            `info` ou `todo`
        ```
        ````

=== "`tip`"
    !!! tip "Pour une astuce"
        `tip`, `hint` ou `important`
        ````markdown
        ```markdown
        !!! tip "Pour une astuce"
            `tip`, `hint` ou `important`
        ```
        ````

=== "`done`"
    !!! done "Pour une réussite"
        `done`, `check` ou `success`
        ````markdown
        ```markdown
        !!! done "Pour une réussite"
            `done`, `check` ou `success`
        ```
        ````

=== "`faq`"
    !!! faq "Pour une question"
        `faq`, `help` ou `question`
        ````markdown
        ```markdown
        !!! faq "Pour une question"
            `faq`, `help` ou `question`
        ```
        ````

=== "`warning`"
    !!! warning "Pour une difficulté"
        `warning`, `caution` ou `attention`
        ````markdown
        ```markdown
        !!! warning "Pour une difficulté"
            `warning`, `caution` ou `attention`
        ```
        ````

=== "`fail`"
    !!! fail "Pour un échec"
        `fail`, `failure` ou `missing`
        ````markdown
        ```markdown
        !!! fail "Pour un échec"
            `fail`, `failure` ou `missing`
        ```
        ````

=== "`danger`"
    !!! danger "Pour un danger"
        `danger` ou `error`
        ````markdown
        ```markdown
        !!! danger "Pour un danger"
            `danger` ou `error`
        ```
        ````

=== "`bug`"
    !!! bug "Pour un bogue"
        `bug`
        ````markdown
        ```markdown
        !!! bug "Pour un bogue"
            `bug`
        ```
        ````

=== "`example`"
    !!! example "Pour des exemples"
        `example`
        ````markdown
        ```markdown
        !!! example "Pour des exemples"
            `example`
        ```
        ````

=== "`cite`"
    !!! cite "Pour une citation"
        `cite`
        ````markdown
        ```markdown
        !!! cite "Pour une citation"
            `cite`
        ```
        ````

## Les boutons

Un lien cliquable peut être transformé en bouton en lui adjoignant un élément de CSS `{ .md-button }`

!!! example "Exemples"
    === "Rectangle creux"
        !!! note "Markdown"
            ```markdown
            [Une console Basthon](https://console.basthon.fr/){ .md-button }
            ```
        !!! done "Rendu"
            [Une console Basthon](https://console.basthon.fr/){ .md-button }

    === "Rectangle plein"
        !!! note "Markdown"
            ```markdown
            [Une console Basthon](https://console.basthon.fr/){ .md-button .md-button--primary }
            ```
        !!! done "Rendu"
            [Une console Basthon](https://console.basthon.fr/){ .md-button .md-button--primary }

## Options sur les blocs de code

- Numérotation des lignes
- mise en lumière d'un choix de lignes
- coloration de code en ligne

À suivre


## Affichage des touches
!!! example "Exemple"
        !!! note "Markdown"
            ```markdown
            ++ctrl+alt+del++
            ```
        !!! done "Rendu"
            ++ctrl+alt+del++

## Intégration de fichiers externes

````markdown
```python
--8<--​ "docs/fichier.py"
```
````

## Les palissades (*SuperFences*)

!!! example "Exemple simple"
    !!! note "Entrée"

        ```` markdown

        === "C"

            ``` c
            #include <stdio.h>

            int main(void) {
              printf("Hello world!\n");
              return 0;
            }
            ```

        === "C++"

            ``` c++
            #include <iostream>

            int main(void) {
              std::cout << "Hello world!" << std::endl;
              return 0;
            }
            ```

        ````

    !!! done "Rendu"

        === "C"

            ``` c
            #include <stdio.h>

            int main(void) {
              printf("Hello world!\n");
              return 0;
            }
            ```

        === "C++"

            ``` c++
            #include <iostream>

            int main(void) {
              std::cout << "Hello world!" << std::endl;
              return 0;
            }
            ```

??? danger "Exemple élaboré"
    !!! note "Entrée"

        ```` markdown

        === "Liste non numérotée"

            _Exemple_ :

            ``` markdown
            * Sed sagittis eleifend rutrum
            * Donec vitae suscipit est
            * Nulla tempor lobortis orci
            ```

            _Résultat_ :

            * Sed sagittis eleifend rutrum
            * Donec vitae suscipit est
            * Nulla tempor lobortis orci

        === "Liste numérotée"

            _Exemple_ :

            ``` markdown
            1. Sed sagittis eleifend rutrum
            2. Donec vitae suscipit est
            3. Nulla tempor lobortis orci
            ```

            _Résultat_ :

            1. Sed sagittis eleifend rutrum
            2. Donec vitae suscipit est
            3. Nulla tempor lobortis orci

        ````

    !!! done "Rendu"

        === "Liste non numérotée"

            _Exemple_ :

            ``` markdown
            * Sed sagittis eleifend rutrum
            * Donec vitae suscipit est
            * Nulla tempor lobortis orci
            ```

            _Résultat_ :

            * Sed sagittis eleifend rutrum
            * Donec vitae suscipit est
            * Nulla tempor lobortis orci

        === "Liste numérotée"

            _Exemple_ :

            ``` markdown
            1. Sed sagittis eleifend rutrum
            2. Donec vitae suscipit est
            3. Nulla tempor lobortis orci
            ```

            _Résultat_ :

            1. Sed sagittis eleifend rutrum
            2. Donec vitae suscipit est
            3. Nulla tempor lobortis orci


## Notes de bas de page

## Liste de définitions

## Lien sur les en-têtes

## Icônes et émojis

## Images

## Meta tags
