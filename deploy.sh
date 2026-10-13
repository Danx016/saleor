#!/bin/bash
set -e

echo "==================================================="
echo "         DESPLIEGUE DE SALEOR CON DOCKER          "
echo "==================================================="

# Si no existe .env, crearlo desde .env.example
if [ ! -f .env ]; then
    echo "Creando .env a partir de .env.example..."
    cp .env.example .env
fi

echo "[1/4] Levantando PostgreSQL y Redis..."
docker compose up -d db cache

echo "[2/4] Esperando a que PostgreSQL este listo..."
until docker compose exec -T db pg_isready -U saleor -d saleor; do
    echo "Esperando por PostgreSQL..."
    sleep 2
done

echo "[3/4] Ejecutando migraciones y creando datos de muestra..."
docker compose run --rm api python manage.py migrate
docker compose run --rm api python manage.py populatedb --createsuperuser

echo "[4/4] Levantando todos los servicios (API, Dashboard, Worker, Mailpit)..."
docker compose up -d

echo ""
echo "==================================================="
echo "          DESPLIEGUE EXITOSO EN EL SERVIDOR         "
echo "==================================================="
echo "Dashboard:         http://<TU_IP_O_DOMINIO>:9000/"
echo "GraphQL API:       http://<TU_IP_O_DOMINIO>:8000/graphql/"
echo "Bandeja Emails:    http://<TU_IP_O_DOMINIO>:8025/"
echo ""
echo "Usuario administrador:"
echo "Email:    admin@example.com"
echo "Password: admin"
