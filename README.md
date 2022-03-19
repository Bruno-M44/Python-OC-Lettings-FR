## Résumé

Site web d'Orange County Lettings

## Développement local


### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Bruno-M44/Python-OC-Lettings-FR`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

---
## Déploiement

### Description du fonctionnement du Pipeline CircleCi

#### Lors d'un commit sur n'importe quelle branche autre que la master :
- Lancement du job :
    - build : 
      - créer le build
    - si ok, lancement de test qui lance les tests de l'application
    
#### Lors d'un commit sur la branche master :
   
- Lancement des jobs :
     - build
     - si ok, lancement de test
     - si ok, lancement du job containerize :
        - Cela va créer une image docker et l'uploader sur le docker hub.
     - si ok, lancement de deploy :
        - L'image docker va s'installer sur Heroku.

---

## CircleCi :

[https://app.circleci.com/pipelines/github/Bruno-M44](https://app.circleci.com/pipelines/github/Bruno-M44)

Création des variables d'environnement au niveau du projet :

- Dans **Projets**:
- Cliquez sur `Project Settings`  (Les 3 petits points)
- Cliquez sur `Environment Variables`  
- Cliquez sur `Add Environment Variables`  

|   Nom des Variables  |   Valeurs à renseigner   |  
|---    |---    |  
|   DJANGO_SECRET_KEY   |   `fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s`   |  
|   DOCKER_PASSWORD   |   `zJVkhL4wERc32a`   |  
|   DOCKER_LOGIN |   `brunom44`   |  
| DSN_SENTRY    | `https://9b0b08a4791c473d9332fabedc59e4de@o1162749.ingest.sentry.io/6250264` |  
| HEROKU_API_KEY  |  `96f8ff0b-61e8-49c1-8eb9-ecb6f5257239`  |  
| HEROKU_APP_NAME | `oc-lettings-b44` |  
---

## Docker Hub :

[Docker-Hub brunom44 Repository](https://hub.docker.com/repository/docker/brunom44/oc-lettings) permet de stocker en ligne l'image docker de notre application.  

La commande unique pour récupération de l'application en local et son démarrage immédiat est :

`docker run --pull always -p 8000:8000 --name oc-lettings brunom44/oc-lettings:9b258b461e92f5904dfc9c9d5d50f13ba1487998`  

L'application est accessible à l'adresse suivante : [http://localhost:8000/](http://localhost:8000/)

---

## Heroku :
[L'application sur Heroku](https://oc-lettings-b44.herokuapp.com/)  

---

## Sentry :

Sentry permet de faire le [monitoring de l'application](https://sentry.io/organizations/my-company-6c/projects/oc-lettings/?project=6250264).
