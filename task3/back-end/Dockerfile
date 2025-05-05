# Utiliser une image de base Ubuntu
FROM ubuntu:latest

# Installer Python et pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Installer Flask et flask-cors
RUN pip3 install flask flask-cors

# Copier le fichier API dans le conteneur
WORKDIR /app
COPY ./api.py /app/api.py

# Exposer le port 5252 pour l'API
EXPOSE 5252

# Lancer l'application Flask
CMD ["python3", "api.py"]
 