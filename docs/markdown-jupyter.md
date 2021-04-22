# Markdown pour Jupyter

## Vocabulaire et objectifs

!!! info "Markdown"
    [Markdown](https://fr.wikipedia.org/wiki/Markdown) est un langage de balisage léger qui est traduit en HTML, langage que le navigateur est capable de lire pour produire une page web.

    On peut aussi, à partir d'un fichier Markdown, produire un fichier `.pdf`, ou `.odt`, ou `.docx` en utilisant l'utilitaire [Pandoc](https://fr.wikipedia.org/wiki/Pandoc). Nous ne nous en servirons pas ici.

    Il ne faut que **5 minutes pour avoir les bases** suffisantes.

!!! tip "Utilisation répandue"
    On peut utiliser la syntaxe Markdown dans de nombreuses situations de travail collaboratif.

    - Dans des forums, comme Discourse, **GitLab**, Reddit, Qt, Stack Overflow et Stack Exchange parmi d'autres.
    - Dans des logiciels, comme CodiMD, **Jupyter**, ou **MkDocs** parmi d'autres.

!!! warning "Défauts"
    Soyons honnête, il y a un défaut majeur, Markdown n'est pas unifié.

    - Il existe plusieurs variantes légèrement différentes de Markdown.
    - Pour chaque variante, il peut exister des moteurs de rendus légèrement différents.

    Nous utiliserons ici la partie commune à toute les versions, avec le style le plus commun possible, ce sera en particulier utile pour travaille avec **Jupyter**.
    
    Dans la partie suivante nous travaillerons avec certaines facilités offertes par **MkDocs**.

!!! example "D'autres tutoriels"
    === "En anglais"
        - [Markdown Guide](https://www.markdownguide.org/) ; assez complet.
        - [Markdown Tutorial](https://www.markdowntutorial.com/) ; avec exercices, (multilingue, mais ...)
        - [Tutorial.md](http://agea.github.io/tutorial.md/) ; interactif, mérite une traduction !

    === "En français"
        - [Élaboration et conversion de documents avec Markdown et Pandoc](https://enacit1.epfl.ch/markdown-pandoc/) ; pour les utilisateurs avancés.

## Construire une note

### Quelques exemples

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

    ??? example "Example concret"

        Pour cette page, le brouillon de structure a commencé ainsi

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

### Sauter une ligne

!!! tip "Sans changer de paragraphe"
    On ajoute deux espaces à la fin d'une ligne.

    === "Correct"
        !!! note "Entrée"

            ```markdown
            ligne1  
            ligne2
            ```

        !!! done "Rendu"
            ligne1  
            ligne2

    === "Incorrect"
        !!! note "Entrée"

            ```markdown
            ligne1
            ligne2
            ```

        !!! done "Rendu"
            ligne1
            ligne2
    
    !!! info "Vérifier"
        En sélectionnant le texte, vous verrez deux espaces à la fin de `ligne 1` dans l'entrée correcte.

        Sans les deux espaces, le saut de ligne est considéré comme une unique espace entre les deux lignes, donc une seule ligne pour le navigateur.

        C'est pratique d'avoir son code sans longue ligne, elles sont donc recollées ensuite. C'est une bonne pratique.

        On n'utilise que rarement des sauts de ligne sans changer de paragraphes, vous ne devriez pas en faire, sauf raison motivée. On laisse au navigateur le soin de couper les lignes en fonction de l'affichage disponible : écran large, moyen ou restreint sur téléphone.

!!! warning "Éditeur"
    - Certains éditeurs de texte suppriment les espaces de fin de ligne ; votre document serait modifié !
    - **Conseil** : il est possible, avec son éditeur, d'afficher discrètement les espaces ; c'est une bonne pratique.

### Ligne horizontale

!!! tip "Séparer deux paragraphes"
    On utilise `---` entre les deux paragraphes, avec des lignes vides.

    !!! note "Entrée"

        ```markdown
        Paragraphe 1...

        ---

        Paragraphe 2...
        ```

    !!! done "Rendu"
        Paragraphe 1...

        ---

        Paragraphe 2...

### Listes

!!! tip "Une ligne vide puis..."
    Une liste, comme un nouveau paragraphe, doit être précédée d'une ligne vide.

    Ensuite, on place chaque item sur une ligne en commençant par `-`

    On peut faire des listes numérotées en commençant par `1.`
    
    On place aussi une espace juste avant son item.


    !!! abstract "Liste à puce"
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
            <p>Markdown est <strong>très</strong> utilisé sur de <em>nombreux</em> forums</p>
            <ul>
            <li>Discourse</li>
            <li>GitLab</li>
            <li>Reddit</li>
            <li>Qt</li>
            <li>Stack Overflow</li>
            <li>Stack Exchange</li>
            <li>...</li>
            </ul>
            ```

        On remarquera un peu de mise de style (l'emphase) ; nous y reviendrons.

        On remarque aussi une meilleure lisibilité du Markdown sur le HTML.

    !!! example "Liste numérotée"
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

        Pour information, la traduction pour le navigateur.
        ??? info "Code HTML"

            ```html
            <p>Pour une liste numérotée, la numérotation est automatique !</p>
            <ol>
            <li>Mon premier exemple</li>
            <li>Le troisième, mais le deuxième a été effacé</li>
            <li>Un oubli entre le troisième et quatrième</li>
            <li>Encore un oubli...</li>
            <li>C&#39;était le quatrième au départ.</li>
            <li>Juste un de plus qui sera numéroté correctement.</li>
            </ol>
            ```
        
        On remarque que l'on n'a pas à se soucier de la cohérence de la numérotation dans le source, on peut donc ajouter, ou enlever des items sans revoir la numérotation.

### Liens

!!! tip "Créer un lien avec une URL"
    Une [URL](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) permet d'identifier une ressource et le protocole associé.

    La syntaxe est `[<objet>](<url>)`.
    
    - `<objet>` pourra être du texte ou une image, ou autre.
    - `<url>` pourra être une adresse web, ou mail, ou autre protocole.
    - Une adresse web peut pointer vers un document HTML, une image, un son...

    === "Adresse web"
        !!! note "Entrée"

            ```markdown
            Voici [un lien](https://startpage.com/) vers un moteur de recherche.
            ```
        
        !!! done "Rendu"
            Voici [un lien](https://startpage.com/) vers un moteur de recherche.
    
    === "Adresse mail"
        !!! note "Entrée"

            ```markdown
            Pour [écrire](mailto:john.doe@mail.com) à quelqu'un.
            ```
        
        !!! done "Rendu"
            Pour [écrire](mailto:john.doe@mail.com) à quelqu'un.
    
    === "Numéro de téléphone"
        !!! note "Entrée"

            ```markdown
            Pour [contacter rapidement](tel:+33 1 234 567 890) ce numéro.
            ```
        
        !!! done "Rendu"
            Pour [contacter rapidement](tel:+33 1 234 567 890) ce numéro.
        
        Le lien ne fonctionnera que si la page est lue avec un navigateur qui a accès au protocole. Concrètement, sur un smartphone !

### Emphase

!!! info "Pas trop gras svp !"
    Commençons par indiquer que certains documents abusent des effets de style et la lisibilité en est réduite.

    L'emphase sert à faire ressortir une partie plus importante que le reste. Ce ne peut être qu'_une_ petite partie.

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
        Le tiret-bas est recommandé sur l'astérisque.

        !!! note "Entrée"

            ```markdown
            Du _texte en italique_ entouré de la balise tiret bas *ou* une étoile.
            ```

        !!! done "Rendu"
            Du _texte en italique_ entouré de la balise tiret bas *ou* une étoile.

        ??? info "HTML"

            ```html
            <p>Du <em>texte en italique</em> entouré de la balise tiret bas <em>ou</em> une étoile.</p>
            ```

    === "L'emphase forte"
        L'astérisque est recommandé sur le tiret-bas.

        !!! note "Entrée"

            ```markdown
            Du **texte en gras** entouré de la balise double étoile, __ou__ double tiret bas.
            ```

        !!! done "Rendu"
            Du **texte en gras** entouré de la balise double étoile, __ou__ double tiret bas.


        ??? info "HTML"

            ```html
            <p>Du <strong>texte en gras</strong> entouré de la balise double étoile, <strong>ou</strong> double tiret bas.</p>
            ```

    === "Des mélanges"
        !!! note "Entrée"

            ```markdown
            **_Un_** exemple _avec_ tous *les* cas *__possibles__*, **fort1** ou __fort2__.
            ```

        !!! done "Rendu"
            **_Un_** exemple _avec_ tous *les* cas *__possibles__*, **fort1** ou __fort2__.


        ??? info "HTML"

            ```html
            <p><strong><em>Un</em></strong> exemple <em>avec</em> tous <em>les</em> cas <em><strong>possibles</strong></em>, <strong>fort1</strong> ou <strong>fort2</strong>.</p>
            ```

!!! warning "Recommandation"
    !!! note "Entrée"

        ```markdown
        - Pour l'emphase faible, _un_ tiret-bas.
        - Pour l'emphase forte, **deux** astérisques.
        ```

    !!! done "Rendu"
        - Pour l'emphase faible, _un_ tiret-bas.
        - Pour l'emphase forte, **deux** astérisques.

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
        Voici un example de mail qu'on peut recevoir, témoin d'un échange. Quand un mail est long, on peut avoir envie de répondre dans la partie associée et non tout d'un bloc au départ.
        
        L'un dit « Salut ; À+», l'autre dit « Bonjour ; Merci ».

        !!! note "Entrée"

            ```markdown
            Salut, c'est bon pour dimanche, pour le reste je réponds dans le corps du mail.
            À+
            > Bonjour,  
            > un long blabla...  
            > avec une question pour dimanche.  
            > Et une autre question_1.  

            Réponse à question_1.  

            > Sinon blabla, et question_2.  

            Réponse à question_2.  

            > > Salut,  
            > > Tu fais quoi dimanche ?  
            > > À+  
            
            > Alors, je pense que...  
            > Merci et bonne journée  
            ```
            
        !!! done "Rendu"
            Salut, c'est bon pour dimanche, pour le reste je réponds dans le corps du mail.
            À+
            > Bonjour,  
            > un long blabla...  
            > avec une question pour dimanche.  
            > Et une autre question_1.  

            Réponse à question_1.  

            > Sinon blabla, et question_2.  

            Réponse à question_2.  

            > > Salut,  
            > > Tu fais quoi dimanche ?  
            > > À+  

            > Alors, je pense que...  
            > Merci et bonne journée  

### Code en ligne

!!! tip "Avec l'accent grave"
    Avec un clavier azerty, ++altgr+8++ donne l'[accent grave](https://fr.wikipedia.org/wiki/Accent_grave) `` ` ``

    On utilise la syntaxe : ``Du texte avec un `identifiant` de code``.

    === "Correct"
        !!! note "Entrée"

            ```markdown
            La définition de la fonction `est_premier` commence avec le mot clé `def`

            Elle prend en paramètre un entier `n`

            Elle renvoie un booléen avec le mot clé `return`
            ```

        !!! done "Rendu"
            La définition de la fonction `est_premier` commence avec le mot clé `def`

            Elle prend en paramètre un entier `n`

            Elle renvoie un booléen avec le mot clé `return`
    
    === "Incorrect"
        !!! note "Entrée"

            ```markdown
            La définition de la fonction _est_premier_ commence avec le mot clé **def**

            Elle prend en paramètre un entier _n_

            Elle renvoie un booléen avec le mot clé **return**
            ```

        !!! done "Rendu"
            La définition de la fonction _est_premier_ commence avec le mot clé **def**

            Elle prend en paramètre un entier _n_

            Elle renvoie un booléen avec le mot clé **return**
    
    === "Le futur"
        !!! note "Entrée"

            ```markdown
            La définition de la fonction `#!py3 est_premier` commence avec le mot clé `#!py3 def`

            Elle prend en paramètre un entier `#!py3 n`

            Elle renvoie un booléen avec le mot clé `#!py3 return`
            ```

        !!! done "Rendu"
            La définition de la fonction `#!py3 est_premier` commence avec le mot clé `#!py3 def`

            Elle prend en paramètre un entier `#!py3 n`

            Elle renvoie un booléen avec le mot clé `#!py3 return`

        Ceci n'est possible qu'avec MkDocs, on peut donc avoir la coloration syntaxique en ligne avec des langages variés. Nous y reviendrons plus tard.
