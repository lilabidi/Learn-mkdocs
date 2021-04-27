# Markdown pour MkDocs

Pour ces expériences, on va utiliser...

??? example "... le fichier `mkdocs.yml` suivant"
    ```yaml
    site_name: Expériences
    site_url: https://ens-fr.gitlab.io/experience
    repo_url: https://gitlab.com/ens-fr/experience
    edit_uri: tree/master/docs/
    site_description: Base commune de travail avec MkDocs
    copyright: |
    Copyright &copy; 2021 <a href="https://gitlab.com/ens-fr"  target="_blank" rel="noopener">Franck CHAMBON</a>
    docs_dir: docs

    nav:
        - Accueil: index.md

                                        # JUSTIFICATIONS
    theme:
        name: material
        font: false                     # RGPD
        language: fr                    # français
        palette:                        # Palettes de couleurs jour/nuit
        - scheme: default
            toggle:
                icon: material/weather-sunny
                name: Passer au mode nuit
        - scheme: slate
            toggle:
                icon: material/weather-night
                name: Passer au mode jour
    features:
        - navigation.instant
        - navigation.tabs
        - navigation.expand
        - navigation.top
        - toc.integrate
        - header.autohide


    markdown_extensions:
        - def_list                      # Les listes de définition.
        - attr_list                     # Un peu de CSS et des attributs HTML.
        - footnotes                     # Notes de bas de page.
        - admonition                    # Blocs colorés
        - pymdownx.details              #   qui peuvent se plier/déplier.
        - pymdownx.caret                # Passage ^^souligné^^ ou en ^exposant^.
        - pymdownx.mark                 # Passage ==surligné==.
        - pymdownx.tilde                # Passage ~~barré~~ ou en ~indice~.
        - pymdownx.highlight:           # Coloration syntaxique du code
            linenums: true              #   avec numérotation,
        - pymdownx.inlinehilite         # pour `#!math  <math en ligne>`
        - pymdownx.snippets             # Inclusion de fichiers externe.
        - pymdownx.tasklist:            # Cases à cocher
            custom_checkbox:    false   #   avec cases d'origine
            clickable_checkbox: true    #   et cliquables.
        - pymdownx.tabbed               # Volets glissants.
        - pymdownx.superfences          # Imbrication de blocs.
        - pymdownx.keys                 # Touches du clavier.
        - pymdownx.emoji:               # Émojis
            emoji_index:     !!python/name:materialx.emoji.twemoji
            emoji_generator: !!python/name:materialx.emoji.to_svg
    ```

Pour une utilisation de MathJax, se référer à la [dernière partie](#utilisation-de-mathjax).

En attendant, plus simple.

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

En introduction, pour donner le contenu du fichier `mkdocs.yml` qui est situé dans `docs/`, on a entré :

````markdown
```yaml
--8<---​ "mkdocs.yml"
```
````

??? danger "Pour aller plus loin"
    [La documentation (_en_)](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/)

## Les panneaux coulissant (*SuperFences*)

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

## Utilisation de MathJax

Suivant les indications de la documentation :
    - [MkDocs Matertial - MathJax](https://squidfunk.github.io/mkdocs-material/reference/mathjax/)
    - [arithmatex](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/)
    - [faceless `mkdocs.yml`](https://github.com/facelessuser/pymdown-extensions/blob/main/mkdocs.yml)

1. On modifie le fichier `mkdocs.yml` :

```yaml
markdown_extensions:
    - pymdownx.arithmatex:          # les maths
        generic: true               #    avec $ et $$

extra_javascript:
    - xtra/javascripts/mathjax-config.js                    # MathJax
    - https://polyfill.io/v3/polyfill.min.js?features=es6
    - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

extra_css:
    - xtra/stylesheets/ajustements.css                      # ajustements
```

2. On crée un dossier `docs/xtra/javascripts` dans lequel

    - on place le fichier `mathjax-config.js`

    ```js
        window.MathJax = {
        tex: {
            inlineMath: [["\\(", "\\)"]],
            displayMath: [["\\[", "\\]"]],
            processEscapes: true,
            processEnvironments: true
        },
        options: {
            ignoreHtmlClass: ".*|",
            processHtmlClass: "arithmatex"
        }
        };

        document$.subscribe(() => {
        MathJax.typesetPromise()
        })
    ```

3. On crée un dossier `docs/xtra/stylesheets` dans lequel

    - on place le fichier `ajustements.css`

    ```js
    .md-typeset div.arithmatex  {
        overflow: initial;
    }

    .md-typeset .admonition {
        font-size: 0.8rem;
    }

    .md-typeset details {
        font-size: 0.8rem;
    }
    ```
