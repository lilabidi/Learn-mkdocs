# Aide pour écrire des mathématiques simples

Auteur : Franck CHAMBON

![](assets/MathJax.png)
![](assets/Jupyter.png)
![](assets/katex.png){width=200}
![](assets/material.png){width=200}

!!! abstract "Objectif"
    Écrire des mathématiques dans du code Markdown (ou LaTeX).

    C'est utile pour GeoGebra, Jupyter, CodiMD et MkDocs entre autres...

    !!! example "Exemple"

        === "Rendu"
            En 1735, Leonhard Euler résout le **problème de Bâle** en établissant la formule suivante :

            $$\sum\limits_{k\in\mathbb N^*} \frac 1 {k^2} = \frac {\pi^2}6$$
        
            Cependant, il ne démontrera rigoureusement son résultat qu’en 1741.

        === "Markdown"
            ```markdown
            En 1735, Leonhard Euler résout le **problème de Bâle** en établissant la formule suivante :

            $$\sum\limits_{k\in\mathbb N^*} \frac 1 {k^2} = \frac {\pi^2}6$$
        
            Cependant, il ne démontrera rigoureusement son résultat qu’en 1741.
            ```



!!! done "Un tour d'horizon"

    !!! tip "KaTeX vs MathJax"
        Commençons par un tour d'horizon des possibilités en comparant les deux moteurs de rendu les plus répandus.
        
        [Lancer le tour d'horizon](https://www.intmath.com/cg5/katex-mathjax-comparison.php "KaTeX vs MathJax"){.md-button }

    !!! faq "Que retenir ?"
        [KaTeX](https://katex.org/) permet un rendu performant et plus rapide que [MathJax](https://www.mathjax.org/). La syntaxe est la même, héritée de l'écriture des mathématiques avec [LaTeX](https://fr.wikipedia.org/wiki/LaTeX).

        Si vous ne savez pas l'utiliser, nous allons voir comment écrire des maths, **en commençant par les choses les plus simples**. Chaque partie contient des exercices à réaliser.

## La balise math `$`

!!! tip "Dans la ligne ou un paragraphe dédié"

    !!! warning inline end "Espacement"
        Pas d'espaces après la balise ouvrante, ni avant la balise fermante.

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

??? info "Autres balises"
    Le mode mathématique de MathJax (ou autre moteur de rendu) est largement employé ailleurs aussi ; avec GeoGebra, avec LaTeX et dans de nombreuses utilisations avec Markdown. Il y a des variations dans l'emploi des balises.  

    - Pour le mode en ligne, on trouve parfois, `\(<code math à écrire là>\)`.
    - Pour le mode équation, on trouve souvent `\[<code math à écrire là>\]` dans les documents LaTeX.

!!! example "Exemples"
    !!! done "1. Une équation en ligne"
        | Markdown | Rendu |
        |:--------:|:-----:|
        | `#!latex $$x+y= y +  x$$` | $x+y= y +  x$ |

        :warning: Remarquer que l'espace est correctement mis dans le rendu dans tous les cas.

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

        :warning: Remarquer les différences d'écriture 123 et $123$ dans le rendu incorrect.

??? info "Remarques"
    1. Avec le premier exemple, on voit que l'espacement dans le rendu est correct, indépendamment de la source. C'est bien ! Nous n'avons pas en nous en soucier, le moteur gère très bien !
    2. Avec le second exemple, version incorrecte, bien voir la différence d'écriture des deux premiers $123$. Dans un souci de cohérence :
        + Il vaut mieux mettre tous les nombres avec lesquels ont fait du calcul entre balises maths. Même status, même écriture !
        + Pour des années ou des numéros de page (par exemple), on peut les écrire sans balises maths. Tant qu'on ne fait pas de calcul avec ensuite.
    3. Les espaces sont gérées finement de manière globale.
        + Conseil : écrire de manière à aérer le code, qu'il soit lisible.
        + Le moteur de rendu choisira les bonnes tailles d'espaces à afficher. C'est un principe de fonctionnement.

!!! cite "Motivation"
    L'inspiration du HTML vient de TeX, inventé par [Donald Knuth](https://fr.wikipedia.org/wiki/Donald_Knuth "Article Wikipedia").

    Écrire un document en utilisant LaTeX est une nécessité pour beaucoup d'étudiants en thèse et nombre de professionnels. Ce n'est pas [un apprentissage rapide](https://fr.wikibooks.org/wiki/LaTeX), mais cela permet d'obtenir une très grande qualité. **Ce n'est pas l'objectif de ce cours !** Cela peut néanmoins constituer une introduction. Une [suite de l'apprentissage](http://www.learnlatex.org/fr/) possible.

    Utiliser Markdown, avec quelques connaissances de la balise maths LaTeX, permet de créer facilement des documents scientifiques honorables. Avec Jupyter, on peut facilement alterner entre cellule de texte (_avec des maths_) et cellule de code (_souvent Python_). **C'est l'objectif ce cours.**

!!! example "Exemples avec des espaces"
    On notera l'utilisation de `~` pour obtenir une [espace insécable](https://fr.wikipedia.org/wiki/Espace_ins%C3%A9cable) en mode maths.

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

    En attendant, avec Linux, il suffit
    
    - de taper sur ++altgr+";"++ pour avoir `×`
    - de taper sur ++altgr+":"++ pour avoir `÷`

!!! tip "Rappel cellule Python"
    Dans une cellule de code Python, c'est plus facile :

    - La multiplication s'obtient avec `*`
    - La division s'obtient avec `/`

!!! example "Exemple d'opérations"
    Markdown
    : `#!latex $[5 + 3\times 8 - (1 + 35 \div 5)](18  -  5 \times 2)$`

    Rendu
    : $[5 + 3\times 8 - (1 + 35 \div 5)](18  -  5 \times 2)$

!!! note "Exercice 1 : expression numérique"
    !!! info "Un palindrome"
        $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1001001)$

    1. Calculer avec une cellule Python l'expression numérique précédente, c'est un palindrome.
    2. Afficher cette expression avec son résultat dans une cellule Markdown.
    3. Modifier l'affichage pour insérer de l'espace inter-milliers.

    ??? done "Solution"
        1. Dans une console Python
        ```python
        >>> 3 * 3 * 13 * 6353 * 8969 * (1 + 1480 * 1001001)
        9876543210123456789
        ```
        2. Markdown
        : 
        ```latex
        $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1001001) =
        9876543210123456789$
        ```

            Rendu
        : $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1001001) =
        9876543210123456789$
        
        3. Markdown
        : 
        ```latex
        $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1~001~001) =
        9~876~543~210~123~456~789$
        ```

            Rendu
        : $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1~001~001) =
        9~876~543~210~123~456~789$

        On utilise les espace inter-milliers pour les nombres à **5 chiffres ou plus**. Pour les nombres à 4 chiffres, c'est toléré.

        ??? bug "Espace trop importante ?"
            Pour les puristes, l'espace est un peu trop important avec `~`...

            La bonne solution est d'employer `\,` à la place.

            Markdown
            : 
            ```latex
            $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1\,001\,001) =
            9\,876\,543\,210\,123\,456\,789$
            ```

            Rendu
            : $3 \times 3 \times 13 \times 6353 \times 8969 \times (1 + 1480 \times 1\,001\,001) =
            9\,876\,543\,210\,123\,456\,789$

!!! note "Exercice 2 : une approximation de $\pi$"
    !!! info "Milü"
        $3 + 1 \div (7 + 1 \div 16)$

    1. Calculer avec une cellule Python l'expression numérique précédente.
    2. Compléter alors le code `#!latex $3 + ... \approx \pi$`
    3. (maths) Écrire le membre de gauche comme une seule fraction.
    4. Pour les plus curieux à ce sujet, [un peu de lecture](https://fr.wikipedia.org/wiki/Fraction_continue#D%C3%A9veloppement_en_fraction_continue_du_nombre_%CF%80 "Article Wikipédia")

    ??? done "Solution"
        1. Dans une console Python
        ```python
        >>> 3 + 1 / (7 + 1/16)
        3.1415929203539825
        ```
        2. Markdown
        : ```latex
        $3 + 1 \div (7 + 1 \div 16) \approx \pi$
        ```

            Rendu
        : $3 + 1 \div (7 + 1 \div 16) \approx \pi$
        
        3. On a les étapes
        
        $$A = 3 + 1 ÷ \left(7 + \frac{1}{16} \right)$$

        $$A = 3 + 1 ÷ \left( \frac{7×16}{16} + \frac{1}{16} \right)$$

        $$A = 3 + 1 ÷ \frac{112+1}{16}$$

        $$A = \frac{3×113}{113} + 1 × \frac{16}{113}$$

        $$A = \frac{339}{113} + 1 × \frac{16}{113}$$

        $$A = \frac{339+16}{113}$$

        $$A = \frac{355}{113}$$

        [Milü](https://en.wikipedia.org/wiki/Mil%C3%BC), est le nom donné à une approximation de $\pi$ découverte par le mathématicien and astronome chinois, Zǔ Chōngzhī (祖沖之), né en 429.

## Du calcul littéral

On peut bien sûr utiliser des variables mathématiques, elles seront écrites en italique, avec une police un peu différente.

!!! example "Exemple 1 : calcul littéral"
    Un code et son rendu :

    Markdown
    : 
    ```latex
    Pour tous nombres $k$, $a$, $b$, on a : $k(a+b) = ka + kb$
    ```

    Rendu
    : Pour tous nombres $k$, $a$, $b$, on a : $k(a+b) = ka + kb$

    :warning: Dans le rendu, comparer les lettres `a` (dans «on a», et dans «$ka+kb$»).


!!! example "Exemple 2 : bilan des besoins"
    Un code et son rendu :

    Markdown
    : 
    ```latex
    Le volume d'un pavé droit de longueur $L$,  
    de hauteur $H$ et de profondeur $P$ est $V = L \times H \times P$
    ```
    
    Rendu
    : Le volume d'un pavé droit de longueur $L$,
     de hauteur $H$ et de profondeur $P$ est $V = L \times H \times P$

    :warning: Noter qu'il faut une espace après `\times`, sinon la commande `\timesH` est cherchée et non trouvée.

!!! tip "Remarques"
    Si on souhaite mieux écrire une formule d'aire ou de volume, on devine la nécessité :

    - de savoir écrire des fractions,
    - de savoir écrire des parenthèses à la bonne taille,
    - de savoir écrire des puissances,
    - de savoir écrire en indice,
    - de savoir faire une écriture scripte :
      $\mathscr V$ pour volume, $\mathscr A$ pour aire, $\mathscr C$ pour cercle, ...
    - de savoir écrire quelques lettres grecques, comme $\pi$ ou $\alpha$.

    Voilà donc la suite de notre programme. Pas d'exercices ici, mais plein ensuite !

## Les fractions `\dfrac`

!!! abstract "Le prototype et quelques exemples"
    |Code|Résultat affiché|
    |----|---------------:|
    |`#!latex $\dfrac{num}{den}$`     | $\dfrac{num}{den}$  |
    |`#!latex $\dfrac{22}{7}$`        | $\dfrac{22}{7}$     |
    |`#!latex $5 + \dfrac{x+7}{x-1}$` | $5+\dfrac{x+7}{x-1}$|

!!! note "Exercice 3 : règles et fractions"
    !!! info "Règles de calcul fractionnaire"
        Pour $a$, $b$, $c$ et $d$ des nombres, avec $b$ et $d$ non nuls, on a :

        $\dfrac{a}{b} + \dfrac{c}{b} = \dfrac{a + c}{b}$

        $\dfrac{a}{b} \times \dfrac{c}{d} = \dfrac{a \times c}{b \times d}$

        $a \div \dfrac{b}{d} = a \times \dfrac{d}{b}$

    Copier et compléter, dans une cellule Markdown, les règles fondamentales sur les écritures fractionnaires :

    ```latex
    Pour $a$, $b$, $c$ et $d$ des nombres, avec $b$ et $d$ non nuls, on a :

    $\dfrac{a}{b} + ...$

    $\dfrac{a}{b} \times ...$

    $a \div ...$
    ```

    ??? done "Solution"
        ```latex
        Pour $a$, $b$, $c$ et $d$ des nombres, avec $b$ et $d$ non nuls, on a :

        $\dfrac{a}{b} + \dfrac{c}{b} = \dfrac{a + c}{b}$

        $\dfrac{a}{b} \times \dfrac{c}{d} = \dfrac{a \times c}{b \times d}$

        $a \div \dfrac{b}{d} = a \times \dfrac{d}{b}$
        ```

!!! note "Exercice 4 : autre écriture de Milü"
    Recréer l'expression ci-dessous dans une cellule Markdown.

    $3 + \dfrac{1}{7 + \dfrac{1}{16}} = 
    3 + \dfrac{1}{ \dfrac{7 \times 16 + 1}{16} } =
    \dfrac{3 \times 113}{113} + \dfrac{16}{113} =
    \dfrac{355}{113} \approx \pi$

    ??? done "Solution"
        ```latex
        $3 + \dfrac{1}{7 + \dfrac{1}{16}} = 
        3 + \dfrac{1}{ \dfrac{7 \times 16 + 1}{16} } =
        \dfrac{3 \times 113}{113} + \dfrac{16}{113} =
        \dfrac{355}{113} \approx \pi$
        ```


??? danger "Pour aller plus loin"

    !!! info inline end
        Si le contenu d'un paramètre entre accolades n'est qu'un seul caractère, les accolades ne sont pas nécessaires, on peut les remplacer par de l'espace.
        
        Si ce caractère est un chiffre, on peut même le coller à `\dfrac`, mais on ne le conseille pas, pour des raisons de lisibilité.

    |Code|Résultat|
    |----|--------:|
    |`$\dfrac12$` | $\dfrac12$ |
    |`$\dfrac1x$` | $\dfrac1x$ |
    |`$\dfrac1{x+y}$` | $\dfrac1{x+y}$ |
    |`$\dfrac{1+x}y$` | $\dfrac{1+x}y$ |
    |`$\dfrac ab$` | $\dfrac ab$ |

## Les parenthèses à la bonne taille

!!! abstract "Quel est le problème ?"
    Si on veut placer un bloc (une expression) entre parenthèses, et que l'expression est plus haute que la normale (avec des fractions par exemple), alors les parenthèses normales ne sont pas assez hautes.

    === "Parenthèses trop petites"
        Markdown
        : `#!latex $( \dfrac{a}{b} )$`

        Rendu
        : $( \dfrac{a}{b} )$

!!! done "Solution"
    - On utilisera `#!latex $\left($` pour la parenthèse gauche.
    - On utilisera `#!latex $\right)$` pour la parenthèse droite.

    === "Parenthèses adaptées"
        Markdown
        : `#!latex $\left( \dfrac{a}{b} \right)$`
    
        Rendu
        : $\left( \dfrac{a}{b} \right)$

??? danger "Pour aller plus loin"
    - On utilisera `#!latex $\left[$` pour le crochet gauche.
    - On utilisera `#!latex $\right]$` pour le crochet droit.
    - On utilisera `#!latex $\left\{$` pour l'accolade gauche. :warning: Noter qu'elle a été échappée.
    - On utilisera `#!latex $\right\}$` pour l'accolade droite. :warning: Noter qu'elle a été échappée.

    === "Example avec crochet"
        Markdown
        : `#!latex $\left[ \dfrac{a}{b} \right]$`
    
        Rendu
        : $\left[ \dfrac{a}{b} \right]$

    === "Example avec accolade"
        Markdown
        : `#!latex $\left\{ \dfrac{a}{b} \right\}$`
    
        Rendu
        : $\left\{ \dfrac{a}{b} \right\}$

    === "Example complexe"
        Markdown
        : `#!latex $\left[ \left(\dfrac{a}{b} + \dfrac{c}{d} \right) \times
        \left\{  \dfrac {\dfrac{e}{f}} {\dfrac{g}{h}}   \right\}  \right]$`
    
        Rendu
        : $\left[ \left(\dfrac{a}{b} + \dfrac{c}{d} \right) \times
        \left\{  \dfrac {\dfrac{e}{f}} {\dfrac{g}{h}}   \right\}  \right]$

??? danger "Pour aller encore plus loin"
    - On utilisera `#!latex $\right.$` pour finir à droite une sélection commencée par un délimiteur gauche.
    - On utilisera `#!latex $\left.$` pour commencer à gauche une sélection qui se finira par un délimiteur droit.
    - On a le droit de commencer à **gauche** par une parenthèse (ou crochet ou accolade) qui **ouvre**.
    - On a le droit de finir à **droite** par une parenthèse (ou crochet ou accolade) qui **ferme**.

    === "Exemple"
        Markdown
        : `#!latex $\left] \dfrac{a}{b} \right.$`
    
        Rendu
        : $\left] \dfrac{a}{b} \right.$

## Les puissances `a^n`

!!! tip inline "L'accent circonflexe"
    Markdown
    : `#!latex $a^{n}$`
    
    Rendu
    :  $a^{n}$

!!! warning "Mode mathématique"
    Écrire en exposant de cette manière est pour le mode mathématique, entre `$`.

    L'intérieur des accolades est un contenu mathématique, pas du texte.

    Pour écrire deuxième en abrégé, on écrit `2^e^` pour 2^e^, sans entrer dans le mode mathématique.

    :warning: Bien penser aux accolades.

!!! example "Exemples"
    === "Correct"
        Markdown
        : `#!latex $a^{42}$`
        
        Rendu
        :  $a^{42}$

        👍 $42$ est bien mis en exposant en entier.

    === "Incorrect"
        Markdown
        : `#!latex $a^42$`
        
        Rendu
        :  $a^42$

        :warning: Seul le $4$ est mis en exposant...

!!! note "Exercice 5 : règles et puissances"
    !!! abstract "Les règles"
        Pour tous nombres $a$, $b$, $c$ non nuls, et tous entiers $n$, $m$, on a :

        $a^n \times a^m = a^{n+m}$

        $a^n \times b^n = (a \times b)^n$

        $\dfrac{a^n}{a^m} = a^{n-m}$

        $\dfrac{a^n}{b^n} = \left(\dfrac{a}{b}\right)^n$

        $\left( a^n \right)^m = a^{n \times m}$

        $a^{-n} = \dfrac {1} {a^n}$

    Copier et compléter le code Markdown ci-dessous, au sujet des règles sur les puissances.

    ```latex
    Pour tous nombres $a$, $b$, $c$ non nuls, et tous entiers $n$, $m$, on a :

    $a^n \times a^m = $

    $a^n \times b^n = $

    $\dfrac{a^n}{a^m} = $

    $\dfrac{a^n}{b^n} = $

    $\left( a^n \right)^m = $

    $a^{-n} = $
    ```

    ??? done "Solution"
        ```latex
        Pour tous nombres $a$, $b$, $c$ non nuls, et tous entiers $n$, $m$, on a :

        $a^n \times a^m = a^{n + m}$

        $a^n \times b^n = (a \times b)^n$

        $\dfrac{a^n}{a^m} = a^{n - m}$

        $\dfrac{a^n}{b^n} = \left( \dfrac{a}{b} \right)^n$

        $\left( a^n \right)^m = a^{n \times m}$

        $a^{-n} = \dfrac 1 {a^n}$
        ```

## La Racine carrée

!!! done  inline "Méthode"
    Markdown
    : `#!latex $\sqrt{x}$`
    
    Rendu
    : $\sqrt{x}$

!!! info "Remarques"
    - Pourquoi `sqrt` ?
        - En anglais _**sq**uare-**r**oo**t**_
        - `sqrt` est donc très souvent utilisé.
    - :warning: Bien penser aux accolades.
        - Sinon tout n'est pas inclus dans la racine.


!!! note "Exercice 6 : Théorème de Pythagore"
    !!! abstract "Un example classique"
        $ABC$ est un triangle rectangle en $A$, avec $AB = 45$, $AC = 28$. Calculer $BC$.

        Réponse :
        
        $ABC$ est un triangle rectangle en $A$, d'après le théorème de Pythagore, on a :
        
        $BC^2 = AB^2 + AC^2$

        $BC^2 = 45^2 + 28^2$

        $BC^2 = 2809$, avec $BC$ positif, donc

        $BC = \sqrt{2809}$

        $BC = 53$ ; la longueur de $BC$ est $53$.

    En vous inspirant du modèle ci-dessus, rédiger une solution au problème suivant :

    !!! danger "Problème"
        $RST$ est un triangle rectangle en $R$, avec $RT = 21$, $RS=28$. Calculer $ST$.


    À vous de modifier, compléter (et réutiliser) le code suivant :

    ```latex
    $ABC$ est un triangle rectangle en $A$, avec $AB = 45$, $AC = 28$. Calculer $BC$.

    Réponse :
    
    $ABC$ est un triangle rectangle en $A$, d'après le théorème de Pythagore, on a :
    
    $BC^2 =$
    ```

    ??? done "Solution"
        ```latex
        $RST$ est un triangle rectangle en $R$, avec $RT = 21$, $RS=28$. Calculer $ST$.

        Réponse :
        
        $RST$ est un triangle rectangle en $R$, d'après le théorème de Pythagore, on a :
        
        $ST^2 = RS^2 + RT^2$

        $ST^2 = 28^2 + 21^2$

        $ST^2 = 1225$, avec $ST$ positif, donc

        $ST = \sqrt{1225}$

        $ST = 35$ ; la longueur de $ST$ est $35$.
        ```

## Les indices `a_n`

!!! tip inline "Le tiret-bas"
    Markdown
    : `#!latex $a_{n}$`
    
    Rendu
    :  $a_{n}$

!!! warning "Mode mathématique"
    Écrire en indice de cette manière est pour le mode mathématique, entre `$`.

    L'intérieur des accolades est un contenu mathématique, pas du texte.

    Pour écrire du texte en indice, à l'intérieur du mode mathématique,
     on utilise `\text`, comme dans $p_{\text{carré}}$ avec `#!latex $p_{\text{carré}}$`
    
    :warning: Bien penser aux accolades.

!!! example "Exemples"
    === "Correct"
        Markdown
        : `#!latex $a_{42}$`
        
        Rendu
        :  $a_{42}$

        👍 $42$ est bien mis en indice en entier.

    === "Incorrect"
        Markdown
        : `#!latex $a_42$`
        
        Rendu
        :  $a_42$

        :warning: Seul le $4$ est mis en indice...

!!! example "Volume d'un cylindre"
    Par exemple, pour $V_\text{cylindre}$, on écrit `#!latex $V_\text{cylindre}$`.

    Nous verrons à la section suivante comment utiliser une écriture cursive pour un plus joli

    $$\mathscr V_\text{cylindre}$$

## Écriture scripte, pour aires, volumes, cercles

!!! abstract "Certaines lettres à démarquer"
    En mode **math**ématique, on utilise, entre autres, l'écriture **scr**ipte,

    d'où la commande `#!latex $\mathscr{ }$`.

    |Markdown|Rendu|
    |--------|----:|
    |`#!latex Le cercle $\mathscr C$`|Le cercle $\mathscr C$|
    |`#!latex Le volume $\mathscr V$`|Le volume $\mathscr V$|
    |`#!latex L'aire $\mathscr A_{RST}$`|L'aire $\mathscr A_{RST}$|
    |`#!latex L'aire $\mathscr A_\text{triangle}$`|L'aire $\mathscr A_\text{triangle}$|

    Noter dans les deux derniers exemples, que
    
    - `RST` est bien en mode math, alors que
    - `\text{triangle}` produit du texte dans le mode math.
    
    C'est bien la bonne méthode.

## [Écriture de lettres grecques](https://fr.wikibooks.org/wiki/LaTeX/%C3%89crire_des_math%C3%A9matiques#Lettres_grecques)

!!! abstract "Par leur nom latin"
    Pour utiliser les lettres grecques, il suffit de taper leur nom en caractères latins précédé d'une contre-oblique.
    
    Par exemple, **en mode mathématique** :

    |Markdown|Rendu|
    |-------:|:----|
    |`#!latex $\alpha$` | $\alpha$ |
    |`#!latex $\chi$`   | $\chi$   |
    |`#!latex $\omega$` | $\omega$ |
    |`#!latex $\Omega$` | $\Omega$ |

    Les lettres identiques aux lettres latines ne sont pas définies :
    
    - le alpha capital est identique au $A$,
    - le khi capitale est identique au $X$.
    
??? danger "Variantes de certaines lettres"
    === "Classique"
        |Markdown|Rendu|
        |-------:|:----|
        |`#!latex $\epsilon$` | $\epsilon$ |
        |`#!latex $\theta$`   | $\theta$   |
        |`#!latex $\pi$`      | $\pi$      |
        |`#!latex $\rho$`     | $\rho$     |
        |`#!latex $\sigma$`   | $\sigma$   |
        |`#!latex $\phi$`     | $\phi$     |

    === "Variante"
        |Markdown|Rendu|
        |-------:|:----|
        |`#!latex $\varepsilon$` | $\varepsilon$ |
        |`#!latex $\vartheta$`   | $\vartheta$   |
        |`#!latex $\varpi$`      | $\varpi$      |
        |`#!latex $\varrho$`     | $\varrho$     |
        |`#!latex $\varsigma$`   | $\varsigma$   |
        |`#!latex $\varphi$`     | $\varphi$     |

!!! note "Exercice 7 : belles formules de géométrie"
    Écrire de belles formules pour :

    - Le carré
        * Le périmètre d'un carré de côté $a$.
        * L'aire d'un carré de côté $a$.
    - Le rectangle
        * Le périmètre d'un rectangle de côtés $a$ et $b$.
        * L'aire d'un rectangle de côtés $a$ et $b$.
    - Le triangle
        * Le périmètre d'un triangle de côtés $a$, $b$ et $c$.
        * L'aire d'un triangle de côté $b$ et de hauteur associée $h$.
    - Le cercle et le disque
        * La circonférence d'un cercle de rayon $r$.
        * L'aire d'un disque de rayon $r$.
    - Les volumes pour
        + Un pavé droit de côtés $L$, $H$, $P$.
        + Un prisme droit dont la base a une aire $\mathscr A_\text{base}$, et une hauteur $h$ associée.
        + Une pyramide dont la base a une aire $\mathscr A_\text{base}$, et une hauteur $h$ associée.
        + Une boule de rayon $r$.

    ??? done "Solution"
        === "Rendu"
            - Le carré
                - Le périmètre d'un carré de côté $a$ est
                  $p_\text{carré} = 4a$.
                - L'aire d'un carré de côté $a$ est
                  $\mathscr A_\text{carré} = a^2$.
            - Le rectangle
                - Le périmètre d'un rectangle de côtés $a$ et $b$ est
                  $p_\text{rectangle} = 2(a+b)$.
                - L'aire d'un rectangle de côtés $a$ et $b$ est
                  $\mathscr A_\text{rectangle} = ab$.
            - Le triangle
                - Le périmètre d'un triangle de côtés $a$, $b$ et $c$ est
                  $p_\text{triangle} = a+b+c$.
                - L'aire d'un triangle de côté $b$ et de hauteur associée $h$ est
                  $\mathscr A_\text{triangle} = \dfrac{bh}{2}$.
            - Le cercle et le disque
                - La circonférence d'un cercle de rayon $r$ est
                  $p_\text{cercle} = 2\pi r$.
                - L'aire d'un disque de rayon $r$ est
                  $\mathscr A_\text{disque} = \pi r^2$.
            - Les volumes pour
                - Un pavé droit de côtés $L$, $H$, $P$ a pour volume
                  $\mathscr V_{pavé} = L \times H \times P$.
                - Un prisme droit dont la base a une aire $\mathscr A_\text{base}$,
                  et une hauteur $h$ associée a pour volume
                  $\mathscr V_{prisme} = \mathscr A_\text{base} \times h$.
                - Une pyramide dont la base a une aire $\mathscr A_\text{base}$,
                  et une hauteur $h$ associée a pour volume
                  $\mathscr V_{pyramide} = \dfrac {1}{3} \mathscr A_\text{base} \times h$.
                - Une boule de rayon $r$ a pour volume
                  $\mathscr V_{boule} = \dfrac{4}{3} \pi r^3$.

        === "Markdown"
            ```markdown
            - Le carré
                - Le périmètre d'un carré de côté $a$ est
                  $p_\text{carré} = 4a$.
                - L'aire d'un carré de côté $a$ est
                  $\mathscr A_\text{carré} = a^2$.
            - Le rectangle
                - Le périmètre d'un rectangle de côtés $a$ et $b$ est
                  $p_\text{rectangle} = 2(a+b)$.
                - L'aire d'un rectangle de côtés $a$ et $b$ est
                  $\mathscr A_\text{rectangle} = ab$.
            - Le triangle
                - Le périmètre d'un triangle de côtés $a$, $b$ et $c$ est
                  $p_\text{triangle} = a+b+c$.
                - L'aire d'un triangle de côté $b$ et de hauteur associée $h$ est
                  $\mathscr A_\text{triangle} = \dfrac{bh}{2}$.
            - Le cercle et le disque
                - La circonférence d'un cercle de rayon $r$ est
                  $p_\text{cercle} = 2\pi r$.
                - L'aire d'un disque de rayon $r$ est
                  $\mathscr A_\text{disque} = \pi r^2$.
            - Les volumes pour
                - Un pavé droit de côtés $L$, $H$, $P$ a pour volume
                  $\mathscr V_{pavé} = L \times H \times P$.
                - Un prisme droit dont la base a une aire $\mathscr A_\text{base}$,
                  et une hauteur $h$ associée a pour volume
                  $\mathscr V_{prisme} = \mathscr A_\text{base} \times h$.
                - Une pyramide dont la base a une aire $\mathscr A_\text{base}$,
                  et une hauteur $h$ associée a pour volume
                  $\mathscr V_{pyramide} = \dfrac {1}{3} \mathscr A_\text{base} \times h$.
                - Une boule de rayon $r$ a pour volume
                  $\mathscr V_{boule} = \dfrac{4}{3} \pi r^3$.
            ```

??? danger "Remarque technique sur les unités"
    On devrait utiliser une [espace **fine** insécable](https://fr.wikipedia.org/wiki/Espace_ins%C3%A9cable) entre la partie numérique et l'unité.

    - Pour simplifier, on peut utiliser une espace-mot insécable à la place.
    - Pour écrire les unités facilement, on pourra donc suivre les exemples :

    |Markdown|Rendu|
    |--------|----:|
    |`#!latex $41~\text{km}$` |$41~\text{km}$ |
    |`#!latex $35~\text{m}^2$`|$35~\text{m}^2$|

## Pour aller plus loin

- Avec ce qui a été vu précédemment, on peut écrire une large partie d'un cours de mathématique au collège.
- Une partie de cette [section](https://fr.wikibooks.org/wiki/LaTeX/%C3%89crire_des_math%C3%A9matiques) est valable pour le mode mathématique en Markdown.
La [suite](https://fr.wikibooks.org/wiki/LaTeX/Math%C3%A9matiques) pourra être utile.
