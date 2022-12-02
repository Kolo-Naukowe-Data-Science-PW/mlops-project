import os

yaml_files_dir = os.path.join(os.path.abspath(__file__), "..")
models_dir = os.path.join(yaml_files_dir, "..", "01_containerized_ml_models")


def main():

    api_used = [4, 10]
    for file in os.listdir(models_dir):
        model_number = int(file.split("_")[-1])
        if model_number in api_used:
            os.chdir(os.path.join(models_dir, file))
            os.system(f"docker build -t model_api_{model_number} .")

    os.chdir(yaml_files_dir)
    os.system("kubectl apply -f .")


if __name__ == "__main__":
    main()
