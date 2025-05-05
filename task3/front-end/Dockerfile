# Utiliser l'image officielle de Nginx
FROM nginx:latest

# Copier le répertoire contenant les fichiers front-end dans le répertoire de Nginx
COPY ./softy-pinko-front-end /usr/share/nginx/html

# Copier la configuration Nginx
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# Exposer le port 80
EXPOSE 80
