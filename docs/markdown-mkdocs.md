# Markdown pour MkDocs

On voit des choses en plus, essentiellement on va faire le tour de https://squidfunk.github.io/mkdocs-material/reference/abbreviations/

À suivre...

Pour ces expériences, on va utiliser un fichier `mkdocs.yml` qui ressemble à

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
