import os

YAML_FILES_DIR = os.path.join(os.path.abspath(__file__), "..")
MODELS_DIR = os.path.join(YAML_FILES_DIR, "..", "01_containerized_ml_models")


def main():

    api_used = [4, 10]
    for file in os.listdir(MODELS_DIR):
        model_number = int(file.split("_")[-1])
        if model_number in api_used:
            os.chdir(os.path.join(MODELS_DIR, file))
            os.system(f"docker build -t model_api_{model_number} .")

    os.chdir(YAML_FILES_DIR)
    os.system("kubectl apply -f .")


if __name__ == "__main__":
    main()
