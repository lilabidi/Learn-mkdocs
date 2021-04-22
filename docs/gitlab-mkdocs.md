# Hébergement du site

!!! info "Plusieurs solutions"
    On pourrait construire (`mkdocs build`) le site et l'héberger à part ; pas facile.
    
    On peut facilement l'héberger sur GitHub ou sur GitLab.
        - Sur GitHub, il y a deux façons de faire :
            - Méthode 1 :
                - Modifier un fichier source.
                - Vérifier le résultat avec `mkdocs serve`.
                - Re-construire le site avec `mkdocs build`.
                - Avec Git, faire un `commit`, puis un `push`.
            - Méthode 2 :
                - Modifier un fichier source.
                - Vérifier le résultat avec `mkdocs serve`.
                - Avec Git, faire un `commit`, puis un `push`.
                - Utiliser l'outil de déploiement `mkdocs gh-deploy --force`
            - Dans tous les cas, sur GitHub, il y a des risques de confusion avec une branche `gh-page` qui pourrait être créée. On compte aussi **4 étapes**.
        - Sur GitLab, il y a une façon raisonnable de faire :
            - Modifier un fichier source en Markdown.
            - Vérifier le résultat avec `mkdocs serve`.
            - Avec Git, faire un `commit`, puis un `push`.

    Avec GitLab, il y a une étape en moins, de plus aucun risque de confusion de branche, il n'y a pas d'autre branche créée.

    Les autres étapes sont plus ou moins obligatoires.

    - Modifier la source. **Obligatoire** : vous voulez modifier votre site, non ?
    - Vérifier le résultat avec `mkdocs serve`. **Facultatif** : vous êtes certain de votre coup ?
    - Utiliser Git. **Obligatoire** (en vrai non, mais ce serait bien plus complexe). Vous souhaitez que votre modification reste en local, ou que le monde entier soit au courant ?

!!! done "C'est facile !"
    Une fois tout configuré, l'objet de cette page, il suffit de faire comme cet exemple animé.

    1. Noter le cercle vert coché, qui témoigne que le dernier déploiement s'est bien déroulé.

        ![avant le push](avant-push.png)

    2. On modifie le site.

        ![vidéo en gif](vidéo.gif)

    3. Si on réactualise la page du projet sur GitLab, le témoin passe à `pipeline: en cours`

        ![juste après le push](après-push.png)

    4. Après quelques secondes, (ou minutes) 
        - Si un problème survient (mauvaise configuration),
            - vous recevez un mail sur l'échec, le cercle contient une croix rouge.
            - Vous recevrez un mail pour chaque nouveau `push` jusqu'au succès inclus.
        - Si le cercle passe au vert, le site est déployé silencieusement, et on continue le travail.
    
    5. L'animation montrait
        - une modification d'un code source (celui-ci même).
        - Un `commit` grâce à l'outil graphique de VSCodium (en haut à gauche).
        - Un `push`, toujours avec VSCodium.
        - Cela peut aussi se faire avec d'autres éditeurs...

!!! faq "Comment ça fonctionne ?"
    Pour modifier le source, c'est en local. Vous modifiez un fichier Markdown, une image ou tout autre document. Les autres sections de ce tutoriel servent à ça. La vérification va souvent de paire avec `mkdocs serve`.
    
    Dans une journée de travail, on fait plusieurs modifications.
        - À chaque étape importante on fait un `commit` qui décrit l'ensemble des modifications, un peu comme un journal de bord. On peut faire plusieurs `commit` sans faire de `push`. Un `commit` s'accompagne toujours d'un commentaire.
        - Lorsqu'on souhaite synchroniser son travail avec le dépôt distant, on fait un `push`. L'ensemble des modifications est envoyée avec les étapes de transitions évoquées par les `commit`.
    
    Techniquement, on pourrait revoir l'historique du dépôt `commit` par `commit`. Dans le cadre d'un travail collaboratif, chaque `commit` est signé de son auteur. C'est un moment du `push` que l'authentification est vérifiée. La méthode la plus efficace est de passer `SSH`.

!!! abstract "Authentification SSH"
    Montrons comment faire...