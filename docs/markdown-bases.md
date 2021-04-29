# Markdown

Auteur : Franck CHAMBON

## Vocabulaire et objectifs

!!! info "Markdown"
    [Markdown](https://fr.wikipedia.org/wiki/Markdown) est un langage de balisage léger qui est traduit en HTML, langage que le navigateur est capable de lire pour produire une page web.

    On peut aussi, à partir d'un fichier Markdown `.md`, produire un fichier `.pdf`, ou `.odt`, ou `.docx` en utilisant l'utilitaire [Pandoc](https://fr.wikipedia.org/wiki/Pandoc). Nous ne nous en servirons pas ici.

    Il ne faut que **5 minutes pour avoir les bases** suffisantes.

!!! tip "Utilisation répandue"
    On peut utiliser la syntaxe Markdown dans de nombreuses situations de travail collaboratif.

    - Dans des forums, comme Discourse, **GitLab**, Reddit, Qt, Stack Overflow et Stack Exchange parmi d'autres.
    - Dans des logiciels, comme **CodiMD**, **Jupyter**, ou **MkDocs** parmi d'autres.

!!! warning "Défaut"
    Soyons honnêtes, il y a un défaut, Markdown n'est pas unifié.

    - Il existe plusieurs variantes légèrement différentes de Markdown.
    - Pour chaque variante, il peut exister des moteurs de rendus légèrement différents.

    Nous utiliserons ici la partie commune à toutes les versions, avec le style le plus commun possible, ce sera en particulier utile pour travailler avec **Jupyter**.
    
    Dans la partie suivante nous travaillerons avec certaines facilités offertes par **MkDocs**.

!!! example "D'autres tutoriels"
    === "En anglais"
        - [Markdown Guide](https://www.markdownguide.org/) ; assez complet.
        - [Markdown Tutorial](https://www.markdowntutorial.com/) ; avec exercices, (multilingue, mais ...)
        - [Tutorial.md](http://agea.github.io/tutorial.md/) ; interactif, mérite une traduction !

    === "En français"
        - [Élaboration et conversion de documents avec Markdown et Pandoc](https://enacit1.epfl.ch/markdown-pandoc/) ; pour les utilisateurs avancés.

## Les bases de Markdown

!!! tip "Quelques exemples"
    |Objectif|Markdown|Rendu|
    |:-----|:------|:----|
    |Créer un lien|`[texte cliquable](https://mon_lien.fr)`|[texte cliquable](https://mon_lien.fr)|
    |Emphase faible|`Un _mot_ discret` | Un _mot_ discret |
    |Emphase forte|`Un **mot** visible` | Un **mot** visible |
    |Du code en ligne|``Une boucle `for` `` |Une boucle `for`|

### Architecture

!!! tip "La première étape"
    Un document doit être structuré en parties et sous parties.

    Le titre d'une partie (ou en-têtes) est précédé d'un ou plusieurs croisillons : `#`

    Sur un clavier azerty, Le croisillon s'obtient avec ++altgr+3++.

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

        :warning: Ce rendu dépend du moteur...

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

    Il ne faut pas indenter son paragraphe dans le fichier source.

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
        
        !!! fail "Rendu"

            <pre>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at cursus nibh, et lobortis mauris. Sed tempus turpis quis turpis pulvinar, ac vehicula dui convallis. Phasellus tempus massa quam, ac mollis libero cursus eget. Donec convallis a nisl vitae scelerisque. Ut vel nisl id augue ullamcorper lobortis at id dolor.
            </pre>

        :warning: Le texte devient du code en bloc, avec une police à chasse fixe.

### Aller à la ligne

!!! tip "Sans changer de paragraphe"
    Dans de **rares** cas, si on souhaite sauter de ligne, sans changer de paragraphe, on ajoute deux espaces à la fin d'une ligne.

    === "Correct"
        !!! note "Entrée"

            ```markdown
            ligne1␣␣  
            ligne2
            ```

        !!! done "Rendu"
            ligne1  
            ligne2
        
        🤞 : On a symbolisé les deux espaces avec `␣␣`, mais **il faut utiliser l'espace classique**. `␣␣` ne sert que d'illustration.

    === "Incorrect"
        !!! note "Entrée"

            ```markdown
            ligne1
            ligne2
            ```

        !!! fail "Rendu"
            ligne1
            ligne2

        :warning: Échec uniquement si on voulait forcer un saut de ligne.
    
    !!! info "Deux espaces ou plus"
        En sélectionnant le texte, vous verrez deux **véritables** espaces à la fin de `ligne 1` dans l'entrée correcte.

        Sans les deux espaces, le saut de ligne est considéré comme une unique espace entre les deux lignes, donc une seule ligne pour le navigateur.

        On peut mettre plus de deux espaces.

    !!! tip "Bonne pratique"
        Il est pratique d'avoir son code sans longue ligne,
        on peut donc les couper **dans le source où on veut**.
        Elles sont donc recollées ensuite, dans un seul paragraphe.
        Ce paragraphe sera adapté à chaque écran, c'est au navigateur de choisir les sauts de ligne.
        C'est une bonne pratique.

        On n'utilise que **rarement** des sauts de ligne forcés (avec les deux espaces en fin de ligne), sans changer de paragraphes, vous ne devriez pas en faire, sauf raison motivée. On laisse au navigateur le soin de couper les lignes en fonction de l'affichage disponible : écran large, moyen ou restreint sur téléphone.

!!! warning "Éditeur"
    - Certains éditeurs de texte suppriment les espaces de fin de ligne ; votre document serait modifié !
    - **Conseil** : il est possible, avec son éditeur, d'afficher discrètement les espaces ; c'est une bonne pratique.

### Ligne horizontale

!!! tip "Séparer deux paragraphes"
    On utilise `---` entre les deux paragraphes, avec des lignes vides de part et d'autre.

    === "Correct"
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

    === "Incorrect"
        !!! note "Entrée"

            ```markdown
            Paragraphe 1...
            ---
            Paragraphe 2...
            ```

        !!! fail "Rendu"
            <big>**Paragraphe 1...**</big>

            Paragraphe 2...
        
        :warning: Il s'agit en fait d'une **méthode non recommandée** pour créer des en-têtes !

### Listes

!!! tip "Une ligne vide puis..."
    Une liste, comme un nouveau paragraphe, **doit être précédée d'une ligne vide**.
    Certains moteurs Markdown acceptent qu'il n'y ait pas de saut de ligne, comme avec Jupyter,
     mais pas tous.
    
    !!! info "Les règles"
        - Sauter une ligne avant la première puce.
        - Ensuite, on place chaque item sur une ligne en commençant par `-`
        - On peut faire des listes numérotées en commençant par `1.`
        - On place aussi une espace juste avant son item.


    !!! abstract "Liste à puce"
        !!! note "Entrée"

            ```markdown
            Markdown est **très** utilisé dans de _nombreuses_ situations

            - Jupyter
            - MkDocs
            - Discourse
            - GitLab
            - Reddit
            - Qt
            - Stack Overflow
            - Stack Exchange
            - ...
            ```

        !!! done "Rendu"
            Markdown est **très** utilisé dans de _nombreuses_ situations

            - Jupyter
            - MkDocs
            - Reddit
            - Qt
            - Stack Overflow
            - Stack Exchange
            - ...

        Pour information, la traduction pour le navigateur.
        ??? info "Code HTML"

            ```html
            <p>Markdown est <strong>très</strong> utilisé dans de <em>nombreuses</em> situations</p>
            <ul>
            <li>Jupyter</li>
            <li>MkDocs</li>
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

!!! warning "Technique avancée"
    On peut imbriquer les listes numérotées ou non.

    On indente la liste imbriquée qu'il est inutile de séparer avec des lignes vides. Contrairement à la première liste.

    !!! note "Entrée"

        ```markdown
        1. un
        1. deux
            - machin
            - chose
                31. Pour commencer à 31
                1984. Ce ne sera pas 1984 !
        1. trois
        ```

    !!! done "Rendu"
        1. un
        1. deux
            - machin
            - chose
                31. Pour commencer à 31
                1984. Ce ne sera pas 1984 !
        1. trois
    
    :warning: Le rendu de la numérotation des listes imbriquées dépend du moteur. Ne pas lui faire confiance.

    De même, on peut imbriquer des paragraphes, des blocs de code, en les indentant en plus également de la même manière.

!!! info "Autres puces, indentation"
    Avec certains moteurs Markdown, il est possible d'utiliser les puces `*`, `-`, `+`.

    Nous ne recommandons d'**utiliser que les puces `-`**.

    Pour les listes imbriquées, nous recommandons une **indentation de 4 espaces**.

### Liens

!!! tip "Créer un lien avec une URL"
    Une [URL](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) permet d'identifier une ressource et le protocole associé.

    La syntaxe est `[<objet>](<url>)`
    
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

    !!! warning "Technique avancée"
        On peut ajouter une info bulle au lien.

        La syntaxe est `[<objet>](<url> "<message>")`

        !!! note "Entrée"

            ```markdown
            Un autre moteur de recherche est [DuckDuckGo](https://duckduckgo.com/ "Votre confidentialité, simplifiée").
            ```
        
        !!! done "Rendu"
            Un autre moteur de recherche est [DuckDuckGo](https://duckduckgo.com/ "Votre confidentialité, simplifiée").

    !!! done "Technique simplifiée"
        Si on souhaite simplement activer l'url, sans changer le nom, ni mettre d'info-bulle.

        La syntaxe est `< url >`

        Le protocole est automatiquement déduit.

        !!! note "Entrée"

            ```markdown
            - Mon site web <https://mon_joli_site.fr>
            - Mon mail <prénom.nom@chez.moi>
            ```

        !!! done "Rendu"
            - Mon site web <https://mon_joli_site.fr>
            - Mon mail <prénom.nom@chez.moi>

### Emphase

!!! info "Pas trop gras svp !"
    Commençons par indiquer que certains documents abusent des effets de style et la lisibilité en est réduite.

    L'emphase sert à faire ressortir une partie plus importante que le reste. Ce ne peut être qu'_une_ petite partie.

!!! abstract "Définitions"
    - L'emphase faible sert à faire ressortir discrètement du texte. Elle est **souvent** en _italique_, mais on peut changer cela dans une feuille de style en cascade (CSS).
    - De même, l'emphase forte est souvent en gras, mais on pourrait décider dans la feuille CSS de modifier ce style en couleur rouge et souligné en noir. Et puis changer un autre jour ; l'ensemble du document soumis à la feuille CSS est modifié.

    ??? info "Balises HTML"
        - `<em>` pour l'emphase faible
        - `<strong>` pour l'emphase forte
        - il en existe d'autres.
        - En Markdown, on peut aussi inclure quelques balises HTML au milieu du Markdown. Ce sera dans la partie avancée... Dans un premier temps, on recommande de ne pas en inclure.

!!! tip "Astérisque et tiret-bas"
    === "L'emphase faible"
        Le tiret-bas est recommandé.

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
        L'astérisque est recommandé.

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

### Code en bloc

!!! tip "En indentant le bloc, 4 espaces"
    La méthode simple pour qu'un extrait ne soit pas formaté est de décaler le bloc de 4 espaces ou plus. On saute également une ligne avant et après, comme pour un paragraphe.

    === "Correct"
        !!! note "Entrée"

            ```markdown
            Voici un code Python

                n = 47**2 + 31**2
            ```

        !!! done "Rendu"
            Voici un code Python

                n = 47**2 + 31**2

    === "Incorrect"
        !!! note "Entrée"

            ```markdown
            Voici un code Python

            n = 47**2 + 31**2
            ```

        !!! fail "Rendu"
            Voici un code Python

            n = 47**2 + 31**2
        
        :warning: Ici le moteur a interprété une partie avec de l'emphase forte.

!!! info "Et la coloration syntaxique ?"
    Nous verrons cela dans [une partie de Markdown avancé](#coloration-syntaxique-du-code).

### Code en ligne

!!! tip "Avec l'accent grave"
    Avec un clavier azerty, ++altgr+8++ donne l'[accent grave](https://fr.wikipedia.org/wiki/Accent_grave) `` ` ``

    On utilise la syntaxe : ``Du texte avec un `identifiant` de code``.

    === "Correct"
        !!! note "Entrée"

            ```markdown
            La définition de la fonction `premier` commence avec le mot clé `def`

            Elle prend en paramètre un entier `n`

            Elle renvoie un booléen avec le mot clé `return`
            ```

        !!! done "Rendu"
            La définition de la fonction `premier` commence avec le mot clé `def`

            Elle prend en paramètre un entier `n`

            Elle renvoie un booléen avec le mot clé `return`
    
    === "Incorrect"
        !!! note "Entrée"

            ```markdown
            La définition de la fonction _premier_ commence avec le mot clé **def**

            Elle prend en paramètre un entier _n_

            Elle renvoie un booléen avec le mot clé **return**
            ```

        !!! fail "Rendu"
            La définition de la fonction _premier_ commence avec le mot clé **def**

            Elle prend en paramètre un entier _n_

            Elle renvoie un booléen avec le mot clé **return**

        :warning: Les effets de texte ne servent pas à désigner des bouts de code.
    
    === "Le futur avec MkDocs"
        !!! note "Entrée"

            ```markdown
            La définition de la fonction `#!py3 premier` commence avec le mot clé `#!py3 def`

            Elle prend en paramètre un entier `#!py3 n`

            Elle renvoie un booléen avec le mot clé `#!py3 return`
            ```

        !!! done "Rendu"
            La définition de la fonction `#!python premier` commence avec le mot clé `#!python def`

            Elle prend en paramètre un entier `#!python n`

            Elle renvoie un booléen avec le mot clé `#!python return`

        Ceci n'est possible qu'avec MkDocs, et des extensions, on peut donc avoir la coloration syntaxique en ligne avec des langages variés. **Nous y reviendrons plus tard.**

    !!! warning "Technique avancée"
        Si on souhaite écrire du code en ligne qui contient des `` ` ``,
         il suffit d'encadrer le morceau avec plus de `` ` `` qu'il n'y en a consécutivement dans le morceau.
        === "Exemple simple"
            !!! note "Entrée"
                ```markdown
                Afficher **du code** avec accent grave : `` un entier `n` ``
                ```

            !!! done "Rendu"
                Afficher **du code** avec accent grave : `` un entier `n` ``

        === "Exemple élaboré"
            !!! note "Entrée"
                ```markdown
                - Afficher 1`` ` `` : `` ` ``
                - Afficher  2`` ` `` : ``` `` ```
                - Afficher le code précédent : ```` - Afficher  2`` ` `` : ``` `` ``` ````
                ```

            !!! done "Rendu"
                - Afficher 1`` ` `` : `` ` ``
                - Afficher  2`` ` `` : ``` `` ```
                - Afficher le code précédent : ```` - Afficher  2`` ` `` : ``` `` ``` ````

### Images

!!! tip "Un lien précédé de `!`"
    La syntaxe est avec ou sans l'info-bulle

    - `![<texte alternatif>](<url> "<info-bulle>")`
    - `![<texte alternatif>](<url>)`

    !!! note "Entrée"

        ```markdown
        Le logo du langage Markdown
        
        ![M, flèche vers le bas](https://fr.wikipedia.org/wiki/Markdown#/media/Fichier:Markdown-mark.svg "sur Wikipédia")
        ```
    
    !!! done "Rendu"
        Le logo du langage Markdown
        
        ![M, flèche vers le bas](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)

!!! info "Texte alternatif"
    Une bonne pratique est de renseigner un texte alternatif, il est utilisé par les robots.

    - Certains robots lisent à voix haute le contenu pour des humains, les images sont remplacées par le texte alternatif lu. Utile pour les mal-voyants.
    - Certains robots font de l'indexation de site, un bon texte alternatif aide au référencement.
    - Si la cible n'est plus disponible, cela arrive, le texte alternatif remplace l'image.

!!! warning "absolu ou relatif"
    Il faut faire attention à bien écrire son url.

    - Si c'est en local, vérifier le chemin d'accès.
    - Si c'est sur le web, bien préfixer avec le protocole `http`

### Tableaux

!!! tip "Avec le tube"
    Le caractère `|` ([barre verticale](https://fr.wikipedia.org/wiki/Barre_verticale) ou tube) s'obtient avec ++altgr+6++.

    On construit un tableau suivant le modèle suivant.

    !!! note "Entrée"

        ```markdown
        | Objectif | Markdown | Rendu |
        |---------|-------------|---|
        | Créer un lien    | `[texte cliquable](https://mon_lien.fr)` | [texte cliquable](https://mon_lien.fr) |
        | Emphase faible   | `Un _mot_ discret`    | Un _mot_ discret   |
        | Emphase forte    | `Un **mot** visible`  | Un **mot** visible |
        | Du code en ligne | ``Une boucle `for` `` | Une boucle `for`   |
        ```
    
    !!! done "Rendu"
        | Objectif | Markdown | Rendu |
        |----------|----------|-------|
        | Créer un lien    | `[texte cliquable](https://mon_lien.fr)` | [texte cliquable](https://mon_lien.fr) |
        | Emphase faible   | `Un _mot_ discret`    | Un _mot_ discret   |
        | Emphase forte    | `Un **mot** visible`  | Un **mot** visible |
        | Du code en ligne | ``Une boucle `for` `` | Une boucle `for`   |

    ??? bug "HTML"
        Un code équivalent est bien plus délicat à écrire à la main, à lire et à maintenir...

        ```html
        <table>
        <thead>
        <tr>
        <th>Objectif</th>
        <th>Markdown</th>
        <th>Rendu</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>Créer un lien</td>
        <td><code>[texte cliquable](https://mon_lien.fr)</code></td>
        <td><a href="https://mon_lien.fr">texte cliquable</a></td>
        </tr>
        <tr>
        <td>Emphase faible</td>
        <td><code>Un _mot_ discret</code></td>
        <td>Un <em>mot</em> discret</td>
        </tr>
        <tr>
        <td>Emphase forte</td>
        <td><code>Un **mot** visible</code></td>
        <td>Un <strong>mot</strong> visible</td>
        </tr>
        <tr>
        <td>Du code en ligne</td>
        <td><code>Une boucle `for` </code></td>
        <td>Une boucle <code>for</code></td>
        </tr>
        </tbody>
        </table>
        ```

    !!! info "Quelques informations"
        - Il n'est **pas nécessaire** que les tubes soient bien alignés.
        - On peut inclure du Markdown dans les cellules.
        - La seconde ligne propose des options pour chaque colonne.
            - `|:---|` pour un alignement de la colonne à gauche
            - `|---:|` pour un alignement de la colonne à droite
            - `|:--:|` pour une colonne centrée

## Exercices simples

### Facile 1

...

### Autre

...

### (NSI) Tableau donné par Python

!!! tip "Liste Python vers Markdown"
    Donner une fonction Python qui renvoie un texte en Markdown : le tableau de valeur pour une suite donnée en paramètre avec une liste.

    ```python
    def tableau_markdown(liste: list) -> str:
        lignes = []
        ajout = lignes.append
        # ... à compléter
        return "\n".join(lignes)
    ```

!!! example "Exemple"
    Pour la liste $[0, 1, 1, 2, 3, 5, 8, 13]$, on souhaite un premier rendu

    |n|0|1|2|3|4|5|6|7|
    |-|-|-|-|-|-|-|-|-|
    |u_n|0|1|1|2|3|5|8|13|

    _Un_ code Markdown valable est

    ```markdown
    |n|0|1|2|3|4|5|6|7|
    |-|-|-|-|-|-|-|-|-|
    |u_n|0|1|1|2|3|5|8|13|
    ```

    Ainsi on aimerait avoir

    ```python
    >>> tableau_markdown([0, 1, 1, 2, 3, 5, 8, 13])
    '|n|0|1|2|3|4|5|6|7|\n|-|-|-|-|-|-|-|-|-|\n|u_n|0|1|1|2|3|5|8|13|\n'
    ```

[Résoudre en ligne](https://console.basthon.fr/?script=eJx9UdtqAjEQfV_YfxjigwprcHe1imAfWvraH1Ap6e5YYmOyzaW1kI_pq9_hjzVpqhSEzgRCZs6cc5K0uAXLngUy97Rn-rVVH3IguLG4gLgNYXQLxupFnkEIwV8kGljCapMKbKecDefUoKzrULap1QNKKZy-oFH7TpyOFnVqaLROSyBrSehO8agXh4d5FpMQkmc9eDigbniDsXR_IYh0HdOWa2gRBEu6MC-gc9wAHk7HxkWcwCDbIo3jjxhmDOxVy7c89BqEN9fnAj6BAcrAZIxyJjI2aC0mUnoxE-1YNBbKPGPGoLbXT7YaF1D-rKqAuoBpEU2V9WYIyyWs08VD9L30Y1_6ytd-4qf-xs_8WvrRVYaie0rYhJ76uS_rUO__cVT942hSRQP1LFk4C1_EfgUmlY-gM2-nubQDcqfZuyLhR74B39mmdg){.md-button}

??? faq "Indice 1"
    Pour construire la ligne 2, on pourrait faire

    ```python
    q = len(liste)
    ligne_2 = '|-'*(q+1) + '|'
    ajout(ligne_2)
    ```

??? faq "Indice 2"
    Pour construire la ligne 1, on pourrait faire

    ```python
    q = len(liste)
    ligne_1 = ['|n|'] # le début de la ligne 1
    for i in range(q):
        ligne_1.append(f'{i}|') # chaque morceau
    ajout("".join(ligne_1))
    ```

??? faq "Indice 3"
    La ligne 3 est très proche de la ligne 1.

??? faq "Indice 4"
    Vide.

??? done "Solution"

    ```python
    def tableau_markdown(liste: list) -> str:
        lignes = []
        ajout = lignes.append

        # ligne 1
        q = len(liste)
        ligne_1 = ['|n|'] # le début de la ligne 1
        for i in range(q):
            ligne_1.append(f'{i}|') # chaque morceau
        ajout("".join(ligne_1))

        # ligne 2
        ligne_2 = '|-'*(q+1) + '|'
        ajout(ligne_2)

        # ligne 3
        ligne_3 = ['|u_n|'] # le début de la ligne 3
        for i in range(q):
            ligne_3.append(f'{liste[i]}|') # chaque morceau
        ajout("".join(ligne_3))
        
        # ligne 4 vide !
        ajout('')

        return "\n".join(lignes)
    ```

## Markdown avancé

### Coloration syntaxique du code

!!! tip "Quelques exemples de programmes"
    === "Correct"
        !!! note "Entrée"
            ````markdown
            ```python
            for i in range(10):
                print("Salut à tous !")
            ```

            ```c
            #include<stdio.h>
            int main(){
                int i;
                for(i = 0; i < 10; i++){
                    printf("Salut à tous !\n");
                }
                return 0;
            }
            ```
            ````

        !!! done "Rendu"
            ```python
            for i in range(10):
                print("Salut à tous !")
            ```

            ```c
            #include<stdio.h>
            int main(){
                int i;
                for(i = 0; i < 10; i++){
                    printf("Salut à tous !\n");
                }
                return 0;
            }
            ```

    === "Incorrect"
        !!! note "Entrée"
            ````markdown
            for i in range(10):
                print("Salut à tous !")

            #include<stdio.h>
            int main(){
                int i;
                for(i = 0; i < 10; i++){
                    printf("Salut à tous !\n");
                }
                return 0;
            }
            ````

        !!! fail "Rendu"
            for i in range(10):
                print("Salut à tous !")

            \#include<stdio.h>
            int main(){
                int i;
                for(i = 0; i < 10; i++){
                    printf("Salut à tous !\n");
                }
                return 0;
            }

        :warning: On perd l'indentation et on peut avoir des effets non désirés !

!!! abstract "Méthode"
    Il suffit d'écrire
    
    - avant le bloc ```` ```<nom_du_langage> ````
    - après le bloc ```` ``` ````
    
    La [liste des langages supportés](https://support.codebasehq.com/articles/tips-tricks/syntax-highlighting-in-markdown) contient entre autres aussi :

    - `bash`, `diff` et `console`
    - `markdown`
    - `latex`, `tex` et `asy`
    - `html` et `css`
    - `ocaml`
    - `sql`
    - `yaml`

??? warning "Utilisation avancée"
    Suivant le même principe que pour le code en ligne, pour donner une coloration syntaxique à un bloc qui contient lui-même un bloc, on peut utiliser un accent grave `` ` `` supplémentaire dans les délimiteurs. Exemple :

    === "Correct"
        !!! note "Entrée"
            `````markdown
            ````markdown
            ```python
            print("Salut")
            ```

            ```c
            puts("Salut");
            ```
            ````
            `````
        !!! done "Rendu"
            ````markdown
            ```python
            print("Salut")
            ```

            ```c
            puts("Salut");
            ```
            ````
        Le code source de ce document comportait
        
        ``````markdown
        `````markdown
        ...
        `````
        ``````
        
        Ceci pour afficher l'entrée correcte, et deux blocs de 6 `` ` ``, pour afficher cette remarque.
    === "Incorrect"
        !!! note "Entrée"
            `````markdown
            ```markdown
            ```python
            print("Salut")
            ```

            ```c
            puts("Salut");
            ```
            ```
            `````
        !!! fail "Rendu"
            ```markdown
            ```python
            print("Salut")
            ```

            ```c
            puts("Salut");
            ```
            ```
        :warning: Rien ne peut être structuré...

!!! info "Numérotation des lignes, et marquage"
    - Il suffit d'ajouter `linenums="1"` (ou un autre nombre) pour faire débuter la numérotation.
    - Pour marquer des lignes en particulier, on utilise `hlines="<tranches et numéros>"`

    === "numérotation classique"
        !!! note "Entrée"
            ````markdown
            ```python linenums="1"
            def bubble_sort(items):
                for i in range(len(items)):
                    for j in range(len(items) - 1 - i):
                        if items[j] > items[j + 1]:
                            items[j], items[j + 1] = items[j + 1], items[j]
            ```
            ````
        
        !!! done "Rendu"
            ```python linenums="1"
            def bubble_sort(items):
                for i in range(len(items)):
                    for j in range(len(items) - 1 - i):
                        if items[j] > items[j + 1]:
                            items[j], items[j + 1] = items[j + 1], items[j]
            ```

!!! bug "Bug ?"
    J'ai constaté des ratés de coloration syntaxique avec ```` ``` c++ ````.

    Recommendations :

    - Pas d'espace entre ```` ``` ```` et le nom du langage.
    - Utiliser `cpp` à la place de `c++`

### Texte barré

!!! tip "On encadre d'un double `~`"
    === "Correct"
        !!! note "Entrée"
            ```markdown
            La Terre ~~est plate~~ bleue comme une orange.
            ```

        !!! done "Rendu"
            La Terre ~~est plate~~ bleue comme une orange.

    === "Incorrect"
        !!! note "Entrée"
            ```markdown
            La Terre ~~ est plate~~ bleue comme une orange.

            La Terre ~~est plate ~~ bleue comme une orange.
            ```

        !!! fail "Rendu"
            La Terre ~~ est plate~~ bleue comme une orange.

            La Terre ~~est plate ~~ bleue comme une orange.
        
        :warning: Le double `~` doit être collé au morceau à barrer.

!!! warning "Pas valable avec tous les Markdown !"
    On en dispose avec CodiMD, Jupyter, mais aussi MkDocs avec l'extension `tilde`, et nous utiliserons.

### Texte souligné

!!! tip "On encadre d'un double `^`"
    === "Correct"
        !!! note "Entrée"
            ```markdown
            La Terre bleue ^^comme^^ une orange.
            ```

        !!! done "Rendu"
            La Terre bleue ^^comme^^ une orange.

    === "Incorrect"
        !!! note "Entrée"
            ```markdown
            La Terre est bleue ^^ comme^^ une orange.

            La Terre est bleue ^^comme ^^ une orange.
            ```

        !!! fail "Rendu"
            La Terre est bleue ^^ comme^^ une orange.

            La Terre est bleue ^^comme ^^ une orange.
        
        :warning: Le double `^` doit être collé au morceau à barrer.

!!! warning "Pas valable avec tous les Markdown !"
    On en dispose avec CodiMD, mais aussi MkDocs avec l'extension `caret`, et nous utiliserons.

    Pour Jupyter, il faut utiliser la balise HTML `<u>`. :warning: Cependant le contenu ne pourra pas contenir de balise Markdown.

### Texte surligné

!!! tip "On encadre d'un double `=`"
    === "Correct"
        !!! note "Entrée"
            ```markdown
            La Terre bleue comme ==une orange==.
            ```

        !!! done "Rendu"
            La Terre bleue comme ==une orange==.

    === "Incorrect"
        !!! note "Entrée"
            ```markdown
            La Terre est bleue comme == une orange==.

            La Terre est bleue comme ==une orange ==.
            ```

        !!! fail "Rendu"
            La Terre est bleue comme == une orange==.

            La Terre est bleue comme ==une orange ==.
        
        :warning: Le double `=` doit être collé au morceau à barrer.

!!! warning "Pas valable avec tous les Markdown !"
    On en dispose avec CodiMD, mais aussi MkDocs.

    Pour Jupyter, il faut utiliser la balise HTML `<mark>`. :warning: Cependant le contenu ne pourra pas contenir de balise Markdown.

### Case à cocher

!!! tip "On préfixe par `- [ ]` ou `- [x]`"
    !!! note "Entrée"
        ```markdown
        Une liste de tâches
        
        - [ ] à faire
        - [x] fini
        - [ ] presque
        - [x] fait depuis longtemps
        ```

    !!! done "Rendu"
        Une liste de tâches
        
        - [ ] à faire
        - [x] fini
        - [ ] presque
        - [x] fait depuis longtemps

!!! abstract "Méthode"
    Comme pour une liste, mais on commence par
    
    `- [ ]` pour une case non cochée,

    `- [x]` pour une case cochée.

!!! info "Cliquables ?"
    Avec certains logiciels, les cases à cocher sont cliquables, ce qui permet de modifier leur état.

    - ❌ Avec Jupyter, les cases à cocher ne sont pas cliquables.
    - ✅ Avec CodiMD, elles le sont, et le fichier source est modifié à la volée.
    - ❓ Avec MkDocs, on peut choisir globalement sa préférence, dans ce document, elles sont cliquables.

### Émojis

!!! tip "🤪👩‍🎨🚦🚂⚔️"
    Il suffit de coller vos émojis préférés depuis un site.
    
    - [Emojipedia](https://emojipedia.org/)
    - [GetEmoji](https://getemoji.com/)
    - [Copy and Paste Emoji](https://www.copyandpasteemoji.com/)
    - [wpRock](https://wprock.fr/t/emoji/) ; avec recherche en français.
    - [emoji copy](https://www.emojicopy.com/) ; permet d'en copier plusieurs à la fois.
    - ...

## Exercices élaborés

### Exercice 1

???

### Exercice 2

???
