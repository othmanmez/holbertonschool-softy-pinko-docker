# Utilisation de l'image Python de base
FROM python:3.9-slim

# Répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . /app/

# Exposer le port
EXPOSE 5252

# Commande pour démarrer l'application
CMD ["python", "app.py"]
