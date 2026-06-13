# housing-api-g7

Housing API G7 con FastAPI, PostgreSQL y Nginx.

## Despliegue con Docker Compose

1. Si no tienes un archivo `.env`, crealo desde el ejemplo:

```bash
cp .env.example .env
```

Si ya tienes `.env`, no lo sobrescribas; usa `.env.example` como referencia y agrega `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` y `HTTP_PORT`.

2. Edita `.env` y cambia `POSTGRES_PASSWORD` por una clave segura.

3. Construye y levanta los contenedores:

```bash
docker compose up -d --build
```

4. Verifica el estado:

```bash
docker compose ps
```

5. Prueba la API desde el VPS:

```bash
curl http://localhost/
```

Nginx publica el puerto `80` y reenvia las peticiones al contenedor `api` en el puerto interno `8000`. La base de datos PostgreSQL queda solo dentro de la red Docker.
