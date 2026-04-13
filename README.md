[![Abrir en GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/MicrosoftDocs/mslearn-advanced-copilot)

# API de Clima para Viajes con FastAPI

Este proyecto contiene una API web en Python construida con FastAPI.
Expone información histórica de temperatura mínima y máxima por país,
ciudad y mes a partir del archivo weather.json.

[![Powered by Awesome Copilot](https://img.shields.io/badge/Powered_by-Awesome_Copilot-blue?logo=githubcopilot)](https://aka.ms/awesome-github-copilot)

## Inicio rápido

### 1) Requisitos

- Python 3.10 o superior
- pip

### 2) Clonar el repositorio

```bash
git clone https://github.com/MicrosoftDocs/mslearn-advanced-copilot.git
cd mslearn-advanced-copilot
```

### 3) Crear y activar un entorno virtual

Linux o macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4) Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5) Ejecutar la API

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

La aplicación quedará disponible en:

- Documentación Swagger: http://localhost:8000/docs
- Documentación ReDoc: http://localhost:8000/redoc
- Ruta raíz: http://localhost:8000/ (redirige a /docs)

## Endpoints disponibles

### Obtener países

- Método: GET
- Ruta: /countries
- Respuesta: lista de países disponibles

Ejemplo:

```bash
curl http://localhost:8000/countries
```

### Obtener ciudades por país o región

- Método: GET
- Ruta: /countries/{country}
- Respuesta: lista de ciudades del país o región indicado
- Error 404: si el país o región no existe

Ejemplos:

```bash
curl http://localhost:8000/countries/Spain
curl http://localhost:8000/countries/Portugal
```

### Obtener clima por país, ciudad y mes

- Método: GET
- Ruta: /countries/{country}/{city}/{month}
- Respuesta: objeto JSON con temperaturas high y low

Ejemplo:

```bash
curl http://localhost:8000/countries/Spain/Seville/January
```

## Ejecutar pruebas

Este proyecto utiliza pytest.

```bash
pytest -q
```

Si usas un entorno virtual, confirma que esté activado antes de ejecutar
las pruebas para evitar errores de dependencias.

## Estructura general del proyecto

- main.py: aplicación FastAPI y definición de rutas
- weather.json: datos históricos de clima
- test_main.py: pruebas automáticas
- static/: recursos estáticos del frontend

## Desarrollo recomendado

- Usa modo recarga con --reload durante el desarrollo.
- Consulta /docs para explorar y probar los endpoints.
- Agrega pruebas en test_main.py cada vez que incorpores una ruta nueva.

## Avisos legales

Microsoft y los contribuidores otorgan licencia para la documentación y
otros contenidos de este repositorio bajo la licencia Creative Commons
Attribution 4.0 International Public License:
https://creativecommons.org/licenses/by/4.0/legalcode

El código fuente se distribuye bajo licencia MIT. Revisa los archivos
LICENSE y LICENSE-CODE para más detalles.

Microsoft, Windows, Microsoft Azure y otros nombres de productos o
servicios de Microsoft mencionados en la documentación pueden ser marcas
registradas en Estados Unidos y otros países.

Información de privacidad:
https://privacy.microsoft.com/en-us/
