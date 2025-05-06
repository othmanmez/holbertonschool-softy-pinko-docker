FROM ubuntu:latest

# Éviter les demandes d'entrée utilisateur
ENV DEBIAN_FRONTEND=noninteractive

# Installer Python3, pip3 et supprimer la restriction EXTERNALLY-MANAGED
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm /usr/lib/python*/EXTERNALLY-MANAGED

# Installer Flask avec pip3
RUN pip3 install flask

# Définir le dossier de travail
WORKDIR /app

# Copier le fichier api.py dans l'image
COPY ./api.py /app/api.py

# Commande pour lancer le serveur Flask
CMD ["python3", "api.py"]
