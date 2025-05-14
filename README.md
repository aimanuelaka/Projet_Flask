# 📚 Application Flask de Gestion des Étudiants

Une application web développée avec **Flask** permettant de gérer des étudiants (CRUD), avec authentification sécurisée, interface responsive Bootstrap, interactions AJAX, et déploiement via Docker.

---

## 🚀 Fonctionnalités

- 🔐 Authentification avec **Flask-Login** et mots de passe hashés avec **Flask-Bcrypt**
- 🧑‍🎓 CRUD complet des étudiants (Nom, Email)
- 📊 Liste interactive avec **DataTables** (tri, pagination, recherche)
- ⚡️ AJAX pour les opérations de création, modification et suppression (sans rechargement)
- 🎨 Interface moderne grâce à **Bootstrap 5**
- 🐳 Déploiement facile avec **Docker**

---

## 🛠️ Stack Technique

- Python 3.10
- Flask / Flask-WTF / Flask-Login / Flask-Bcrypt / Flask-SQLAlchemy
- SQLite (base de données)
- Bootstrap 5
- jQuery + DataTables
- Docker

---

## 🖼️ Aperçu

> Screenshots ou démo GIF ici *(optionnel)*

---

---

##. 🔒 Sécurité
CSRF protection activée via Flask-WTF

Mots de passe hachés avec Bcrypt

Accès aux routes restreint aux utilisateurs connectés

--- 
##. 🤝 Contribuer
Les contributions sont les bienvenues ! Forkez le projet, créez une branche, soumettez un pull request.

##. 📄 Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d’informations.

##. 👤 Auteur
Développé par Votre @aimanuelaka
N’hésitez pas à me contacter pour toute suggestion ou collaboration.


##. 📁 Arborescence
```bash
Copier
Modifier
.
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   ├── ajouter_etudiant.html
│   ├── etudiants.html
│   └── ...
├── static/             # fichiers JS/CSS si nécessaires
└── README.md

---




---

##. 📦 Installation Locale

#1. **Cloner le dépôt**

```bash
git clone https://github.com/aimanuelaka/Flask_Etudiant.git
cd Flask_Etudiant

---

#2.Créer un environnement virtuel et l'activer


Copier
Modifier
python -m venv venv
source venv/bin/activate  # sur Windows : venv\Scripts\activate
Installer les dépendances

bash
Copier
Modifier
pip install -r requirements.txt
Lancer l’application

bash
Copier
Modifier
python app.py

