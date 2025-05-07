En quelques mots...
Ce projet, c'est une API REST qu'on a construite avec FastAPI. L'idée, c'est de pouvoir gérer facilement tout un catalogue d'objets qu'on appelle ici des Items (imaginez des produits dans une boutique, par exemple). Et le truc cool, c'est qu'on a vraiment pensé à tout : c'est sécurisé, on a des tests qui tournent tout seuls pour vérifier que tout marche bien, on a même un outil (flake8) qui nous aide à écrire un code propre, et tout ça se met à jour et se déploie automatiquement grâce à GitHub Actions et Render.


Ce qu'on peut faire avec l'API :
 On peut faire tout ce qu'il faut sur les produits : les créer, les afficher, les modifier et les supprimer (le fameux CRUD !).

 On a mis en place des tests automatiques avec pytest, comme ça, on est sûrs que tout fonctionne nickel sans avoir à tout vérifier à la main à chaque fois.
 On utilise flake8 pour que notre code soit bien propre et respecte les bonnes pratiques. C'est un peu notre coach de style pour le code ! 

 Grâce à GitHub Actions, quand on change le code, tout se construit et se teste automatiquement. C'est comme avoir un petit robot qui vérifie tout pour nous !

 Et le déploiement ? C'est Render qui s'en occupe ! Dès qu'il y a une mise à jour, hop, c'est en ligne automatiquement. Hyper pratique !


Les outils qu'on a utilisés :
-Python 3.11 (la base de tout !)
-FastAPI (notre super framework pour l'API)
-Uvicorn (pour faire tourner l'API)
-Pydantic (pour valider nos données, c'est important !)
-Pytest (pour nos tests automatiques)
-Flake8 (notre coach de style de code)
-GitHub Actions (pour l'automatisation)
-Render (pour héberger l'API)
Pour l'installer chez vous :

Bash

git clone https://github.com/monpseudo/3DVP.git
cd 3DVP
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

DIFFICULTER RENCONTRER
Déjà, au début, mes tests, ils passaient pas. Un test en particulier, pour supprimer un produit, il me disait que le message de l'API était pas bon. En fait, c'était juste un smiley qui manquait, mais bon, un test qui foire, c'est toujours stressant ! Ça m'a appris qu'il faut vraiment être précis quand on teste et bien comprendre ce que l'API renvoie exactement.

Après, quand j'ai voulu rendre mon code un peu plus propre avec flake8, là, c'était la fête aux erreurs ! Des lignes vides pas au bon endroit, des espaces qui traînent, des commentaires mal formés... J'me suis rendu compte que respecter les conventions de style, c'est pas juste pour faire joli, ça aide vraiment à lire le code plus facilement.

Et puis, Git, quelle aventure ! J'ai eu toutes les peines du monde à pousser mon projet sur GitHub. Des erreurs bizarres, comme quoi il trouvait pas le dépôt, ou que ma branche locale n'existait pas... J'ai dû trifouiller pas mal de commandes avant de comprendre comment ça marchait vraiment, comment lier ma branche locale au dépôt distant, tout ça.

Ah oui, et flake8 qui me disait qu'il existait pas ! Fallait juste l'installer dans mon environnement virtuel, mais sur le coup, j'étais un peu perdu. Ça m'a montré qu'il faut bien penser à installer tous les outils dont on a besoin.

Pour tester mon API, j'ai essayé de taper une commande GET direct dans le terminal... grosse erreur ! J'ai appris qu'il faut un client HTTP pour ça, comme un navigateur ou un outil spécialisé.

Et le pompon, c'est quand j'ai voulu automatiser tout ça avec GitHub Actions. Mon workflow plantait parce qu'il trouvait pas flake8 ! Encore une histoire d'installation, fallait que je l'ajoute à mon fichier de dépendances.

Même mon éditeur de code m'a fait des frayeurs avec un avertissement sur ma clé privée pour le déploiement. Apparemment, c'est normal, mais sur le moment, ça inquiète !