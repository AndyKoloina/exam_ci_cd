# On utilise Nginx pour servir du contenu statique
FROM nginx:alpine

# On copie tes fichiers (index.html, css, etc.) dans le dossier web de Nginx
COPY . /usr/share/nginx/html

# Cloud Run écoute sur le port 8080 par défaut, on configure Nginx pour ça
RUN sed -i 's/listen  80;/listen 8080;/' /etc/nginx/conf.d/default.conf

EXPOSE 8080