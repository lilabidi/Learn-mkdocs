# Markdown pour MkDocs

Pour ces expériences, on va utiliser...

??? example "... le fichier `mkdocs.yml` suivant"
    ```yaml
    site_name: Expériences
    site_url: https://ens-fr.gitlab.io/experience
    repo_url: https://gitlab.com/ens-fr/experience
    edit_uri: tree/master/docs/
    site_description: Base expérimentale de travail avec MkDocs
    copyright: |
    Copyright &copy; 2021 <a href="https://gitlab.com/ens-fr" target="_blank" rel="noopener">Votre prénom et NOM</a>
    docs_dir: docs

    nav:
        - Accueil: index.md

                                        # JUSTIFICATIONS
    theme:
        name: material
        font: false                     # RGPD ; pas de fonte Google
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
        - footnotes                     # Notes[^1] de bas de page.  [^1]: ma note.
        - admonition                    # Blocs colorés  !!! info "ma remarque"
        - pymdownx.details              #   qui peuvent se plier/déplier.
        - pymdownx.caret                # Passage ^^souligné^^ ou en ^exposant^.
        - pymdownx.mark                 # Passage ==surligné==.
        - pymdownx.tilde                # Passage ~~barré~~ ou en ~indice~.
        - pymdownx.highlight            # Coloration syntaxique du code
        - pymdownx.inlinehilite         # pour  `#!python  <python en ligne>`
        - pymdownx.snippets             # Inclusion de fichiers externe.
        - pymdownx.tasklist:            # Cases à cocher  - [ ]  et - [x]
            custom_checkbox:    false   #   avec cases d'origine
            clickable_checkbox: true    #   et cliquables.
        - pymdownx.tabbed               # Volets glissants.  === "Mon volet"
        - pymdownx.superfences          # Imbrication de blocs.
        - pymdownx.keys:                # Touches du clavier.  ++ctrl+d++
            separator: "\uff0b"
        - pymdownx.emoji:               # Émojis  :boom:
            emoji_index:     !!python/name:materialx.emoji.twemoji
            emoji_generator: !!python/name:materialx.emoji.to_svg

    extra:
        social:
            - icon: fontawesome/brands/github # ou autre
            link: https://github.com/votreid
            - icon: fontawesome/brands/gitlab # ou autre
            link: https://gitlab.com/votreid
            - icon: fontawesome/brands/discord #ou autre
            link: https://discord.gg/votrecode
    ```

Pour une utilisation de MathJax, se référer à la [dernière partie](#utilisation-de-mathjax).

En attendant, plus simple, les possibilités de Markdown avec MkDocs.

## Les admonitions

!!! info "Pourquoi ?"
    Elles permettent de délimiter des blocs de contenu
      avec une touche de couleur, sans créer de nouvelles
      entrées dans la table des matières.
    
    Elles structurent donc sans alourdir les onglets de navigation.

!!! example "Exemple"
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

!!! example "Les types de boites"
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

    On verra dans les recettes élaborées comment fabriquer ses propres boîtes, couleur et icône.

## Les boutons

Un lien cliquable peut être transformé en bouton en lui adjoignant un élément de CSS `{ .md-button }`

!!! example "Exemples"
    === "Rectangle creux"
        !!! note "Entrée"
            ```markdown
            [Une console Basthon](https://console.basthon.fr/){ .md-button }
            ```
        !!! done "Rendu"
            [Une console Basthon](https://console.basthon.fr/){ .md-button }

    === "Rectangle plein"
        !!! note "Entrée"
            ```markdown
            [Une console Basthon](https://console.basthon.fr/){ .md-button .md-button--primary }
            ```
        !!! done "Rendu"
            [Une console Basthon](https://console.basthon.fr/){ .md-button .md-button--primary }

## Options sur les blocs de code

!!! tip "Numérotation des lignes et marquage"
    - Il suffit d'ajouter `linenums="1"` (ou un autre nombre) pour faire débuter la numérotation.
    - Pour marquer des lignes en particulier, on utilise `hl_lines="<tranches et numéros>"`


!!! example "Exemples"
    === "Sans numérotation"
        !!! note "Entrée"
            ````markdown
            ```python
            --8<--- "docs/scripts/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python
            --8<--- "docs/scripts/exemple.py"
            ```

    === "Numérotation classique"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1"
            --8<--- "docs/scripts/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1"
            --8<--- "docs/scripts/exemple.py"
            ```

    === "Numérotation décalée"
        !!! note "Entrée"
            ````markdown
            ```python linenums="42"
            --8<--- "docs/scripts/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="42"
            --8<--- "docs/scripts/exemple.py"
            ```

    === "Marquage d'une ligne"
        !!! note "Entrée"
            ````markdown
            ```python hl_lines="2"
            --8<--- "docs/scripts/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python hl_lines="2"
            --8<--- "docs/scripts/exemple.py"
            ```

    === "Marquage d'une ligne, avec numérotation"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1" hl_lines="2"
            --8<--- "docs/scripts/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1" hl_lines="2"
            --8<--- "docs/scripts/exemple.py"
            ```

    === "Marquage de lignes éparses"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1" hl_lines="2 5"
            --8<--- "docs/scripts/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1" hl_lines="2 5"
            --8<--- "docs/scripts/exemple.py"
            ```

    === "Marquage d'une tranche"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1" hl_lines="2-4"
            --8<--- "docs/scripts/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1" hl_lines="2-4"
            --8<--- "docs/scripts/exemple.py"
            ```

    === "Marquage lignes et tranches"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1" hl_lines="1 2 3-3 5-5"
            --8<--- "docs/scripts/exemple.py"
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1" hl_lines="1 2 3-3 5-5"
            --8<--- "docs/scripts/exemple.py"
            ```

??? bug "Bug ???"
    1. J'ai constaté des ratés de coloration syntaxique avec ```` ``` c++ ````.

        - Recommendations :
            - Pas d'espace entre ```` ``` ```` et le nom du langage.
            - Utiliser `cpp` à la place de `c++`

    2. Ne pas choisir l'option globale `linenums: false` dans `mkdocs.yml`
        - On ne peut plus la réactiver ensuite
        - On peut toutefois choisir `linenums: true`, (mais sans la mettre en pause ???)

## Affichage des touches

!!! example "Exemple 1"
        !!! note "Markdown"
            ```markdown
            ++ctrl+alt+del++
            ```
        !!! done "Rendu"
            ++ctrl+alt+del++

!!! example "Exemple 2"
        !!! note "Markdown"
            ```markdown
            ++"⇑ Maj."+"Entrée ↵"++
            ```
        !!! done "Rendu"
            ++"⇑ Maj."+"Entrée ↵"++
        
        On peut définir ses propres touches avec `"ma touche"`


La liste des touches disponibles est dans la [documentation](
    https://facelessuser.github.io/pymdown-extensions/extensions/keys/#key-map-index).

## Intégration de fichiers externes

!!! info "Le cas simple"
    En introduction, pour donner le contenu du fichier `mkdocs.yml` qui est situé dans `docs/`, on a entré :

    ````markdown
    ```yaml
    --8<---​ "mkdocs.yml"
    ```
    ````

!!! warning "Points techniques"
    - :warning: Il faut donner le chemin en partant de la racine du projet.
    - Le contenu du fichier est remplacé dans le code source Markdown avant interprétation et son indentation est respectée, même si l'intégration se fait dans un bloc. :warning: Ce n'est pas le cas si `--8<--- <exemple>` est inclus dans une macro, l'indentation n'est plus respectée. On l'utilisera donc en dehors de macros.

!!! tip "Inclure un affichage de script"
    On prendra l'exemple de l'affichage de `docs/scripts/exemple.py`

    !!! note "Entrée"
        ````markdown
        Affichage de `docs/scripts/exemple.py`

        ```python
        --8<--- "docs/scripts/exemple.py"   <"ne RIEN écrire ici">
        ```

        Une fonction de tri.
        ````
    
    !!! done "Rendu"
        Affichage de `docs/scripts/exemple.py`

        ```python
        --8<--- "docs/scripts/exemple.py"
        ```

        Une fonction de tri.
    
    :warning: Il ne faut **rien** écrire après le nom de fichier, **pas même d'espace** !


??? danger "Pour aller plus loin"
    [La documentation (_en_)](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/)

## Les panneaux coulissant (*SuperFences*)

!!! example "Exemple simple"
    !!! note "Entrée"

        ```` markdown

        === "`C`"

            ```c
            #include <stdio.h>

            int main(void) {
              printf("Hello world!\n");
              return 0;
            }
            ```

        === "`C++`"

            ```cpp
            #include <iostream>

            int main(void) {
              std::cout << "Hello world!" << std::endl;
              return 0;
            }
            ```

        ````

    !!! done "Rendu"

        === "C"

            ```c
            #include <stdio.h>

            int main(void) {
              printf("Hello world!\n");
              return 0;
            }
            ```

        === "C++"

            ```cpp
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
            - Sed sagittis eleifend rutrum
            - Donec vitae suscipit est
            - Nulla tempor lobortis orci
            ```

            _Résultat_ :

            - Sed sagittis eleifend rutrum
            - Donec vitae suscipit est
            - Nulla tempor lobortis orci

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
            - Sed sagittis eleifend rutrum
            - Donec vitae suscipit est
            - Nulla tempor lobortis orci
            ```

            _Résultat_ :

            - Sed sagittis eleifend rutrum
            - Donec vitae suscipit est
            - Nulla tempor lobortis orci

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

!!! tip "Avec `[^id]` et `[^id]: description`"
    On place une indication de note en bas de page avec `[^id]` où `id` est un identifiant.

!!! example "Exemple"
    !!! note "Entrée"
        ```markdown
        Lorem ipsum[^ip] dolor sit amet, consectetur adipiscing[^ad] elit.[^el]

        [^ip]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.

        [^ad]:
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
            nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
            massa, nec semper lorem quam in massa.

        [^el]:
            Ce texte [Lorem ipsum ...](https://fr.wikipedia.org/wiki/Lorem_ipsum)
            est un faux-texte destiné à remplir la vide.
        ```

    !!! done "Rendu"
        Lorem ipsum[^ip] dolor sit amet, consectetur adipiscing[^ad] elit.[^el]

        [^ip]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.

        [^ad]:
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
            nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
            massa, nec semper lorem quam in massa.

        [^el]:
            Ce texte [Lorem ipsum ...](https://fr.wikipedia.org/wiki/Lorem_ipsum)
            est un faux-texte destiné à remplir la vide.
    
    :warning: Les identifiants sont numérotés automatiquement par ordre d'arrivée.
    
    - Ici, la première note (`ip`) est accessible avec un lien local `#fn:ip`, comme [ici](#fn:ip).
    - Le retour ici se fait avec `#fnref:ip` comme [ceci](#fnref:ip).

## Liste de définitions

!!! tip "Pour une paire (clé, valeurs)"
    Les listes de définition sont idéales, par exemple pour une liste de paramètres à une fonction...

!!! example "Example"
    !!! note "Entrée"
        ```markdown
        `Lorem ipsum dolor sit amet`
        :   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
            tellus non sem sollicitudin, quis rutrum leo facilisis.

        `Cras arcu libero`
        :   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
            ut eros sed sapien ullamcorper consequat. Nunc ligula ante.

            Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
            Nam vulputate tincidunt fringilla.
            Nullam dignissim ultrices urna non auctor.
        ```

    !!! done "Rendu"
        `Lorem ipsum dolor sit amet`
        :   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
            tellus non sem sollicitudin, quis rutrum leo facilisis.

        `Cras arcu libero`
        :   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
            ut eros sed sapien ullamcorper consequat. Nunc ligula ante.

            Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
            Nam vulputate tincidunt fringilla.
            Nullam dignissim ultrices urna non auctor.
    
    :warning: En suivant la bonne indentation, on peut avoir plusieurs paragraphes dans une définition.


## Lien sur les en-têtes

## Icônes et émojis

:octicons-heart-fill-24:{ .heart }

??? savoir "Cœur"
    Alors ? ok

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

    - on place le fichier `ajustements.css` ; merci @sebhoa

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
