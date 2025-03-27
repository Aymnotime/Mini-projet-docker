# Utilisation de l'image Python officielle
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier de l'application
COPY app.py app.py

# Installer Flask et le connecteur MySQL directement
RUN pip install flask mysql-connector-python

# Exposer le port 5000
EXPOSE 5000

# Commande pour lancer l'application Flask
CMD ["python", "app.py"]
