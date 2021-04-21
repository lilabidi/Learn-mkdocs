# Les bases du Markdown

## Vocabulaire et objectifs

!!! info "Markdown"
    [Markdown](https://fr.wikipedia.org/wiki/Markdown) est un langage de balisage léger qui est traduit en HTML, langage que le navigateur est capable de lire pour produire une page web.

    On peut aussi, à partir d'un fichier Markdown, produire un fichier `.pdf`, ou `.odt`, ou `.docx` en utilisant l'utilitaire [Pandoc](https://fr.wikipedia.org/wiki/Pandoc). Nous ne nous en servirons pas ici.

!!! tip "Utilisation répandue"
    On peut utiliser la syntaxe Markdown dans de nombreuses situations de travail collaboratif.

    - Dans des forums, comme Discourse, GitLab, Reddit, Qt, Stack Overflow et Stack Exchange parmi d'autres.
    - Dans des logiciels, comme CodiMD.

## Construire une note

### Architecture

!!! tip "La première étape"
    Un document doit être structuré en parties et sous parties.

    Le titre d'une partie (ou en-têtes) est précédé d'un ou plusieurs croisillons : `#`

    On saute une ligne après.

    ??? example "Example"

        Pour cette page, la structure a commencé ainsi
        ```markdown
        # Les bases du Markdown

        ## Vocabulaire et objectifs

        ## Construire une note

        ### Architecture

        Avec croisillons.

        ### Paragraphes

        Avec saut de ligne.

        ### Listes

        Avec `-`, ou `1.`

        Imbriquées...

        ### Liens

        url et image

        ### Emphase

        `_` et `*`

        ### Citations

        `>`

        ### Bloc de code

        Par décalage.

        ### Code en ligne

        Avec `` ` ``

        ### Ligne horizontale

        Avec `---`
        ```

### Paragraphes

!!! tip "Le saut de ligne"
    Pour séparer les paragraphes, il suffit de sauter une ligne.

    Il ne faut pas indenter son paragraphe.

    === "Correct"
        !!! note "Entrée"
            ```markdown
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at cursus nibh, et lobortis mauris. Sed tempus turpis quis turpis pulvinar, ac vehicula dui convallis. Phasellus tempus massa quam, ac mollis libero cursus eget. Donec convallis a nisl vitae scelerisque. Ut vel nisl id augue ullamcorper lobortis at id dolor.
            ```
        !!! done "Résultat"
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at cursus nibh, et lobortis mauris. Sed tempus turpis quis turpis pulvinar, ac vehicula dui convallis. Phasellus tempus massa quam, ac mollis libero cursus eget. Donec convallis a nisl vitae scelerisque. Ut vel nisl id augue ullamcorper lobortis at id dolor.

    === "Incorrect"
        !!! note "Entrée"
            ```markdown
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at cursus nibh, et lobortis mauris. Sed tempus turpis quis turpis pulvinar, ac vehicula dui convallis. Phasellus tempus massa quam, ac mollis libero cursus eget. Donec convallis a nisl vitae scelerisque. Ut vel nisl id augue ullamcorper lobortis at id dolor.
            ```
        
        Le texte devient du code en bloc, avec une police à chasse fixe.
        !!! warning "Résultat"
            <pre>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at cursus nibh, et lobortis mauris. Sed tempus turpis quis turpis pulvinar, ac vehicula dui convallis. Phasellus tempus massa quam, ac mollis libero cursus eget. Donec convallis a nisl vitae scelerisque. Ut vel nisl id augue ullamcorper lobortis at id dolor.
            </pre>

### Listes

Avec `-`, ou `1.`

Imbriquées...

### Liens

url et image


### Emphase

`_` et `*`

### Citations

`>`

### Bloc de code

Par décalage.

### Code en ligne

Avec `` ` ``

### Ligne horizontale

Avec `---`



