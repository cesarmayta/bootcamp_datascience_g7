# para ver versión de docker
docker version

# para descargar una imagen
docker pull nginx

# para ver mis imagenes
docker images

# para desplegar un contenedor
docker run -d -p 8080:80 --name mi-nginx nginx

# para ver mis contenedores
docker ps

# para detener un contenedor
docker stop mi-nginx

# ver contenedores apagados
docker ps --all

# para eliminar un contenedor
docker rm mi-nginx 

# para desplegar un contenedor y poder detenerlo y eliminarlo al mismo tiempo
docker run -d --rm -p 8080:80 --name mi-nginx nginx


# para interactuar con nuestro contenedor

## para ver los logs
docker logs mi-nginx

## para ejecutar un comando dentro del contenedor
docker exec mi-nginx ls

## para ingresar al terminal de mi contenedor
docker exec -it mi-nginx bash
exit


# VOLUMENES
docker volume ls
docker volume create web
docker run -d --rm -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html --name nginx-custom nginx

