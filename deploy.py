import os
import subprocess
import time

def check_docker():
    try:
        result = subprocess.run(['docker', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Docker is installed and accessible.")
    except subprocess.CalledProcessError as e:
        print("Docker is not installed or not accessible in the current PATH.")
        print(e)
        exit(1)

def image_exists(image_name):
    result = subprocess.run(['docker', 'images', '-q', image_name], stdout=subprocess.PIPE)
    return result.stdout.strip() != b''

def container_exists(container_name):
    result = subprocess.run(['docker', 'ps', '-aqf', f'name={container_name}'], stdout=subprocess.PIPE)
    return result.stdout.strip() != b''

def pull_image(image_name):
    print(f"Pulling Docker image {image_name}...")
    subprocess.run(['docker', 'pull', image_name])

def run_container(image_name, container_name, run_command):
    if not container_exists(container_name):
        print(f"Running Docker container {container_name} from image {image_name}...")
        subprocess.run(run_command)
    else:
        print(f"Docker container {container_name} already exists. Skipping run.")

def build_image(image_name, dockerfile_path='.'):
    if not image_exists(image_name):
        print(f"Building Docker image {image_name}...")
        subprocess.run(['docker', 'build', dockerfile_path, '-t', image_name])
    else:
        print(f"Docker image {image_name} already exists. Skipping build.")

def create_and_start_containers(model_name):
    print("Creating and starting Docker containers...")
    env_vars = os.environ.copy()
    env_vars['OLLAMA_MODEL'] = model_name
    subprocess.run(['docker-compose', 'up', '-d'], env=env_vars)

def wait_for_container(container_name):
    print(f"Waiting for container {container_name} to be ready...")
    while True:
        result = subprocess.run(['docker', 'inspect', '-f', '{{.State.Health.Status}}', container_name], stdout=subprocess.PIPE)
        if result.stdout.strip() == b'healthy':
            break
        time.sleep(1)
    print(f"Container {container_name} is ready.")

def download_model(container_name, model_name='phi'):
    print(f"Downloading model {model_name} into container {container_name}...")
    result = subprocess.run(['docker', 'exec', '-it', container_name, 'ollama', 'run', model_name])
    if result.returncode != 0:
        print(f"Failed to download model {model_name} into container {container_name}.")
    else:
        print(f"Successfully downloaded model {model_name} into container {container_name}.")

def main():
    check_docker()

    # Paso 1: Verifica si la imagen existe, y si no, la descarga
    ollama_docker_image = 'ollama/ollama'
    app_image = 'jose/ollama-langchain'
    
    if not image_exists(ollama_docker_image):
        pull_image(ollama_docker_image)

    # Paso 2: Verifica si la imagen de la app existe, y si no, la construye
    build_image(app_image, '.')

    # Paso 3: Pide el nombre del modelo y crea/inicia los contenedores
    model_name = input("Enter the model name to download (default is 'phi'): ") or 'phi'
    create_and_start_containers(model_name)

    # Paso 4: Espera a que el contenedor `ollama-container` esté listo
    # wait_for_container("ollama-container")

    # Paso 5: Descarga el modelo en el contenedor `ollama-container`
    download_model("ollama-container", model_name)

    # Paso 6: Opción para mantener los contenedores en ejecución o cerrarlos
    keep_running = input("Do you want to keep the containers running? (yes/no): ").strip().lower()
    if keep_running != 'yes':
        print("Stopping and removing containers...")
        subprocess.run(['docker-compose', 'down'])


if __name__ == '__main__':
    main()
