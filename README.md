# Notion Learning Extraction

Un projet d'extraction automatique des données d'apprentissage depuis une **base de données Notion** vers une **base SQLite**.

## 📋 Description

Ce projet récupère les informations d'apprentissage (ressources, cours, livres, etc.) stockées dans Notion et les extrait dans une base de données SQLite pour analyse ultérieure.

## 🎯 Fonctionnalités

- ✅ Connexion à l'API Notion
- ✅ Extraction des données de la datasource Notion
- ✅ Transformation et normalisation des données
- ✅ Sauvegarde dans SQLite (`notion_pipe.db`)
- ✅ Automatisation via cron (exécution quotidienne à 18h)
- ✅ Logging des extractions

## 📁 Structure du Projet

```
notionlearning/
├── extraction.py              # Script principal d'extraction
├── run_extraction.sh         # Script wrapper pour cron
├── learnings_data.csv        # Export CSV (optionnel)
├── notion_pipe.db            # Base de données SQLite
├── cron.log                  # Logs des exécutions cron
├── DataSourceExploration.ipynb  # Exploration des données
├── Exploration.ipynb         # Notebook d'analyse
├── Dockerfile               # Configuration Docker/Metabase
└── README.md               # Ce fichier
```

## 🔧 Installation

### Prérequis
- Python 3.8+
- pip
- Virtualenv (recommandé)

### Étapes

1. **Cloner le projet**
```bash
cd <chemin-du-projet>
```

2. **Créer un environnement virtuel**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install python-dotenv notion-client pandas
```

4. **Configurer les variables d'environnement**

Créer un fichier `.env` à la racine :
```
NOTION_TOKEN=your_notion_api_token
DATA_SOURCE_ID=your_datasource_id
```

## 🚀 Utilisation

### Exécution manuelle
```bash
python3 extraction.py
```

### Exécution via le script wrapper
```bash
chmod +x run_extraction.sh
./run_extraction.sh
```

### Automatisation avec Cron

La tâche cron est déjà configurée :
```bash
0 18 * * * <chemin-du-projet>/run_extraction.sh
```

**Explications :**
- `0` = minute 0
- `18` = 18h (6h du soir)
- `* * *` = tous les jours

Pour éditer le cron :
```bash
crontab -e
```

Pour voir les tâches cron :
```bash
crontab -l
```

## 📊 Données Extraites

Le script extrait les champs suivants de Notion :
- **Title** : Nom de la ressource
- **Source** : Type de source (Youtube, Udemy, Livre, etc.)
- **Date Started** : Date de début d'apprentissage
- **Status** : Statut de progression
- **Topic** : Sujet/Catégorie
- **URL** : Lien vers la ressource
- Et autres propriétés personnalisées

## 📝 Logs

Les logs sont enregistrés dans `cron.log` :
```
====Extraction dim. 11 janv. 2026 18:44:16 CET ====
Datasource fetched successfully.
Learnings Extracted Successfully.
Number of learnings extracted: 26
Extraction Finished Successfully.
```

## 🗄️ Base de Données

La base SQLite `notion_pipe.db` contient une table `learnings` avec tous les enregistrements extraits.

Pour explorer la base :
```bash
sqlite3 notion_pipe.db
sqlite> .mode column
sqlite> .headers on
sqlite> SELECT * FROM learnings;
```

## 📦 Docker (Metabase)

Un Dockerfile est fourni pour visualiser les données avec Metabase :
```bash
docker run -d -p 3000:3000 \
  -v metabase-data:/metabase-data \
  -v <chemin-du-projet>:/notion_project \
  -e "MB_DB_FILE=/metabase-data/metabase.db" \
  --name metabase \
  metabase/metabase
```

Accédez ensuite à : `http://localhost:3000`

## 🔒 Sécurité

- Ne jamais commiter le fichier `.env` avec les tokens
- Ajouter `.env` à `.gitignore`

## 📚 Ressources Utiles

- [Documentation Notion API](https://developers.notion.com/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [SQLite Documentation](https://www.sqlite.org/cli.html)
- [Crontab Guide](https://crontab.guru/)

## 👤 Auteur

<MM>

## 📄 Licence

MIT
