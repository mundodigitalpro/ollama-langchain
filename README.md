
# Ollama LangChain

Este proyecto es una aplicación basada en Docker que utiliza el modelo `ollama` junto con LangChain para procesamiento y generación de lenguaje natural. La configuración permite desplegar el modelo en contenedores Docker, facilitando la implementación y el uso en entornos controlados.

## Descripción

La aplicación Ollama LangChain utiliza Docker para desplegar un modelo de procesamiento de lenguaje natural (NLP) llamado `ollama`. Este proyecto contiene configuraciones de `docker-compose` para manejar varios contenedores y gestionar el entorno de la aplicación de forma eficiente.

## Estructura del Proyecto

- **data/ollama**: Contiene datos específicos del modelo, como blobs y manifiestos.
- **deploy.py**: Script de despliegue que automatiza la configuración y el inicio de los contenedores Docker.
- **docker-compose.yml**: Archivo de configuración para Docker Compose que define los servicios necesarios.
- **clean.sh**: Script para limpiar todos los contenedores, volúmenes, redes y datos de Docker para el proyecto.

## Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [GitHub CLI](https://cli.github.com/) (opcional para gestión de repositorio desde la terminal)

## Instrucciones de Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/mundodigitalpro/ollama-langchain.git
   cd ollama-langchain
   ```

2. Construye y despliega los contenedores:

   ```bash
   python3 deploy.py
   ```

3. Para limpiar el entorno de Docker después de las pruebas, usa el script `clean.sh`:

   ```bash
   ./clean.sh
   ```

## Uso

Este proyecto está diseñado para facilitar el despliegue de modelos de lenguaje en un entorno Docker. Puedes personalizar el modelo que deseas usar especificando el nombre en el script `deploy.py`.

## Notas

- Asegúrate de tener los permisos adecuados para acceder y modificar los archivos y directorios del proyecto.
- El archivo `.gitignore` está configurado para excluir datos temporales y archivos específicos del entorno, como los datos de `data/ollama`.

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request. Cualquier contribución es bienvenida.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.
