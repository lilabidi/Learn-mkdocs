# Aide pour écrire des mathématiques simples

Auteur : Franck CHAMBON

![](assets/Jupyter.png){align=right}

!!! abstract "Objectif"
    Écrire des mathématiques dans du code Markdown.

    C'est utile pour Jupyter, CodiMD et MkDocs entre autres...

![](assets/MathJax.png){align=right}


!!! done "Un tour d'horizon"
    $$\sum\limits_{k\in\mathbb N^*} \frac 1 {k^2} = \frac {\pi^2}6 \quad \text{: Problème de Bâle, résolu par Leonhard Euler.}$$

    Commençons par un tour d'horizon des possibilités en [comparant les deux moteurs](https://www.intmath.com/cg5/katex-mathjax-comparison.php "KaTeX vs MathJax") de rendu les plus répandus.

    Nous allons voir comment écrire des maths, en commençant par les choses les plus simples. Chaque partie contient des exercices à réaliser.

## La balise math `$`

!!! faq "Dans la ligne ou un paragraphe dédié"
    Il y a deux façons de placer des maths dans un document Markdown :

    1. Au milieu du texte qu'on écrit ; en ligne. **Le signe `$` de chaque côté.**
        - Dans ce cas : `#!latex Du texte avant $<code math à écrire ici>$ du texte après.`
    2. Dans un paragraphe dédié, centré ; en mode équation. **Le double `$$` de chaque côté.**
        - Dans ce cas:
        ```latex
        Paragraphe précédent.

        $$<code math à écrire ici>$$

        Paragraphe suivant.
        ```

!!! warning "Espacement"
    Pas d'espaces après la balise ouvrante, ni avant la balise fermante.

??? info "Autres balises"
    Le mode mathématique de MathJax (ou autre moteur de rendu) est largement employé ailleurs aussi ; avec GeoGebra, avec LaTeX et dans de nombreuses utilisations avec Markdown. Il y a des variations dans l'emploi des balises.  

    - Pour le mode en ligne, on trouve parfois, `\(<code math à écrire là>\)`.
    - Pour le mode équation, on trouve souvent `\[<code math à écrire là>\]` dans les documents LaTeX.

!!! example "Exemples"
    !!! done "1. Une équation en ligne"
        | Markdown | Rendu |
        |:--------:|:-----:|
        | `#!latex $$x+y= y +  x$$` | $x+y= y +  x$ |

        :warning: Remarquer que l'espace est correctement mis dans tous les cas.

    !!! done "2. Des maths insérés dans du texte"
        === "Incorrect"
            Markdown
            : `#!latex La somme de $123$ et 123 est égale à $123 +123$. `

            Rendu
            : La somme de $123$ et 123 est égale à $123 +123$.

        === "Correct"
            Markdown
            : `#!latex La somme de $123$ et $123$ est égale à $123 +123$. `
            
            Rendu
            : La somme de $123$ et $123$ est égale à $123 +123$.

        :warning: Remarquer les différences d'écriture 123 et $123$.

??? info "Remarques"
    1. Avec le premier exemple, on voit que l'espacement dans le rendu est correct, indépendamment de la source. C'est bien ! Nous n'avons pas en nous en soucier, le moteur gère très bien !
    2. Avec le second exemple, bien voir la différence d'écriture des deux premiers $123$ (en mode `Incorrect`). Dans un souci de cohérence :
        + Il vaut mieux mettre tous les nombres avec lesquels ont fait du calcul entre balises maths. Même status, même écriture !
        + Pour des années ou des numéros de page (par exemple), on peut les écrire sans balises maths. Tant qu'on ne fait pas de calcul avec ensuite.
    3. Les espaces sont gérées finement de manière globale.
        + Conseil : écrire de manière à aérer le code, qu'il soit lisible.
        + Le moteur de rendu choisira les bonnes tailles d'espaces à afficher. C'est un principe de fonctionnement.

!!! note "Motivation"
    L'inspiration du HTML vient de TeX, inventé par [Donald Knuth](https://fr.wikipedia.org/wiki/Donald_Knuth "Article Wikipedia").

    Écrire un document en utilisant LaTeX est une nécessité pour beaucoup d'étudiants en thèse et nombre de professionnels. Ce n'est pas [un apprentissage rapide](https://fr.wikibooks.org/wiki/LaTeX), mais cela permet d'obtenir une très grande qualité. **Ce n'est pas l'objectif de ce cours !** Cela peut néanmoins constituer une introduction.

    Utiliser Markdown, avec quelques connaissances de la balise maths LaTeX, permet de créer facilement des documents scientifiques honorables. Avec Jupyter, on peut facilement alterner entre cellule de texte (_avec des maths_) et cellule de code (_souvent Python_). **C'est l'objectif ce cours.**

!!! example "Exemples avec des espaces"
    On notera l'utilisation de `~` pour obtenir une espace insécable en mode maths.

    |Markdown|Rendu|Commentaire|
    |---|---:|:---|
    |`#!latex $12 34 56 78 90$` | $12 34 56 78 90$| Les espaces sont ignorées. |
    |`#!latex $123~456~789$` | $123~456~789$| Les espaces sont insécables, ...|
    |`#!latex $12~34~56~78~90$` | $12~34~56~78~90$| ... et c'est plus lisible. |
    |`#!latex $123.456~m$`|$123.456~m$| L'unité, ici, n'est pas écrite avec la bonne police. |
    |`#!latex $123.456~\mathrm{m}$`|$123.456~\mathrm{m}$| Méthode correcte. |
    |`#!latex $47.02~\mathrm{m}^2$`|$47.02~\mathrm{m}^2$| Méthode correcte. |

    Les deux derniers exemples seront revus à la fin de cette page.

??? danger "Plus de détails sur les espaces ; :warning: technique :warning:"
    Comme dans les balises HTML, la gestion des espaces est laissée au moteur de rendu, pour chaque cas.

    Dans les balises maths, entre deux lettres ou chiffres, les espaces sont ignorées.
    
    Pour modifier l'espace que LaTeX a prévu, il y a plusieurs possibilités complexes :

    - l'espace fine `\,` ($\frac3{18}$ de em)
    - l'espace fine négative `\!` ($\frac{-3}{18}$ de em)
    - l'espace moyenne `\:` ($\frac4{18}$ de em)
    - l'espace large `\;` ($\frac5{18}$ de em)
    - le cadratin `\quad` ($1$ em)
    - le double cadratin `\qquad` ($2$ em)
    - Le em étant une unité, la largeur de la lettre M avec la police courante.

    Il y a un moyen simple de créer une [espace insécable](https://fr.wikipedia.org/wiki/Espace_ins%C3%A9cable) en mode mathématique :

    - `~` est une bonne idée pour le séparateur des milliers.
    - `~` est une bonne idée pour séparer un nombre et son unité.
    - L'espace insécable permet qu'un bloc ne soit pas coupé en fin de ligne. C'est important
    - ! (sic) Par exemple, un point d'exclamation doit rester collé à son mot précédent.
        + Il est séparé par une espace insécable en français.
        + En anglais, il est collé au mot précédent, sans espace.

## Les 4 opérations et les nombres

!!! done "Opérations"
    Dans une cellule Markdown, à l'intérieur de balises math,

    - L'addition s'obtient avec `+`
    - La soustraction s'obtient avec `-`
    - La multiplication s'obtient avec `\times`
    - La division s'obtient avec `\div`

??? info "Claviers du futur"
    D'ici quelque<u>s</u> ~~temps~~ années les claviers respectant la nouvelle norme AFNOR donneront accès rapidement à ×, ÷, et seront plus commodes pour écrire certaines lettres comme É, È, Ç, ...

!!! tip "Rappel cellule Python"
    Dans une cellule de code Python, c'est plus facile :

    - La multiplication s'obtient avec `*`
    - La division s'obtient avec `/`

!!! example "Exemple d'opérations"
    Markdown
    : `#!latex $[5 + 3\times8 - (1 + 35\div5)](18  -  5 \times 2)$`
    
    Rendu
    : $[5 + 3\times8 - (1 + 35\div5)](18  -  5 \times 2)$

!!! faq "Exercice 1 : expression numérique"
    ![un calcul](assets/exo1.png)

    1. Calculer avec une cellule Python l'expression numérique précédente,
    2. puis afficher cette expression avec son résultat dans une cellule Markdown.
    3. Modifier l'affichage pour insérer de l'espace inter-milliers.

    ??? done "Solution"
        1.  
        ```python
        >>> 3 * 3 * 13 * 6353 * 8969 * (1 + 1480 * 1001001)
        9876543210123456789
        ```
        2. Markdown
        : `#!latex $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1001001) = 9876543210123456789$`

            Rendu
            : $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1001001) = 9876543210123456789$
        
        3. Markdown
        : `#!latex $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1~001~001) = 9~876~543~210~123~456~789$`

            Rendu
            : $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1~001~001) = 9~876~543~210~123~456~789$



        ??? bug "Espace trop important"
            Pour les puristes, l'espace est un peu trop important avec `~`...

            La bonne solution est d'employer `\,` à la place.

            Markdown
            : `#!latex $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1\,001\,001) = 9\,876\,543\,210\,123\,456\,789$`

            Rendu
            : $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1\,001\,001) = 9\,876\,543\,210\,123\,456\,789$

!!! faq "Exercice 2 : première approximation de $\pi$"
    ![un calcul](assets/exo2.png)

    1. Calculer avec une cellule Python l'expression numérique précédente.
    2. Compléter alors le code `#!latex $3 + ... \approx \pi$`
    3. (maths) Écrire le membre de gauche comme une seule fraction.
    4. Pour les plus curieux à ce sujet, [un peu de lecture](https://fr.wikipedia.org/wiki/Fraction_continue#D%C3%A9veloppement_en_fraction_continue_du_nombre_%CF%80 "Article Wikipédia")
