# Les bases du Markdown

## Vocabulaire et objectifs

!!! info "Markdown"
    [Markdown](https://fr.wikipedia.org/wiki/Markdown) est un langage de balisage léger qui est traduit en HTML, langage que le navigateur est capable de lire pour produire une page web.

    On peut aussi, à partir d'un fichier Markdown, produire un fichier `.pdf`, ou `.odt`, ou `.docx` en utilisant l'utilitaire [Pandoc](https://fr.wikipedia.org/wiki/Pandoc). Nous ne nous en servirons pas ici.

!!! tip "Utilisation répandue"
    On peut utiliser la syntaxe Markdown dans de nombreuses situations de travail collaboratif.

    - Dans des forums, comme Discourse, **GitLab**, Reddit, Qt, Stack Overflow et Stack Exchange parmi d'autres.
    - Dans des logiciels, comme CodiMD, ou **Jupyter**.

!!! warning "Défauts"
    Soyons honnête, il y a un défaut majeur, Markdown n'est pas unifié.

    - Il existe plusieurs variantes légèrement différentes de Markdown.
    - Pour chaque variante, il peut exister des moteurs de rendus légèrement différents.

    Nous utiliserons ici la partie commune à toute les versions, avec le style le plus commun possible. Dans la partie « avancée » nous travaillerons avec certaines facilités de MkDocs.


!!! example "D'autres tutoriels"
    Suivant votre goût pour l'anglais et votre temps :

    - https://www.markdowntutorial.com/ _in english by GitHub_
    - [Syntaxe assez complète](https://michelf.ca/projets/php-markdown/syntaxe/)
    - [another, in english, by GitHub](http://agea.github.io/tutorial.md/)
    - [Un résumé assez succinct](https://github.com/luong-komorebi/Markdown-Tutorial/blob/master/README_fr.md)
    - [Élaboration et conversion de documents avec Markdown et Pandoc](https://enacit1.epfl.ch/markdown-pandoc/) ; pour les utilisateurs avancés.

    Il ne faut que **5 minutes pour avoir les bases** suffisantes.

    On reprend ci-dessous l'essentiel.

## Construire une note

### Résumé

|Objectif|Markdown|Rendu|
|:-----|:------|:----|
|Créer un lien|`[texte cliquable](mon_lien.fr)`|[texte cliquable](mon_lien.fr)|
|Emphase faible|`Un _mot_ discret` | Un _mot_ discret |
|Emphase forte|`Un **mot** visible` | Un **mot** visible |
|Du code en ligne|``Une boucle `for` `` |Une boucle `for`|


### Architecture

!!! tip "La première étape"
    Un document doit être structuré en parties et sous parties.

    Le titre d'une partie (ou en-têtes) est précédé d'un ou plusieurs croisillons : `#`

    On ajoute une espace après le dernier croisillon.

    On saute une ligne avant et après l'en-tête.

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

=== "Correct"
    !!! note "Entrée"
        ```markdown
        # Mon super titre

        Mon premier paragraphe.
        ```
    !!! done "Rendu"
        <big><strong>Mon super titre</strong></big>

        Mon premier paragraphe.

=== "Incorrect"
    !!! note "Entrée"

        ```markdown
        #Mon super titre
        Mon premier paragraphe.
        ```

    !!! fail "Rendu"
        \#Mon super titre Mon premier paragraphe.

    Ce rendu dépend du moteur...

### Paragraphes

!!! tip "Le saut de ligne"
    Pour séparer les paragraphes, il suffit de sauter une ligne.

    Il ne faut pas indenter son paragraphe.

    === "Correct"
        !!! note "Entrée"
            ```markdown
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at cursus nibh, et lobortis mauris. Sed tempus turpis quis turpis pulvinar, ac vehicula dui convallis. Phasellus tempus massa quam, ac mollis libero cursus eget. Donec convallis a nisl vitae scelerisque. Ut vel nisl id augue ullamcorper lobortis at id dolor.
            ```
        !!! done "Rendu"
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at cursus nibh, et lobortis mauris. Sed tempus turpis quis turpis pulvinar, ac vehicula dui convallis. Phasellus tempus massa quam, ac mollis libero cursus eget. Donec convallis a nisl vitae scelerisque. Ut vel nisl id augue ullamcorper lobortis at id dolor.

    === "Incorrect"
        !!! note "Entrée"
            ```markdown
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at cursus nibh, et lobortis mauris. Sed tempus turpis quis turpis pulvinar, ac vehicula dui convallis. Phasellus tempus massa quam, ac mollis libero cursus eget. Donec convallis a nisl vitae scelerisque. Ut vel nisl id augue ullamcorper lobortis at id dolor.
            ```
        
        Le texte devient du code en bloc, avec une police à chasse fixe.
        !!! warning "Rendu"
            <pre>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at cursus nibh, et lobortis mauris. Sed tempus turpis quis turpis pulvinar, ac vehicula dui convallis. Phasellus tempus massa quam, ac mollis libero cursus eget. Donec convallis a nisl vitae scelerisque. Ut vel nisl id augue ullamcorper lobortis at id dolor.
            </pre>

### Listes

!!! tip "Une ligne vide puis..."
    Une liste, comme un nouveau paragraphe, doit être précédée d'une ligne vide.

    Ensuite, on place chaque item sur une ligne en commençant par `-`

    On peut faire des listes numérotées en commençant par `1.`
    
    On place aussi une espace juste avant son item.

!!! example "Exemples"
    === "Liste à puce"
        !!! note "Entrée"
            ```markdown
            Markdown est **très** utilisé sur de _nombreux_ forums

            - Discourse
            - GitLab
            - Reddit
            - Qt
            - Stack Overflow
            - Stack Exchange
            - ...
            ```

        !!! done "Rendu"
            Markdown est **très** utilisé sur de _nombreux_ forums

            - Discourse
            - GitLab
            - Reddit
            - Qt
            - Stack Overflow
            - Stack Exchange
            - ...

        Pour information, la traduction pour le navigateur.
        ??? info "Code HTML"
            ```html
            <p>Markdown est <strong>très</strong> utilisé sur de <em>nombreux</em> forums
            <ul>
                <li>Discourse</li>
                <li>GitLab</li>
                <li>Reddit</li>
                <li>Qt</li>
                <li>Stack Overflow</li>
                <li>Stack Exchange</li>
                <li>...</li>
            </ul>
            </p>
            ```
        
        On remarquera un peu de mise de style (l'emphase) ; nous y reviendrons.

        On remarque aussi une meilleure lisibilité du Markdown sur le HTML.

    === "Liste numérotée"
        !!! note "Entrée"
            ```markdown
            Pour une liste numérotée, la numérotation est automatique !
            
            1. Mon premier exemple
            3. Le troisième, mais le deuxième a été effacé
            3. Un oubli entre le troisième et quatrième
            3. Encore un oubli...
            4. C'était le quatrième au départ.
            1. Juste un de plus qui sera numéroté correctement.
            ```
        
        !!! done "Rendu"
            Pour une liste numérotée, la numérotation est automatique !
            
            1. Mon premier exemple
            3. Le troisième, mais le deuxième a été effacé
            3. Un oubli entre le troisième et quatrième
            3. Encore un oubli...
            4. C'était le quatrième au départ.
            1. Juste un de plus qui sera numéroté correctement.

### Liens

url et image

### Emphase

!!! info "Pas trop gras svp !"
    Commençons par indiquer que certains documents abusent des effets de style et la lisibilité en est réduite.

    L'emphase sert à faire ressortir une partie plus importante que le reste. Ce ne peut être qu'une petite partie.

!!! abstract "Définitions"
    - L'emphase faible sert à faire ressortir discrètement du texte. Elle est **souvent** en _italique_, mais on peut changer cela dans une feuille de style en cascade (CSS).
    - De même, l'emphase forte est souvent en gras, mais on pourrait décider dans la feuille CSS de modifier ce style en couleur rouge et souligné en noir. Et puis changer un autre jour ; l'ensemble du document soumis à la feuille CSS est modifié.
    - En HTML, ces balises sont

        - `<em>` pour l'emphase faible
        - `<strong>` pour l'emphase forte
    - Il existe aussi en HTML des balises pour forcer l'italique ou le gras, elles sont souvent déconseillées.
    - En Markdown, il n'y en a pas. Cependant, on peut souvent inclure des balises HTML au milieu du Markdown. Ce sera dans la partie avancée...

!!! tip "Astérisque et tiret-bas"
    === "L'emphase faible"
        !!! note "Entrée"

            ```markdown
            _blabla_
            ```

        !!! done "Rendu"
            _blabla_

        ??? info "HTML"
            ```html
            <em>blabla</em>
            ```

    === "L'emphase forte"
        !!! note "Entrée"
            ```markdown
            **blabla**
            ```

        !!! done "Rendu"
            **blabla**

        ??? info "HTML"
            ```html
            <strong>blabla</strong>
            ```

    === "Des mélanges"
        !!! note "Entrée"
            ```markdown
            **blabla**
            ```
        !!! done "Rendu"
            **blabla**

        ??? info "HTML"
            ```html
            <em>blabla</em>
            ```

### Citations

!!! tip "Avec un chevron"
    Suivant l'ancien modèle sur les mails en mode texte, quand on répond à un message, le texte est décalé et chaque ligne est précédée d'un chevron `>`.

    === "Exemple simple"
        !!! note "Entrée"
            ```markdown
            > **Cookie** :
            >
            > - Anciennement petit gâteau sucré, qu'on acceptait avec plaisir.
            > - Aujourd'hui : petit fichier informatique drôlement salé, qu'il faut refuser avec véhémence.

            De Luc Fayard, _Dictionnaire impertinent des branchés_
            ```
            
        !!! done "Rendu"
            > **Cookie** :
            >
            > - Anciennement petit gâteau sucré, qu'on acceptait avec plaisir.
            > - Aujourd'hui : petit fichier informatique drôlement salé, qu'il faut refuser avec véhémence.

            De Luc Fayard, _Dictionnaire impertinent des branchés_

    === "Citations imbriquées"
        blabla à suivre...

### Bloc de code

Par décalage.

Par nommage.

### Code en ligne

Avec `` ` ``

### Ligne horizontale

Avec `---`
