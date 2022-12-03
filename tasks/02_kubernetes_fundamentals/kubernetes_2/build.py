import os

MY_DIR = os.path.realpath(os.path.dirname(__file__))
IMAGES_DIR = os.path.join(MY_DIR, "..", "..", "01_containerized_ml_models")


def main():
    # start cluster (uncomment if not set via docker desktop)
    # os.system("minikube start")
    # os.system("minikube docker-env")
    # os.system("eval $(minikube -p minikube docker-env)")

    models = {'4', '8', '16'}

    # build docker images
    for model in models:
        os.chdir(os.path.join(IMAGES_DIR, f"model_api_{model}"))
        os.system(f"docker build -t model-{model} .")

    # deploy pods
    os.chdir(MY_DIR)
    for model in models:
        os.system(f"kubectl apply -f model-{model}.yaml")
    os.system("kubectl apply -f ingress.yaml")


if __name__ == "__main__":
    main()
