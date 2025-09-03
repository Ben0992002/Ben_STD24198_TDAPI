# Preparation-Examen Pratique - API & Spécification OpenAPI

Ce dépôt contient la solution complète pour l'exercice 1 du TD d'API. Il inclut les spécifications OpenAPI (OAS3) pour chaque exercice ainsi que le code Python de l'API correspondante.

## Structure du projet

- **`api.py`** : Le code source de l'API, développé avec FastAPI.
- **`exo1.yml`** : Spécification OAS3 pour l'exercice 1 (`GET /ping`).
- **`exo2.yml`** : Spécification OAS3 pour l'exercice 2 (`GET /welcome` et `GET /students`).
- **`exo3.yml`** : Spécification OAS3 pour l'exercice 3 (modèle `Student` et route `POST /students`).
- **`exo4.yml`** : Spécification OAS3 pour l'exercice 4 (`GET /students` et `POST /students`).
- **`exo5.yml`** : Spécification OAS3 pour l'exercice 5 (autorisation via en-tête HTTP).
- **`exo6.yml`** : Spécification OAS3 pour l'exercice 6 (route `PUT` pour la mise à jour).

## Comment utiliser l'API

Pour lancer l'API, assurez-vous d'avoir Python et les bibliothèques nécessaires installées, puis exécutez la commande suivante dans votre terminal :

```bash
uvicorn api:app --reload
