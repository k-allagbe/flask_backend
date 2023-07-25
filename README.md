# Projet de test pour Entrevue ACIA

Fournir un exercice pratique pour un stagiaire d'application dorsale pour valider les connaissances en Python, en SQL, en gestion de code source et en interface de programmation.

## Prérequis

Pour exécuter ce projet, vous devez installer les logiciels suivants :

- Python 3.8 ou supérieur
- pip (Gestionnaire de paquets Python)
- virtualenv (optionnel mais recommandé)

## Installation

### 1. Cloner le dépôt

Ouvrez un terminal et clonez ce dépôt avec la commande suivante :

```bash
git clone https://github.com/k-allagbe/flask_backend.git
```


### 2. Configuration de l'environnement

Il est recommandé d'utiliser `virtualenv` pour créer un environnement isolé pour le projet. Vous pouvez installer `virtualenv` avec pip :
```bash
pip install virtualenv
```

Ensuite, créez un nouvel environnement virtuel dans le dossier du projet :
```bash
cd flask_version
virtualenv venv
```

Activez l'environnement virtuel :

Sous Windows :
```bash
.\venv\Scripts\activate
```

Sous Unix ou MacOS :
```bash
source venv/bin/activate
```


### 3. Installation des dépendances

Installez les dépendances du projet avec pip :

```bash
pip install -r requirements.txt
```



### 4. Configuration de la base de données

Créez un fichier `.env` à la racine du projet (flask_version) et renseignez-y les informations de connexion à votre base de données :

```bash
DB_USER=votre_nom_utilisateur
DB_PASSWORD=votre_mot_de_passe
DB_HOST=le_server_postgres
DB_NAME=votre_nom_base_de_donnees
DB_SCHEMA_2=votre_nom_schema
DB_TOP_100_VIEW=votre_nom_vue
```


Remplacez `votre_nom_utilisateur`, `votre_mot_de_passe`, `le_server_postgres`, `votre_nom_base_de_donnees`, `votre_nom_schema` et `votre_nom_vue` par les bonnes informations.

### 5. Démarrage de l'application

Vous pouvez maintenant démarrer l'application avec la commande suivante :

```bash
python main.py
```


L'application devrait être disponible à l'adresse suivante : `http://localhost:5000/`

## Exécution des tests

Pour exécuter les tests, utilisez la commande suivante :
```bash
python -m pytest
```

## Tests des routes API

Pour tester les routes de l'API, vous pouvez utiliser l'outil de votre choix comme Postman, curl, etc.

### Route `/api/top`

Cette route renvoie le top N des documents avec les scores les plus élevés. Le paramètre N est optionnel et sa valeur par défaut est 1. Si N est défini et qu'il est inférieur à 1 ou supérieur à 100, la route renvoie une erreur.

Pour tester cette route, utilisez la commande curl suivante :

```bash
curl http://localhost:5000/api/top?n=2
```

Cela devrait renvoyer les deux documents avec les scores les plus élevés. 

