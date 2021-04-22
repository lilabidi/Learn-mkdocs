# Débuter avec MkDocs

Auteur : Franck CHAMBON

Présentation des premiers pas pour construire un site web statique avec [MkDocs for Material](https://squidfunk.github.io/mkdocs-material/).

À l'instar de cette page, il y a quelques éléments dynamiques et la construction est assez élémentaire pour être proposée aux élèves en SNT, ou bien en NSI pour la documentation de projet.

## Prérequis

!!! note "Définitions"
    Par **machine**, on entend PC, smartphone ou tablette Android. On peut créer ou mettre à jour ce genre de site depuis n'importe quel type de machine qui a accès à Internet.

    Par **PC**, on entend un ordinateur avec un système d'exploitation Windows, Mac ou Linux.

    Pour **Linux**, on prendra l'exemple d'une distribution basée sur les paquets debian, sinon vous devriez savoir adapter ce qui suit sans difficulté.

!!! tip "Machine raisonnablement à jour"
    === "Android"
        ??? tip "Passer en mode développeur"
            - Accéder à `Paramètres` de l’appareil Android
            - Aller dans les paramètres `Système`
            - Aller dans ` À propos du téléphone `
            - Tapoter 7 fois ` Numéro de build `
            - C'est fait !

        !!! exemple "Mises à jour"
            1. Installer [F-Droid](https://www.f-droid.org/fr/).
            2. À partir de F-Droid, installer [Termux](https://termux.com/)
            4. Dans Termux, entrer
            ```bash
            apt update
            apt upgrade
            apt install python
            pip install --upgrade pip
            ```
    === "Linux"
        ??? tip "Administration"
            Dans un terminal entrer
            ``` bash
            sudo apt update
            sudo apt upgrade
            sudo dpkg --configure -a
            sudo apt install python3-pip
            ```
            Redémarrer, pour que le `PATH` inclut bien votre chemin de binaires, c'est probablement déjà le cas...

            !!! info "Gestionnaire de paquets Python"
                [pip](https://fr.wikipedia.org/wiki/Pip_(gestionnaire_de_paquets)) est le gestionnaire de paquets Python, suivant votre machine la commande est `pip` ou `pip3`.

                Dans la suite on la désignera par `pip`, si c'est `pip3` ; adapter.


        !!! example "Mises à jour"
            Dans un terminal entrer
            ``` bash
            pip install --upgrade pip
            ```
    
    === "Mac"
        ??? tip "Administration"
            Aucune idée... toute aide bienvenue
        
        !!! example "Mises à jour"
            Dans un terminal entrer
            ``` bash
            pip install --upgrade pip
            ```

            À confirmer ????

    === "Windows"
        ??? tip "Administration"
            Aucune idée... toute aide bienvenue
        
        !!! example "Mises à jour"
            Dans un terminal entrer
            ``` bash
            python -m pip install --upgrade pip
            ```

## Installation

!!! done "Vérification"
    Vérifier votre installation suivant votre machine avec

    === "python / pip"
        ```bash
        $ python --version
        Python 3.8.5
        $ pip --version
        pip 21.0.1 from .../lib/python3.8/site-packages/pip (python 3.8)
        ```

    === "python3 / pip3"
        ```bash
        $ python3 --version
        Python 3.8.5
        $ pip3 --version
        pip 21.0.1 from .../lib/python3.8/site-packages/pip (python 3.8)
        ```

    Si une erreur survient, contacter l'administrateur de la machine.

!!! tip "Material for MkDocs"
    Dans un terminal, avec `pip` ou `pip3` selon votre machine.

    === "python / pip"
        ```bash
        pip install mkdocs-material
        ```

    === "python3 / pip3"
        ```bash
        pip3 install mkdocs-material
        ```

    Cela installe plusieurs paquets utiles automatiquement.

## Créer un nouveau MkDocs

!!! tip "Votre expérience"
    Dans un terminal, remplacer `expérience` par un identifiant de votre choix. Sans espace, c'est mieux.

    ```bash
    mkdocs new expérience
    cd expérience
    ```

    Si vous étiez **déjà** dans un répertoire vide pour votre expérience

    ```bash
    mkdocs new .
    ```

    `.` désignant le répertoire courant.

!!! done "Vérification"
    Vous devriez avoir eu le message correspondant suivant

    <pre>
    INFO    -  Creating project directory: expérience
    INFO    -  Writing config file: expérience/mkdocs.ym
    INFO    -  Writing initial docs: expérience/docs/index.md
    </pre>

## Suivi en direct

!!! abstract "Au programme"
    Nous allons construire un site web, d'abord en local sur votre machine.

    On pourra le consulter depuis votre navigateur Internet.

    À chaque modification d'un fichier, le site sera mis à jour.

!!! tip "Construction à la volée"
    Dans un terminal, entrer

    ```bash
    mkdocs serve
    ```

    !!! done "Victoire ?"
        Vous aurez une sortie qui ressemble à 

        <pre>
        INFO    -  Building documentation... 
        INFO    -  Cleaning site directory 
        INFO    -  Documentation built in 0.07 seconds 
        <font color="#4E9A06">[I 210422 09:39:37 server:335]</font> Serving on <u>http://127.0.0.1:8000</u>
        INFO    -  Serving on <u>http://127.0.0.1:8000</u>
        <font color="#4E9A06">[I 210422 09:39:37 handlers:62]</font> Start watching changes
        INFO    -  Start watching changes
        </pre>

    !!! bug "Échec ?"
        Si vous avez une sortie qui ressemble à
        <pre>
        INFO    -  Building documentation... 

        Config file '...expérience/docs/mkdocs.yml' does not exist.
        </pre>
        C'est que vous avez lancé la commande dans le mauvais répertoire.

!!! tip "Visionnage en direct"
    Ouvrir votre navigateur Web à l'adresse indiquée.

    Avec Linux, il suffit de faire un clic-droit sur l'adresse [http://127.0.0.1:8000/](http://127.0.0.1:8000/), puis `Ouvrir le lien`.
    
    Mettre ce lien dans les en marque-page ; vous y reviendrez souvent :wink:.

    Si vous avez un second écran, c'est le moment d'y placer le navigateur :sunglasses:

    ![premier affichage](./images/premier.png)

!!! note "Modifions le site"
    Les fichiers dans le répertoire ont pour l'instant cette architecture

    ```
    .
    ├─ docs/
    │  └─ index.md
    └─ mkdocs.yml
    ```

!!! done "Victoire"
    Avec un bon éditeur de texte, éditer le fichier `docs/index.md`

    Voici ce qu'on peut faire.

    ![modif1 index.md](./images/modif1.svg)

    Avec pour résultat.

    ![résultat modif1](./images/modif1.png)

    À chaque fois qu'un fichier sera modifié et **enregistré**, le site sera mis à jour dans le navigateur.

    **Faîtes vos premières expériences !**

!!! info "Le site n'est pas encore construit physiquement"
    Il est possible de construire physiquement le site avec

    ```bash
    mkdocs build
    ```

    C'est utile si avez une solution pour l'héberger ...

    Pour nous ce sera inutile.
