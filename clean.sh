#!/bin/bash

# Detener todos los contenedores en ejecución
docker stop $(docker ps -q)

# Eliminar todos los contenedores
docker rm $(docker ps -a -q)

# Eliminar todas las imágenes
docker rmi $(docker images -a -q)

# Eliminar todos los volúmenes
docker volume rm $(docker volume ls -q)

# Eliminar todas las redes personalizadas (excepto las predeterminadas)
docker network rm $(docker network ls -q | grep -v "bridge\|host\|none")

# Eliminar todas las imágenes intermedias y capas de imágenes
docker system prune -a -f

# Eliminar la caché de construcción
docker builder prune -f

echo "Docker cleanup completed."
