# 🛡️ Microservicio de Verificación de Personas en Lista Negra

Este proyecto implementa un microservicio REST en **FastAPI** que permite verificar si una persona se encuentra en una **lista negra almacenada en PostgreSQL**.

---

## 📌 Requisitos previos

- Python 3.10+
- Docker y Docker Compose
- PostgreSQL (se puede usar el contenedor definido en `docker-compose.yml`)
- Alembic (para migraciones)

---

## ⚙️ Configuración de la base de datos con Docker

El proyecto incluye un `docker-compose.yml` de ejemplo para levantar una base de datos PostgreSQL:

```yaml
version: "3.9"

services:
  db:
    image: postgres:15
    container_name: verificacion-personas
    restart: always
    environment:
      POSTGRES_USER: test
      POSTGRES_PASSWORD: pruebatecnica
      POSTGRES_DB: verificacion-personas
    ports:
      - "5433:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
    driver: local
```

### Levantar la base de datos

```bash
docker-compose up -d
```

La base quedará disponible en:

```
postgresql://test:pruebatecnica@localhost:5433/verificacion-personas
```

---

## 🗄️ Migraciones con Alembic

Antes de ejecutar la API, debes aplicar las migraciones con **Alembic** para crear las tablas necesarias.

Ejecuta:

```bash
alembic upgrade head
```

Esto creará la tabla `personas_bloqueadas` y cargará automáticamente **10 registros de prueba**.

---

## 👤 Datos iniciales cargados

La lista negra contiene los siguientes registros:

- juan pérez
- maría lópez
- carlos hernández
- ana gonzález
- pedro ramírez
- lucía martínez
- josé fernández
- elena castro
- miguel torres
- sofía díaz

---

## 🔑 Seguridad con JWT

La API está protegida mediante **JWT hardcodeado**.

En el archivo `.env` se deben configurar las siguientes variables:

```env
DATABASE_URL="postgresql://test:pruebatecnica@localhost:5433/verificacion-personas"
HARDCODED_JWT="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTc1NDAwNzY4OCwiZXhwIjoxNzU0MDExMjg4fQ.606OUHGpL0mRq1qkyKcusk7-YcApj3XfS5MxHDHYY2w"
```

⚠️ **Nota**: Para acceder a los endpoints, es obligatorio enviar el header con el token:

```
Authorization: Bearer <HARDCODED_JWT>
```

---

## ▶️ Ejecutar la API

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

La API estará disponible en:

```
http://127.0.0.1:8000
```

---

## 📖 Documentación automática

FastAPI expone la documentación OpenAPI automáticamente en:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Ejemplo de uso

### Request
```http
POST /users/verificar
Authorization: Bearer <HARDCODED_JWT>
Content-Type: application/json

{
  "nombre_completo": "juan pérez"
}
```

### Response
```json
{
  "encontrado": true
}
```

---

## 📌 Notas

- Si se envían datos incorrectos, la API devuelve `400 Bad Request`.
- Si ocurre un error en la conexión a la BD, devuelve `500 Internal Server Error`.
- La autenticación con JWT es **simulada (hardcodeada)**, solo para fines de la prueba técnica.

---
