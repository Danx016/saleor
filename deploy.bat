@echo off
chcp 65001 >nul
echo ===================================================
echo           DESPLIEGUE LOCAL DE SALEOR
echo ===================================================
echo.

where docker >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Docker no está instalado o no se encuentra en el PATH.
    echo.
    echo Por favor instala Docker Desktop:
    echo 1. Descárgalo desde: https://www.docker.com/products/docker-desktop/
    echo    o ejecuta en PowerShell como Administrador:
    echo    winget install -e --id Docker.DockerDesktop
    echo 2. Inicia Docker Desktop y asegúrate de que el motor esté corriendo.
    echo 3. Vuelve a ejecutar este script.
    echo.
    pause
    exit /b 1
)

docker info >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Docker Desktop está instalado pero no está en ejecución.
    echo Por favor abre la aplicación Docker Desktop y espera a que inicie.
    echo.
    pause
    exit /b 1
)

echo [1/4] Levantando base de datos PostgreSQL y Redis...
docker compose up -d db cache
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Falló al levantar la base de datos o Redis.
    pause
    exit /b 1
)

echo.
echo [2/4] Ejecutando migraciones de base de datos...
docker compose run --rm api python manage.py migrate
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Falló la ejecución de migraciones.
    pause
    exit /b 1
)

echo.
echo [3/4] Poblando catálogo de ejemplo y creando usuario administrador...
docker compose run --rm api python manage.py populatedb --createsuperuser

echo.
echo [4/4] Levantando todos los servicios (API, Dashboard, Worker, Mailpit)...
docker compose up -d

echo.
echo ===================================================
echo           ¡DESPLIEGUE COMPLETADO CON ÉXITO!
echo ===================================================
echo.
echo Accesos disponibles:
echo - Dashboard (Panel Admin):  http://localhost:9000/
echo - GraphQL API & Playground: http://localhost:8000/graphql/
echo - Bandeja de emails (Mailpit): http://localhost:8025/
echo.
echo Credenciales de administrador por defecto:
echo - Email:    admin@example.com
echo - Password: admin
echo.
pause
