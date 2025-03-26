FROM ubuntu:latest

# Mettre à jour les paquets et installer mysql-client
RUN apt-get update && \
    apt-get install -y mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Démarrer un shell Bash
CMD ["bash"]
