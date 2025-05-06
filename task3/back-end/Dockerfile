FROM python:3.12-slim

# Installer les dépendances
RUN apt-get update && apt-get install -y python3-pip

# Installer Flask et Flask-CORS
RUN pip install flask flask-cors

# Créer un répertoire de travail
WORKDIR /app

# Copier le fichier de l'API
COPY api.py /app/api.py

# Exposer le port
EXPOSE 5252

# Lancer le serveur Flask
CMD ["python", "api.py"]
