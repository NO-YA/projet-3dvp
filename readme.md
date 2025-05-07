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