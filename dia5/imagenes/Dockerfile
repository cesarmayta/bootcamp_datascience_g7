#imagen base
FROM ubuntu:latest

#actualización e instalación de python
RUN apt-get update
RUN apt-get install python3 python3-dev python3-pip -y

#copiamos los archivos a la imagen
COPY index.html .

#ejecutamcos un comando terminal
CMD ["python3","-m","http.server","5000"]

#exponemos el puerto
EXPOSE 5000