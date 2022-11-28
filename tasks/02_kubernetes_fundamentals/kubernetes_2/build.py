import os

MY_DIR = os.path.abspath(os.curdir)
IMAGES_DIR = os.path.join(MY_DIR, "..", "..", "01_containerized_ml_models")

if __name__ == "__main__":
    # start cluster (uncomment if not set via docker desktop)
    # os.system("minikube start")
    # os.system("minikube docker-env")
    # os.system("eval $(minikube -p minikube docker-env)")

    # build docker images
    for folder in os.listdir(IMAGES_DIR):
        if folder.startswith("model_api_"):
            name = os.path.splitext(folder)[0].split("_")[-1]

            os.system(
                f"docker build -t model-{name} {os.path.join(IMAGES_DIR, folder)}"
            )

    # deploy pods
    for file in os.listdir(MY_DIR):
        if file.startswith("model"):
            os.system(f"kubectl apply -f {file}")
    os.system(f"kubectl apply -f ingress.yaml")
