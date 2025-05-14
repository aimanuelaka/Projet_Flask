# Étape 1 : Choisir une image de base (image Python)
FROM python:3.10-slim

# Étape 2 : Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /Flask_Etudiant

# Étape 3 : Copier le fichier requirements.txt d'abord
COPY requirements.txt .

# Étape 4 : Installer les dépendances depuis le fichier requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Étape 5 : Copier tous les fichiers restants dans le conteneur
COPY . /Flask_Etudiant

# Étape 6 : Exposer le port sur lequel l'app écoute (par défaut Flask écoute sur le port 5000)
EXPOSE 5000

# Étape 7 : Commande pour démarrer l'application Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
